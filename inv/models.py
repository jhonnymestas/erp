from django.db import models

import erpp.cita.models
import erpp.cmp.models
import erpp.conta.models
import erpp.fac.models
import erpp.gen.models
import erpp.per.models
import erpp.serv.models
from erpp.bases.models import ClaseModelo


class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categorias"


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria', 'descripcion')


class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Marca',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marca"


class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Unidad Medida',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural = "Unidades de Medida"


class Producto(ClaseModelo):
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()
    
    class Meta:
        verbose_name_plural = "Productos"
        unique_together = ('codigo', 'codigo_barra')


# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*


"""
    Clases correspondientes a las tablas
    de tipo: ALMACEN
"""


class Maestromotivosingresoalmacen(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcion = models.CharField(label='Descripción', max_length=50)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestromotivosingresoalmacen'


class Maestromotivossalidaalmacen(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcion = models.CharField(label='Descripción', max_length=50)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestromotivossalidaalmacen'


class AlmAreas(models.Model):
    idalm_area = models.AutoField(label='IDAlm.Area', primary_key=True)
    empresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='Empresa')
    sucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='Sucursal')
    almacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='Almacen')
    descripcion = models.CharField(label='Descripción', max_length=50)
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'almareas'


class Tipogrupo(models.Model):
    idtipogrupo = models.AutoField(label='IDTipoGrupo', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigotipogrupo = models.CharField(label='Código Del Tipo De Grupo', max_length=50)
    descripcion = models.CharField(label='Descripción', max_length=200, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=100, blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'tipogrupo'


class Tamaniogrupo(models.Model):
    idtamaniogrupo = models.AutoField(label='IDTamanioGrupo', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigotamaniogrupo = models.CharField(label='Código De Tamaño De Grupo', max_length=50)
    descripcion = models.CharField(label='Descripción', max_length=200, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=100, blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'tamaniogrupo'


class Principalgrupo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigoprincipalgrupo = models.CharField(label='Código Principal Del Grupo', max_length=50)
    descripcion = models.CharField(label='Descripción', max_length=200, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=100, blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'principalgrupo'


class Formagrupo(models.Model):
    idformagrupo = models.AutoField(label='IDFormaGrupo', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigoformagrupo = models.CharField(label='Código Forma De Grupo', max_length=50)
    descripcion = models.CharField(label='Descripción', max_length=200, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=100, blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'formagrupo'


class Detallegrupo(models.Model):
    iddetallegrupo = models.AutoField(label='IDDetalleGrupo', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigodetallegrupo = models.CharField(label='Código Detalle Grupo', max_length=50)
    descripcion = models.CharField(label='Descripción', max_length=200, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=100, blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'detallegrupo'


class Areagrupo(models.Model):
    idareagrupo = models.AutoField(primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigoareagrupo = models.CharField(label='Código Área Grupo', max_length=50)
    descripcion = models.CharField(label='Descripción', max_length=200, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=100, blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'areagrupo'


class Areas(models.Model):
    id = models.IntegerField(verbose_name='ID')
    codigoarea = models.CharField(label='Código Área', max_length=10)
    descripcion = models.CharField(label='Descripción', max_length=50)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'areas'


class Maestroproductos(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoproducto = models.CharField(label='Código Del Producto', max_length=60)
    nombrecomercial = models.CharField(label='Nombre Comercial', max_length=200)
    descripcion = models.CharField(label='Descripción', max_length=200)
    maestrounidadesdemedida = models.ForeignKey(erpp.gen.models.Maestrounidadesdemedida, on_delete=models.CASCADE, verbose_name='MaestroUnidadesDeMedida')
    codigounidadmedida = models.CharField(label='Código De Unidad De Medida', max_length=20)
    medida = models.DecimalField(label='Medida', max_digits=12, decimal_places=5)
    maestrolineascomerciales = models.ForeignKey(erpp.gen.models.Maestrolineascomerciales, on_delete=models.CASCADE, verbose_name='MaestroLineasComerciales')
    codigolineacomercial = models.CharField(label='Código De Linea Comercial', max_length=20)
    procedencia = models.CharField(label='Procedencia', max_length=60)
    codigoubicacion = models.CharField(label='Código Ubicación', max_length=20)
    codigogrupo = models.CharField(label='Código De Grupo', max_length=20)
    costopromediosoles = models.DecimalField(label='Costo Promedio En Soles', max_digits=11, decimal_places=2)
    costopromediodolares = models.DecimalField(label='Costo Promedio En Dólares', max_digits=13, decimal_places=4)
    fechacostopromedio = models.DateTimeField(label='Fecha De Costo Promedio')
    ultimocostosoles = models.DecimalField(label='Último Costo En Soles', max_digits=11, decimal_places=2)
    ultimocostodolares = models.DecimalField(label='Último Costo En Dólares', max_digits=13, decimal_places=4)
    fechaultimocosto = models.DateTimeField(label='Fecha Del Último Costo')
    fechaultimomovimiento = models.DateTimeField(label='Fecha Del Último Movimiento')
    precioventasoles = models.DecimalField(label='Precio De Venta En Soles', max_digits=11, decimal_places=5)
    precioventadolares = models.DecimalField(label='Precio De Venta En Dólares', max_digits=13, decimal_places=4)
    totalingresos = models.IntegerField(verbose_name='Total De Ingresos')
    totalsalidas = models.IntegerField(verbose_name='Total De Salidas')
    stockmaximo = models.IntegerField(verbose_name='Stock Máximo')
    stockminimo = models.IntegerField(verbose_name='Stock Mínimo')
    saldo = models.IntegerField(verbose_name='Saldo')
    recalcular = models.BooleanField(verbose_name='¿Recalcular?', default=False)
    desdemes = models.IntegerField(verbose_name='Desde El Mes')
    desdeanhio = models.IntegerField(verbose_name='Desde El Año')
    margen = models.IntegerField(verbose_name='Margen')
    ingresosvencidos = models.IntegerField(verbose_name='Ingresos Vencidos')
    salidasvencidas = models.IntegerField(verbose_name='Salidas Vencidas')
    saldovencidos = models.IntegerField(verbose_name='Saldo Vencidos')
    loteproduccion = models.CharField(label='Lote De Producción', max_length=20)
    codigoaplicacion = models.CharField(label='Código De La Aplicación', max_length=20)
    kilos = models.DecimalField(label='Kilos', max_digits=12, decimal_places=5)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    numeroparte = models.CharField(label='Número De Parte', max_length=75)
    equipoproteccionp = models.BooleanField(verbose_name='¿Equipo De Protección P?', default=False)
    tipoactualizacion = models.CharField(label='Tipo De Actualización', max_length=1)
    rotacion = models.CharField(label='Rotación', max_length=1, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    servicio = models.BooleanField(verbose_name='¿Servicio?', blank=True, null=True)
    clasificacion = models.CharField(label='Clasificación', max_length=5, blank=True, null=True)
    cantidadsugerida = models.IntegerField(verbose_name='Cantidad Sugerida', blank=True, null=True)
    precioventamanual = models.BooleanField(verbose_name='¿Precio De Venta Manual?', blank=True, null=True)
    manodeobra = models.DecimalField(label='Mano De Obra', max_digits=18, decimal_places=3, blank=True, null=True)
    unidadmedidaentero = models.CharField(label='Unidad De Medida Entero', max_length=20, blank=True, null=True)
    factordeconversion = models.DecimalField(label='Factor De Conversión', max_digits=18, decimal_places=6, blank=True, null=True)
    controlasaldo = models.BooleanField(verbose_name='¿Controla Saldo?', blank=True, null=True)
    areagrupo = models.ForeignKey(Areagrupo, on_delete=models.CASCADE, verbose_name='AreaGrupo', blank=True, null=True)
    detallegrupo = models.ForeignKey(Detallegrupo, on_delete=models.CASCADE, verbose_name='DetalleGrupo', blank=True, null=True)
    formagrupo = models.ForeignKey(Formagrupo, on_delete=models.CASCADE, verbose_name='FormaGrupo', blank=True, null=True)
    principalgrupo = models.ForeignKey(Principalgrupo, on_delete=models.CASCADE, verbose_name='PrincipalGrupo', blank=True, null=True)
    taminiogrupo = models.ForeignKey(Tamaniogrupo, on_delete=models.CASCADE, verbose_name='TaminioGrupo', blank=True, null=True)
    tipogrupo = models.ForeignKey(Tipogrupo, on_delete=models.CASCADE, verbose_name='TipoGrupo', blank=True, null=True)
    componentebase = models.ForeignKey(erpp.gen.models.Componentebase, on_delete=models.CASCADE, verbose_name='ComponenteBase', blank=True, null=True)

    class Meta:
        db_table = 'maestroproductos'


class Productodescuento(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    descripcion = models.CharField(label='Descripción', max_length=20)
    porcentaje = models.DecimalField(label='Porcentaje', max_digits=5, decimal_places=2)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'productodescuento'


class Ajustealmacen(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigoajuste = models.CharField(label='Código De Ajuste', max_length=20)
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    tipoajuste = models.IntegerField(verbose_name='Tipo De Ajuste')
    fechamovimientoreferencial = models.DateTimeField(label='Fecha De Movimiento Referencial')
    areaorigen = models.ForeignKey(Areas, on_delete=models.CASCADE, verbose_name='AreaOrigen')
    areadestino = models.ForeignKey(AlmAreas, on_delete=models.CASCADE, verbose_name='AreaDestino')
    motivo = models.CharField(label='Motivo', max_length=30)
    comentario = models.CharField(label='Comentario', max_length=500)
    codigousuario = models.CharField(label='Codigo De Usuario', max_length=36)
    fechahoraregistro = models.DateTimeField(label='Fecha y Hora De Registro')
    estadoregistro = models.BooleanField(verbose_name='¿Estado Registro?', default=False)
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal', blank=True, null=True)
    tiposucursal = models.IntegerField(verbose_name='Tipo Sucursal', blank=True, null=True)
    observaciontipo = models.ForeignKey(erpp.conta.models.Observaciondocumento, on_delete=models.CASCADE, verbose_name='ObservacionTipo', blank=True, null=True)

    class Meta:
        db_table = 'ajustealmacen'


class Almacencabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigoalmacen = models.CharField(label='Código De Almacen', max_length=20)
    maestromotivosingresoalmacen = models.ForeignKey(Maestromotivosingresoalmacen, on_delete=models.CASCADE, verbose_name='MaestroMotivosIngresoAlmacen')
    maestromotivossalidaalmacen = models.ForeignKey(Maestromotivossalidaalmacen, on_delete=models.CASCADE, verbose_name='MaestroMotivosSalidaAlmacen')
    tipomovimiento = models.CharField(label='Tipo De Movimiento', max_length=30)
    numerooperacion = models.CharField(label='Número De Operación', max_length=20)
    fechaoperacion = models.DateTimeField(label='Fecha De Operación')
    maestroproveedor = models.ForeignKey(erpp.gen.models.Maestroproveedores, on_delete=models.CASCADE, verbose_name='MaestroProveedor')
    codigoproveedor = models.CharField(label='Código De Proveedor', max_length=20)
    tipodocumentoreferido = models.CharField(label='Tipo De Documento Referido', max_length=100)
    numeroserie = models.CharField(label='Número De Serie', max_length=20)
    numerodocumentoreferido = models.CharField(label='Número De DocumentoReferido', max_length=20)
    maestrocliente = models.ForeignKey(erpp.fac.models.Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroCliente')
    codigocliente = models.CharField(label='Código De Cliente', max_length=20)
    maestromoneda = models.ForeignKey(erpp.gen.models.Maestromoneda, on_delete=models.CASCADE, verbose_name='MaestroMoneda')
    moneda = models.CharField(label='Moneda', max_length=30)
    maestrotipocambio = models.ForeignKey(erpp.gen.models.Maestrotipodecambio, on_delete=models.CASCADE, verbose_name='MaestroTipoCambio')
    tipocambio = models.DecimalField(label='Tipo De Cambio', max_digits=13, decimal_places=4)
    totaldescuentosoles = models.DecimalField(label='Total Descuento En Soles', max_digits=13, decimal_places=4)
    totaldescuentodolares = models.DecimalField(label='Total Descuento En Dólares', max_digits=13, decimal_places=4)
    importetotalsoles = models.DecimalField(label='Importe Total En Soles', max_digits=13, decimal_places=4)
    importetotaldolares = models.DecimalField(label='Importe Total En Dólares', max_digits=13, decimal_places=4)
    completada = models.BooleanField(verbose_name='¿Completada?', default=False)
    procesado = models.BooleanField(verbose_name='¿Procesado?', default=False)
    maestroformadepago = models.ForeignKey(erpp.gen.models.Maestroformasdepago, on_delete=models.CASCADE, verbose_name='MaestroFormaDePago')
    codigoformapago = models.CharField(label='Código Forma De Pago', max_length=20)
    maestrovendedor = models.ForeignKey(erpp.fac.models.Maestrovendedores, on_delete=models.CASCADE, verbose_name='MaestroVendedor')
    codigovendedor = models.CharField(label='Código De Vendedor', max_length=20)
    anulado = models.BooleanField(verbose_name='¿Anulado?', default=False)
    codigousuario = models.CharField(label='Código Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    estadodocumento = models.CharField(label='Estado Del Documento', max_length=50, blank=True, null=True)
    codigocentrocosto = models.CharField(label='Código Centro De Costo', max_length=20, blank=True, null=True)
    conigv = models.BooleanField(verbose_name='¿Con IGV?', blank=True, null=True)
    fechavencimiento = models.DateTimeField(label='Fecha De Vencimiento', blank=True, null=True)
    ordendecompra = models.ForeignKey(erpp.cmp.models.Ordencompracabecera, on_delete=models.CASCADE, verbose_name='OrdenDeCompra', blank=True, null=True)
    tieneextorno = models.BooleanField(verbose_name='¿Tiene Extorno?', blank=True, null=True)

    class Meta:
        db_table = 'almacencabecera'


class Almacenconfiguracion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa', blank=True, null=True)
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal', blank=True, null=True)
    codigosolicitudhotline = models.CharField(label='Código De Solicitud Hotline', max_length=10)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'almacenconfiguracion'


class Almacendetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    almacencabecera = models.ForeignKey(Almacencabecera, on_delete=models.CASCADE, verbose_name='AlmacenCabecera')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigoalmacen = models.CharField(label='Código De Almacen', max_length=20, blank=True, null=True)
    numerooperacion = models.CharField(label='Número De Operación', max_length=20, blank=True, null=True)
    tipomovimiento = models.ForeignKey(erpp.per.models.Maestrotipomovimiento, on_delete=models.CASCADE, verbose_name='TipoMovimiento')
    movimiento = models.CharField(label='Movimiento', max_length=30, blank=True, null=True)
    almacenorigendestino = models.CharField(label='Almacen Origen/Destino', max_length=20, blank=True, null=True)
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    codigoproducto = models.CharField(label='Código Del Producto', max_length=20, blank=True, null=True)
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5, blank=True, null=True)
    saldooperacion = models.DecimalField(label='Saldo De La Operación', max_digits=12, decimal_places=5, blank=True, null=True)
    costosoles = models.DecimalField(label='Costo En Soles', max_digits=11, decimal_places=4, blank=True, null=True)
    costodolares = models.DecimalField(label='Costo En Dólares', max_digits=13, decimal_places=4, blank=True, null=True)
    preciocostosoles = models.DecimalField(label='Precio Del Costo En Soles', max_digits=11, decimal_places=4, blank=True, null=True)
    preciocostodolares = models.DecimalField(label='Precio Del Costo En Dólares', max_digits=13, decimal_places=4, blank=True, null=True)
    precioventasoles = models.DecimalField(label='Precio De Venta En Soles', max_digits=13, decimal_places=4, blank=True, null=True)
    precioventadolares = models.DecimalField(label='Precio De Venta En Dólares', max_digits=13, decimal_places=4, blank=True, null=True)
    productodescuento = models.ForeignKey(Productodescuento, on_delete=models.CASCADE, verbose_name='ProductoDescuento', blank=True, null=True)
    porcentajedescuento = models.DecimalField(label='Porcentaje De Descuento', max_digits=12, decimal_places=5, blank=True, null=True)
    descuentodolares = models.DecimalField(label='Descuento En Dólares', max_digits=12, decimal_places=5, blank=True, null=True)
    descuentosoles = models.DecimalField(label='Descuento En Soles', max_digits=12, decimal_places=5, blank=True, null=True)
    desglosefacturas = models.CharField(label='Desglose De Facturas', max_length=10, blank=True, null=True)
    entregafutura = models.DecimalField(label='Entrega Futura', max_digits=12, decimal_places=5, blank=True, null=True)
    numerodesglose = models.IntegerField(verbose_name='Número De Desglose', blank=True, null=True)
    fletesoles = models.DecimalField(label='Flete En Soles', max_digits=13, decimal_places=4, blank=True, null=True)
    fletedolares = models.DecimalField(label='Flete En Dólares', max_digits=13, decimal_places=4, blank=True, null=True)
    gastosadministracionsoles = models.DecimalField(label='Gastos De Administración En Soles', max_digits=13, decimal_places=4, blank=True, null=True)
    gastosadministraciondolares = models.DecimalField(label='Gastos De Administración En Dólares', max_digits=13, decimal_places=4, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=20, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=80, blank=True, null=True)
    estado = models.IntegerField(verbose_name='Estado', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    descuentoporcentajeflota = models.DecimalField(label='Descuento De Porcentaje Flota', max_digits=5, decimal_places=2, blank=True, null=True)
    maestrocentrodecosto = models.ForeignKey(erpp.gen.models.Maestrocentrosdecostos, on_delete=models.CASCADE, verbose_name='MaestroCentroDeCosto', blank=True, null=True)
    costoacumuladosoles = models.DecimalField(label='Costo Acumulado En Soles', max_digits=11, decimal_places=4, blank=True, null=True)
    costoacumuladodolares = models.DecimalField(label='Costo Acumulado En Dólares', max_digits=11, decimal_places=4, blank=True, null=True)
    detallereferencia = models.ForeignKey(Detallegrupo, on_delete=models.CASCADE, verbose_name='DetalleReferencia', blank=True, null=True)
    cantidadenteros = models.DecimalField(label='Cantidad De Enteros', max_digits=18, decimal_places=6, blank=True, null=True)
    areaorigen = models.ForeignKey(Areas, on_delete=models.CASCADE, verbose_name='AreaOrigen', blank=True, null=True)
    areaprocedencia = models.ForeignKey(Areas, on_delete=models.CASCADE, verbose_name='AreaProcedencia', blank=True, null=True)
    costooperativosoles = models.DecimalField(label='Costo Operativo En Soles', max_digits=11, decimal_places=4, blank=True, null=True)
    costooperativodolares = models.DecimalField(label='Costo Operativo En Dólares', max_digits=11, decimal_places=4, blank=True, null=True)

    class Meta:

        db_table = 'almacendetalle'


class Almacenubicacionproducto(models.Model):
    id = models.AutoField(primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    maestroalmacendetalle = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacenDetalle')
    maestrocubiculo = models.ForeignKey(erpp.gen.models.Maestrocubiculo, on_delete=models.CASCADE, verbose_name='MaestroCubiculo')
    maestrovehiculo = models.ForeignKey(erpp.fac.models.Maestrovehiculo, on_delete=models.CASCADE, verbose_name='MaestroVehiculo')
    fechaproduccion = models.DateTimeField(label='Fecha De Producción')
    codigocubiculo = models.CharField(label='Código De Cubículo', max_length=20)
    loteproduccion = models.CharField(label='Lote De Producción', max_length=20)
    caracteristicalote = models.CharField(label='Característica Del Lote', max_length=60)
    placarodaje = models.CharField(label='Placa Rodaje', max_length=75)
    color = models.CharField(label='Color', max_length=75)
    tipo = models.CharField(label='Tipo', max_length=75)
    vehiculomarca = models.ForeignKey(erpp.conta.models.Vehiculomarca, on_delete=models.CASCADE, verbose_name='VehiculoMarca')
    vehiculomodelo = models.ForeignKey(erpp.conta.models.Vehiculomodelo, on_delete=models.CASCADE, verbose_name='VehiculoModelo')
    motor = models.CharField(label='Motor', max_length=75)
    chasis = models.CharField(label='Chasis', max_length=75)
    numerounidad = models.CharField(label='Número De Unidad', max_length=75)
    kilometraje = models.IntegerField(verbose_name='Kilometraje')
    anhiofabricacion = models.IntegerField(verbose_name='Año De Fabricación')
    placaoval = models.CharField(label='Placa Oval', max_length=100)
    clavecomercial = models.CharField(label='Clave Comercial', max_length=75)
    maestrocliente = models.ForeignKey(erpp.fac.models.Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroCliente')
    ordenpedido = models.ForeignKey(erpp.serv.models.Ordenpedido, on_delete=models.CASCADE, verbose_name='OrdenPedido')
    maestrovehiculoestado = models.ForeignKey(erpp.fac.models.Maestrovehiculoestado, on_delete=models.CASCADE, verbose_name='MaestroVehiculoEstado')
    maestrovendedor = models.ForeignKey(erpp.fac.models.Maestrovendedores, on_delete=models.CASCADE, verbose_name='MaestroVendedor')
    maestrovehiculocombustible = models.ForeignKey('Maestrovehiculocombustible', models.DO_NOTHING, label='IDMaestroVehiculoCombustible')
    fechallegada = models.DateTimeField(label='Fecha De Llegada')
    valorsoles = models.DecimalField(label='Valor Soles', max_digits=11, decimal_places=2)
    valordolares = models.DecimalField(label='Valor Dólares', max_digits=13, decimal_places=4)
    llavero = models.IntegerField(verbose_name='Llavero')
    placa = models.CharField(label='Placa', max_length=10)
    numeromotor = models.CharField(label='Número Motor', max_length=20)
    recogida = models.BooleanField(verbose_name='¿Recogida?', default=False)
    numeropoliza = models.CharField(label='Número Poliza', max_length=20)
    fechallegadapoliza = models.DateTimeField(label='Fecha De Llegada De La Poliza')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'almacenubicacionproducto'


class Cierrealmacen(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    numeroalmacen = models.CharField(label='Número Del Almacen', max_length=1)
    fechacierrealmacen = models.DateTimeField(label='Fecha De Cierre Del Almacen')
    glosa = models.CharField(label='Glosa', max_length=500)
    numerooperacioningreso = models.CharField(label='Número De Operación De Ingreso', max_length=20)
    numerooperacionsalida = models.CharField(label='Número De Operación De Salida', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'cierrealmacen'
        unique_together = (('idmaestroalmacen', 'idmaestroempresa', 'idmaestrosucursal', 'fechacierrealmacen'),)


class Componenteproducto(models.Model):
    idcomponente = models.AutoField(label='IdComponente', primary_key=True)
    maestroproductopadre = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProductoPadre')
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    cantidad = models.DecimalField(label='Cantidad', max_digits=18, decimal_places=5)
    observaciones = models.CharField(label='Observaciones', max_length=500)
    estadoregistro = models.BooleanField(verbose_name='¿Estado De Registro?', default=False)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    area = models.ForeignKey(Areas, on_delete=models.CASCADE, verbose_name='Area', blank=True, null=True)
    descripcionimpresion = models.CharField(label='Descripción De Impresión', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'componenteproducto'


class Expedientedetalleregistrospublico(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroexpediente = models.ForeignKey(erpp.gen.models.Maestroexpediente, on_delete=models.CASCADE, verbose_name='MaestroExpediente')
    titulo = models.IntegerField(verbose_name='Título')
    fecharecepcion = models.DateTimeField(label='Fecha De Recepción')
    cargo = models.BooleanField(verbose_name='¿Cargo?', default=False)
    descripcionobservacion = models.CharField(label='Descripción/Observación', max_length=500)
    observacion = models.BooleanField(verbose_name='¿Observación?', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'expedientedetalleregistrospublico'


class Experiencialaboralpersonal(models.Model):
    idexperiencialaboralpersonal = models.AutoField(label='IDExperienciaLaboralPersonal', primary_key=True)
    fechainicio = models.DateField(label='Fecha De Inicio')
    fechacese = models.DateField(label='Fecha De Cese')
    motivo = models.CharField(label='Motivo', max_length=255)
    institucion = models.CharField(label='Institución', max_length=255)
    observacion = models.CharField(label='Observación', max_length=255, blank=True, null=True)
    cargo = models.CharField(label='Cargo', max_length=100)
    maestropersonal = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    usuario = models.CharField(label='Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')

    class Meta:
        db_table = 'experiencialaboralpersonal'


class Guiaremisioncabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    trabajador = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='Trabajador')
    numero = models.IntegerField(verbose_name='Número')
    sucursalorigen = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='SucursalOrigen')
    sucursaldestino = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='SucursalDestino')
    maestrocliente = models.ForeignKey(erpp.fac.models.Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroCliente')
    maestrotransportista = models.ForeignKey(erpp.gen.models.Maestrotransportistas, on_delete=models.CASCADE, verbose_name='MaestroTransportista')
    fechatraslado = models.DateField(label='Fecha De Traslado')
    maestromotivo = models.ForeignKey(erpp.gen.models.Maestromotivo, on_delete=models.CASCADE, verbose_name='MaestroMotivo')
    marca = models.CharField(label='Marca', max_length=50)
    placa = models.CharField(label='Placa', max_length=50)
    licenciaconducir = models.CharField(label='Licencia De Conducir', max_length=50)
    documentopago = models.ForeignKey(erpp.fac.models.Documentofactura, on_delete=models.CASCADE, verbose_name='DocumentoPago')
    numeropago = models.IntegerField(verbose_name='Número Del Pago')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=100)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    tipoguiaremision = models.IntegerField(verbose_name='Tipo De Guía Remisión', blank=True, null=True)
    almacenorigen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='AlmacenOrigen', blank=True, null=True)
    maestroempresadestino = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresaDestino', blank=True, null=True)
    serie = models.CharField(label='Serie', max_length=10, blank=True, null=True)
    marcavehiculo = models.ForeignKey(erpp.conta.models.Vehiculomarca, on_delete=models.CASCADE, verbose_name='MarcaVehiculo', blank=True, null=True)
    almacendestino = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='AlmacenDestino', blank=True, null=True)
    direcciondestino = models.CharField(label='Dirección Del Destino', max_length=300, blank=True, null=True)
    estadoguiaremision = models.IntegerField(verbose_name='Estado Guía De Remisión', blank=True, null=True)
    esguiaexterna = models.BooleanField(verbose_name='¿Es Guia Externa?', blank=True, null=True)
    seriepago = models.CharField(label='Serie Del Pago', max_length=10, blank=True, null=True)
    direccionorigen = models.CharField(label='Direccion Origen', max_length=300, blank=True, null=True)
    pesototal = models.DecimalField(label='Peso Total', max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        db_table = 'guiaremisioncabecera'


class Guiaremisiondetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    guiaremisioncabecera = models.ForeignKey(Guiaremisioncabecera, on_delete=models.CASCADE, verbose_name='GuiaRemisionCabecera')
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    cantidadentero = models.DecimalField(label='Cantidad Entero', max_digits=12, decimal_places=5)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    productolibre = models.CharField(label='Producto Libre', max_length=500, blank=True, null=True)
    areadestino = models.ForeignKey(Areas, on_delete=models.CASCADE, verbose_name='AreaDestino', blank=True, null=True)
    areaorigen = models.ForeignKey(Areas, on_delete=models.CASCADE, verbose_name='AreaOrigen', blank=True, null=True)
    cantidadactualizada = models.DecimalField(label='Cantidad Actualizada', max_digits=12, decimal_places=5, blank=True, null=True)

    class Meta:
        db_table = 'guiaremisiondetalle'


class Maestroaccesoriosequipamiento(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcionaccesorioequipamiento = models.CharField(label='Descripción Accesorio/Equipamiento', max_length=200)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroaccesoriosequipamiento'


class Maestroalmacenoperaciones(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigooperacion = models.CharField(label='Código De Operación', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=50)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroalmacenoperaciones'


class Maestrogrupos(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigogrupo = models.CharField(label='Código De Grupo', max_length=20)
    codigoalmacen = models.CharField(label='Código De Almacen', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    cuentacontable = models.CharField(label='CuentaContable', max_length=50)
    porcentajedescuento = models.DecimalField(label='Porcentaje De Descuento', max_digits=5, decimal_places=2, blank=True, null=True)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    porcentajeganancia = models.DecimalField(label='Porcentaje De Ganancia', max_digits=5, decimal_places=2, blank=True, null=True)
    cuentactbventas = models.CharField(label='Cuenta Contable Ventas', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'maestrogrupos'


class Maestroproductocomplementario(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    producto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='Producto')
    complementario = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='Complementario')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroproductocomplementario'


class Maestroproductoimagen(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    foto = models.BinaryField(label='Foto')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroproductoimagen'


class Maestroproductokit(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    producto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='Producto')
    productokit = models.IntegerField(verbose_name='ProductoKit')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroproductokit'


class Maestroproductosustituto(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    maestroproductosustituto = models.ForeignKey(erpp.inv.models.Maestroproductosustituto, on_delete=models.CASCADE, verbose_name='MaestroProductoSustituto')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroproductosustituto'


class Maestrotipolinea(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigotipolinea = models.CharField(label='Código Tipo De Línea', max_length=20)
    nombretipolinea = models.CharField(label='Nombre Tipo De Línea', max_length=60)
    descripcion = models.CharField(label='Descripción', max_length=120)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipolinea'


class Maestrotiporotacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigorotacion = models.CharField(label='Código De Rotación', max_length=5, blank=True, null=True)
    nombre = models.CharField(label='Nombre', max_length=20, blank=True, null=True)
    descripcion = models.CharField(label='Descripción', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'maestrotiporotacion'


class Pedplant(models.Model):
    id = models.IntegerField(verbose_name='ID', primary_key=True)
    almarea = models.ForeignKey(AlmAreas, on_delete=models.CASCADE, verbose_name='AlmArea')
    producto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='Producto')
    unidadmedida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE, verbose_name='UnidadMedida')
    cantidad = models.IntegerField(verbose_name='Cantidad')

    class Meta:
        db_table = 'pedplant'


class Pedidocabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestrocentrodecosto = models.ForeignKey(erpp.gen.models.Maestrocentrosdecostos, on_delete=models.CASCADE, verbose_name='MaestroCentroDeCosto')
    trabajador = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='Trabajador')
    anulado = models.BooleanField(verbose_name='¿Anulado?', default=False)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    aprobado = models.BooleanField(verbose_name='¿Aprobado?', default=False)
    observacion = models.CharField(label='Observación', max_length=500, blank=True, null=True)
    fechanecesidad = models.DateTimeField(label='Fecha De Necesidad', blank=True, null=True)
    tipoproducto = models.CharField(label='Tipo De Producto', max_length=50, blank=True, null=True)
    tiempoatencion = models.CharField(label='Tiempo De Atención', max_length=50, blank=True, null=True)
    tiposuministro = models.CharField(label='Tipo De Suministro', max_length=50, blank=True, null=True)
    totaldolares = models.DecimalField(label='Total En Dólares', max_digits=18, decimal_places=4, blank=True, null=True)
    totalsoles = models.DecimalField(label='Total En Soles', max_digits=18, decimal_places=2, blank=True, null=True)
    idtipocambio = models.ForeignKey(erpp.gen.models.Maestrotipodecambio, on_delete=models.CASCADE, verbose_name='TipoCambio', blank=True, null=True)
    tipocambio = models.DecimalField(label='Tipo De Cambio', max_digits=6, decimal_places=4, blank=True, null=True)
    servicio = models.BooleanField(verbose_name='¿Servicio?', blank=True, null=True)
    solicitaraprobacion = models.BooleanField(verbose_name='¿Solicitar Aprobacion?', blank=True, null=True)
    fechallegada = models.DateField(label='Fecha De Llegada', blank=True, null=True)
    valegenerado = models.BooleanField(verbose_name='¿Vale Generado?', blank=True, null=True)
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen', blank=True, null=True)

    class Meta:
        db_table = 'pedidocabecera'


class Pedidodetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    pedidocabecera = models.ForeignKey(Pedidocabecera, on_delete=models.CASCADE, verbose_name='PedidoCabecera')
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    motivo = models.CharField(label='Motivo', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    cotizado = models.BooleanField(verbose_name='¿Cotizado?', blank=True, null=True)
    calificado = models.BooleanField(verbose_name='¿Calificado?', blank=True, null=True)
    comprado = models.BooleanField(verbose_name='¿Comprado?', blank=True, null=True)
    especificacion = models.CharField(label='Especificación', max_length=500, blank=True, null=True)
    dolares = models.DecimalField(label='Dólares', max_digits=18, decimal_places=2, blank=True, null=True)
    soles = models.DecimalField(label='Soles', max_digits=18, decimal_places=2, blank=True, null=True)
    nuevodolares = models.DecimalField(label='Nuevo Dólar', max_digits=18, decimal_places=2, blank=True, null=True)
    nuevosoles = models.DecimalField(label='Nuevo Sol', max_digits=18, decimal_places=2, blank=True, null=True)
    cantidadaprobada = models.DecimalField(label='Cantidad Aprobada', max_digits=18, decimal_places=2, blank=True, null=True)
    aprobado = models.BooleanField(verbose_name='¿Aprobado?', blank=True, null=True)
    descripcionproductoref = models.CharField(label='Descripcion Del Producto Referido', max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'pedidodetalle'


class Pedidogenericodetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    facturacabecera = models.ForeignKey(erpp.fac.models.Facturaclientecabecera, on_delete=models.CASCADE, verbose_name='FacturaCabecera')
    maestroplato = models.ForeignKey(erpp.fac.models.Maestroplats, on_delete=models.CASCADE, verbose_name='MaestroPlato')
    tipoplato = models.IntegerField(verbose_name='Tipo De Plato')
    precioventaunitario = models.DecimalField(label='Precio De Venta Unitario', max_digits=11, decimal_places=2)
    cantidad = models.DecimalField(label='Cantidad', max_digits=14, decimal_places=2)
    fechahoraregistro = models.DateTimeField(label='Fecha y Hora De Registro')
    estadoregistro = models.BooleanField(verbose_name='¿Estado De Registro?', default=False)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    observaciondetalle = models.CharField(label='Observación Del Detalle', max_length=500)
    impresacomanda = models.IntegerField(verbose_name='Impresa Comanda', blank=True, null=True)

    class Meta:
        db_table = 'pedidogenericodetalle'


class Pedidogenericodetalleanulacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    pedidogenericodetalle = models.ForeignKey(Pedidogenericodetalle, on_delete=models.CASCADE, verbose_name='PedidoGenericoDetalle', blank=True, null=True)
    facturacabecera = models.ForeignKey(erpp.fac.models.Facturaclientecabecera, on_delete=models.CASCADE, verbose_name='FacturaCabecera')
    maestroplato = models.ForeignKey(erpp.fac.models.Maestroplats, on_delete=models.CASCADE, verbose_name='MaestroPlato')
    tipoplato = models.IntegerField(verbose_name='Tipo De Plato')
    precioventaunitario = models.DecimalField(label='Precio De Venta Unitario', max_digits=11, decimal_places=2)
    cantidad = models.DecimalField(label='Cantidad', max_digits=14, decimal_places=2)
    fechahoraregistro = models.DateTimeField(label='Fecha y Hora De Registro')
    estadoregistro = models.BooleanField(verbose_name='¿Estado De Registro?', default=False)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    observaciondetalle = models.CharField(label='Observación Del Detalle', max_length=500)
    impresacomanda = models.IntegerField(verbose_name='Impresa Comanda', blank=True, null=True)

    class Meta:
        db_table = 'pedidogenericodetalleanulacion'


class Produc(models.Model):
    id = models.AutoField(label='ID', primary_key=True, blank=True, null=True)
    f2 = models.FloatField(verbose_name='F2', blank=True, null=True)

    class Meta:
        db_table = 'produc'


class Productoazar(models.Model):
    id = models.AutoField(label='ID')
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    codigoproducto = models.CharField(label='Código Del Producto', max_length=20)
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigoalmacen = models.CharField(label='Código Del Almacen', max_length=20)
    saldo = models.IntegerField(verbose_name='Saldo')
    fecha = models.DateTimeField(label='Fecha')
    tipo = models.CharField(label='Tipo', max_length=5)

    class Meta:
        db_table = 'productoazar'


class Productos5Dec(models.Model):
    codigo = models.AutoField(label='Código', primary_key=True, blank=True, null=True)
    descripcion = models.CharField(label='Descripción', max_length=255, blank=True, null=True)
    precio_unitario = models.FloatField(verbose_name='Precio Unitario', blank=True, null=True)
    ruta = models.CharField(label='Ruta', max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'productos5dec'
        
        
class Productounitarioimagen(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    almacenubicacionproducto = models.ForeignKey(Almacenubicacionproducto, on_delete=models.CASCADE, verbose_name='AlmacenUbicacionProducto')
    foto = models.BinaryField(label='Foto', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    nombrefoto = models.CharField(label='Nombre De La Foto', max_length=50, blank=True, null=True)
    solicitudnotacredito = models.ForeignKey(erpp.fac.models.Solicitudnotacredito, on_delete=models.CASCADE, verbose_name='SolicitudNotaCredito', blank=True, null=True)
    pedidocabecera = models.ForeignKey(Pedidocabecera, on_delete=models.CASCADE, verbose_name='PedidoCabecera', blank=True, null=True)
    ordencompradetalle = models.ForeignKey(erpp.cmp.models.Ordencompradetalle, on_delete=models.CASCADE, verbose_name='OrdenCompraDetalle', blank=True, null=True)

    class Meta:
        db_table = 'productounitarioimagen'


class Saldoareahistorial(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    area = models.ForeignKey(Areas, on_delete=models.CASCADE, verbose_name='Area')
    fechasaldo = models.DateField(label='Fecha De Saldo')
    saldoinicial = models.DecimalField(label='Saldo Inicial', max_digits=12, decimal_places=5)
    saldofinal = models.DecimalField(label='Saldo Final', max_digits=12, decimal_places=5)

    class Meta:
        db_table = 'saldoareahistorial'


class Saldosdelanhio(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen', blank=True, null=True)
    codigoalmacen = models.CharField(label='Código Del Almacen', max_length=20, blank=True, null=True)
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto', blank=True, null=True)
    codigoproducto = models.CharField(label='Código Del Producto', max_length=20, blank=True, null=True)
    fecha = models.DateField(label='Fecha', blank=True, null=True)
    saldomes = models.DecimalField(label='Saldo Del Mes', max_digits=11, decimal_places=2, blank=True, null=True)
    costopromediosoles = models.DecimalField(label='Costo Promedio En Soles', max_digits=11, decimal_places=2, blank=True, null=True)
    costopromediodolares = models.DecimalField(label='Costo Promedio En Dólares', max_digits=13, decimal_places=4, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'saldosdelanhio'


class Saldosxalmacenes(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigoalmacen = models.CharField(label='Código Del Almacen', max_length=20)
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    codigoproducto = models.CharField(label='Código Del Producto', max_length=20)
    numerooperacion = models.CharField(label='Número De Operación', max_length=20)
    cantidadingresosalmacen = models.DecimalField(label='Cantidad De Ingresos Del Almacen', max_digits=12, decimal_places=5)
    cantidadsalidasalmacen = models.DecimalField(label='Cantidad De Salidas Del Almacen', max_digits=12, decimal_places=5)
    saldoalmacen = models.DecimalField(label='Saldo Del Almacen', max_digits=12, decimal_places=5)
    entregafutura = models.DecimalField(label='Entrega Futura', max_digits=12, decimal_places=5)
    saldofisico = models.DecimalField(label='Saldo Físico', max_digits=12, decimal_places=5)
    codigoubicacion = models.CharField(label='Código De Ubicación', max_length=20, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    rotacion = models.CharField(label='Rotación', max_length=5, blank=True, null=True)
    ultimocostodolares = models.DecimalField(label='Último Costo En Dólares', max_digits=12, decimal_places=5, blank=True, null=True)
    ultimocostosoles = models.DecimalField(label='Último Costo En Soles', max_digits=12, decimal_places=5, blank=True, null=True)
    costopromediodolares = models.DecimalField(label='Costo Promedio En Dólares', max_digits=12, decimal_places=5, blank=True, null=True)
    costopromediosoles = models.DecimalField(label='Costo Promedio En Soles', max_digits=12, decimal_places=5, blank=True, null=True)
    importeacumuladodolares = models.DecimalField(label='Importe Acumulado En Dólares', max_digits=12, decimal_places=5, blank=True, null=True)
    importeacumuladosoles = models.DecimalField(label='Importe Acumulado En Soles', max_digits=12, decimal_places=5, blank=True, null=True)

    class Meta:
        db_table = 'saldosxalmacenes'


class Saldosxarea(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroarea = models.ForeignKey(Areas, on_delete=models.CASCADE, verbose_name='MaestroArea')
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='IDMaestroProducto')
    codigoproducto = models.CharField(label='Código Del Producto', max_length=20)
    numerooperacion = models.CharField(label='Número De Operación', max_length=20)
    cantidadingresosalmacen = models.DecimalField(label='Cantidad De Ingresos Del Almacen', max_digits=12, decimal_places=5)
    cantidadsalidasalmacen = models.DecimalField(label='Cantidad De Salidas Del Almacen', max_digits=12, decimal_places=5)
    saldoalmacen = models.DecimalField(label='Saldo Del Almacen', max_digits=12, decimal_places=5)
    entregafutura = models.DecimalField(label='Entrega Futura', max_digits=12, decimal_places=5)
    saldofisico = models.DecimalField(label='Saldo Físico', max_digits=12, decimal_places=5)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    rotacion = models.CharField(label='Rotación', max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'saldosxarea'


class Stock(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa', blank=True, null=True)
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal', blank=True, null=True)
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen', blank=True, null=True)
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    stockactual = models.IntegerField(verbose_name='Stock Actual')
    stockminimo = models.IntegerField(verbose_name='Stock Mínimo')
    stockmaximo = models.IntegerField(verbose_name='Stock Máximo')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'stock'


class Tablaimagen(models.Model):
    id = models.AutoField(label='Id', primary_key=True)
    imagen = models.BinaryField(label='Imagen', blank=True, null=True)

    class Meta:
        db_table = 'tablaimagen'


class Transformacioncabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    motivo = models.CharField(label='Motivo', max_length=500)
    precioventasoles = models.DecimalField(label='Precio De Venta En Soles', max_digits=18, decimal_places=2, blank=True, null=True)
    precioventadolares = models.DecimalField(label='Precio De Venta En Dólares', max_digits=18, decimal_places=2, blank=True, null=True)
    fechatransformacion = models.DateTimeField(label='Fecha De Transformación', blank=True, null=True)
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MestroAlmacen', blank=True, null=True)
    almaceningreso = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='AlmacenIngreso', blank=True, null=True)
    almacensalida = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='AlmacenSalida', blank=True, null=True)
    tipotransformacion = models.IntegerField(verbose_name='Tipo De Transformación', blank=True, null=True)

    class Meta:
        db_table = 'transformacioncabecera'


class Transformaciondetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    transformacioncabecera = models.ForeignKey(Transformacioncabecera, on_delete=models.CASCADE, verbose_name='TransformacionCabecera')
    maestroproducto = models.ForeignKey(Maestroproductos, on_delete=models.CASCADE, verbose_name='MaestroProducto')
    cantidad = models.DecimalField(label='Cantidad', max_digits=18, decimal_places=2)
    costosoles = models.DecimalField(label='Costo En Soles', max_digits=18, decimal_places=2, blank=True, null=True)
    costodolares = models.DecimalField(label='Costo En Dólares', max_digits=18, decimal_places=2, blank=True, null=True)
    esiingreso = models.BooleanField(verbose_name='¿Es Ingreso?', blank=True, null=True)
    conceptolibre = models.CharField(label='Concepto Libre', max_length=200, blank=True, null=True)
    almacencabecera = models.ForeignKey(Almacencabecera, on_delete=models.CASCADE, verbose_name='AlmacenCabecera', blank=True, null=True)

    class Meta:
        db_table = 'transformaciondetalle'


class Trasladounidad(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    almacenubicacionproducto = models.ForeignKey(Almacenubicacionproducto, on_delete=models.CASCADE, verbose_name='AlmacenUbicacionProducto')
    fechallegada = models.DateTimeField(label='Fecha De Llegada')
    maestrocliente = models.ForeignKey(erpp.fac.models.Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroCliente')
    numerofactura = models.CharField(label='Número De Factura', max_length=20)
    numeroembarque = models.CharField(label='Número De Embarque', max_length=20)
    numerocase = models.CharField(label='Número De Case', max_length=5)
    revisado = models.BooleanField(verbose_name='¿Revisado?', default=False)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'trasladounidad'


class Usuarioalmacen(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    user = models.ForeignKey(erpp.cita.models.Usuarioweb, on_delete=models.CASCADE, verbose_name='User', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36, blank=True, null=True)
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen', blank=True, null=True)

    class Meta:
        db_table = 'usuarioalmacen'
