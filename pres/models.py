from django.db import models

import erpp.conta.models
import erpp.fac.models
import erpp.gen.models
import erpp.inv.models


class Controlgasto(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    fecha = models.DateField(label='Fecha')
    maestroproveedor = models.ForeignKey(erpp.gen.models.Maestroproveedores, on_delete=models.CASCADE, verbose_name='MaestroProveedor')
    facturacabecera = models.ForeignKey(erpp.fac.models.Facturaclientecabecera, on_delete=models.CASCADE, verbose_name='FacturaCabecera')
    numerofactura = models.CharField(label='Número De Factura', max_length=75)
    maestroproducto = models.ForeignKey(erpp.inv.models.Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    preciosoles = models.DecimalField(label='Precio En Soles', max_digits=11, decimal_places=2)
    preciodolares = models.DecimalField(label='Precio En Dólares', max_digits=13, decimal_places=4)
    area = models.ForeignKey(erpp.inv.models.Areas, on_delete=models.CASCADE, verbose_name='Area')
    observacion = models.CharField(label='Observación', max_length=500)
    motivo = models.CharField(label='Motivo', max_length=255)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'controlgasto'


class Presupuesto(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigopresupuesto = models.CharField(label='Código De Presupuesto', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=100)
    mayor = models.BooleanField(verbose_name='¿Mayor?', default=False)
    codigocuentamayor = models.CharField(label='Codigo De Cuenta Mayor', max_length=20)
    itemsrelacionados = models.IntegerField(verbose_name='Ítems Relacionados')
    cuenta = models.CharField(label='Cuenta', max_length=100, blank=True, null=True)
    cuentaii = models.CharField(label='Cuenta II', max_length=100, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'presupuesto'


class Presupuestoanuales(models.Model):
    id = models.IntegerField(verbose_name='ID')
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigopresupuesto = models.CharField(label='Código De Presupuesto', max_length=50)
    tipo = models.CharField(label='Tipo', max_length=50)
    codigopresupuestopadre = models.CharField(label='Código De Presupuesto Padre', max_length=50, blank=True, null=True)
    descripcion = models.CharField(label='Descripción', max_length=250)
    idcentrocostos = models.ForeignKey(erpp.gen.models.Maestrocentrosdecostos, on_delete=models.CASCADE, verbose_name='CentroCostos', blank=True, null=True)
    centrocostos = models.CharField(label='Centro De Costos', max_length=50, blank=True, null=True)
    idcuentacontable = models.ForeignKey(erpp.conta.models.Cuentasbancos, on_delete=models.CASCADE, verbose_name='CuentaContable', blank=True, null=True)
    cuentacontable = models.CharField(label='Cuenta Contable', max_length=50, blank=True, null=True)
    enero = models.DecimalField(label='Enero', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentajeenero = models.DecimalField(label='Porcentaje Enero', max_digits=5, decimal_places=2, blank=True, null=True)
    febrero = models.DecimalField(label='Febrero', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentajefebrero = models.DecimalField(label='Porcentaje Febrero', max_digits=5, decimal_places=2, blank=True, null=True)
    marzo = models.DecimalField(label='Marzo', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentajemarzo = models.DecimalField(label='Porcentaje Marzo', max_digits=5, decimal_places=2, blank=True, null=True)
    abril = models.DecimalField(label='Abril', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentajeabril = models.DecimalField(label='Porcentaje Abril', max_digits=5, decimal_places=2, blank=True, null=True)
    mayo = models.DecimalField(label='Mayo', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentajemayo = models.DecimalField(label='Porcentaje Mayo', max_digits=5, decimal_places=2, blank=True, null=True)
    junio = models.DecimalField(label='Junio', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentajejunio = models.DecimalField(label='Porcentaje Junio', max_digits=5, decimal_places=2, blank=True, null=True)
    julio = models.DecimalField(label='Julio', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentajejulio = models.DecimalField(label='Porcentaje Julio', max_digits=5, decimal_places=2, blank=True, null=True)
    agosto = models.DecimalField(label='Agosto', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentajeagosto = models.DecimalField(label='Porcentaje Agosto', max_digits=5, decimal_places=2, blank=True, null=True)
    septiembre = models.DecimalField(label='Septiembre', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentajeseptiembre = models.DecimalField(label='Porcentaje Septiembre', max_digits=5, decimal_places=2, blank=True, null=True)
    octubre = models.DecimalField(label='Octubre', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentajeoctubre = models.DecimalField(label='Porcentaje Octubre', max_digits=5, decimal_places=2, blank=True, null=True)
    noviembre = models.DecimalField(label='Noviembre', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentajenoviembre = models.DecimalField(label='Porcentaje Noviembre', max_digits=5, decimal_places=2, blank=True, null=True)
    diciembre = models.DecimalField(label='Diciembre', max_digits=12, decimal_places=2, blank=True, null=True)
    porcentajediciembre = models.DecimalField(label='Porcentaje Diciembre', max_digits=5, decimal_places=2, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=20, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=80, blank=True, null=True)
    estado = models.IntegerField(verbose_name='Estado', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    anhio = models.IntegerField(verbose_name='Año')

    class Meta:
        db_table = 'presupuestoanuales'


class Presupuestodetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigopresupuesto = models.CharField(label='Código De Presupuesto', max_length=20)
    periodomes = models.IntegerField(verbose_name='Periodo Mes')
    periodoanhio = models.IntegerField(verbose_name='Periodo Año')
    montopresupuestadosoles = models.DecimalField(label='Monto Presupuestado En Soles', max_digits=18, decimal_places=2)
    montopresupuestadodolares = models.DecimalField(label='Monto Presupuestado En Dólares', max_digits=18, decimal_places=4)
    maestrotipocambio = models.ForeignKey(erpp.gen.models.Maestrotipodecambio, on_delete=models.CASCADE, verbose_name='MaestroTipoCambio')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=50)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'presupuestodetalle'