from django.db import models

import erpp.cmp.models
import erpp.fac.models
import erpp.gen.models
import erpp.inv.models
import erpp.per.models
import erpp.serv.models


class Aprobaciones(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    esgrupal = models.BooleanField(verbose_name='¿Es Grupal?', default=False)
    taller = models.BooleanField(verbose_name='¿Taller?', default=False)
    valortaller = models.DecimalField(verbose_name='Valor Taller', max_digits=12, decimal_places=4)
    ventas = models.BooleanField(verbose_name='¿Ventas?', default=False)
    valorventas = models.DecimalField(label='Valor De Ventas', max_digits=12, decimal_places=4)
    logistica = models.BooleanField(verbose_name='¿Logistica?', default=False)
    valorlogistica = models.DecimalField(label='Valor De Logistica', max_digits=12, decimal_places=4)
    almacen = models.BooleanField(verbose_name='¿Almacen?', default=False)
    valoralmacen = models.DecimalField(label='Valor De Almacen', max_digits=12, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresas = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
                                        verbose_name='MaestroEmpresas')
    maestrosucursales = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
                                          verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'aprobaciones'


class Aprobacionesdetalle(models.Model):
    id = models.AutoField(LABEL='ID', primary_key=True)
    cargotrabajador = models.ForeignKey(erpp.per.models.Cargostrabajador, on_delete=models.CASCADE,
                                        verbose_name='CargosTrabajador')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresas = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE,
                                        verbose_name='MaestroEmpresas')
    maestrosucursales = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE,
                                          verbose_name='MaestroSucursales')
    aprobaciones = models.ForeignKey(Aprobaciones, on_delete=models.CASCADE,
                                     verbose_name='Aprobaciones')

    class Meta:
        db_table = 'aprobacionesdetalle'


class Aprobacionesfacturacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    factura = models.ForeignKey(erpp.fac.models.Facturacioncaja, on_delete=models.CASCADE,
                                verbose_name='FacturacionCaja')
    aprobacion = models.ForeignKey(Aprobaciones, on_delete=models.CASCADE,
                                   verbose_name='Aprobaciones')
    aprobadogeneral = models.BooleanField(verbose_name='¿Aprobado General?', blank=True, null=True)
    fechaaprobaciongeneral = models.DateTimeField(label='Fecha De Aprobación General', blank=True, null=True)
    montogeneral = models.DecimalField(label='Monto General', max_digits=12, decimal_places=2, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'aprobacionesfacturacion'


class Aprobacionesfacturadetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    aprobacionfactura = models.ForeignKey(Aprobacionesfacturacion, on_delete=models.CASCADE,
                                          verbose_name='AprobacionesFactura')
    aprobaciondetalle = models.ForeignKey(Aprobacionesdetalle, on_delete=models.CASCADE,
                                          verbose_name='AprobacionesDetalle')
    aprobado = models.BooleanField(verbose_name='¿Aprobado?', blank=True, null=True)
    motivo = models.CharField(label='Motivo', max_length=150, blank=True, null=True)
    fechaaprobacion = models.DateTimeField(label='Fecha De Aprobación', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'aprobacionesfacturadetalle'


class Aprobacionesordencompra(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    ordencompra = models.ForeignKey(erpp.cmp.models.Ordencompracabecera, on_delete=models.CASCADE,
                                    verbose_name='OrdenCompraCabecera')
    aprobacion = models.ForeignKey(Aprobaciones, on_delete=models.CASCADE,
                                   verbose_name='Aprobaciones')
    aprobadogeneral = models.BooleanField(verbose_name='¿Aprobado General?', blank=True, null=True)
    fechaaprobaciongeneral = models.DateTimeField(label='Fecha De Aprobación General', blank=True, null=True)
    montogeneral = models.DecimalField(label='Monto General', max_digits=12, decimal_places=2, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'aprobacionesordencompra'


class Aprobacionesordencompradetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    aprobacionordencompra = models.ForeignKey(Aprobacionesordencompra, on_delete=models.CASCADE,
                                              verbose_name='AprobacionesOrdenCompra')
    aprobaciondetalle = models.ForeignKey(Aprobacionesdetalle, on_delete=models.CASCADE,
                                          verbose_name='AprobacionesDetalle')
    aprobado = models.BooleanField(verbose_name='¿Aprobado?', blank=True, null=True)
    motivo = models.CharField(label='Motivo', max_length=150, blank=True, null=True)
    fechaaprobacion = models.DateTimeField(label='Fecha De Aprobación', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'aprobacionesordencompradetalle'


class Aprobacionespedidos(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    pedido = models.ForeignKey(erpp.inv.models.Pedidocabecera, on_delete=models.CASCADE, verbose_name='PedidoCabecera')
    aprobacion = models.ForeignKey(Aprobaciones, on_delete=models.CASCADE, verbose_name='Aprobaciones')
    aprobadogeneral = models.BooleanField(verbose_name='¿Aprobado General?', blank=True, null=True)
    fechaaprobaciongeneral = models.DateTimeField(label='Fecha De Aprobación General', blank=True, null=True)
    tiposolicitud = models.ForeignKey(erpp.serv.models.Tiposolicitud, on_delete=models.CASCADE,
                                      verbose_name='TipoSolicitud', blank=True, null=True)
    viaaprobacion = models.ForeignKey(erpp.fac.models.Viaaprobacion, on_delete=models.CASCADE,
                                      verbose_name='ViaAprobacion', blank=True, null=True)
    montogeneral = models.DecimalField(label='Monto General', max_digits=12, decimal_places=2)
    logistica = models.DecimalField(label='¿Logística?', default=False)
    taller = models.BooleanField(verbose_name='¿Taller?', default=False)
    ventas = models.BooleanField(verbose_name='¿Ventas?', default=False)
    almacen = models.BooleanField(verbose_name='¿Almacen?', default=False)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'aprobacionespedidos'


class Aprobacionespedidosdetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    aprobacionpedido = models.ForeignKey(Aprobacionespedidos, on_delete=models.CASCADE,
                                         verbose_name='AprobacionesPedido')
    aprobaciondetalle = models.ForeignKey(Aprobacionesdetalle, on_delete=models.CASCADE,
                                          verbose_name='AprobacionesDetalle')
    aprobado = models.BooleanField(verbose_name='¿Aprobado?', blank=True, null=True)
    motivo = models.CharField(label='Motivo', max_length=150)
    fechaaprobacion = models.DateTimeField(label='Fecha De Aprobación', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'aprobacionespedidosdetalle'
