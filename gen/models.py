from django.db import models

import erpp.cmp.models
import erpp.conta.models
import erpp.fac.models
import erpp.serv.models


class Configuracionreportes(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    nombrearchivo = models.CharField(label='Nombre De Archivo', max_length=50, blank=True, null=True)
    nombrevisual = models.CharField(label='Nombre Visual', max_length=100, blank=True, null=True)
    modulo = models.CharField(label='Módulo', max_length=50, blank=True, null=True)
    maestro = models.BooleanField(verbose_name='¿Maestro?', blank=True, null=True)
    ruta = models.CharField(label='Ruta', max_length=100, blank=True, null=True)
    icono = models.CharField(label='Ícono', max_length=100, blank=True, null=True)
    abreviacion = models.CharField(label='Abreviación', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'configuracionreportes'


class Maestroempresas(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestrotipoempresa = models.ForeignKey(erpp.gen.models.Maestrotipoempresa, on_delete=models.CASCADE, verbose_name='MaestroTipoEmpresa')
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20)
    codigotipoempresa = models.CharField(label='Codigo Tipo Empresa', max_length=20)
    representantelegal = models.CharField(label='Representante Legal', max_length=200)
    contacto = models.CharField(label='Contacto', max_length=200)
    descripcion = models.CharField(label='Descripción', max_length=200)
    descripcionlarga = models.CharField(label='Descripción Larga', max_length=200, blank=True, null=True)
    direccion = models.CharField(label='Direccion', max_length=200)
    ruc = models.CharField(label='RUC', max_length=22)
    telefono = models.CharField(label='Teléfono', max_length=25)
    fax = models.CharField(label='Fax', max_length=25)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    contabautomatico = models.BooleanField(verbose_name='¿Contabilizador Automático?', blank=True, null=True)
    tipocontab1as2cc3tod4otr = models.IntegerField(verbose_name='Tipo Contabilizador', blank=True, null=True)
    firmadigital = models.TextField(label='Firma Digital', blank=True, null=True)

    class Meta:
        db_table = 'maestroempresas'


class Maestrosucursales(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20)
    codigosucursal = models.CharField(label='Código De La Sucursal', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=200)
    direccion = models.CharField(label='Dirección', max_length=500)
    codigociudad = models.CharField(label='Código De La Ciudad', max_length=20)
    responsable = models.CharField(label='Responsable', max_length=100)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    ubigeo = models.ForeignKey(erpp.gen.models.Maestroubigeo, on_delete=models.CASCADE, verbose_name='Ubigeo')
    numero = models.IntegerField(verbose_name='Número')
    interior = models.CharField(label='Interior', max_length=20)
    zona = models.CharField(label='Zona', max_length=20)
    telefono = models.CharField(label='Teléfono', max_length=25)
    celular = models.CharField(label='Celular', max_length=25)
    email = models.CharField(label='Email', max_length=60)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    direccioncompleta = models.CharField(label='Dirección Completa', max_length=500, blank=True, null=True)
    lcsunat = models.IntegerField(verbose_name='LC Sunat')

    class Meta:
        db_table = 'maestrosucursales'
        unique_together = (('codigosucursal', 'idmaestroempresa'),)


class Maestrocontrolcalidad(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    nombre = models.CharField(label='Nombre', max_length=100)
    tipocontrol = models.ForeignKey(erpp.conta.models.Controlcontable, on_delete=models.CASCADE, verbose_name='TipoControl')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrocontrolcalidad'


class Hojacalidad(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    ordenserviciocabecera = models.ForeignKey(erpp.serv.models.Ordenserviciocabecera, on_delete=models.CASCADE, verbose_name='OrdenServicioCabecera')
    maestrocontrolcalidad = models.ForeignKey(Maestrocontrolcalidad, on_delete=models.CASCADE, verbose_name='MaestroControlCalidad')
    resultado = models.CharField(label='Resultado', max_length=75)
    etapa = models.CharField(label='Etapa', max_length=75)
    observaciones = models.CharField(label='Observaciones', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    fechaingreso = models.DateField(label='Fecha De Ingreso', blank=True, null=True)

    class Meta:
        db_table = 'hojacalidad'


class Maestroalmacenes(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigosucursal = models.CharField(label='Código De La Sucursal', max_length=20)
    codigoalmacen = models.CharField(label='Código Del Almacen', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    viatipo = models.CharField(label='Vía Tipo', max_length=60)
    vianombre = models.CharField(label='Vía Nombre', max_length=60)
    numero = models.CharField(label='Número', max_length=15)
    interior = models.CharField(label='Interior', max_length=15)
    zona = models.CharField(label='Zona', max_length=60)
    ubigeo = models.ForeignKey(erpp.gen.models.Maestroubigeo, on_delete=models.CASCADE, verbose_name='Ubigeo')
    direccion = models.CharField(label='Dirección', max_length=500)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    tipoalm = models.CharField(label='Tipo Almacen', max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'maestroalmacenes'


class Maestrobancos(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigobanco = models.CharField(label='Código Del Banco', max_length=20)
    nombrebanco = models.CharField(label='Nombre Del Banco', max_length=60)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    ruc = models.CharField(label='RUC', max_length=11)
    direccion = models.CharField(label='Dirección', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrobancos'
        unique_together = (('codigobanco', 'idmaestroempresa'),)


class Maestrocentrosdecostos(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigocentrocostos = models.CharField(label='Código Centro De Costos', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    mayor = models.BooleanField(verbose_name='Mayor')
    codigocuentamayor = models.CharField(label='Código Cuenta Mayor', max_length=20)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrocentrosdecostos'


class Maestrociudades(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    ubigeo = models.ForeignKey(erpp.gen.models.Maestroubigeo, on_delete=models.CASCADE, verbose_name='Ubigeo')
    codigociudad = models.CharField(label='Código De La Ciudad', max_length=20)
    nombreciudad = models.CharField(label='Nombre De La Ciudad', max_length=20)
    nombrepais = models.CharField(label='Nombre Del País', max_length=20)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrociudades'
        unique_together = (('codigociudad', 'idmaestroempresa'),)


class Maestrodatosgenerales(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    fld1 = models.CharField(label='FLD1', max_length=1)
    porcentajeigv = models.DecimalField(label='Porcentaje IGV', max_digits=5, decimal_places=2)
    mensajeenfacturas = models.CharField(label='Mensaje En Facturas', max_length=60)
    porcentajeinteresletrasnormal = models.DecimalField(label='Porcentaje De Interés En Letras Normal', max_digits=5, decimal_places=2)
    porcentajeinteresletrasatrazado = models.DecimalField(label='Porcentaje De Interés En Letras Atrazado', max_digits=5, decimal_places=2)
    descuentomayoristasoles = models.DecimalField(label='Descuento Mayorista En Soles', max_digits=11, decimal_places=2)
    descuentomayoristadolares = models.DecimalField(label='Descuento Mayorista En Dólares', max_digits=13, decimal_places=4)
    gastosadministrativosletrassoles = models.DecimalField(label='Gastos Administrativos De Letras En Soles', max_digits=11, decimal_places=2)
    gastosadministrativosletrasdolares = models.DecimalField(label='Gastos Administrativos De Letras En Dólares', max_digits=13, decimal_places=4)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    descuentorepuestos = models.DecimalField(label='Descuento En Repuestos', max_digits=5, decimal_places=2, blank=True, null=True)
    descuentotaller = models.DecimalField(label='Descuento En Taller', max_digits=5, decimal_places=2, blank=True, null=True)
    importeretencion = models.DecimalField(label='Importe De Retención', max_digits=11, decimal_places=4, blank=True, null=True)
    porcentajeretencion = models.DecimalField(label='Porcentaje De Retención', max_digits=5, decimal_places=2, blank=True, null=True)
    saldosnegativos = models.BooleanField(verbose_name='¿Saldos Negativos?', blank=True, null=True)
    horastrabajo = models.IntegerField(verbose_name='Horas De Trabajo', blank=True, null=True)
    porcentajeutilidadproductoalmacen = models.DecimalField(label='Porcentaje De Utilidad En Producto Almacen', max_digits=5, decimal_places=2, blank=True, null=True)
    porcentajeutilidadproductoventa = models.DecimalField(label='Porcentaje De Utilidad En Producto Venta', max_digits=5, decimal_places=2, blank=True, null=True)
    porcentajedescuentoflotas = models.DecimalField(label='Porcentaje De Descuento En Flotas', max_digits=5, decimal_places=2, blank=True, null=True)
    cuentacontableigv = models.CharField(label='Cuenta Contable IGV', max_length=50, blank=True, null=True)
    cuentacontablerenta = models.CharField(label='Cuenta Contable Renta', max_length=50, blank=True, null=True)
    cuentacontablefacturacliente = models.CharField(label='Cuenta Contable Factura Cliente', max_length=50, blank=True, null=True)
    cuentacontableretencion = models.CharField(label='Cuenta Contable Retención', max_length=50, blank=True, null=True)
    maestroclientestockordenpedido = models.ForeignKey(erpp.fac.models.Maestroclientes, on_delete=models.CASCADE, verbose_name='MaestroClienteStockOrdenPedido', blank=True, null=True)
    cuentacontablecierrecaja = models.CharField(label='Cuenta Contable Cierre Caja', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'maestrodatosgenerales'
        unique_together = (('fld1', 'idmaestroempresa'),)


class Maestrodocumentossunat(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    tipodocumento = models.CharField(label='Tipo De Documento', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    essunat = models.BooleanField(verbose_name='¿Es Sunat?', blank=True, null=True)

    class Meta:
        db_table = 'maestrodocumentossunat'
        unique_together = (('idmaestroempresa', 'tipodocumento'),)


class Maestroempresadatosadicionales(models.Model):
    id = models.OneToOneField('Maestroempresas', models.DO_NOTHING, label='ID', primary_key=True)
    logofondo = models.BinaryField(label='Logo Fondo', blank=True, null=True)
    logoreporte = models.BinaryField(label='Logo Reporte', blank=True, null=True)
    colorbarra = models.CharField(label='Color Barra', max_length=9, blank=True, null=True)
    colorfondo = models.CharField(label='Color Fondo', max_length=9, blank=True, null=True)
    colorreportes = models.CharField(label='Color Reportes', max_length=9, blank=True, null=True)
    tipodeletra = models.CharField(label='Tipo De Letra', max_length=50, blank=True, null=True)
    fechainicio = models.DateField(label='Fecha Inicio')
    fechatermino = models.DateField(label='Fecha Termino')
    nrousuariosmax = models.IntegerField(verbose_name='Número De Usuarios Máximo')
    tamanhobdmb = models.IntegerField(verbose_name='Tamaño BDMB')
    email = models.CharField(label='EMail', max_length=259)

    class Meta:
        db_table = 'maestroempresadatosadicionales'


class Maestroestadosdeatencion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    color = models.CharField(label='Color', max_length=50)
    descripcion = models.CharField(label='Descripción', max_length=200)
    cantidadmaxima = models.IntegerField(verbose_name='Cantidad Máxima')
    prioridad = models.IntegerField(verbose_name='Prioridad')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroestadosdeatencion'


class Maestroestadocivil(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoestadocivil = models.CharField(label='Código Estado Civil', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=15)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroestadocivil'


class Maestroformasdepago(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoformapago = models.CharField(label='Código De Forma De Pago', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    diascredito = models.IntegerField(verbose_name='Días Credito')
    tasainteressoles = models.DecimalField(label='Tasa De Interés En Soles', max_digits=5, decimal_places=2)
    tasainteresdolares = models.DecimalField(label='Tasa De Interés En Dólares', max_digits=5, decimal_places=2)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    maestrotipoformapago = models.ForeignKey(erpp.gen.models.Maestrotipoformapago, on_delete=models.CASCADE, verbose_name='MaestroTipoFormaPago')
    tipoformapago = models.CharField(label='Tipo Forma De Pago', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroformasdepago'
        unique_together = (('codigoformapago', 'idmaestroempresa'),)


class Maestrolineascomerciales(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigolineacomercial = models.CharField(label='Código De Línea Comercial', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrolineascomerciales'


class Maestromaterialconstruccion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcion = models.CharField(label='Descripción', max_length=50)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestromaterialconstruccion'


class Maestromoneda(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigomoneda = models.CharField(label='Código De Moneda', unique=True, max_length=20)
    nombre = models.CharField(label='Nombre', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestromoneda'


class Maestromotivo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestromotivo'


class Maestromotor(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcionmotor = models.CharField(label='Descripción Del Motor', max_length=100)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestromotor'


class Maestronacionalidad(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigonacionalidad = models.CharField(label='Código De La Nacionalidad', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestronacionalidad'


class Maestrooperacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    nombreoperacion = models.CharField(label='Nombre De La Operación', max_length=500)
    descripcion = models.CharField(label='Descripción', max_length=500, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=50)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=50)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrooperacion'


class Maestropaisemisordocumento(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigopaisemisordocumento = models.CharField(label='Código Del País Emisor Del Documento', max_length=20)
    nombrepaisemisor = models.CharField(label='Nombre Del País Emisor', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestropaisemisordocumento'


class Maestroproveedores(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    nombrecomercial = models.CharField(label='Nombre Del Comercial', max_length=200)
    propietario = models.CharField(label='Propietario', max_length=200)
    pais = models.CharField(label='País', max_length=20)
    viatipo = models.CharField(label='Vía Tipo', max_length=60)
    vianombre = models.CharField(label='Vía Nombre', max_length=60)
    numero = models.CharField(label='Número', max_length=15)
    interior = models.CharField(label='Interior', max_length=15)
    zona = models.CharField(label='Zona', max_length=60)
    ubigeo = models.ForeignKey(erpp.gen.models.Maestroubigeo, on_delete=models.CASCADE, verbose_name='Ubigeo')
    direccion = models.CharField(label='Dirección', max_length=500)
    personajuridica = models.BooleanField(verbose_name='¿Persona Jurídica?', default=False)
    telefono = models.CharField(label='Teléfono', max_length=25)
    fax = models.CharField(label='Fax', max_length=25)
    ruc = models.CharField(label='RUC', max_length=11)
    tipoproveedor = models.CharField(label='Tipo De Proveedor', max_length=20)
    email = models.CharField(label='Email', max_length=60)
    paginaweb = models.CharField(label='Página Web', max_length=60)
    codigolinea = models.CharField(label='Código De Línea', max_length=20)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    idtipoproveedor = models.ForeignKey(erpp.cmp.models.Maestrotipoproveedores, on_delete=models.CASCADE, verbose_name='TipoProveedor')
    marca = models.CharField(label='Marca', max_length=75)
    detraccion = models.CharField(label='Detracción', max_length=75)
    observacion = models.CharField(label='Observación', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    primerapellido = models.CharField(label='Primer Apellido', max_length=50, blank=True, null=True)
    segundoapellido = models.CharField(label='Segundo Apellido', max_length=50, blank=True, null=True)
    nombres = models.CharField(label='Nombres', max_length=50, blank=True, null=True)
    codigocuentacontable = models.CharField(label='Código De Cuenta Contable', max_length=20, blank=True, null=True)
    codigocuentacontabledolar = models.CharField(label='Código De Cuenta Contable En Dólares', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'maestroproveedores'
        unique_together = (('idmaestroempresa', 'nombrecomercial', 'ruc', 'tipoproveedor'),)


class Maestrorepresentantedelbanco(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestrobanco = models.ForeignKey(Maestrobancos, on_delete=models.CASCADE, verbose_name='MaestroBanco')
    nombres = models.CharField(label='Nombres', max_length=50)
    apellidopaterno = models.CharField(label='Apellido Paterno', max_length=50)
    apellidomaterno = models.CharField(label='Apellido Materno', max_length=50)
    dni = models.CharField(label='DNI', max_length=8)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrorepresentantedelbanco'
        unique_together = (('dni', 'idmaestroempresa'),)


class Maestroseccion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoseccion = models.CharField(label='Código De La Sección', max_length=20)
    clasetabla = models.CharField(label='Clase Tabla', max_length=4)
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroseccion'


class Maestrotipocontrato(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigotipocontrato = models.CharField(label='Código Tipo De Contrato', max_length=20)
    clasetabla = models.CharField(label='Clase Tabla', max_length=5)
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipocontrato'


class Maestrotipodecambio(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    fechacambio = models.DateTimeField(label='Fecha De Cambio')
    codigomoneda = models.CharField(label='Código De La Moneda', max_length=20)
    dolarpromedio = models.DecimalField(label='Dolar Promedio', max_digits=13, decimal_places=4)
    dolarcompra = models.DecimalField(label='Dolar Compra', max_digits=13, decimal_places=4)
    dolarventa = models.DecimalField(label='Dolar Venta', max_digits=13, decimal_places=4)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipodecambio'


class Maestrotipoempresa(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigotipoempresa = models.CharField(label='Código Tipo De Empresa', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipoempresa'


class Maestrotipofinanciamiento(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigofinanciamiento = models.CharField(label='Código Del Financiamiento', max_length=20)
    nombrefinanciamiento = models.CharField(label='Nombre Del Financiamiento', max_length=60)
    descripcion = models.CharField(label='Descripción', max_length=60)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipofinanciamiento'


class Maestrotipoformapago(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    centrodecosto = models.ForeignKey(Maestrocentrosdecostos, on_delete=models.CASCADE, verbose_name='CentroDeCosto')
    descripcion = models.CharField(label='Descripción', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipoformapago'


class Maestrotipooperacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    tipooperacion = models.CharField(label='Tipo De Operación', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipooperacion'
        unique_together = (('idmaestroempresa', 'tipooperacion'),)


class Maestrotipoorden(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    nombre = models.CharField(label='Nombre', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipoorden'


class Maestrotiposangre(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripciontiposangre = models.CharField(label='Descripción Tipo De Sangre', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotiposangre'


class Maestrotiposdocumentos(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    tipomovimiento = models.CharField(label='Tipo De Movimiento', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    nacional = models.BooleanField(verbose_name='¿Nacional?', default=False)
    ingreso = models.BooleanField(verbose_name='¿Ingreso?', default=False)
    factura = models.BooleanField(verbose_name='¿Factura?', default=False)
    creditofiscal = models.BooleanField(verbose_name='¿Crédito Fiscal?', default=False)
    operacionresta = models.BooleanField(verbose_name='¿Operación Resta?', default=False)
    valorado = models.BooleanField(verbose_name='¿Valorado?', default=False)
    otros = models.CharField(label='Otros', max_length=20)
    tipodocumento = models.CharField(label='Tipo De Documento', max_length=20)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    proveedorcliente = models.BooleanField(verbose_name='¿Proveedor Del Cliente?', blank=True, null=True)
    pertenecientea = models.CharField(label='Perteneciente A', max_length=1, blank=True, null=True)
    tipooperacionsunat = models.CharField(label='Tipo De Operacion Sunat', max_length=5, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotiposdocumentos'
        unique_together = (('idmaestroempresa', 'tipomovimiento'),)


class Maestrotiposdocumentostabla12(models.Model):
    id = models.AutoField(label='ID', unique=True)
    tipooperacion = models.CharField(label='Tipo De Operación', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)

    class Meta:
        db_table = 'maestrotiposdocumentostabla12'


class Maestrotipovia(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigotipovia = models.CharField(label='Código Tipo Vía', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipovia'


class Maestrotipozona(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigotipozona = models.CharField(label='Código Tipo De Zona', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipozona'


class Maestrotransportistas(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigosucursal = models.CharField(label='Código De La Sucursal', max_length=20)
    codigotransportista = models.CharField(label='Código Del Transportista', max_length=20)
    razonsocial = models.CharField(label='Razón Social', max_length=60)
    ruc = models.CharField(label='RUC', max_length=11)
    direccion = models.CharField(label='Dirección', max_length=60)
    certificadoinscripcion = models.CharField(label='Certificado De Inscripción', max_length=20)
    nombrecomercial = models.CharField(label='Nombre Del Comercial', max_length=60)
    tipo = models.CharField(label='Tipo', max_length=20)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestrosucursales = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursales')

    class Meta:
        db_table = 'maestrotransportistas'
        unique_together = (('codigotransportista', 'idmaestroempresa'), ('idmaestroempresa', 'ruc'),)


class Maestroubigeo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigoregion = models.CharField(label='Código De Región', max_length=2)
    codigodepartamento = models.CharField(label='Código Del Departamento', max_length=2)
    codigoprovincia = models.CharField(label='Código De La Provincia', max_length=2)
    codigodistrito = models.CharField(label='Código Del Distrito', max_length=2)
    nombreregion = models.CharField(label='Nombre De La Región', max_length=100)
    nombredepartamento = models.CharField(label='Nombre Del Departamento', max_length=100)
    nombreprovincia = models.CharField(label='Nombre De La Provincia', max_length=100)
    nombredistrito = models.CharField(label='Nombre Del Distrito', max_length=100)

    class Meta:
        db_table = 'maestroubigeo'


class Maestrounidadesdemedida(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigounidadmedida = models.CharField(label='Código De La Unidad Medida', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    valor = models.IntegerField(verbose_name='Valor')
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    unidaddemedidasunat = models.ForeignKey(erpp.gen.models.Maestrounidadesdemedida, on_delete=models.CASCADE, verbose_name='UnidadDeMedidaSunat', blank=True, null=True)

    class Meta:
        db_table = 'maestrounidadesdemedida'
        unique_together = (('codigounidadmedida', 'idmaestroempresa'),)


class Maestrounidadesdemedidatabla6(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigounidadmedida = models.CharField(label='Código De Unidad De Medida', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    abreviacion = models.CharField(label='Abreviacion', max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'maestrounidadesdemedidatabla6'


class Maestrousuario(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigo = models.CharField(label='Código', max_length=36)
    descripcion = models.CharField(label='Descripción', max_length=60)
    codigoresponsabilidad = models.CharField(label='Código De Responsabilidad', max_length=20)
    usuario = models.CharField(label='Usuario', max_length=15)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigosucursal = models.CharField(label='Código De La Sucursal', max_length=20)
    codigoalmacen = models.CharField(label='Código Del Almacen', max_length=20)
    numeroseriegr = models.CharField(label='Número De Serie De Guía De Responsabilidad', max_length=20)
    numeroguiar = models.CharField(label='Número De Guía De Responsabilidad', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrousuario'
        unique_together = (('codigoresponsabilidad', 'idmaestroempresa'), ('codigousuario', 'idmaestroempresa'),)


class Maestrousuarionotasventas(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestrousuario = models.ForeignKey(Maestrousuario, on_delete=models.CASCADE, verbose_name='MaestroUsuario')
    maestroalmacen = models.ForeignKey(Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen')
    codigosucursal = models.CharField(label='Código De La Sucursal', max_length=20)
    codigoalmacen = models.CharField(label='Código Del Almacen', max_length=20)
    numeroseried = models.CharField(label='Número De Serie D', max_length=20)
    numerodocumentod = models.CharField(label='Número De Documento D', max_length=20)
    numeroseriec = models.CharField(label='Número De Serie C', max_length=20)
    numerodocumentoc = models.CharField(label='Número De Documento C', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrousuarionotasventas'


class Maestrozonas(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigozona = models.CharField(label='Código De La Zona', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    maestrociudades = models.ForeignKey(Maestrociudades, on_delete=models.CASCADE, verbose_name='MaestroCiudades')
    codigociudad = models.CharField(label='Código De La Ciudad', max_length=20)
    maestrovendedor = models.ForeignKey(Maestroproveedores, on_delete=models.CASCADE, verbose_name='MaestroVendedor')
    codigovendedor = models.CharField(label='Código Del Vendedor', max_length=20)
    metaventassoles = models.DecimalField(label='Meta De Ventas En Soles', max_digits=11, decimal_places=2)
    metaventasdolares = models.DecimalField(label='Meta De Ventas En Dólares', max_digits=13, decimal_places=4)
    metacobranzasoles = models.DecimalField(label='Meta De Cobranza En Soles', max_digits=11, decimal_places=2)
    metacobranzadolares = models.DecimalField(label='Meta De Cobranza En Dólares', max_digits=13, decimal_places=4)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrozonas'
        unique_together = (('codigozona', 'idmaestroempresa'),)


class Reniec(models.Model):
    dni = models.CharField(label='DNI', primary_key=True, max_length=8)
    apellidopaterno = models.CharField(label='Apellido Paterno', max_length=40, blank=True, null=True)
    apellidomaterno = models.CharField(label='Apellido Materno', max_length=40, blank=True, null=True)
    nombre = models.CharField(label='Nombre', max_length=30, blank=True, null=True)
    sexo = models.CharField(label='Sexo', max_length=1)

    class Meta:
        db_table = 'reniec'


class Reportegenerados(models.Model):
    idreporte = models.AutoField(label='IdReporte', primary_key=True)
    rutafisica = models.TextField(label='Ruta Física')
    archivo = models.CharField(label='Archivo', max_length=200)
    fechacreacion = models.DateField(label='Fecha De Creación')

    class Meta:
        db_table = 'reportegenerados'


class Secuencias(models.Model):
    nombresecuencia = models.CharField(label='Nombre De Secuencia', primary_key=True, max_length=255)
    semilla = models.IntegerField(verbose_name='Semilla')
    incremento = models.IntegerField(verbose_name='Incremento')
    valoractual = models.IntegerField(verbose_name='Valor Actual', blank=True, null=True)

    class Meta:
        db_table = 'secuencias'


class UsuarioSistemas(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    empresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresas')
    surcursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursales')
    almacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacenes')

    class Meta:
        db_table = 'usuariosistemas'


class Maestrocubiculo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigocubiculo = models.CharField(label='Código Del Cubículo', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrocubiculo'


class Maestroexpediente(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroexpedientesituacion = models.ForeignKey(erpp.gen.models.Maestroexpedientesituacion, on_delete=models.CASCADE, verbose_name='MaestroExpedienteSituacion')
    ordenpedido = models.ForeignKey(erpp.serv.models.Ordenpedido, on_delete=models.CASCADE, verbose_name='OrdenPedido')
    maestroformapago = models.ForeignKey(Maestrotipoformapago, on_delete=models.CASCADE, verbose_name='MaestroFormaPago')
    numerooperacion = models.IntegerField(verbose_name='Número De La Operación')
    tarjetapropiedad = models.BooleanField(verbose_name='¿Tarjeta De Propiedad?', default=False)
    fechallegadatarjetapropiedad = models.DateTimeField(label='Fecha De Llegada Tarjeta De Propiedad')
    placa = models.CharField(label='Placa', max_length=7)
    fechallegadaplaca = models.DateTimeField(label='Fecha De Llegada Placa')
    inscripcionmunicipalidad = models.BooleanField(verbose_name='¿Inscripción Municipalidad?', default=False)
    numerorecibomunicipalidad = models.CharField(label='Número De Recibo Municipalidad', max_length=10)
    leasing = models.BooleanField(verbose_name='¿Leasing?', default=False)
    numerocuotas = models.IntegerField(verbose_name='Número Cuotas')
    declaracionjurada = models.BooleanField(verbose_name='¿Declaración Jurada?', default=False)
    cartapodertarjeta = models.BooleanField(verbose_name='¿Carta Poder Tarjeta?', default=False)
    cartapoderplaca = models.BooleanField(verbose_name='¿Carta Poder Placa?', default=False)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroexpediente'


class Maestroexpedientesituacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroexpedientesituacion'


class Componentebase(models.Model):
    idcompbase = models.IntegerField(verbose_name='IDCompBase', primary_key=True)
    codigocompbase = models.CharField(label='Código De Componente Base', max_length=50)
    descripcion = models.CharField(label='Descripción', max_length=200, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=100, blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'componentebase'


class Maestrotipoaveria(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcion = models.CharField(label='Descripción', max_length=100)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipoaveria'