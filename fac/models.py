from django.db import models

# Para los signals
from django.db.models.signals import post_save
# , post_delete
from django.dispatch import receiver
from django.db.models import Sum

import erpp.cita.models
import erpp.cmp.models
import erpp.conta.models
import erpp.gen.models
import erpp.inv.models
import erpp.per.models
import erpp.serv.models

from erpp.bases.models import ClaseModelo, ClaseModelo2
from erpp.inv.models import Producto


class Cliente(ClaseModelo):
    NAT = 'Natural'
    JUR = 'Jurídica'
    TIPO_CLIENTE = [
        (NAT, 'Natural'),
        (JUR, 'Jurídica')
    ]
    nombres = models.CharField(
        max_length=100
    )
    apellidos = models.CharField(
        max_length=100
    )
    celular = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CLIENTE,
        default=NAT
    )

    def __str__(self):
        return '{} {}'.format(self.apellidos, self.nombres)

    def save(self, *args, **kwargs):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Cliente, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Clientes"

    
class FacturaEnc(ClaseModelo2):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.id)

    def save(self):
        self.total = self.sub_total - self.descuento
        super(FacturaEnc, self).save()

    class Meta:
        verbose_name_plural = "Encabezado Facturas"
        verbose_name = "Encabezado Factura"
        permissions = [
            ('sup_caja_facturaenc', 'Permisos de Supervisor de Caja Encabezado')
        ]
    

class FacturaDet(ClaseModelo2):
    factura = models.ForeignKey(FacturaEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio))
        self.total = self.sub_total - float(self.descuento)
        super(FacturaDet, self).save()
    
    class Meta:
        verbose_name_plural = "Detalles Facturas"
        verbose_name = "Detalle Factura"
        permissions = [
            ('sup_caja_facturadet', 'Permisos de Supervisor de Caja Detalle')
        ]


@receiver(post_save, sender=FacturaDet)
def detalle_fac_guardar(sender, instance, **kwargs):
    factura_id = instance.factura.id
    producto_id = instance.producto.id

    enc = FacturaEnc.objects.get(pk=factura_id)
    if enc:
        sub_total = FacturaDet.objects \
            .filter(factura=factura_id) \
            .aggregate(sub_total=Sum('sub_total')) \
            .get('sub_total', 0.00)
        
        descuento = FacturaDet.objects \
            .filter(factura=factura_id) \
            .aggregate(descuento=Sum('descuento')) \
            .get('descuento', 0.00)
        
        enc.sub_total = sub_total
        enc.descuento = descuento
        enc.save()

    prod = Producto.objects.filter(pk=producto_id).first()
    if prod:
        cantidad = int(prod.existencia) - int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


class Cajadetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    cajacabecera = models.ForeignKey(
        erpp.conta.models.Cajacabecera,
        on_delete=models.CASCADE,
        verbose_name='CajaCabecera'
    )
    codempresa = models.IntegerField(verbose_name='Código De Empresa', blank=True, null=True)
    codcaja = models.CharField(label='Código De Caja', max_length=20, blank=True, null=True)
    nrocaja = models.IntegerField(verbose_name='Número De Caja', blank=True, null=True)
    item = models.IntegerField(verbose_name='Ítem', blank=True, null=True)
    tipodocumento = models.CharField(label='Tipo De Documento', max_length=20, blank=True, null=True)
    serie = models.CharField(label='Serie', max_length=20, blank=True, null=True)
    numero = models.CharField(label='Número', max_length=20, blank=True, null=True)
    fechadoc = models.DateTimeField(label='Fecha De Documentación', blank=True, null=True)
    codcuenta = models.TextField(label='Código De Cuenta', blank=True, null=True)
    codcentrodecostos = models.TextField(label='Código De Centro De Costos', blank=True, null=True)
    debe = models.BooleanField(verbose_name='¿Debe?', blank=True, null=True)
    glosa = models.TextField(label='Glosa', blank=True, null=True)
    moneda = models.TextField(label='Moneda', blank=True, null=True)
    t_c = models.DecimalField(label='Tipo De Cliente', max_digits=13, decimal_places=4, blank=True, null=True)
    totalsoles = models.DecimalField(label='Total En Soles', max_digits=11, decimal_places=2, blank=True, null=True)
    totaldolares = models.DecimalField(label='Total En Dólares', max_digits=11, decimal_places=2, blank=True, null=True)
    hora = models.TimeField(label='Hora', blank=True, null=True)
    usuario = models.TextField(label='Usuario', blank=True, null=True)
    tipocorrentista = models.BooleanField(verbose_name='¿Tipo Correntista?', blank=True, null=True)
    codproveedor = models.CharField(label='Código De Proveedor', max_length=11, blank=True, null=True)
    coddistcc = models.IntegerField(verbose_name='Código De Dist CC', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    tcorrentista = models.CharField(label='Tipo Correntista', max_length=6, blank=True, null=True)
    procedencia = models.IntegerField(verbose_name='Procedencia', blank=True, null=True)
    diferenciacambio = models.DecimalField(
        label='Diferencia Cambio',
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'cajadetalle'


class Cajeroserie(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestrocajero = models.ForeignKey(
        erpp.fac.models.Maestrocajeros,
        on_delete=models.CASCADE,
        verbose_name='MaestroCajero',
        blank=True,
        null=True
    )
    serie = models.CharField(label='Serie', max_length=20, blank=True, null=True)
    tipodocumento = models.IntegerField(verbose_name='Tipo De Documento', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36, blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=20, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=80, blank=True, null=True)
    estado = models.IntegerField(verbose_name='Estado', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)

    class Meta:
        db_table = 'cajeroserie'


class Cierrefacturacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    fecha = models.DateField(label='Fecha')
    cerrado = models.BooleanField(verbose_name='Cerrado')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    trabajador = models.ForeignKey(
        erpp.cita.models.Maestrotrabajotaller,
        on_delete=models.CASCADE,
        verbose_name='Trabajador'
    )
    empresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='Empresa')
    sucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='Sucursal')
    saldoinical = models.DecimalField(label='Saldo Inical', max_digits=12, decimal_places=3)
    fechacierre = models.DateTimeField(label='Fecha De Cierre', blank=True, null=True)
    cajachicadeclara = models.DecimalField(
        label='Caja Chica Declaración',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    efectivodeclara = models.DecimalField(
        label='Efectivo Declaración',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    visadeclara = models.DecimalField(label='Visa Declaración', max_digits=12, decimal_places=3, blank=True, null=True)
    masterdeclara = models.DecimalField(
        label='Master Declaración',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    valesalimenticiosdeclara = models.DecimalField(
        label='Vales Alimenticios Declaración',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    valesdeclara = models.DecimalField(
        label='Vales Declaración',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    creditodeclara = models.DecimalField(
        label='Crédito Declaración',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    conspersonaldeclara = models.DecimalField(
        label='Constancia Personal Declaración',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    connopagadodeclara = models.DecimalField(
        label='Constancia No Pagado Declaración',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    otrosdeclara = models.DecimalField(
        label='Otros Declaración',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    cajachica = models.DecimalField(label='Caja Chica', max_digits=12, decimal_places=3, blank=True, null=True)
    efectivo = models.DecimalField(label='Efectivo', max_digits=12, decimal_places=3, blank=True, null=True)
    visa = models.DecimalField(label='Visa', max_digits=12, decimal_places=3, blank=True, null=True)
    master = models.DecimalField(label='Master', max_digits=12, decimal_places=3, blank=True, null=True)
    valesalimenticios = models.DecimalField(
        label='Vales Alimenticios',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    vales = models.DecimalField(label='Vales', max_digits=12, decimal_places=3, blank=True, null=True)
    credito = models.DecimalField(label='Crédito', max_digits=12, decimal_places=3, blank=True, null=True)
    conspersonal = models.DecimalField(
        label='Constancia Personal',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    connopagado = models.DecimalField(
        label='Constancia No Pagada',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    otros = models.DecimalField(label='Otros', max_digits=12, decimal_places=3, blank=True, null=True)
    codigocajero = models.CharField(label='Código Cajero', max_length=20, blank=True, null=True)
    cajachicasis = models.DecimalField(label='Caja Chica Sis', max_digits=12, decimal_places=3, blank=True, null=True)
    efectivosis = models.DecimalField(label='Efectivo Sis', max_digits=12, decimal_places=3, blank=True, null=True)
    visasis = models.DecimalField(label='Visa Sis', max_digits=12, decimal_places=3, blank=True, null=True)
    mastersis = models.DecimalField(label='Master Sis', max_digits=12, decimal_places=3, blank=True, null=True)
    valesalimenticiossis = models.DecimalField(
        label='Vales Alimenticios Sis',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    valessis = models.DecimalField(label='Vales Sis', max_digits=12, decimal_places=3, blank=True, null=True)
    creditosis = models.DecimalField(label='Crédito Sis', max_digits=12, decimal_places=3, blank=True, null=True)
    conspersonalsis = models.DecimalField(
        label='Constancia Personal Sis',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    connopagadosis = models.DecimalField(
        label='Constancia No Pagada Sis',
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    otrossil = models.DecimalField(label='Otros Sil', max_digits=12, decimal_places=3, blank=True, null=True)

    class Meta:
        db_table = 'cierrefacturacion'


class Cierrefacturaciondetalle(models.Model):
    idcierrefacturaciondetalle = models.AutoField(label='IdCierreFacturacionDetalle', primary_key=True)
    cierrefacturacion = models.ForeignKey(Cierrefacturacion, on_delete=models.CASCADE, verbose_name='CierreFacturacion')
    maestroformadepago = models.ForeignKey(
        erpp.gen.models.Maestroformasdepago,
        on_delete=models.CASCADE,
        verbose_name='MaestroFormaDePago'
    )
    totaldeclara = models.DecimalField(label='Total Declaraciones', max_digits=18, decimal_places=3)
    totalsistema = models.DecimalField(label='Total Sistema', max_digits=18, decimal_places=3)
    diferencia = models.DecimalField(label='Diferencia', max_digits=18, decimal_places=3)
    fecharegistro = models.DateTimeField(label='Fecha De Registro')
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'cierrefacturaciondetalle'


class Cierreordenservicio(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    ordenserviciocabecera = models.ForeignKey(
        erpp.serv.models.Ordenserviciocabecera,
        on_delete=models.CASCADE,
        verbose_name='OrdenServicioCabecera'
    )
    especialista = models.ForeignKey(
        erpp.per.models.Maestropersonal,
        on_delete=models.CASCADE,
        verbose_name='Especialista'
    )
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'cierreordenservicio'


class Clientedireccion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestrocliente = models.ForeignKey(
        erpp.fac.models.Maestroclientes,
        on_delete=models.CASCADE,
        verbose_name='MaestroCliente'
    )
    domiciliodetalle = models.ForeignKey(
        erpp.fac.models.Domiciliodetalle,
        on_delete=models.CASCADE,
        verbose_name='DomicilioDetalle'
    )

    class Meta:
        db_table = 'clientedireccion'


class Clientesmigrar(models.Model):
    tipo_persona = models.CharField(label='Tipo Persona', max_length=255, blank=True, null=True)
    tipo_de_documento_de_identidad_del_cliente = models.CharField(
        label='Tipo de Documento de Identidad del cliente',
        max_length=255,
        blank=True,
        null=True
    )
    ruc = models.CharField(label='RUC', max_length=255, blank=True, null=True)
    razon_social = models.CharField(label='Razón Social', max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'clientesmigrar'


class Controlventa(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    facturacabecera = models.ForeignKey(
        erpp.fac.models.Facturaclientecabecera,
        on_delete=models.CASCADE,
        verbose_name='FacturaCabecera'
    )
    numerofactura = models.CharField(label='Número De Factura', max_length=75)
    fecha = models.DateField(label='Fecha')
    montosoles = models.DecimalField(label='Monto En Soles', max_digits=11, decimal_places=2)
    montodolares = models.DecimalField(label='Monto En Dólares', max_digits=13, decimal_places=4)
    maestromoneda = models.ForeignKey(
        erpp.gen.models.Maestromoneda,
        on_delete=models.CASCADE,
        verbose_name='MaestroMoneda'
    )
    maestrotipocambio = models.ForeignKey(
        erpp.gen.models.Maestrotipodecambio,
        on_delete=models.CASCADE,
        verbose_name='MaestroTipoCambio'
    )
    porcentaje = models.DecimalField(label='Porcentaje', max_digits=5, decimal_places=2)
    utilidadsoles = models.DecimalField(label='Utilidad En Soles', max_digits=11, decimal_places=2)
    utilidaddolares = models.DecimalField(label='Utilidad En Dólares', max_digits=13, decimal_places=4)
    lugar = models.ForeignKey(erpp.gen.models.Maestroubigeo, on_delete=models.CASCADE, verbose_name='Lugar')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'controlventa'


class Cotizacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    pedidocabecera = models.ForeignKey(
        erpp.inv.models.Pedidocabecera,
        on_delete=models.CASCADE,
        verbose_name='PedidoCabecera'
    )
    pedidodetalle = models.ForeignKey(
        erpp.inv.models.Pedidodetalle,
        on_delete=models.CASCADE,
        verbose_name='PedidoDetalle'
    )
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    cotizado = models.BooleanField(verbose_name='¿Cotizado?', default=False)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    imagenscaneada = models.CharField(label='Imagen Escaneada', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'cotizacion'


class Cotizacionclientecabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    solicituddeproductodetalle = models.ForeignKey(
        erpp.fac.models.Solicituddeproductocabecera,
        on_delete=models.CASCADE,
        verbose_name='SolicitudDeProductoDetalle',
        blank=True,
        null=True
    )
    fechacotizacion = models.DateTimeField(label='Fecha De Cotización')
    numero = models.CharField(label='Número', max_length=20)
    maestrocliente = models.ForeignKey(
        erpp.fac.models.Maestroclientes,
        on_delete=models.CASCADE,
        verbose_name='MaestroCliente'
    )
    servicio = models.CharField(label='Servicio', max_length=50)
    equipo = models.CharField(label='Equipo', max_length=50)
    modelo = models.CharField(label='Modelo', max_length=50)
    anhio = models.IntegerField(verbose_name='Año')
    unidad = models.CharField(label='Unidad', max_length=50)
    placa = models.CharField(label='Placa', max_length=20)
    coloquial = models.CharField(label='Coloquial', max_length=20)
    serie = models.CharField(label='Serie', max_length=50)
    tiempoentrega = models.IntegerField(verbose_name='Tiempo De Entrega')
    lugar = models.ForeignKey(erpp.gen.models.Maestroubigeo, on_delete=models.CASCADE, verbose_name='Lugar')
    valorventasoles = models.DecimalField(label='Valor De Venta En Soles', max_digits=11, decimal_places=2)
    valorventadolares = models.DecimalField(label='Valor De Venta En Dólares', max_digits=13, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'cotizacionclientecabecera'


class Cotizacionclientedetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    cotizacionclientecabecera = models.ForeignKey(
        Cotizacionclientecabecera,
        on_delete=models.CASCADE,
        verbose_name='CotizacionClienteCabecera'
    )
    productoservicio = models.ForeignKey(
        erpp.inv.models.Maestroproductos,
        on_delete=models.CASCADE,
        verbose_name='ProductoServicio'
    )
    producto = models.BooleanField(verbose_name='Producto')
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    preciounitariosoles = models.DecimalField(label='Precio Unitario En Soles', max_digits=11, decimal_places=2)
    preciounitariodolares = models.DecimalField(label='Precio Unitario En Dólares', max_digits=13, decimal_places=4)
    porcentajedescuento = models.DecimalField(
        label='Porcentaje De Descuento',
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )
    subtotalsoles = models.DecimalField(label='SubTotal En Soles', max_digits=11, decimal_places=2)
    subtotaldolares = models.DecimalField(label='SubTotal En Dolares', max_digits=13, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'cotizacionclientedetalle'


class Datoclientedelivey(models.Model):
    iddatoclientedelivery = models.AutoField(label='IdDatoClienteDelivery', primary_key=True)
    telefono = models.CharField(label='Teléfono', max_length=10)
    numerodocumentoidentidad = models.CharField(label='Número De Documento De Identidad', max_length=20)
    nombrecliente = models.CharField(label='Nombre Del Cliente', max_length=300)
    direccioncliente = models.CharField(label='Dirección Del Cliente', max_length=500)
    referenciadireccioncliente = models.CharField(label='Referencia y Direccion Del Cliente', max_length=300)
    nombretransportista = models.CharField(label='Nombre Del Transportista', max_length=500)

    class Meta:
        db_table = 'datoclientedelivey'


class Documentofactura(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    codigosucursal = models.CharField(label='Código Sucursal', max_length=50)
    numerodocumentofacbol = models.CharField(label='Número Documento Factura/Boleta', max_length=50)
    tipomovimiento = models.CharField(label='Tipo Movimiento', max_length=50)
    idtipomovimiento = models.ForeignKey(
        erpp.per.models.Maestrotipomovimiento,
        on_delete=models.CASCADE,
        verbose_name='TipoMovimiento'
    )
    numerodocumentoalmacen = models.IntegerField(verbose_name='Número Documento Almacen')
    facturaclientecabecera = models.ForeignKey(
        erpp.fac.models.Facturaclientecabecera,
        on_delete=models.CASCADE,
        verbose_name='FacturaClienteCabecera'
    )
    almacencabecera = models.ForeignKey(
        erpp.inv.models.Almacencabecera,
        on_delete=models.CASCADE,
        verbose_name='AlmacenCabecera'
    )
    ordencompraclientecabecera = models.ForeignKey(
        erpp.fac.models.Ordencompraclientecabecera,
        on_delete=models.CASCADE,
        verbose_name='OrdenCompraClienteCabecera'
    )
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=50)
    autorizado = models.CharField(label='Autorizado', max_length=50)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    ordenpedido = models.ForeignKey(
        erpp.serv.models.Ordenpedido,
        on_delete=models.CASCADE,
        verbose_name='OrdenPedido',
        blank=True,
        null=True
    )
    tallercabecera = models.ForeignKey(
        erpp.fac.models.Tallerfactura,
        on_delete=models.CASCADE,
        verbose_name='TallerCabecera'
    )
    texto = models.TextField(label='Texto', blank=True, null=True)

    class Meta:
        db_table = 'documentofactura'


class Domiciliodetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    maestrotipovia = models.ForeignKey(
        erpp.gen.models.Maestrotipovia,
        on_delete=models.CASCADE,
        verbose_name='MaestroTipoVia'
    )
    nombrevia = models.CharField(label='Nombre Vía', max_length=75)
    numerovia = models.IntegerField(verbose_name='Número Vía')
    departamento = models.CharField(label='Departamento', max_length=75)
    interior = models.CharField(label='Interior', max_length=20)
    manzana = models.CharField(label='Manzana', max_length=1)
    lote = models.IntegerField(verbose_name='Lote')
    kilometro = models.CharField(label='Kilometro', max_length=75)
    block = models.CharField(label='Block', max_length=15)
    etapa = models.CharField(label='Etapa', max_length=15)
    maestrotipozona = models.ForeignKey(
        erpp.gen.models.Maestrotipozona,
        on_delete=models.CASCADE,
        verbose_name='MaestroTipoZona'
    )
    nombrezona = models.CharField(label='Nombre de la Zona', max_length=75)
    referenciavivienda = models.CharField(label='Referencia Vivienda', max_length=500)
    ubigeodireccion = models.ForeignKey(
        erpp.gen.models.Maestroubigeo,
        on_delete=models.CASCADE,
        verbose_name='UbigeoDireccion'
    )
    direccioncompleta = models.CharField(label='Dirección Completa', max_length=200)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    personal = models.ForeignKey(
        erpp.per.models.Maestropersonal,
        on_delete=models.CASCADE,
        verbose_name='Personal',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'domiciliodetalle'


class Ejecucionserviciocabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    numerotarjeta = models.CharField(label='Número Tarjeta', max_length=75)
    maestrotrabajotaller = models.ForeignKey(
        erpp.cita.models.Maestrotrabajotaller,
        on_delete=models.CASCADE,
        verbose_name='MaestroTrabajoTaller'
    )
    maestroserviciotaller = models.ForeignKey(
        erpp.serv.models.Maestroserviciotaller,
        on_delete=models.CASCADE,
        verbose_name='MaestroServicioTaller'
    )
    tiempo = models.IntegerField(verbose_name='Tiempo')
    tiempotablalavadosecado = models.IntegerField(verbose_name='Tiempo Tabla Lavado Secado', blank=True, null=True)
    tiempotablacontrolcalidad = models.IntegerField(verbose_name='Tiempo Tabla Control/Calidad', blank=True, null=True)
    tiempotablarevisionasesor = models.IntegerField(verbose_name='Tiempo Tabla Revision Asesor', blank=True, null=True)
    porcentaje = models.DecimalField(label='Porcentaje', max_digits=5, decimal_places=2)
    terminado = models.BooleanField(verbose_name='¿Terminado?', default=False)
    ordenserviciocabecera = models.ForeignKey(
        erpp.serv.models.Ordenserviciocabecera,
        on_delete=models.CASCADE,
        verbose_name='OrdenServicioCabecera'
    )
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    observacioncontrolista = models.CharField(label='Observación Controlista', max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'ejecucionserviciocabecera'


class Facturaclientecabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    maestrodocumentosunat = models.ForeignKey(
        erpp.gen.models.Maestrodocumentossunat,
        on_delete=models.CASCADE,
        verbose_name='MaestroDocumentoSunat'
    )
    fechaemision = models.DateField(label='Fecha De emisión')
    numeroserie = models.CharField(label='Número De Serie', max_length=20)
    numerodocumentofb = models.CharField(label='Número De Documento Factura/Boleta', max_length=20)
    maestrocliente = models.ForeignKey(
        erpp.fac.models.Maestroclientes,
        on_delete=models.CASCADE,
        verbose_name='MaestroCliente'
    )
    nombrecliente = models.CharField(label='Nombre Del Cliente', max_length=200)
    ordencompraclientecabecera = models.ForeignKey(
        erpp.cmp.models.Ordencompracabecera,
        on_delete=models.CASCADE,
        verbose_name='OrdenCompraClienteCabecera',
        blank=True,
        null=True
    )
    ordenpedido = models.ForeignKey(
        erpp.serv.models.Ordenpedido,
        on_delete=models.CASCADE,
        verbose_name='OrdenPedido',
        blank=True,
        null=True
    )
    factura = models.CharField(label='Factura', max_length=20)
    numerodocumento = models.CharField(label='Número De Documento', max_length=20)
    tipodocumrequerido = models.CharField(label='Tipo De Documento Requerido', max_length=20)
    seriedocumentorequerido = models.CharField(
        label='Serie De Documento Requerido',
        max_length=5,
        blank=True,
        null=True
    )
    numerodocumentorequerido = models.CharField(label='Número Documento Requerido', max_length=20)
    tipodocumentooc = models.CharField(label='Tipo De Documento OC', max_length=20)
    numerodocumentooc = models.CharField(label='Número Documento OC', max_length=20)
    diferenciasoles = models.DecimalField(label='Diferencia En Soles', max_digits=19, decimal_places=2)
    numerodocumentoformapago = models.CharField(label='Número De Documento Forma Pago', max_length=20)
    concepto = models.TextField(label='Concepto')
    maestrovendedor = models.ForeignKey(
        erpp.fac.models.Maestrovendedores,
        on_delete=models.CASCADE,
        verbose_name='MaestroVendedor'
    )
    maestrocaja = models.ForeignKey(erpp.fac.models.Maestrocajas, on_delete=models.CASCADE, verbose_name='MaestroCaja')
    tipofactura = models.CharField(label='Tipo De Factura', max_length=20)
    guiadespacho = models.CharField(label='Guía De Despacho', max_length=60)
    referenciapresupuesto = models.CharField(label='Referencia Del Presupuesto', max_length=60)
    maestrobanco = models.ForeignKey(
        erpp.gen.models.Maestrobancos,
        on_delete=models.CASCADE,
        verbose_name='MaestroBanco'
    )
    saldopendientesoles = models.DecimalField(label='Saldo Pendiente En Soles', max_digits=11, decimal_places=2)
    saldopendientedolares = models.DecimalField(label='Saldo Pendiente En Dólares', max_digits=13, decimal_places=4)
    maestrocentrodecosto = models.ForeignKey(
        erpp.gen.models.Maestrocentrosdecostos,
        on_delete=models.CASCADE,
        verbose_name='MaestroCentroDeCosto'
    )
    maestromoneda = models.ForeignKey(
        erpp.gen.models.Maestromoneda,
        on_delete=models.CASCADE,
        verbose_name='MaestroMoneda'
    )
    maestrotipocambio = models.ForeignKey(
        erpp.gen.models.Maestrotipodecambio,
        on_delete=models.CASCADE,
        verbose_name='MaestroTipoCambio'
    )
    totalsoles = models.DecimalField(label='Total En Soles', max_digits=11, decimal_places=2)
    totaldolares = models.DecimalField(label='Total En Dólares', max_digits=13, decimal_places=4)
    totaligvsoles = models.DecimalField(label='Total IGV En Soles', max_digits=11, decimal_places=2)
    totaligvdolares = models.DecimalField(label='Total IGV En Dólares', max_digits=13, decimal_places=4)
    maestroformapago = models.ForeignKey(
        erpp.gen.models.Maestroformasdepago,
        on_delete=models.CASCADE,
        verbose_name='MaestroFormaPago'
    )
    descuentosoles = models.DecimalField(label='Descuento En Soles', max_digits=11, decimal_places=2)
    descuentodolares = models.DecimalField(label='Descuento En Dólares', max_digits=13, decimal_places=4)
    fechavencimiento = models.DateTimeField(label='Fecha De Vencimiento')
    cobrador = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='Cobrador')
    codigocobrador = models.CharField(label='Código De Cobrador', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    imprimida = models.BooleanField(verbose_name='¿Imprimida?', blank=True, null=True)
    detalle = models.IntegerField(verbose_name='Detalle', blank=True, null=True)
    anulada = models.BooleanField(verbose_name='¿Anulada?', blank=True, null=True)
    estadodocumento = models.CharField(label='Estado Del Documento', max_length=50)
    tipodecambio = models.DecimalField(label='Tipo De Cambio', max_digits=6, decimal_places=4, blank=True, null=True)
    afectoigv = models.IntegerField(verbose_name='Afecto IGV', blank=True, null=True)
    importecanceladosoles = models.DecimalField(
        label='Importe Cancelado En Soles',
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True
    )
    importecanceladodolares = models.DecimalField(
        label='Importe Cancelado En Dólares', max_digits=11,
        decimal_places=2, blank=True, null=True
    )
    items = models.IntegerField(verbose_name='Ítems', blank=True, null=True)
    usuario = models.CharField(label='Usuario', max_length=150, blank=True, null=True)
    imprimedocumento = models.CharField(label='Imprime Documento', max_length=200, blank=True, null=True)
    requesicion = models.CharField(label='Requesición', max_length=50, blank=True, null=True)
    adelanto = models.BooleanField(verbose_name='¿Adelanto?', blank=True, null=True)
    tienedetraccion = models.BooleanField(verbose_name='¿Tiene Detracción?', blank=True, null=True)
    esformatolargo = models.BooleanField(verbose_name='¿Es Formato Largo?', blank=True, null=True)
    numerocontable = models.IntegerField(verbose_name='Número Contable', blank=True, null=True)
    vouchercabecera = models.ForeignKey(
        erpp.conta.models.Vouchercabecera, on_delete=models.CASCADE,
        verbose_name='VoucherCabecera', blank=True, null=True
    )
    maestrocajero = models.ForeignKey(
        erpp.fac.models.Maestrocajeros, on_delete=models.CASCADE,
        verbose_name='MaestroCajero', blank=True, null=True
    )
    fechaimpresion = models.DateTimeField(label='Fecha De Impresion', blank=True, null=True)
    tipodocumentoimprimeen = models.ForeignKey(
        erpp.conta.models.TiposDeDocumentos,
        on_delete=models.CASCADE, verbose_name='TipoDocumentoImprimeEn',
        blank=True, null=True
     )
    seriedocumentoimprimeen = models.CharField(label='Serie Documento Imprime En', max_length=5, blank=True, null=True)
    numerodocumentoimprimeen = models.CharField(label='Número Documento Imprime En', max_length=20, blank=True, null=True)
    noesfacturadetallada = models.BooleanField(verbose_name='¿No Es Factura Detallada?', blank=True, null=True)
    accionnotadecredito = models.ForeignKey(
        erpp.conta.models.Maestroaccionnotadecredito, on_delete=models.CASCADE,
        verbose_name='AccionNotaDeCredito', blank=True, null=True
    )
    motivonotadecredito = models.ForeignKey(
        erpp.conta.models.Notascreditocabecera, on_delete=models.CASCADE,
        verbose_name='MotivoNotaDeCredito', blank=True, null=True
    )
    maestroturnocaja = models.ForeignKey(
        erpp.fac.models.Maestroturnoscaja, on_delete=models.CASCADE,
        verbose_name='MaestroTurnoCaja', blank=True, null=True
    )
    maestrovehiculo = models.ForeignKey(
        erpp.fac.models.Maestrovehiculo, on_delete=models.CASCADE,
        verbose_name='MaestroVehiculo', blank=True, null=True
    )
    maestroalmacen = models.ForeignKey(
        erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE,
        verbose_name='MaestroAlmacen', blank=True, null=True
    )
    condescargoporalmacen = models.BooleanField(verbose_name='¿Con Descargo Por Almacen?', blank=True, null=True)
    direccioncliente = models.CharField(label='Direccion Del Cliente', max_length=500, blank=True, null=True)
    totalvaletarjetasoles = models.DecimalField(
        label='Total Vale Tarjeta En Soles', max_digits=14,
        decimal_places=2, blank=True, null=True
    )
    datoclientedelivery = models.ForeignKey(
        erpp.fac.models.Datoclientedelivey, on_delete=models.CASCADE,
        verbose_name='DatoClienteDelivery', blank=True, null=True
    )
    efectivovale = models.DecimalField(label='Efectivo Vale', max_digits=14, decimal_places=2, blank=True, null=True)
    tipoventa = models.CharField(label='Tipo Venta', max_length=50, blank=True, null=True)
    telefonodatoclienteref = models.CharField(
        label='Telefono Dato Cliente Referencia',
        max_length=50, blank=True, null=True
    )
    clienteallamardatoclienteref = models.CharField(
        label='Cliente A Llamar Dato Cliente Referencia',
        max_length=50, blank=True, null=True
    )
    clientedirecciondatoclienteref = models.CharField(
        label='Cliente Dirección Dato Cliente Referencia',
        max_length=250, blank=True, null=True
    )
    clientedireccionreferenciadatoclienteref = models.CharField(
        label='Cliente Dirección Referencia Dato Cliente Referencia',
        max_length=250, blank=True, null=True
    )
    transportistadatoclienteref = models.CharField(
        label='Transportista Dato Cliente Referencia',
        max_length=250, blank=True, null=True
    )
    firma = models.CharField(label='Firma', max_length=500, blank=True, null=True)
    bolsas = models.DecimalField(label='Bolsas', max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'facturaclientecabecera'


class Facturaclientedetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    facturaclientecabecera = models.ForeignKey(
        Facturaclientecabecera, on_delete=models.CASCADE,
        verbose_name='FacturaClienteCabecera', blank=True, null=True
    )
    trabajotaller = models.BooleanField(verbose_name='¿Trabajo Taller?', default=False)
    serviciotaller = models.BooleanField(verbose_name='¿Servicio Taller?', default=False)
    producto = models.BooleanField(verbose_name='¿Producto?', blank=True, null=True)
    productoservicio = models.ForeignKey(
        erpp.inv.models.Maestroproductos, on_delete=models.CASCADE,
        verbose_name='ProductoServicio')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    subtotalsoles = models.DecimalField(label='Subtotal En Soles', max_digits=11, decimal_places=2)
    subtotaldolares = models.DecimalField(label='Subtotal En Dólares', max_digits=13, decimal_places=4)
    preciosoles = models.DecimalField(label='Precio En Soles', max_digits=11, decimal_places=2)
    preciodolares = models.DecimalField(label='Precio En Dólares', max_digits=13, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    productolibre = models.CharField(label='Producto Libre', max_length=500, blank=True, null=True)
    requesicion = models.CharField(label='Requesición', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'facturaclientedetalle'


class Facturacioncaja(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    descripcion = models.CharField(label='Descripción', max_length=250)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    fechacreacion = models.IntegerField(verbose_name='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=250)
    maestrocajero = models.ForeignKey(
        erpp.fac.models.Maestrocajeros, on_delete=models.CASCADE,
        verbose_name='MaestroCajero'
    )

    class Meta:
        db_table = 'facturacioncaja'


class Maestrocajas(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    codigosucursal = models.CharField(label='CodigoSucursal', max_length=20)
    codigocaja = models.CharField(label='Código De Caja', max_length=20)
    numerocaja = models.CharField(label='Número De Caja', max_length=20)
    tipocaja = models.CharField(label='Tipo De Caja', max_length=20)
    maestromoneda = models.ForeignKey(
        erpp.gen.models.Maestromoneda, on_delete=models.CASCADE,
        verbose_name='MaestroMoneda'
    )
    moneda = models.CharField(label='Moneda', max_length=2)
    nombre = models.CharField(label='Nombre', max_length=60)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    codigocuentacontable = models.CharField(label='Código Cuenta Contable', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'maestrocajas'
        unique_together = (('codigocaja', 'idmaestroempresa'),)


class Maestrocajeros(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    codigocajero = models.CharField(label='Código Del Cajero', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    usuario = models.ForeignKey(
        erpp.gen.models.Maestrousuario, on_delete=models.CASCADE,
        verbose_name='Usuario', blank=True, null=True
    )

    class Meta:
        db_table = 'maestrocajeros'


class Maestroclientetipo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    codigotipocliente = models.CharField(label='Código Tipo De Cliente', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    descripcionadicional = models.CharField(label='Descripción Adicional', max_length=500)

    class Meta:
        db_table = 'maestroclientetipo'


class Maestroclientes(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    maestrotipocliente = models.ForeignKey(
        Maestroclientetipo, on_delete=models.CASCADE,
        verbose_name='MaestroTipoCliente'
    )
    codigotipocliente = models.CharField(label='Código Tipo Cliente', max_length=20)
    codigosucursal = models.CharField(label='Código De La Sucursal', max_length=20)
    codigocliente = models.CharField(label='Codigo Del Cliente', max_length=20)
    razonsocial = models.TextField(label='Razón Social')
    nombres = models.TextField(label='Nombres')
    primerapellido = models.CharField(label='Primer Apellido', max_length=60)
    segundoapellido = models.CharField(label='Segundo Apellido', max_length=60)
    fechanacimiento = models.DateField(label='Fecha De Nacimiento')
    nombrepadre = models.CharField(label='Nombre Del Padre', max_length=75)
    nombremadre = models.CharField(label='Nombre De La Madre', max_length=75)
    viatipo = models.CharField(label='Vía Tipo', max_length=60)
    vianombre = models.CharField(label='Vía Nombre', max_length=60)
    numero = models.CharField(label='Número', max_length=15)
    interior = models.CharField(label='Interior', max_length=15)
    zona = models.CharField(label='Zona', max_length=60)
    ubigeo = models.ForeignKey(erpp.gen.models.Maestroubigeo, on_delete=models.CASCADE, verbose_name='Ubigeo')
    codigociudad = models.CharField(label='Código De La Ciudad', max_length=20)
    maestrotipodocumento = models.ForeignKey(
        erpp.gen.models.Maestrotiposdocumentos, on_delete=models.CASCADE,
        verbose_name='MaestroTipoDocumento'
    )
    numerodocumentoidentificacion = models.CharField(label='Número Del Documento De Identificacion', max_length=15)
    personajuridica = models.BooleanField(verbose_name='¿Persona Jurídica?', default=False)
    ruc = models.CharField(label='RUC', max_length=11)
    contacto = models.CharField(label='Contacto', max_length=500)
    telefono1 = models.CharField(label='Teléfono 1', max_length=25)
    telefono2 = models.CharField(label='Teléfono 2', max_length=25)
    telefonocelular = models.CharField(label='Teléfono Celular', max_length=25)
    email = models.CharField(label='EMail', max_length=60)
    fax = models.CharField(label='Fax', max_length=25)
    fecharegistro = models.DateTimeField(label='Fecha Registro')
    limitecreditosoles = models.DecimalField(label='Límite Crédito Soles', max_digits=11, decimal_places=2)
    limitecreditodolares = models.DecimalField(label='Límite Crédito Dolares', max_digits=13, decimal_places=4)
    montototaldeudasoles = models.DecimalField(
        label='Monto Total De La Deuda En Soles',
        max_digits=11, decimal_places=2
    )
    montototaldeudadolares = models.DecimalField(
        label='Monto Total De La Deuda En Dólares',
        max_digits=13, decimal_places=4
    )
    observaciones = models.CharField(label='Observaciones', max_length=60)
    codigocobrador = models.CharField(label='Código Del Cobrador', max_length=20)
    codigozona = models.CharField(label='Código De La Zona', max_length=20)
    codigoestado = models.CharField(label='Código Del Estado', max_length=20)
    agenteretencion = models.BooleanField(verbose_name='¿Agente De Retención?', default=False)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    numeromaximoordenservicio = models.IntegerField(verbose_name='Número Máximo Orden/Servicio', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    direccioncompleta = models.CharField(label='Dirección Completa', max_length=200, blank=True, null=True)
    listaaprobda = models.CharField(label='Lista Aprobada', max_length=5, blank=True, null=True)
    clienteempresa = models.ForeignKey(
        erpp.fac.models.Maestroclientes, on_delete=models.CASCADE,
        verbose_name='ClienteEmpresa', blank=True, null=True
    )

    class Meta:
        db_table = 'maestroclientes'


class Maestrogastoscaja(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    codigogasto = models.CharField(label='Código Del Gasto', max_length=20)
    nombregasto = models.CharField(label='Nombre Del Gasto', max_length=60)
    descripcion = models.CharField(label='Descripción', max_length=60)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrogastoscaja'


class Maestrohorarioturnopersonal(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    lunesingeso = models.TimeField(label='Lunes Ingeso')
    martesingeso = models.TimeField(label='Martes Ingeso')
    miercolesingeso = models.TimeField(label='Miércoles Ingeso')
    juevesingeso = models.TimeField(label='Jueves Ingeso')
    viernesingeso = models.TimeField(label='Viernes Ingeso')
    sabadoingeso = models.TimeField(label='Sábado Ingeso')
    domingoingeso = models.TimeField(label='Domingo Ingeso')
    lunessalida = models.TimeField(label='Lunes Salida')
    martessalida = models.TimeField(label='Martes Salida')
    miercolessalida = models.TimeField(label='Miércoles Salida')
    juevessalida = models.TimeField(label='Jueves Salida')
    viernessalida = models.TimeField(label='Viernes Salida')
    sabadosalida = models.TimeField(label='Sábado Salida')
    domingosalida = models.TimeField(label='Domingo Salida')
    lunesingesoii = models.TimeField(label='Lunes Ingeso II')
    martesingesoii = models.TimeField(label='Martes Ingeso II')
    miercolesingesoii = models.TimeField(label='Miércoles Ingeso II')
    juevesingesoii = models.TimeField(label='Jueves Ingeso II')
    viernesingesoii = models.TimeField(label='Viernes Ingeso II')
    sabadoingesoii = models.TimeField(label='Sábado Ingeso II')
    domingoingesoii = models.TimeField(label='Domingo Ingeso II')
    lunessalidaii = models.TimeField(label='Lunes Salida II')
    martessalidaii = models.TimeField(label='Martes Salida II')
    miercolessalidaii = models.TimeField(label='Miércoles Salida II')
    juevessalidaii = models.TimeField(label='Jueves Salida II')
    viernessalidaii = models.TimeField(label='Viernes Salida II')
    sabadosalidaii = models.TimeField(label='Sábado Salida II')
    domingosalidaii = models.TimeField(label='Domingo Salida II')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrohorarioturnopersonal'


class Maestroimpresora(models.Model):
    id = models.AutoField(label='Id', primary_key=True)
    nombreimpresora = models.CharField(label='Nombre De Impresora', max_length=50, blank=True, null=True)
    almacen = models.ForeignKey(
        erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE,
        verbose_name='Almacen', blank=True, null=True
    )
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación', blank=True, null=True)
    area = models.ForeignKey(
        erpp.inv.models.Areas, on_delete=models.CASCADE,
        verbose_name='Area', blank=True, null=True
    )
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa', blank=True, null=True
    )

    class Meta:
        db_table = 'maestroimpresora'


class Maestroplanilla(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    codigoplanilla = models.CharField(label='Código De La Planilla', max_length=20)
    tipoplanilla = models.ForeignKey(
        erpp.per.models.Maestrotipoplanilla, on_delete=models.CASCADE,
        verbose_name='TipoPlanilla'
    )
    maestrotiposervidor = models.ForeignKey(
        erpp.per.models.Maestrotiposervidor, on_delete=models.CASCADE,
        verbose_name='MaestroTipoServidor'
    )
    centrodecostos = models.ForeignKey(
        erpp.gen.models.Maestrocentrosdecostos, on_delete=models.CASCADE,
        verbose_name='CentroDeCostos'
    )
    tituloplanilla = models.CharField(label='Título De La Planilla', max_length=75)
    tituloplanillaabreviado = models.CharField(label='Título De La Planilla Abreviado', max_length=30)
    fechainicio = models.DateTimeField(label='Fecha De Inicio')
    fechatermino = models.DateTimeField(label='Fecha De Termino')
    anio = models.IntegerField(verbose_name='Año')
    mes = models.IntegerField(verbose_name='Mes')
    semana = models.IntegerField(verbose_name='Semana')
    diasnormales = models.DecimalField(label='Días Normales', max_digits=5, decimal_places=2)
    dominical = models.IntegerField(verbose_name='Dominical')
    porcentajedescuentocuentacorriente = models.DecimalField(
        label='Porcentaje De Descuento De La Cuenta Corriente',
        max_digits=5, decimal_places=2
    )
    cerrada = models.BooleanField(verbose_name='¿Cerrada?', default=False)
    pagosegurovida = models.BooleanField(verbose_name='¿Pago Del Seguro De Vida?', default=False)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    numeroasientoctb = models.IntegerField(verbose_name='Número Asiento Contable', blank=True, null=True)
    boletagenerada = models.BooleanField(verbose_name='¿Boleta Generada?', blank=True, null=True)
    fechacontabilizacion = models.DateTimeField(label='Fecha De Contabilización', blank=True, null=True)
    conboleta = models.BooleanField(verbose_name='¿Con Boleta?', blank=True, null=True)

    class Meta:
        db_table = 'maestroplanilla'


class Maestroplantillaalmacenpedido(models.Model):
    id = models.AutoField(label='Id', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestroalmacen = models.ForeignKey(
        erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE,
        verbose_name='MaestroAlmacen'
    )
    idmaestroproducto = models.ForeignKey(
        erpp.inv.models.Maestroproductos,
        on_delete=models.CASCADE,
        verbose_name='MaestroProducto'
    )
    maestroarea = models.ForeignKey(
        erpp.inv.models.Areas, on_delete=models.CASCADE,
        verbose_name='MaestroArea'
    )
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    fechahoraregistro = models.DateTimeField(label='Fecha y Hora Del Registro')

    class Meta:
        db_table = 'maestroplantillaalmacenpedido'


class Maestroplats(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    descripccionplato = models.CharField(label='Descripcción Del Plato', max_length=200, blank=True, null=True)
    unidadmedida = models.ForeignKey(
        erpp.gen.models.Maestrounidadesdemedida, on_delete=models.CASCADE,
        verbose_name='UnidadMedida'
    )
    grupo = models.ForeignKey(
        erpp.inv.models.Maestrogrupos, on_delete=models.CASCADE,
        verbose_name='Grupo'
    )
    producto1 = models.ForeignKey(
        erpp.inv.models.Maestroproductos, on_delete=models.CASCADE,
        verbose_name='IDProducto1', blank=True, null=True
    )
    producto2 = models.ForeignKey(
        erpp.inv.models.Maestroproductos, on_delete=models.CASCADE,
        verbose_name='Producto2', blank=True, null=True
    )
    producto3 = models.ForeignKey(
        erpp.inv.models.Maestroproductos, on_delete=models.CASCADE,
        verbose_name='Producto3', blank=True, null=True
    )
    producto = models.ForeignKey(
        erpp.inv.models.Maestroproductos, on_delete=models.CASCADE,
        verbose_name='Producto', blank=True, null=True
    )
    lunes = models.BooleanField(verbose_name='¿Lunes?', blank=True, null=True)
    luneshoraini1 = models.DateTimeField(label='Lunes Hora Inicial 1', blank=True, null=True)
    luneshorafin1 = models.DateTimeField(label='Lunes Hora Final 1', blank=True, null=True)
    luneshoraini2 = models.DateTimeField(label='Lunes Hora Inicial 2', blank=True, null=True)
    luneshorafin2 = models.DateTimeField(label='Lunes Hora Final 2', blank=True, null=True)
    martes = models.BooleanField(verbose_name='¿Martes?', blank=True, null=True)
    marteshoraini1 = models.DateTimeField(label='Martes Hora Inicial 1', blank=True, null=True)
    marteshorafin1 = models.DateTimeField(label='Martes Hora Final 1', blank=True, null=True)
    marteshoraini2 = models.DateTimeField(label='Martes Hora Inicial 2', blank=True, null=True)
    marteshorafin2 = models.DateTimeField(label='Martes Hora Final 2', blank=True, null=True)
    miercoles = models.BooleanField(verbose_name='¿Miércoles?', blank=True, null=True)
    miercoleshoraini1 = models.DateTimeField(label='Miercoles Hora Inicial 1', blank=True, null=True)
    miercoleshorafin1 = models.DateTimeField(label='Miercoles Hora Final 1', blank=True, null=True)
    miercoleshoraini2 = models.DateTimeField(label='Miercoles Hora Inicial 2', blank=True, null=True)
    miercoleshorafin2 = models.DateTimeField(label='Miercoles Hora Final 2', blank=True, null=True)
    jueves = models.BooleanField(verbose_name='¿Jueves?', blank=True, null=True)
    jueveshoraini1 = models.DateTimeField(label='Jueves Hora Inicial 1', blank=True, null=True)
    jueveshorafin1 = models.DateTimeField(label='Jueves Hora Final 1', blank=True, null=True)
    juveshoraini2 = models.DateTimeField(label='Juves Hora Inicial 2', blank=True, null=True)
    jueveshorafin2 = models.DateTimeField(label='Jueves Hora Final 2', blank=True, null=True)
    viernes = models.BooleanField(verbose_name='¿Viernes?', blank=True, null=True)
    vierneshoraini1 = models.DateTimeField(label='Viernes Hora Inicial 1', blank=True, null=True)
    vierneshorafin1 = models.DateTimeField(label='Viernes Hora Final 1', blank=True, null=True)
    vierneshoraini2 = models.DateTimeField(label='Viernes Hora Inicial 2', blank=True, null=True)
    vierneshorafin2 = models.DateTimeField(label='Viernes Hora Final 2', blank=True, null=True)
    sabado = models.BooleanField(verbose_name='¿Sábado?', blank=True, null=True)
    sabhoraini1 = models.DateTimeField(label='Sábado Hora Inicial 1', blank=True, null=True)
    sabhorafin1 = models.DateTimeField(label='Sábado Hora Final 1', blank=True, null=True)
    sabhoraini2 = models.DateTimeField(label='Sábado Hora Inicial 2', blank=True, null=True)
    sabhorafin2 = models.DateTimeField(label='Sábado Hora Final 2', blank=True, null=True)
    domingo = models.BooleanField(verbose_name='¿Domingo?', blank=True, null=True)
    domhoraini1 = models.DateTimeField(label='Domingo Hora Inicial 1', blank=True, null=True)
    domhorafin1 = models.DateTimeField(label='Domingo Hora Final 1', blank=True, null=True)
    domhoraini2 = models.DateTimeField(label='Domingo Hora Inicial 2', blank=True, null=True)
    domhorafin2 = models.DateTimeField(label='Domingo Hora Final 2', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa', blank=True, null=True
    )

    class Meta:
        db_table = 'maestroplats'


class Maestroprecios(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    codigosucursal = models.CharField(label='Código De La Sucursal', max_length=20)
    maestroproducto = models.ForeignKey(
        erpp.inv.models.Maestroproductos, on_delete=models.CASCADE,
        verbose_name='MaestroProducto'
    )
    codigoproducto = models.CharField(label='Código Del Producto', max_length=20)
    fechavigencia = models.DateTimeField(label='Fecha De Vigencia')
    descripcion = models.CharField(label='Descripción', max_length=60)
    precioventasoles = models.DecimalField(label='Precio De Venta En Soles', max_digits=11, decimal_places=2)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    precioventadolares = models.DecimalField(label='Precio De Venta Dólares', max_digits=13, decimal_places=4)
    porcentaje1 = models.DecimalField(label='Porcentaje 1', max_digits=5, decimal_places=2)
    porcentaje2 = models.DecimalField(label='Porcentaje 2', max_digits=5, decimal_places=2)
    porcentaje3 = models.DecimalField(label='Porcentaje 3', max_digits=5, decimal_places=2)
    preciototalsoles = models.DecimalField(label='Precio Total En Soles', max_digits=11, decimal_places=2)
    preciototaldolares = models.DecimalField(label='Precio Total En Dólares', max_digits=13, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroprecios'


class Maestrotipocliente(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    codigotipocliente = models.CharField(label='Codigo Tipo De Cliente', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipocliente'


class Maestroturnoscaja(models.Model):
    id = models.AutoField(label='Id', primary_key=True)
    maestrocajero = models.ForeignKey(
        erpp.fac.models.Maestrocajeros, on_delete=models.CASCADE,
        verbose_name='MaestroCajero'
    )
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    descripcion = models.CharField(label='Descripción', max_length=500)
    fechainicio = models.DateTimeField(label='Fecha De Inicio')
    fechafin = models.DateTimeField(label='Fecha De Finalización')
    horainicio = models.TimeField(label='Hora De Inicio', blank=True, null=True)
    horafin = models.TimeField(label='Hora De Finalización', blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=500)
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=500)
    turnocerrado = models.BooleanField(verbose_name='¿Turno Cerrado?', blank=True, null=True)

    class Meta:
        db_table = 'maestroturnoscaja'


class Maestrovehiculo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    placarodaje = models.CharField(label='Placa De Rodaje', max_length=75)
    color = models.CharField(label='Color', max_length=75)
    tipo = models.CharField(label='Tipo', max_length=75)
    maestromarca = models.ForeignKey(
        erpp.conta.models.Vehiculomarca, on_delete=models.CASCADE,
        verbose_name='MaestroMarca'
    )
    motor = models.CharField(label='Motor', max_length=75)
    modelo = models.CharField(label='Modelo', max_length=75)
    chasis = models.CharField(label='Chasis', max_length=75)
    nrounidad = models.CharField(label='Número De Unidad', max_length=75)
    kilometraje = models.IntegerField(verbose_name='Kilometraje')
    anhiofabricacion = models.IntegerField(verbose_name='Año De Fabricación')
    placaoval = models.CharField(label='Placa Oval', max_length=100)
    maestrocliente = models.ForeignKey(
        erpp.fac.models.Maestroclientes, on_delete=models.CASCADE,
        verbose_name='MaestroCliente'
    )
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    tallerasesores = models.ForeignKey(
        erpp.serv.models.Tallerasesores, on_delete=models.CASCADE,
        verbose_name='TallerAsesores', blank=True, null=True
    )
    coordenadax = models.DecimalField(label='Coordenada X', max_digits=18, decimal_places=6, blank=True, null=True)
    coordenaday = models.DecimalField(label='Coordenada Y', max_digits=18, decimal_places=6, blank=True, null=True)
    piso = models.ForeignKey(
        erpp.gen.models.Maestromaterialconstruccion, on_delete=models.CASCADE,
        verbose_name='Piso', blank=True, null=True
    )
    maestrooperacion = models.ForeignKey(
        erpp.gen.models.Maestrooperacion, on_delete=models.CASCADE,
        verbose_name='MaestroOperacion', blank=True, null=True
    )
    pertenencia = models.CharField(label='Pertenencia', max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'maestrovehiculo'


class Maestrovehiculoaccesorios(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    descripcion = models.CharField(label='Descripción', max_length=50)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrovehiculoaccesorios'


class Maestrovehiculoestado(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    descripcion = models.CharField(label='Descripción', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrovehiculoestado'


class Maestrovehiculocombustible(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    descripcion = models.CharField(label='Descripción', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrovehiculocombustible'


class Maestrovendedores(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    codigosucursal = models.CharField(label='Código De La Sucursal', max_length=20)
    codigovendedor = models.CharField(label='Código Del Vendedor', max_length=20)
    nombrevendedor = models.CharField(label='Nombre Del Vendedor', max_length=150)
    direccion = models.CharField(label='Direccion', max_length=200)
    telefono = models.CharField(label='Teléfono', max_length=25)
    fechaingreso = models.DateTimeField(label='Fecha De Ingreso')
    tipo = models.CharField(label='Tipo', max_length=20)
    metaventasoles = models.DecimalField(label='Meta De Venta En Soles', max_digits=11, decimal_places=2)
    metaventadolares = models.DecimalField(label='Meta De Venta En Dólares', max_digits=13, decimal_places=4)
    metacobranzasoles = models.DecimalField(label='Meta De Cobranza En Soles', max_digits=11, decimal_places=2)
    metacobranzadolares = models.DecimalField(label='Meta De Cobranza En Dólares', max_digits=13, decimal_places=4)
    comisionsoles = models.DecimalField(label='Comisión En Soles', max_digits=11, decimal_places=2)
    comisiondolares = models.DecimalField(label='Comisión Dólares', max_digits=13, decimal_places=4)
    garantias = models.CharField(label='Garantóas', max_length=200)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    codigoservidor = models.CharField(label='Codigo Del Servidor', max_length=20, blank=True, null=True)
    usuariosistema = models.ForeignKey(
        erpp.inv.models.Usuarioalmacen, on_delete=models.CASCADE,
        verbose_name='UsuarioSistema', blank=True, null=True
    )

    class Meta:
        db_table = 'maestrovendedores'
        unique_together = (('codigovendedor', 'idmaestroempresa'),)


class Maestroversionmodelo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    nombreversion = models.CharField(label='Nombre De La Versión', max_length=100)
    vehiculomodelo = models.ForeignKey(
        erpp.conta.models.Vehiculomodelo, on_delete=models.CASCADE,
        verbose_name='VehiculoModelo'
    )
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroversionmodelo'


class Ordencompraclientecabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    fechadocumento = models.DateField(label='Fecha De Documento')
    numerodocumento = models.IntegerField(verbose_name='Número De Documento', blank=True, null=True)
    solicituddeproductocabecera = models.ForeignKey(erpp.fac.models.Solicituddeproductocabecera, on_delete=models.CASCADE, verbose_name='SolicituddeProductoCabecera')
    maestrocliente = models.ForeignKey(Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroCliente')
    maestromoneda = models.ForeignKey(erpp.gen.models.Maestromoneda, on_delete=models.CASCADE, verbose_name='MaestroMoneda')
    maestrotipocambio = models.ForeignKey(erpp.gen.models.Maestrotipodecambio, on_delete=models.CASCADE, verbose_name='MaestroTipoCambio')
    totaligvsoles = models.DecimalField(label='Total De IGV En Soles', max_digits=11, decimal_places=2, blank=True, null=True)
    totaligvdolares = models.DecimalField(label='Total De IGV En Dólares', max_digits=11, decimal_places=4, blank=True, null=True)
    totalsoles = models.DecimalField(label='Total En Soles', max_digits=11, decimal_places=2)
    totaldolares = models.DecimalField(label='Total En Dólares', max_digits=13, decimal_places=4)
    tiempoentrega = models.CharField(label='Tiempo De Entrega', max_length=50, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    estadodocumento = models.CharField(label='Estado Del Documento', max_length=50, blank=True, null=True)
    observacion = models.TextField(label='Observación', blank=True, null=True)

    class Meta:
        db_table = 'ordencompraclientecabecera'


class Ordencompraclientedetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    ordencompraclientecabecera = models.ForeignKey(Ordencompraclientecabecera, on_delete=models.CASCADE, verbose_name='OrdenCompraClienteCabecera')
    cotizacionclientedetalle = models.ForeignKey(erpp.fac.models.Cotizacionclientedetalle, on_delete=models.CASCADE, verbose_name='CotizacionClienteDetalle', blank=True, null=True)
    preciounitariosoles = models.DecimalField(label='Precio Unitario En Soles', max_digits=11, decimal_places=2)
    preciounitariodolares = models.DecimalField(label='Precio Unitario En Dólares', max_digits=13, decimal_places=4)
    maestroproducto = models.ForeignKey(erpp.inv.models.Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    porcentajedescuento = models.DecimalField(label='Porcentaje De Descuento', max_digits=10, decimal_places=4, blank=True, null=True)
    descuentomontosoles = models.DecimalField(label='Descuento Del Monto En Soles', max_digits=12, decimal_places=4, blank=True, null=True)
    descuentomontodolares = models.DecimalField(label='Descuento Del Monto En Dólares', max_digits=12, decimal_places=4, blank=True, null=True)
    subtotalsoles = models.DecimalField(label='Subtotal En Soles', max_digits=11, decimal_places=2)
    subtotaldolares = models.DecimalField(label='Subtotal En Dólares', max_digits=13, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    esproducto = models.BooleanField(verbose_name='¿Es Producto?', blank=True, null=True)

    class Meta:
        db_table = 'ordencompraclientedetalle'


class Preciario(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestrosmodelo = models.ForeignKey(erpp.fac.models.Maestroversionmodelo, on_delete=models.CASCADE, verbose_name='MaestrosModelo')
    nombremodelo = models.CharField(label='Nombre Del Modelo', max_length=80)
    version = models.CharField(label='Versión', max_length=20)
    numeromotor = models.CharField(label='Número De Motor', max_length=80)
    transmision = models.CharField(label='Transmisión', max_length=80)
    maestrotrabajotaller = models.ForeignKey(erpp.cita.models.Maestrotrabajotaller, on_delete=models.CASCADE, verbose_name='MaestroTrabajoTaller')
    mantenimiento = models.CharField(label='Mantenimiento', max_length=80)
    montoproductos = models.DecimalField(label='Monto De Productos', max_digits=11, decimal_places=2)
    montomanoobra = models.DecimalField(label='Monto De Mano De Obra', max_digits=11, decimal_places=2, blank=True, null=True)
    montomateriales = models.DecimalField(label='Monto De Materiales', max_digits=11, decimal_places=2, blank=True, null=True)
    maestroactividadtaller = models.ForeignKey(erpp.serv.models.Maestroactividadtaller, on_delete=models.CASCADE, verbose_name='MaestroActividadTaller', blank=True, null=True)
    tiempominutos = models.IntegerField(verbose_name='Tiempo En Minutos', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'preciario'


class Recetas(models.Model):
    principal = models.ForeignKey(erpp.inv.models.Principalgrupo, verbose_name='Principal', blank=True, null=True)
    componente = models.ForeignKey(erpp.inv.models.Componenteproducto, verbose_name='Componente', blank=True, null=True)
    cantidad = models.FloatField(verbose_name='Cantidad', blank=True, null=True)
    f4 = models.CharField(label='F4', max_length=255, blank=True, null=True)
    f5 = models.CharField(label='F5', max_length=255, blank=True, null=True)
    f6 = models.CharField(label='F6', max_length=255, blank=True, null=True)
    f7 = models.CharField(label='F7', max_length=255, blank=True, null=True)
    f8 = models.CharField(label='F8', max_length=255, blank=True, null=True)
    f9 = models.CharField(label='F9', max_length=255, blank=True, null=True)
    f10 = models.CharField(label='F10', max_length=255, blank=True, null=True)
    f11 = models.CharField(label='F11', max_length=255, blank=True, null=True)
    f12 = models.CharField(label='F12', max_length=255, blank=True, null=True)
    f13 = models.CharField(label='F13', max_length=255, blank=True, null=True)
    f14 = models.CharField(label='F14', max_length=255, blank=True, null=True)
    f15 = models.CharField(label='F15', max_length=255, blank=True, null=True)
    f16 = models.CharField(label='F16', max_length=255, blank=True, null=True)
    f17 = models.CharField(label='F17', max_length=255, blank=True, null=True)
    f18 = models.CharField(label='F18', max_length=255, blank=True, null=True)
    f19 = models.CharField(label='F19', max_length=255, blank=True, null=True)
    f20 = models.CharField(label='F20', max_length=255, blank=True, null=True)
    f21 = models.CharField(label='F21', max_length=255, blank=True, null=True)
    f22 = models.CharField(label='F22', max_length=255, blank=True, null=True)
    f23 = models.CharField(label='F23', max_length=255, blank=True, null=True)
    f24 = models.CharField(label='F24', max_length=255, blank=True, null=True)
    f25 = models.CharField(label='F25', max_length=255, blank=True, null=True)
    f26 = models.CharField(label='F26', max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'recetas'


class Saldoscaja(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20)
    esdebe = models.BooleanField(verbose_name='EsDebe')
    importesoles = models.DecimalField(label='Importe En Soles', max_digits=10, decimal_places=2)
    importedolares = models.DecimalField(label='Importe En Dólares', max_digits=10, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'saldoscaja'


class Solicituddeproductocabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestrocliente = models.ForeignKey(Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroCliente')
    fechasolicitud = models.DateField(label='Fecha De Solicitud')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'solicitudseproductocabecera'


class Solicituddeproductodetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    solicituddeproductocabecera = models.ForeignKey(Solicituddeproductocabecera, on_delete=models.CASCADE, verbose_name='SolicitudDeProductoCabecera')
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    maestroproducto = models.ForeignKey(erpp.inv.models.Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    modelo = models.CharField(label='Modelo', max_length=50)
    numero = models.IntegerField(verbose_name='Número')
    anhio = models.IntegerField(verbose_name='Año')
    unidad = models.CharField(label='Unidad', max_length=50)
    chasis = models.CharField(label='Chasis', max_length=50)
    motor = models.CharField(label='Motor', max_length=50)
    observacion = models.CharField(label='Observación', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'solicituddeproductodetalle'


class Solicitudhotlinecabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestrocliente = models.ForeignKey(Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroCliente')
    fechasolicitud = models.DateField(label='Fecha De Solicitud')
    numerosolicitud = models.CharField(label='Número De Solicitud', max_length=20)
    solicitante = models.CharField(label='Solicitante', max_length=100)
    prioridad = models.CharField(label='Prioridad', max_length=5)
    ordentaller = models.CharField(label='Orden Del Taller', max_length=20)
    tipoordentaller = models.CharField(label='Tipo De Orden Del Taller', max_length=75)
    asesor = models.CharField(label='Asesor', max_length=100)
    tecnico = models.CharField(label='Técnico', max_length=100)
    maestrovehiculo = models.ForeignKey(Maestrovehiculo, on_delete=models.CASCADE, verbose_name='MaestroVehiculo')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'solicitudhotlinecabecera'


class Solicitudhotlinedetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    solicitudhotlinecabecera = models.ForeignKey(Solicitudhotlinecabecera, on_delete=models.CASCADE, verbose_name='SolicitudHotLineCabecera')
    maestroproducto = models.ForeignKey(erpp.inv.models.Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    almacenubicacionproducto = models.ForeignKey(erpp.inv.models.Almacenubicacionproducto, on_delete=models.CASCADE, verbose_name='AlmacenUbicacionProducto')
    cf = models.CharField(label='CF', max_length=50, blank=True, null=True)
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    observacion = models.CharField(label='Observación', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'solicitudhotlinedetalle'


class Solicitudnotacredito(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    fechasolicitud = models.DateTimeField(label='Fecha De Solicitud')
    motivo = models.CharField(label='Motivo', max_length=20)
    otromotivo = models.BooleanField(verbose_name='Otro Motivo')
    detallemotivo = models.CharField(label='Detalle Del Motivo', max_length=500)
    maestroproducto = models.ForeignKey(erpp.inv.models.Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    facturaproveedordetalle = models.ForeignKey(erpp.cmp.models.Facturasproveedoresdetalle, on_delete=models.CASCADE, verbose_name='FacturaProveedorDetalle')
    productounitarioimagen = models.ForeignKey(erpp.inv.models.Productounitarioimagen, on_delete=models.CASCADE, verbose_name='ProductoUnitarioImagen')
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    empresa = models.CharField(label='Empresa', max_length=50, blank=True, null=True)
    direccion = models.CharField(label='Dirección', max_length=50, blank=True, null=True)
    ruc = models.CharField(label='RUC', max_length=50, blank=True, null=True)
    telefono = models.CharField(label='Teléfono', max_length=50, blank=True, null=True)
    email = models.CharField(label='Email', max_length=50, blank=True, null=True)
    contacto = models.CharField(label='Contacto', max_length=50, blank=True, null=True)
    fechafactura = models.DateTimeField(label='Fecha De Factura', blank=True, null=True)
    producto = models.CharField(label='Producto', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'solicitudnotacredito'


class Solicitudnotacreditoproductounitarioimagen(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    productounitarioimagen = models.ForeignKey(erpp.inv.models.Productounitarioimagen, on_delete=models.CASCADE, verbose_name='ProductoUnitarioImagen')
    solicitudnotacredito = models.ForeignKey(Solicitudnotacredito, on_delete=models.CASCADE, verbose_name='SolicitudNotaCredito')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'solicitudnotacreditoproductounitarioimagen'


class Tallerfactura(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    facturaclientecabecera = models.ForeignKey(Facturaclientecabecera, on_delete=models.CASCADE, verbose_name='FacturaClienteCabecera')
    ordenserviciocabecera = models.ForeignKey(erpp.serv.models.Ordenserviciocabecera, on_delete=models.CASCADE, verbose_name='OrdenServicioCabecera')
    servicioportercerocabecera = models.ForeignKey(erpp.serv.models.Servicioportercerocabecera, on_delete=models.CASCADE, verbose_name='ServicioPorTerceroCabecera')
    hojacalidad = models.ForeignKey(erpp.gen.models.Hojacalidad, on_delete=models.CASCADE, verbose_name='HojaCalidad')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'tallerfactura'


class Vendedormetaobjetivo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestrovendedor = models.ForeignKey(Maestrovendedores, on_delete=models.CASCADE, verbose_name='MaestroVendedor')
    vehiculomodelo = models.ForeignKey(erpp.conta.models.Vehiculomodelo, on_delete=models.CASCADE, verbose_name='VehiculoModelo')
    cantidadplanificada = models.IntegerField(verbose_name='Cantidad Planificada')
    cantidadalcanzada = models.IntegerField(verbose_name='Cantidad Alcanzada')
    fechainicio = models.DateTimeField(label='Fecha De Inicio')
    fechafin = models.DateTimeField(label='Fecha De Finalización')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'vendedormetaobjetivo'


class Ventadescuento(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcion = models.CharField(label='Descripción', max_length=250)
    porcentaje = models.DecimalField(label='Porcentaje', max_digits=5, decimal_places=2)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=50)
    autorizado = models.CharField(label='Autorizado', max_length=50)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'ventadescuento'


class Viaaprobacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    descripcion = models.CharField(label='Descripción', max_length=100)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'viaaprobacion'
