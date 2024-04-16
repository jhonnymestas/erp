from django.db import models

import erpp.cita.models
import erpp.fac.models
import erpp.gen.models
import erpp.inv.models
import erpp.per.models


class Guiaservicio(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    numero = models.IntegerField(verbose_name='Número')
    maestroproveedor = models.ForeignKey(erpp.gen.models.Maestroproveedores, on_delete=models.CASCADE, verbose_name='MaestroProveedor')
    numerofactura = models.CharField(label='Número De La Factura', max_length=20)
    unidad = models.CharField(label='Unidad', max_length=20)
    cotizacion = models.ForeignKey(erpp.fac.models.Cotizacion, on_delete=models.CASCADE, verbose_name='Cotizacion')
    maestromoneda = models.ForeignKey(erpp.gen.models.Maestromoneda, on_delete=models.CASCADE, verbose_name='MaestroMoneda')
    maestrotipocambio = models.ForeignKey(erpp.gen.models.Maestrotipodecambio, on_delete=models.CASCADE, verbose_name='MaestroTipoCambio')
    utilidadsoles = models.DecimalField(label='Utilidad En Soles', max_digits=11, decimal_places=2)
    utilidaddolares = models.DecimalField(label='Utilidad En Dólares', max_digits=13, decimal_places=4)
    costosoles = models.DecimalField(label='Costo En Soles', max_digits=11, decimal_places=2)
    costodolares = models.DecimalField(label='Costo En Dólares', max_digits=13, decimal_places=4)
    maestroproducto = models.ForeignKey(erpp.inv.models.Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    observacion = models.CharField(label='Observación', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'guiaservicio'


class Historiaalertasistema(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    nombremodulo = models.CharField(label='Nombre Del Módulo', max_length=100)
    asunto = models.CharField(label='Asunto', max_length=200)
    usuario = models.ForeignKey(erpp.cita.models.Usuarioweb, on_delete=models.CASCADE, verbose_name='Usuario')
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'historiaalertasistema'


class Historiaclinicadetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigalmacen = models.CharField(label='Código Del Almacen', max_length=20)
    ordenserviciocabecera = models.ForeignKey(erpp.serv.models.Ordenserviciocabecera, on_delete=models.CASCADE, verbose_name='OrdenServicioCabecera')
    numeroordenservicio = models.CharField(label='Número Orden Del Servicio', max_length=20)
    esservicio = models.BooleanField(verbose_name='¿Es Servicio?', default=False)
    maestrotiposdocumentos = models.ForeignKey(erpp.gen.models.Maestrotiposdocumentos, on_delete=models.CASCADE, verbose_name='MaestroTiposDocumentos', blank=True, null=True)
    tipomovimiento = models.CharField(label='Tipo De Movimiento', max_length=20, blank=True, null=True)
    nrodocumento = models.CharField(label='Número Del Documento', max_length=20, blank=True, null=True)
    codigoproducto = models.CharField(label='Código Del Producto', max_length=20)
    cantidad = models.DecimalField(label='Cantidad', max_digits=11, decimal_places=2)
    moneda = models.CharField(label='Moneda', max_length=20)
    preciounitario = models.DecimalField(label='Precio Unitario', max_digits=11, decimal_places=2)
    valorventa = models.DecimalField(label='Valor De La Venta', max_digits=11, decimal_places=2)
    porcentajedescuento = models.DecimalField(label='Porcentaje Del Descuento', max_digits=11, decimal_places=2)
    descuentomonto = models.DecimalField(label='Descuento Del Monto', max_digits=11, decimal_places=2)
    impuesto = models.DecimalField(label='Impuesto', max_digits=11, decimal_places=2)
    totalventa = models.DecimalField(label='Total De La Venta', max_digits=11, decimal_places=2)
    preciounitariodolares = models.DecimalField(label='Precio Unitario En Dólares', max_digits=11, decimal_places=2)
    valorventadolares = models.DecimalField(label='Valor De Venta En Dólares', max_digits=11, decimal_places=2)
    descuentomontodolares = models.DecimalField(label='Descuento Del Monto En Dólares', max_digits=11, decimal_places=2)
    impuestodolares = models.DecimalField(label='Impuesto En Dólares', max_digits=11, decimal_places=2)
    totalventadolares = models.DecimalField(label='Total De Venta En Dólares', max_digits=11, decimal_places=2)
    realizadopor = models.CharField(label='Realizado Por', max_length=100, blank=True, null=True)
    fechaoperacion = models.DateTimeField(label='Fecha De La Operación')
    descripcionservicioproducto = models.CharField(label='Descripción Del Servicio Del Producto', max_length=500, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    almacencabecera = models.ForeignKey(erpp.inv.models.Almacencabecera, on_delete=models.CASCADE, verbose_name='AlmacenCabecera', blank=True, null=True)
    valorcomprasoles = models.DecimalField(label='Valor De La Compra En Soles', max_digits=13, decimal_places=4, blank=True, null=True)
    valorcompradolares = models.DecimalField(label='Valor De La Compra En Dólares', max_digits=13, decimal_places=4, blank=True, null=True)
    esmigracion = models.BooleanField(verbose_name='¿Es Migración?', blank=True, null=True)

    class Meta:
        db_table = 'historiaclinicadetalle'


class Maestroactividadtaller(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoservicio = models.CharField(label='Código Del Servicio', max_length=20, blank=True, null=True)
    nombre = models.CharField(label='Nombre', max_length=75)
    preciosoles = models.DecimalField(label='Precio En Soles', max_digits=11, decimal_places=2)
    preciodolar = models.DecimalField(label='Precio En Dólares', max_digits=13, decimal_places=4)
    modelo = models.CharField(label='Modelo', max_length=75)
    tiempo = models.IntegerField(verbose_name='Tiempo')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    codigocuentacontable = models.CharField(label='Código Cuenta Contable', max_length=50, blank=True, null=True)
    orden = models.IntegerField(verbose_name='Orden', blank=True, null=True)

    class Meta:
        db_table = 'maestroactividadtaller'


class Maestroserviciorepuesto(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcion = models.CharField(label='Descripción', max_length=75)
    maestroactividadtaller = models.ForeignKey(Maestroactividadtaller, on_delete=models.CASCADE, verbose_name='MaestroActividadTaller')
    maestroproducto = models.ForeignKey(erpp.inv.models.Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestrosmodelo = models.ForeignKey(erpp.fac.models.Maestroversionmodelo, on_delete=models.CASCADE, verbose_name='MaestrosModelo', blank=True, null=True)
    nombremodelo = models.CharField(label='Nombre Modelo', max_length=80, blank=True, null=True)
    version = models.CharField(label='Versión', max_length=20, blank=True, null=True)
    numeromotor = models.CharField(label='Número Motor', max_length=80, blank=True, null=True)
    transmision = models.CharField(label='Transmisión', max_length=20, blank=True, null=True)
    preciario = models.ForeignKey(erpp.fac.models.Preciario, on_delete=models.CASCADE, verbose_name='Preciario', blank=True, null=True)

    class Meta:
        db_table = 'maestroserviciorepuesto'


class Maestroserviciotaller(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroactividadtaller = models.ForeignKey(Maestroactividadtaller, on_delete=models.CASCADE, verbose_name='MaestroActividadTaller')
    maestrotrabajotaller = models.ForeignKey(erpp.cita.models.Maestrotrabajotaller, on_delete=models.CASCADE, verbose_name='MaestroTrabajoTaller')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroserviciotaller'


class Maestroservicios(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoservicio = models.CharField(label='Código Del Servicio', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=80)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroservicios'


class Maestrotecnico(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigotecnico = models.CharField(label='Código Del Técnico', max_length=20)
    nombretecnico = models.CharField(label='Nombre Del Técnico', max_length=120)
    direccion = models.CharField(label='Dirección', max_length=120)
    telefono = models.CharField(label='Teléfono', max_length=25)
    fecharegistro = models.DateTimeField(label='Fecha De Registro')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    libre = models.BooleanField(verbose_name='Libre', blank=True, null=True)
    tiniciados = models.IntegerField(verbose_name='Técnicos Iniciados', blank=True, null=True)

    class Meta:
        db_table = 'maestrotecnico'


class Ordenpedido(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    numeropedido = models.CharField(label='Número Del Pedido', max_length=20)
    maestrovendedor = models.ForeignKey(erpp.fac.models.Maestrovendedores, on_delete=models.CASCADE, verbose_name='MaestroVendedor')
    codigovendedor = models.CharField(label='Código Del Vendedor', max_length=20)
    maestrocliente = models.ForeignKey(erpp.fac.models.Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroCliente')
    maestroclientey_o = models.ForeignKey(erpp.fac.models.Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroClienteY_O', blank=True, null=True)
    codigocliente = models.CharField(label='Código Del Cliente', max_length=20)
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    maestroproducto = models.ForeignKey(erpp.inv.models.Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    partenissan = models.CharField(label='Parte Nissan', max_length=20, blank=True, null=True)
    codigoproducto = models.CharField(label='Código Del Producto', max_length=20)
    maestrotipopago = models.ForeignKey(erpp.gen.models.Maestroformasdepago, on_delete=models.CASCADE, verbose_name='MaestroTipoPago')
    condicionpago = models.CharField(label='Condición De Pago', max_length=10)
    color = models.CharField(label='Color', max_length=50)
    clase = models.CharField(label='Clase', max_length=50)
    modelo = models.CharField(label='Modelo', max_length=50)
    anho = models.IntegerField(verbose_name='Año')
    carroceria = models.CharField(label='Carrocería', max_length=20)
    marca = models.CharField(label='Marca', max_length=10)
    numeroserie = models.CharField(label='Número De Serie', max_length=20)
    numeromotor = models.CharField(label='Número De Motor', max_length=15)
    ejes = models.IntegerField(verbose_name='Ejes')
    cilindros = models.DecimalField(label='Cilindros', max_digits=12, decimal_places=5)
    ruedas = models.IntegerField(verbose_name='Ruedas')
    pasajeros = models.IntegerField(verbose_name='Pasajeros')
    asientos = models.IntegerField(verbose_name='Asientos')
    puertas = models.IntegerField(verbose_name='Puertas')
    pesoseco = models.DecimalField(label='Peso Seco', max_digits=12, decimal_places=5)
    pesobruto = models.DecimalField(label='Peso Bruto', max_digits=12, decimal_places=5)
    cargautil = models.DecimalField(label='Carga Útil', max_digits=12, decimal_places=5)
    largo = models.DecimalField(label='Largo', max_digits=12, decimal_places=5)
    alto = models.DecimalField(label='Alto', max_digits=12, decimal_places=5)
    ancho = models.DecimalField(label='Ancho', max_digits=12, decimal_places=5)
    maestrovehiculocombustible = models.ForeignKey(erpp.fac.models.Maestrovehiculocombustible, on_delete=models.CASCADE, verbose_name='MaestroVehiculoCombustible')
    combustible = models.CharField(label='Combustible', max_length=10)
    distancia_ejes = models.IntegerField(verbose_name='Distancia Entre Los Ejes')
    cilindrada = models.IntegerField(verbose_name='Cilindrada')
    preciocontado = models.DecimalField(label='Precio Contado', max_digits=13, decimal_places=4)
    otrosgastos = models.DecimalField(label='Otros Gastos', max_digits=13, decimal_places=4)
    registrofiscal = models.DecimalField(label='Registro Fiscal', max_digits=13, decimal_places=4)
    descuentos = models.DecimalField(label='Descuentos', max_digits=13, decimal_places=4)
    totalprecioventa = models.DecimalField(label='Total Del Precio De Venta', max_digits=13, decimal_places=4)
    saldofinanciadomes = models.DecimalField(label='Saldo Financiado En El Mes', max_digits=13, decimal_places=4)
    observaciones = models.CharField(label='Observaciones', max_length=500)
    maestrodocumentosunat = models.ForeignKey(erpp.gen.models.Maestrodocumentossunat, on_delete=models.CASCADE, verbose_name='MaestroDocumentoSunat')
    serie = models.CharField(label='Serie', max_length=5)
    numerodocumento = models.CharField(label='Número De Documento', max_length=10)
    numerovehiculo = models.CharField(label='Número De Vehículo', max_length=5)
    valorcompradolares = models.DecimalField(label='Valor De Compra En Dólares', max_digits=13, decimal_places=4)
    tipoformadepago = models.ForeignKey(erpp.gen.models.Maestrotipoformapago, on_delete=models.CASCADE, verbose_name='TipoFormaDePago')
    codigoformadepago = models.CharField(label='Código De La Forma De Pago', max_length=20)
    descripcionotrosgastos = models.CharField(label='Descripción De Otros Gastos', max_length=500)
    observacionespedido = models.CharField(label='Observaciones Del Pedido', max_length=500)
    p_operacion = models.IntegerField(verbose_name='P Operacion')
    potencia = models.CharField(label='Potencia', max_length=50)
    capacidadm3 = models.DecimalField(label='Capacidad M3', max_digits=12, decimal_places=5)
    desplazamiento = models.IntegerField(verbose_name='Desplazamiento')
    accesorios = models.DecimalField(label='Accesorios', max_digits=12, decimal_places=5)
    dua = models.CharField(label='DUA', max_length=40)
    fechasolicitud = models.DateTimeField(label='Fecha De Solicitud')
    pedidonissan = models.CharField(label='Pedido Nissan', max_length=20)
    fechallegadaapuerto = models.DateTimeField(label='Fecha De Llegada Al Puerto')
    factura_boleta = models.BooleanField(verbose_name='¿Factura/Boleta?', default=False)
    codigocomercial = models.CharField(label='Código Comercial', max_length=20)
    numerodeseparacion = models.CharField(label='Número De Separación', max_length=20)
    codigocolorexterior = models.CharField(label='Código Del Color Exterior', max_length=5)
    codigocolorinterior = models.CharField(label='Código Del Color Interior', max_length=5)
    imprimir1 = models.CharField(label='Imprimir 1', max_length=500)
    imprimir2 = models.CharField(label='Imprimir 2', max_length=500)
    placaoval = models.CharField(label='Placa Oval', max_length=100)
    maestromoneda = models.ForeignKey(erpp.gen.models.Maestromoneda, on_delete=models.CASCADE, verbose_name='MaestroMoneda')
    moneda = models.CharField(label='Moneda', max_length=1)
    usuariomodificacion = models.CharField(label='Usuario Modificado', max_length=100)
    fechamodificacion = models.DateTimeField(label='Fecha Modificación')
    numeroseparacion = models.CharField(label='Número De Separación', max_length=20)
    numeroembarque = models.CharField(label='Número De Embarque', max_length=20)
    numerocase = models.CharField(label='Número Case', max_length=20)
    placa = models.CharField(label='Placa', max_length=20, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    estadodocumento = models.CharField(label='Estado Del Documento', max_length=50, blank=True, null=True)
    facturada = models.BooleanField(verbose_name='¿Facturada?', blank=True, null=True)
    km = models.IntegerField(verbose_name='Km', blank=True, null=True)
    fecha = models.DateField(label='Fecha', blank=True, null=True)
    llave = models.CharField(label='Llave', max_length=50, blank=True, null=True)
    lote = models.CharField(label='Lote', max_length=20, blank=True, null=True)
    maestrocliente2 = models.ForeignKey(erpp.fac.models.Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroCliente2', blank=True, null=True)
    notacreditonumero = models.CharField(label='Nota Del Crédito De Número', max_length=20, blank=True, null=True)
    notacreditoserie = models.CharField(label='Nota Del Crédito De Serie', max_length=20, blank=True, null=True)
    notacreditomonto = models.DecimalField(label='Nota Del Crédito Del Monto', max_digits=13, decimal_places=4, blank=True, null=True)
    caracteristicavehiculo = models.ForeignKey(erpp.fac.models.Maestrovehiculoaccesorios, on_delete=models.CASCADE, verbose_name='CaracteristicaVehiculo', blank=True, null=True)
    maestroproveedor = models.ForeignKey(erpp.gen.models.Maestroproveedores, on_delete=models.CASCADE, verbose_name='MaestroProveedor', blank=True, null=True)
    importeflete = models.DecimalField(label='Importe Flete', max_digits=13, decimal_places=4, blank=True, null=True)
    importetramitetarjetaplaca = models.DecimalField(label='Importe Del Trámite Tarjeta/Placa', max_digits=13, decimal_places=4, blank=True, null=True)
    maestroalmacenequipamiento = models.IntegerField(verbose_name='MaestroAlmacenEquipamiento', blank=True, null=True)
    fechallegadavehiculo = models.DateField(label='Fecha De LLegada Del Vehículo', blank=True, null=True)
    horallegadavehiculo = models.TimeField(label='Hora De Llegada Del Vehículo', blank=True, null=True)
    fechaentregavehiculo = models.DateField(label='Fecha De Entrega Del Vehículo', blank=True, null=True)
    horaentregavehiculo = models.TimeField(label='Hora De Entrega Del Vehículo', blank=True, null=True)
    codigomvc = models.CharField(label='Código MVC', max_length=2, blank=True, null=True)
    maestroequipamiento = models.IntegerField(verbose_name='MaestroEquipamiento', blank=True, null=True)

    class Meta:
        db_table = 'ordenpedido'


class Ordenpedidocliente(models.Model):
    ordenpedido = models.ForeignKey(Ordenpedido, on_delete=models.CASCADE, verbose_name='OrdenPedido', blank=True, null=True)
    maestrocliente = models.ForeignKey(erpp.fac.models.Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroCliente', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36, blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=20, blank=True, null=True)
    estado = models.IntegerField(verbose_name='Estado', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    id = models.AutoField(label='ID', primary_key=True)

    class Meta:
        db_table = 'ordenpedidocliente'


class Ordenpedidodetalle(models.Model):
    idordenpedidodetalle = models.AutoField(label='IdOrdenPedidoDetalle', primary_key=True)
    ordenpedidocabecera = models.ForeignKey(Ordenpedido, on_delete=models.CASCADE, verbose_name='OrdenPedidoCabecera')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    descripcion = models.CharField(label='Descripción', max_length=200)
    maestroproducto = models.ForeignKey(erpp.inv.models.Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto', blank=True, null=True)
    preciounitarioventasoles = models.DecimalField(label='Precio Unitario De Venta En Soles', max_digits=14, decimal_places=3)
    preciounitarioventadolares = models.DecimalField(label='Precio Unitario De Venta En Dólares', max_digits=14, decimal_places=3)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'ordenpedidodetalle'


class Ordenserviciocabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    numerotarjeta = models.CharField(label='Número De Tarjeta', max_length=75)
    maestrotipoorden = models.ForeignKey(erpp.gen.models.Maestrotipoorden, on_delete=models.CASCADE, verbose_name='MaestroTipoOrden')
    maestrocliente = models.ForeignKey(erpp.fac.models.Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroCliente')
    maestroclientefactura = models.ForeignKey(erpp.fac.models.Facturaclientecabecera, on_delete=models.CASCADE, verbose_name='MaestroClienteFactura', blank=True, null=True)
    recepcionadopor = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='RecepcionadoPor')
    fecharecepcion = models.DateTimeField(label='Fecha De Recepción')
    descripcion = models.TextField(label='Descripción')
    numerocono = models.IntegerField(verbose_name='Número Cono')
    maestroestadosdeatencion = models.ForeignKey(erpp.gen.models.Maestroestadosdeatencion, on_delete=models.CASCADE, verbose_name='MaestroEstadosDeAtencion')
    maestrovehiculo = models.ForeignKey(erpp.fac.models.Maestrovehiculo, on_delete=models.CASCADE, verbose_name='MaestroVehiculo')
    maestromoneda = models.ForeignKey(erpp.gen.models.Maestromoneda, on_delete=models.CASCADE, verbose_name='MaestroMoneda')
    maestrotipodecambio = models.ForeignKey(erpp.gen.models.Maestrotipodecambio, on_delete=models.CASCADE, verbose_name='MaestroTipoDeCambio')
    fechaentrega = models.DateField(label='Fecha De Entrega')
    horaentrega = models.IntegerField(verbose_name='Hora De Entrega')
    maestroformasdepago = models.ForeignKey(erpp.gen.models.Maestroformasdepago, on_delete=models.CASCADE, verbose_name='MaestroFormasDePago')
    totalsoles = models.DecimalField(label='Total En Soles', max_digits=11, decimal_places=2)
    totaldolares = models.DecimalField(label='Total En Dólares', max_digits=13, decimal_places=4)
    anulado = models.BooleanField(verbose_name='¿Anulado?', default=False)
    numeroorden = models.IntegerField(verbose_name='Número De Orden')
    kilometraje = models.IntegerField(verbose_name='Kilometraje')
    niveldecombustible = models.IntegerField(verbose_name='Nivel De Combustible', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.TextField(label='Acción')
    autorizado = models.TextField(label='Autorizado')
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    terminado = models.BooleanField(verbose_name='¿Terminado?', blank=True, null=True)
    lavado = models.IntegerField(verbose_name='Lavado', blank=True, null=True)
    secado = models.IntegerField(verbose_name='Secado', blank=True, null=True)
    controlcalidad = models.IntegerField(verbose_name='Control De Calidad', blank=True, null=True)
    revisionasesor = models.IntegerField(verbose_name='Revisión Del Asesor', blank=True, null=True)
    listo = models.IntegerField(verbose_name='Listo', blank=True, null=True)
    porordende = models.CharField(label='Por Orden De', max_length=500, blank=True, null=True)
    estadodocumento = models.CharField(label='Estado Del Documento', max_length=50, blank=True, null=True)
    codigotecnico = models.CharField(label='Código Del Técnico', max_length=20, blank=True, null=True)
    horatentativaentrega = models.CharField(label='Hora Tentativa De Entrega', max_length=12, blank=True, null=True)
    numerodecono = models.CharField(label='Número De Cono', max_length=500, blank=True, null=True)
    observacion = models.TextField(label='Observación', blank=True, null=True)
    cita = models.BooleanField(verbose_name='¿Cita?', blank=True, null=True)
    esfactura = models.BooleanField(verbose_name='¿Es Factura?', blank=True, null=True)
    tiempo = models.IntegerField(verbose_name='Tiempo', blank=True, null=True)
    hojadiagn1 = models.BooleanField(verbose_name='¿Hoja De Diagnóstico N 1?', blank=True, null=True)
    hojadiagn2 = models.BooleanField(verbose_name='¿Hoja De Diagnóstico N 2?', blank=True, null=True)
    hojadiagn3 = models.BooleanField(verbose_name='¿Hoja De Diagnóstico N 3?', blank=True, null=True)
    hojadiagn4 = models.BooleanField(verbose_name='¿Hoja De Diagnóstico N 4?', blank=True, null=True)
    hojadiagn5 = models.BooleanField(verbose_name='¿Hoja De Diagnóstico N 5?', blank=True, null=True)
    hojadiagn6 = models.BooleanField(verbose_name='¿Hoja De Diagnóstico N 6?', blank=True, null=True)
    hojadiagn7 = models.BooleanField(verbose_name='¿Hoja De Diagnóstico N 7?', blank=True, null=True)
    hojadiagn8 = models.BooleanField(verbose_name='¿Hoja De Diagnóstico N 8?', blank=True, null=True)
    hojadiagn9 = models.BooleanField(verbose_name='¿Hoja De Diagnóstico N 9?', blank=True, null=True)
    porordendetelefono = models.CharField(label='Por Orden De Teléfono', max_length=30, blank=True, null=True)
    porordendedni = models.CharField(label='Por Orden De DNI', max_length=8, blank=True, null=True)
    porordendecorreo = models.CharField(label='Por Orden De Correo', max_length=100, blank=True, null=True)
    usuario = models.CharField(label='Usuario', max_length=500, blank=True, null=True)
    preciario = models.ForeignKey(erpp.fac.models.Preciario, on_delete=models.CASCADE, verbose_name='Preciario', blank=True, null=True)
    montoproductosservicio = models.DecimalField(label='Monto De Productos y Servicios', max_digits=13, decimal_places=4, blank=True, null=True)
    montomateriales = models.DecimalField(label='Monto De Materiales', max_digits=13, decimal_places=4, blank=True, null=True)
    mantenimientoreal = models.IntegerField(verbose_name='Mantenimiento Real', blank=True, null=True)
    tallercitas = models.ForeignKey(erpp.cita.models.Tallercitas, on_delete=models.CASCADE, verbose_name='TallerCitas', blank=True, null=True)
    observaciondocumentoreferencia = models.TextField(label='Observación Del Documento Referido', blank=True, null=True)

    class Meta:
        db_table = 'ordenserviciocabecera'
        unique_together = (('numerotarjeta', 'idmaestrosucursal', 'anulado'),)


class Ordenserviciodetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    ordenserviciocabecera = models.ForeignKey(Ordenserviciocabecera, on_delete=models.CASCADE, verbose_name='OrdenServicioCabecera')
    maestrotrabajotaller = models.ForeignKey(erpp.cita.models.Maestrotrabajotaller, on_delete=models.CASCADE, verbose_name='MaestroTrabajoTaller')
    maestroserviciotaller = models.ForeignKey(Maestroserviciotaller, on_delete=models.CASCADE, verbose_name='MaestroServicioTaller')
    maestrotescnico = models.ForeignKey(Maestrotecnico, on_delete=models.CASCADE, verbose_name='MaestroTescnico', blank=True, null=True)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    subtotalsoles = models.DecimalField(label='Subtotal En Soles', max_digits=11, decimal_places=2)
    subtotaldolares = models.DecimalField(label='Subtotal En Dólares', max_digits=13, decimal_places=4)
    preciosoles = models.DecimalField(label='Precio En Soles', max_digits=11, decimal_places=2)
    preciodolares = models.DecimalField(label='Precio En Dólares', max_digits=13, decimal_places=4)
    observacion = models.CharField(label='Observación', max_length=200)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    duracionminutos = models.IntegerField(verbose_name='Duración En Minutos', blank=True, null=True)
    descripcion = models.CharField(label='Descripción', max_length=200, blank=True, null=True)
    esproducto = models.BooleanField(verbose_name='¿Es Producto?', blank=True, null=True)
    descuento = models.DecimalField(label='Descuento', max_digits=11, decimal_places=2, blank=True, null=True)
    precioprodref = models.DecimalField(label='Precio Del Produecto Referido', max_digits=11, decimal_places=2, blank=True, null=True)
    preciomaterialesref = models.DecimalField(label='Precio De Los Materiales Referidos', max_digits=11, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'ordenserviciodetalle'


class Ordenservicionivelcombustible(models.Model):
    id = models.IntegerField(verbose_name='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    x = models.DecimalField(label='X', max_digits=18, decimal_places=4)
    y = models.DecimalField(label='Y', max_digits=18, decimal_places=4)
    maestrovehiculo = models.ForeignKey(erpp.fac.models.Maestrovehiculo, on_delete=models.CASCADE, verbose_name='MaestroVehiculo')
    observacion = models.CharField(label='Observación', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'ordenservicionivelcombustible'


class Ordenservicioproductosdetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    ordenserviciodetalle = models.ForeignKey(Ordenserviciodetalle, on_delete=models.CASCADE, verbose_name='OrdenServicioDetalle')
    maestroactividadtaller = models.ForeignKey(erpp.serv.models.Maestroactividadtaller, on_delete=models.CASCADE, verbose_name='MaestroActividadTaller')
    maestroproducto = models.ForeignKey(erpp.inv.models.Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    subtotalsoles = models.DecimalField(label='Subtotal En Soles', max_digits=11, decimal_places=2)
    subtotaldolares = models.DecimalField(label='Subtotal En Dólares', max_digits=13, decimal_places=4)
    preciosoles = models.DecimalField(label='Precio En Soles', max_digits=11, decimal_places=2)
    preciodolares = models.DecimalField(label='Precio En Dólares', max_digits=13, decimal_places=4)
    recogido = models.BooleanField(verbose_name='¿Recogido?', blank=True, null=True)
    cantidadrecogida = models.IntegerField(verbose_name='Cantidad Recogida', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'ordenservicioproductosdetalle'


class Ordenserviciotipoaveria(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestrotipoaveria = models.ForeignKey(erpp.gen.models.Maestrotipoaveria, on_delete=models.CASCADE, verbose_name='MaestroTipoAveria')
    x = models.DecimalField(label='X', max_digits=18, decimal_places=4)
    y = models.DecimalField(label='Y', max_digits=18, decimal_places=4)
    orderserviciocabecera = models.ForeignKey(Ordenserviciocabecera, on_delete=models.CASCADE, verbose_name='OrderServicioCabecera')
    maestrovehiculo = models.ForeignKey(erpp.fac.models.Maestrovehiculo, on_delete=models.CASCADE, verbose_name='MaestroVehiculo')
    observacion = models.CharField(label='Observación', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'ordenserviciotipoaveria'


class Ordenserviciotrabajoadicional(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    ordenserviciocabecera = models.ForeignKey(erpp.serv.models.Ordenserviciocabecera, on_delete=models.CASCADE, verbose_name='OrdenServicioCabecera')
    numeroordenserviciocabecera = models.CharField(label='NúmeroOrdenServicioCabecera', max_length=75)
    personaqueautoriza = models.CharField(label='Persona Que Autoriza', max_length=200)
    descripciontrabajo = models.CharField(label='Descripción Del Trabajo', max_length=200)
    telefono = models.CharField(label='Teléfono', max_length=15)
    aprobacion = models.BooleanField(verbose_name='Aprobación')
    formacomunicaciontelefono = models.CharField(label='Forma De Comunicación Del Teléfono', max_length=75)
    formacomunicacioncorreo = models.CharField(label='Forma De Comunicación Del Correo', max_length=75)
    nuevafechahoraentrega = models.DateTimeField(label='Nueva Fecha y Hora De Entrega', blank=True, null=True)
    preciosoles = models.DecimalField(label='Precio En Soles', max_digits=11, decimal_places=4)
    preciodolares = models.DecimalField(label='Precio En Dólares', max_digits=13, decimal_places=4)
    tiempotabla = models.IntegerField(verbose_name='Tiempo Tabla')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    preciosolesmanoobra = models.DecimalField(label='Precio En Soles Por Mano De Obra', max_digits=11, decimal_places=4, blank=True, null=True)
    preciosolesrepuesto = models.DecimalField(label='Precio En Soles De Repuesto', max_digits=11, decimal_places=4, blank=True, null=True)

    class Meta:
        db_table = 'ordenserviciotrabajoadicional'


class Servicioportercerocabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    ordenserviciocabecera = models.ForeignKey(Ordenserviciocabecera, on_delete=models.CASCADE, verbose_name='OrdenServicioCabecera')
    nombreproveedor = models.CharField(label='Nombre Del Proveedor', max_length=500)
    rucproveedor = models.CharField(label='RUC Del Proveedor', max_length=12)
    maestrodocumentosunat = models.ForeignKey(erpp.gen.models.Maestrodocumentossunat, on_delete=models.CASCADE, verbose_name='MaestroDocumentoSunat')
    maestromoneda = models.ForeignKey(erpp.gen.models.Maestromoneda, on_delete=models.CASCADE, verbose_name='MaestroMoneda')
    maestrotipocambio = models.ForeignKey(erpp.gen.models.Maestrotipodecambio, on_delete=models.CASCADE, verbose_name='MaestroTipoCambio')
    porcentajeadicional = models.DecimalField(label='Porcentaje Adicional', max_digits=5, decimal_places=2)
    totalsoles = models.DecimalField(label='Total En Soles', max_digits=11, decimal_places=2)
    totaldolares = models.DecimalField(label='Total En Dólares', max_digits=13, decimal_places=4)
    totalcompletosoles = models.DecimalField(label='Total Completo En Soles', max_digits=11, decimal_places=2)
    totalcompletodolares = models.DecimalField(label='Total Completo Dólares', max_digits=13, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    numerodocumentoreferido = models.CharField(label='Número Del Documento Referido', max_length=20, blank=True, null=True)
    seriedocumentoreferido = models.CharField(label='Serie Del Documento Referido', max_length=20, blank=True, null=True)
    maestromonedaventa = models.ForeignKey(erpp.gen.models.Maestromoneda, on_delete=models.CASCADE, verbose_name='MaestroMonedaVenta', blank=True, null=True)
    fechadocumento = models.DateField(label='Fecha Del Documento', blank=True, null=True)

    class Meta:
        db_table = 'servicioportercerocabecera'


class Servicioportercerodetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    servicioportercerocabecera = models.ForeignKey(Servicioportercerocabecera, on_delete=models.CASCADE, verbose_name='ServicioPorTerceroCabecera')
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    preciounitariosoles = models.DecimalField(label='Precio Unitario En Soles', max_digits=11, decimal_places=2)
    preciounitariodolares = models.DecimalField(label='Precio Unitario En Dólares', max_digits=13, decimal_places=4)
    descripcion = models.CharField(label='Descripción', max_length=200)
    subtotalsoles = models.DecimalField(label='Subtotal En Soles', max_digits=11, decimal_places=2)
    subtotaldolares = models.DecimalField(label='Subtotal En Dólares', max_digits=13, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    fechahorainicioservicio = models.DateTimeField(label='Fecha y Hora De Inicio Del Servicio', blank=True, null=True)
    fechahorafinservicio = models.DateTimeField(label='Fecha y Hora De Finalizaación Del Servicio', blank=True, null=True)
    horainicio = models.CharField(label='Hora De Inicio', max_length=10, blank=True, null=True)
    horafin = models.CharField(label='Hora De Finalización', max_length=10, blank=True, null=True)
    maestroproveedor = models.ForeignKey(erpp.gen.models.Maestroproveedores, on_delete=models.CASCADE, verbose_name='MaestroProveedor', blank=True, null=True)
    porcentajeadicional = models.DecimalField(label='Porcentaje Adicional', max_digits=13, decimal_places=4, blank=True, null=True)

    class Meta:
        db_table = 'servicioportercerodetalle'


class Tallerasesores(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    nombres = models.CharField(label='Nombres', max_length=150)
    apellido_paterno = models.CharField(label='Apellido Paterno', max_length=50)
    apellido_materno = models.CharField(label='Apellido Materno', max_length=50)
    nombre_completo = models.CharField(label='Nombre Completo', max_length=200)
    estacion = models.ForeignKey(erpp.cita.models.Tallerestacion, on_delete=models.CASCADE, verbose_name='Estacion')
    imagen = models.BinaryField(label='Imagen', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestropersonal = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal', blank=True, null=True)

    class Meta:
        db_table = 'tallerasesores'


class Tallerkilometraje(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    km = models.IntegerField(verbose_name='Kilometraje')

    class Meta:
        db_table = 'tallerkilometraje'


class Tallerordenservicioimagen(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    descripcion = models.CharField(label='Descripción', max_length=200, blank=True, null=True)
    rutaimagen = models.CharField(label='Ruta De La Imagen', max_length=200)
    ordenserviciocabecera = models.ForeignKey(Ordenserviciocabecera, on_delete=models.CASCADE, verbose_name='OrdenServicioCabecera')
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)

    class Meta:
        db_table = 'tallerordenservicioimagen'


class Tallervehiculo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    marca = models.CharField(label='Marca', max_length=50)
    modelo = models.CharField(label='Modelo', max_length=50)
    placa = models.CharField(label='Placa', max_length=50)

    class Meta:
        db_table = 'tallervehiculo'


class Tipobienoservicio(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    usuarioid = models.IntegerField(verbose_name='UsuarioID')
    codigo = models.CharField(label='Código', max_length=50)
    nombre = models.CharField(label='Nombre', max_length=500)
    descripcion = models.CharField(label='Descripción', max_length=500, blank=True, null=True)
    estadoregistro = models.BooleanField(verbose_name='¿Estado De Registro?', default=False)
    fechahoraregistro = models.DateTimeField(label='Fecha y Hora De Registro')

    class Meta:
        db_table = 'tipobienoservicio'


class Tiposolicitud(models.Model):
    id = models.IntegerField(verbose_name='ID')
    descripcion = models.CharField(label='Descripción', max_length=100)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'tiposolicitud'
