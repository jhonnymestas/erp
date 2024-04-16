from django.db import models

# Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from django.core.exceptions import ValidationError

import erpp.conta.models
import erpp.fac.models
import erpp.gen.models
import erpp.inv.models
import erpp.per.models
import erpp.serv.models

from erpp.bases.models import ClaseModelo
from erpp.inv.models import Producto


class Proveedor(ClaseModelo):
    descripcion = models.CharField("Razón Social", max_length=100, unique=True)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    ruc = models.CharField(max_length=11, null=True, blank=True)
    dni = models.CharField(max_length=8, null=True, blank=True)
    cel1 = models.CharField("Celular 1", max_length=15, default="")
    cel2 = models.CharField("Celular 2", max_length=15, default="", blank=True)
    nacional = models.BooleanField("Nacional/Extranjero", default=False, null=True)
    pais = models.CharField(max_length=30, null=True, blank=True)
    ctacont = models.CharField("Cuenta Compras", max_length=15, default="", blank=True)
    ctadet = models.CharField("Cuenta Detracción", max_length=20, default="", blank=True)

    def clean(self):
        if not len(self.cel1) >= 9:
            raise ValidationError(
                {'cel1': "Celular 1 NO VALIDO"})

    def clean(self):
        if isinstance(self.ruc, type(None)):
            if isinstance(self.dni, type(None)):
                raise ValidationError(
                    {'ruc': "Debe Llenar RUC"})

    def __str__(self):
        return f"{self.descripcion} {self.ruc}"

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.direccion = self.direccion.upper()
        self.contacto = self.contacto.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = "Proveedores"


class ComprasEnc(ClaseModelo):
    fecha_compra = models.DateField(null=True, blank=True)
    observacion = models.TextField(blank=True, null=True)
    no_factura = models.CharField(max_length=100)
    fecha_factura = models.DateField()
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        if self.sub_total == None or self.descuento == None:
            self.sub_total = 0
            self.descuento = 0
            
        self.total = self.sub_total - self.descuento
        super(ComprasEnc, self).save()

    class Meta:
        verbose_name_plural = "Encabezado Compras"
        verbose_name = "Encabezado Compra"


class ComprasDet(ClaseModelo):
    compra = models.ForeignKey(ComprasEnc, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio_prv = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    costo = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio_prv))
        self.total = self.sub_total - float(self.descuento)
        super(ComprasDet, self).save()
    
    class Mega:
        verbose_name_plural = "Detalles Compras"
        verbose_name = "Detalle Compra"


@receiver(post_delete, sender=ComprasDet)
def detalle_compra_borrar(sender, instance, **kwargs):
    id_producto = instance.producto.id
    id_compra = instance.compra.id

    enc = ComprasEnc.objects.filter(pk=id_compra).first()
    if enc:
        sub_total = ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('sub_total'))
        descuento = ComprasDet.objects.filter(compra=id_compra).aggregate(Sum('descuento'))
        enc.sub_total = sub_total['sub_total__sum']
        enc.descuento = descuento['descuento__sum']
        enc.save()
    
    prod = Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) - int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()


@receiver(post_save, sender=ComprasDet)
def detalle_compra_guardar(sender, instance, **kwargs):
    id_producto = instance.producto.id
    fecha_compra = instance.compra.fecha_compra

    prod = Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) + int(instance.cantidad)
        prod.existencia = cantidad
        prod.ultima_compra = fecha_compra
        prod.save()


class Facturasproveedorescabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursaleses = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales',
        blank=True,
        null=True
    )
    ordencompracabecera = models.ForeignKey(
        erpp.cmp.models.Ordencompracabecera,
        on_delete=models.CASCADE,
        verbose_name='OrdenCompraCabecera',
        blank=True,
        null=True
    )
    maestroformadepago = models.ForeignKey(
        erpp.gen.models.Maestroformasdepago,
        on_delete=models.CASCADE,
        verbose_name='MaestroFormaDePago',
        blank=True,
        null=True)
    periodo = models.CharField(label='Periodo', max_length=15)
    numerooperacion = models.CharField(label='Número De Operación', max_length=15)
    maestroproveedores = models.ForeignKey(
        erpp.gen.models.Maestroproveedores,
        on_delete=models.CASCADE,
        verbose_name='MaestroProveedor'
    )
    codigoproveedor = models.CharField(label='Código De Proveedor', max_length=20)
    maestromotivofacturaproveedor = models.ForeignKey(
        erpp.cmp.models.Maestromotivosfacturaproveedor,
        on_delete=models.CASCADE,
        verbose_name='MaestroMotivoFacturaProveedor'
    )
    maestrotipomovimiento = models.ForeignKey(
        erpp.per.models.Maestrotipomovimiento,
        on_delete=models.CASCADE,
        verbose_name='MaestroTipoMovimiento'
    )
    tipomovimiento = models.CharField(label='Tipo De Movimiento', max_length=15)
    seriedocumentofb = models.CharField(label='Serie De Documento Factura/Boleta', max_length=20)
    numerodocumentofb = models.CharField(label='Número De Documento Factura/Boleta', max_length=20)
    maestrodocumentosunat = models.IntegerField(verbose_name='Maestro Documento Sunat')
    documentosunat = models.CharField(label='Documento Sunat', max_length=50)
    fechadocumento = models.DateTimeField(label='Fecha De Documento')
    conceptocompra = models.TextField(label='Concepto De Compra')
    igv = models.BooleanField(verbose_name='¿IGV?', default=False)
    solidaridad = models.BooleanField(verbose_name='¿Solidaridad?', default=False)
    asientogenerado = models.CharField(label='Asiento Generado', max_length=15)
    maestromoneda = models.IntegerField(verbose_name='Maestro Moneda')
    moneda = models.CharField(label='Moneda', max_length=15)
    fechacancelacion = models.DateTimeField(label='Fecha De Cancelación')
    maestrotipodecambio = models.ForeignKey(
        erpp.gen.models.Maestrotipodecambio,
        on_delete=models.CASCADE,
        verbose_name='MaestroTipoDeCambio'
    )
    tipocambio = models.DecimalField(label='Tipo De Cambio', max_digits=13, decimal_places=3)
    montosoles = models.DecimalField(label='Monto En Soles', max_digits=11, decimal_places=2)
    montodolares = models.DecimalField(label='Monto En Dólares', max_digits=13, decimal_places=3)
    igvsoles = models.DecimalField(label='IGV En Soles', max_digits=11, decimal_places=2)
    igvdolares = models.DecimalField(label='IGV En Dólares', max_digits=13, decimal_places=3)
    otrosmontossoles = models.DecimalField(label='Otros Montos En Soles', max_digits=11, decimal_places=2)
    otrosmontosdolares = models.DecimalField(label='Otros Montos En Dólares', max_digits=13, decimal_places=3)
    fechacontabilizacion = models.DateTimeField(label='Fecha De Contabilización')
    montototalsoles = models.DecimalField(label='Monto Total En Soles', max_digits=11, decimal_places=2)
    montototaldolares = models.DecimalField(label='Monto Total En Dólares', max_digits=13, decimal_places=3)
    codigocuentatotalventa = models.CharField(label='Código De Cuenta Total De Venta', max_length=15)
    voucher = models.CharField(label='Voucher', max_length=20)
    refcaja = models.CharField(label='RefCaja', max_length=500)
    anulada = models.BooleanField(verbose_name='¿Anulada?', default=False)
    fechallegada = models.DateTimeField(label='Fecha De Llegada')
    glosa = models.TextField(label='Glosa', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=1000)
    estado = models.IntegerField(verbose_name='Estado', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestrocentrocosto = models.ForeignKey(
        erpp.gen.models.Maestrocentrosdecostos,
        on_delete=models.CASCADE,
        verbose_name='MaestroCentroCosto',
        blank=True,
        null=True
    )
    aprobado = models.BooleanField(verbose_name='¿Aprobado?', blank=True, null=True)
    tipoigv = models.CharField(label='Tipo IGV', max_length=50, blank=True, null=True)
    ordenpedido = models.ForeignKey(
        erpp.serv.models.Ordenpedido,
        on_delete=models.CASCADE,
        verbose_name='OrdenPedido',
        blank=True,
        null=True
    )
    fechadetraccion = models.DateField(label='Fecha De Detracción', blank=True, null=True)
    docreferencia = models.ForeignKey(
        erpp.per.models.Personalreferencialaboral,
        on_delete=models.CASCADE,
        verbose_name='DocumentoReferencia',
        blank=True,
        null=True
    )
    seriereferencia = models.CharField(label='Serie De Referencia', max_length=50, blank=True, null=True)
    numeroreferencia = models.CharField(label='Número De Referencia', max_length=50, blank=True, null=True)
    numerocomprobantedetraccion = models.CharField(
        label='Número Comprobante De Detracción',
        max_length=10,
        blank=True,
        null=True
    )
    seriedocretencion = models.CharField(label='Serie Del Documento De Retención', max_length=5, blank=True, null=True)
    numerodocretencion = models.CharField(
        label='Número Del Documento De Retención',
        max_length=10,
        blank=True,
        null=True
    )
    retencion = models.BooleanField(verbose_name='¿Retención?', blank=True, null=True)
    montoretencion = models.DecimalField(
        label='Monto De Retención',
        max_digits=13,
        decimal_places=2,
        blank=True,
        null=True
    )
    fechavencimiento = models.DateTimeField(label='Fecha De Vencimiento', blank=True, null=True)
    montodetraccion = models.DecimalField(
        label='Monto De Detracción',
        max_digits=13,
        decimal_places=2,
        blank=True,
        null=True
    )
    montopercepcion = models.DecimalField(
        label='Monto De Percepción',
        max_digits=13,
        decimal_places=2,
        blank=True,
        null=True
    )
    distribucioncentrocosto = models.IntegerField(verbose_name='Distribución Centro De Costo', blank=True, null=True)
    esgasto = models.BooleanField(verbose_name='¿Es Gasto?', blank=True, null=True)
    observaciones = models.TextField(label='Observaciones', blank=True, null=True)
    almacencabecera = models.IntegerField(verbose_name='Almacen Cabecera', blank=True, null=True)
    bolsas = models.DecimalField(label='Bolsas', max_digits=9, decimal_places=2, blank=True, null=True)
    igvporcentaje = models.DecimalField(
        label='Porcentaje de IGV',
        max_digits=13,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'facturasproveedorescabecera'


class Facturasproveedoresdetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    facturaproveedorcabecera = models.ForeignKey(
        Facturasproveedorescabecera,
        on_delete=models.CASCADE,
        label='FacturaProveedorCabecera')
    numerodocumentofb = models.CharField(label='Número De Documento Factura/Boleta', max_length=20)
    seriedocumentofb = models.CharField(label='Serie De Documento Factura/Boleta', max_length=20)
    maestroproducto = models.ForeignKey(
        erpp.inv.models.Maestroproductos,
        on_delete=models.CASCADE,
        verbose_name='MaestroProductos'
    )
    codigoproducto = models.CharField(label='Código De Producto', max_length=20)
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    preciounitariosoles = models.DecimalField(label='Precio Unitario EnSoles', max_digits=11, decimal_places=4)
    preciounitariodolares = models.DecimalField(label='Precio Unitario En Dólares', max_digits=13, decimal_places=4)
    numerooperacion = models.CharField(label='Número De Operación', max_length=20)
    numeroembarque = models.CharField(label='Número De Embarque', max_length=15)
    numerocase = models.CharField(label='Número Case', max_length=5)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    subtotaldolares = models.DecimalField(
        label='SubTotal En Dólares',
        max_digits=18,
        decimal_places=4,
        blank=True,
        null=True
    )
    subtotalsoles = models.DecimalField(
        label='SubTotal En Soles',
        max_digits=18,
        decimal_places=4,
        blank=True,
        null=True
    )
    maestrocentrocosto = models.ForeignKey(
        erpp.gen.models.Maestrocentrosdecostos,
        on_delete=models.CASCADE,
        verbose_name='MaestroCentroCostos',
        blank=True,
        null=True
    )
    ctactbdiscentrocosto = models.CharField(
        label='Cuenta Contable Dis Centro Costo',
        max_length=50,
        blank=True,
        null=True
    )
    distribucioncentrocosto = models.ForeignKey(
        erpp.conta.models.Distribucioncentrocostocabecera,
        on_delete=models.CASCADE,
        verbose_name='DistribucionCentroCostoCabecera',
        blank=True,
        null=True
    )
    conceptolibre = models.CharField(label='Concepto Libre', max_length=200, blank=True, null=True)
    sinigvcheck = models.BooleanField(verbose_name='¿Sin IGV Check?', blank=True, null=True)
    amarrecabecera = models.ForeignKey(
        erpp.conta.models.Amarrecabecera,
        on_delete=models.CASCADE,
        verbose_name='AmarreCabecera',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'facturasproveedoresdetalle'


class Maestroformasdepagocompras(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    codigoformapago = models.CharField(label='Código Forma De Pago', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=50)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroformasdepagocompras'


class Maestromotivosfacturaproveedor(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    motivo = models.CharField(label='Motivo', max_length=10)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestromotivosfacturaproveedor'


class Maestroporcentajedetraccion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    descripcion = models.CharField(label='Descripción', max_length=500)
    porcentaje = models.DecimalField(label='Porcentaje', max_digits=11, decimal_places=2)
    normativa = models.CharField(label='Normativa', max_length=50, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    esdetraccion = models.BooleanField(verbose_name='¿Es Detracción?', default=False)

    class Meta:
        db_table = 'maestroporcentajedetraccion'


class Maestrotipoproveedores(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    tipoproveedor = models.CharField(label='Tipo De Proveedor', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipoproveedores'
        unique_together = (('idmaestroempresas', 'tipoproveedor'),)


class Maestroestadosordencompra(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    estadoordencompra = models.CharField(label='Estado Orden De Compra', max_length=10)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroestadosordencompra'


class Ordencompracabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    serieorden = models.CharField(label='Serie De Orden', max_length=5, blank=True, null=True)
    numeroorden = models.CharField(label='Número De Orden', max_length=5)
    almacencabecera = models.ForeignKey(
        erpp.inv.models.Almacencabecera,
        on_delete=models.CASCADE,
        verbose_name='AlmacenCabecera'
    )
    maestroalmacendestino = models.ForeignKey(
        erpp.gen.models.Maestroalmacenes,
        on_delete=models.CASCADE,
        verbose_name='MaestroAlmacenDestino'
    )
    numerorequerimiento = models.CharField(label='Número De Requerimiento', max_length=20)
    fechaoperacion = models.DateField(label='Fecha De Operación')
    fechaentrega = models.DateField(label='Fecha De Entrega')
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
    maestroproveedores = models.ForeignKey(
        erpp.gen.models.Maestroproveedores,
        on_delete=models.CASCADE,
        verbose_name='MaestroProveedor'
    )
    maestrocaja = models.ForeignKey(erpp.fac.models.Maestrocajas, on_delete=models.CASCADE, verbose_name='MaestroCaja')
    maestrocajachica = models.ForeignKey(
        erpp.conta.models.Cajachicacabecera,
        on_delete=models.CASCADE,
        verbose_name='MaestroCajaChicaCabecera'
    )
    condicionespago = models.CharField(label='Condiciones De Pago', max_length=15)
    montopagoadelantadosoles = models.DecimalField(
        label='Monto De Pago Adelantado En Soles',
        max_digits=11,
        decimal_places=2
    )
    montopagoadelantadodolares = models.DecimalField(
        label='Monto De Pago Adelantado En Dólares',
        max_digits=13,
        decimal_places=4
    )
    numerodiascredito = models.IntegerField(verbose_name='Número De Días Del Crédito')
    numeroletrascredito = models.IntegerField(verbose_name='Número De Letras Del Credito')
    tipocompra = models.CharField(label='Tipo De Compra', max_length=20)
    glosa = models.CharField(label='Glosa', max_length=200)
    cotizacion = models.ForeignKey(erpp.fac.models.Cotizacion, on_delete=models.CASCADE, verbose_name='Cotizacion')
    maestroestadoordencompra = models.ForeignKey(
        Maestroestadosordencompra,
        on_delete=models.CASCADE,
        verbose_name='MaestroEstadoOrdenCompra'
    )
    sincotizacion = models.BooleanField(verbose_name='¿Sin Cotización?', default=False)
    maestrocentrodecosto = models.ForeignKey(
        erpp.gen.models.Maestrocentrosdecostos,
        on_delete=models.CASCADE,
        verbose_name='MaestroCentroDeCosto'
    )
    anulado = models.BooleanField(verbose_name='¿Anulado?', default=False)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    facturada = models.BooleanField(verbose_name='¿Facturada?', blank=True, null=True)
    codigo = models.CharField(label='Código', max_length=15, blank=True, null=True)
    recibida = models.BooleanField(verbose_name='¿Recibida?', blank=True, null=True)
    aprobado = models.BooleanField(verbose_name='¿Aprobado?', default=False)
    servicio = models.BooleanField(verbose_name='¿Servicio?', blank=True, null=True)
    maestroformadepago = models.ForeignKey(
        erpp.gen.models.Maestroformasdepago,
        on_delete=models.CASCADE,
        verbose_name='MaestroFormaDePago',
        blank=True,
        null=True
    )
    igvsoles = models.DecimalField(label='IGV En Soles', max_digits=18, decimal_places=2, blank=True, null=True)
    igvdolares = models.DecimalField(label='IGV En Dólares', max_digits=18, decimal_places=2, blank=True, null=True)
    ventasoles = models.DecimalField(label='Venta En Soles', max_digits=18, decimal_places=2, blank=True, null=True)
    ventadolares = models.DecimalField(label='Venta En Dólares', max_digits=18, decimal_places=2, blank=True, null=True)
    igv = models.BooleanField(verbose_name='IGV', blank=True, null=True)
    atencion = models.CharField(label='Atención', max_length=500, blank=True, null=True)
    firma = models.CharField(label='Firma', max_length=250, blank=True, null=True)
    idautorizadofirma = models.IntegerField(verbose_name='IdAutorizadoFirma', blank=True, null=True)
    porcentajedescuento = models.DecimalField(
        label='Porcentaje De Descuento',
        max_digits=18,
        decimal_places=4,
        blank=True,
        null=True
    )
    lugaresentrega = models.TextField(label='Lugares De Entrega', blank=True, null=True)

    class Meta:
        db_table = 'ordencompracabecera'


class Ordencompradetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    ordencompracabecera = models.ForeignKey(
        Ordencompracabecera,
        on_delete=models.CASCADE,
        verbose_name='OrdenCompraCabecera'
    )
    preciounitariosoles = models.DecimalField(label='Precio Unitario En Soles', max_digits=15, decimal_places=4)
    preciounitariodolares = models.DecimalField(label='Precio Unitario En Dólares', max_digits=13, decimal_places=4)
    maestroproductos = models.ForeignKey(
        erpp.inv.models.Maestroproductos,
        on_delete=models.CASCADE,
        verbose_name='MaestroProductos'
    )
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    subtotalsoles = models.DecimalField(label='Subtotal En Soles', max_digits=11, decimal_places=4)
    subtotaldolares = models.DecimalField(label='Subtotal En Dólares', max_digits=13, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    facturada = models.BooleanField(verbose_name='¿Facturada?', blank=True, null=True)
    cantidadfacturada = models.DecimalField(
        label='Cantidad Facturada',
        max_digits=12,
        decimal_places=5,
        blank=True,
        null=True
    )
    maestrocentrocosto = models.ForeignKey(
        erpp.gen.models.Maestrocentrosdecostos,
        on_delete=models.CASCADE,
        verbose_name='MaestroCentroCosto',
        blank=True,
        null=True
    )
    cantidadrecibida = models.DecimalField(
        label='Cantidad Recibida',
        max_digits=12,
        decimal_places=5,
        blank=True,
        null=True
    )
    recibida = models.BooleanField(verbose_name='¿Recibida?', blank=True, null=True)
    pedidodetalle = models.ForeignKey(
        erpp.inv.models.Pedidodetalle,
        on_delete=models.CASCADE,
        verbose_name='PedidoDetalle',
        blank=True,
        null=True
    )
    ctactbdiscentrocosto = models.CharField(
        label='Cuenta Contable Dis Centro Costo',
        max_length=50,
        blank=True,
        null=True
    )
    descripcionproductoref = models.CharField(
        label='Descripción Del Producto Referenciado',
        max_length=200,
        blank=True,
        null=True
    )
    unidadmedida = models.ForeignKey(
        erpp.gen.models.Maestrounidadesdemedida,
        on_delete=models.CASCADE,
        verbose_name='MaestroUnidadesMedida',
        blank=True,
        null=True
    )
    observacion = models.CharField(label='Observación', max_length=500, blank=True, null=True)
    codprodref = models.CharField(label='Cod Del Producto Referenciado', max_length=500, blank=True, null=True)
    descuento = models.DecimalField(label='Descuento', max_digits=18, decimal_places=4, blank=True, null=True)

    class Meta:
        db_table = 'ordencompradetalle'


class Proveedoresmigracion(models.Model):
    tipo_persona = models.CharField(label='Tipo Persona', max_length=255, blank=True, null=True)
    tipo_de_documento_de_identidad_del_proveedor = models.CharField(
        label='Tipo de Documento de Identidad del proveedor',
        max_length=255,
        blank=True,
        null=True
    )
    ruc = models.CharField(label='RUC', max_length=255, blank=True, null=True)
    apellidos_y_nombres_denominacion_o_razon_social_del_proveedor_field = models.CharField(
        label='Apellidos y nombres, denominación o razón social del proveedor',
        max_length=255,
        blank=True,
        null=True
    )
    cuenta = models.FloatField(verbose_name='Cuenta', blank=True, null=True)

    class Meta:
        db_table = 'proveedoresmigracion'


class Proveedorlinea(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    maestroprovedores = models.ForeignKey(
        erpp.gen.models.Maestroproveedores,
        on_delete=models.CASCADE,
        verbose_name='MaestroProvedores'
    )
    maestrolineacomerciales = models.ForeignKey(
        erpp.gen.models.Maestrolineascomerciales,
        on_delete=models.CASCADE,
        verbose_name='MaestroLineaComerciales'
    )
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'proveedorlinea'
