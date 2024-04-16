from django.db import models

import erpp.conta.models
import erpp.fac.models
import erpp.gen.models
import erpp.inv.models
import erpp.serv.models


class Cargos(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigocargo = models.CharField(label='Código De Cargo', max_length=10)
    codigocargopadre = models.CharField(label='Código De Cargo Padre', max_length=10)
    descripcion = models.CharField(label='Descripción', max_length=50)
    areas = models.ForeignKey(erpp.inv.models.Areas, on_delete=models.CASCADE, verbose_name='Areas')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestroalmacen = models.ForeignKey(erpp.gen.models.Maestroalmacenes, on_delete=models.CASCADE, verbose_name='MaestroAlmacen', blank=True, null=True)
    maestrocentrodecosto = models.ForeignKey(erpp.gen.models.Maestrocentrosdecostos, on_delete=models.CASCADE, verbose_name='MaestroCentroDeCosto', blank=True, null=True)

    class Meta:
        db_table = 'cargos'


class Cargostrabajador(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE, verbose_name='Cargo')
    trabajador = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='IdTrabajador')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'cargostrabajador'


class Datosplanilla(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestropersonal = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    maestroaccidentetrabajo = models.ForeignKey(erpp.per.models.Maestroaccidentetrabajo, on_delete=models.CASCADE, verbose_name='MaestroAccidenteTrabajo')
    maestronivelcategoria = models.ForeignKey(erpp.per.models.Maestronivelcategoria, on_delete=models.CASCADE, verbose_name='MaestroNivelCategoria')
    maestroregimenlaboral = models.ForeignKey(erpp.per.models.Maestroregimenlaboral, on_delete=models.CASCADE, verbose_name='MaestroRegimenLaboral')
    maestrotipopersonal = models.ForeignKey(erpp.per.models.Maestrotipopersonal, on_delete=models.CASCADE, verbose_name='MaestroTipoPersonal')
    maestrosalud = models.ForeignKey(erpp.per.models.Maestrosalud, on_delete=models.CASCADE, verbose_name='MaestroSalud')
    maestropensiones = models.ForeignKey(erpp.per.models.Maestropensiones, on_delete=models.CASCADE, verbose_name='MaestroPensiones')
    maestroafp = models.ForeignKey(erpp.per.models.Maestroafp, on_delete=models.CASCADE, verbose_name='MaestroAFP')
    maestrocargoocupacion = models.ForeignKey(erpp.per.models.Maestrocargoocupacion, on_delete=models.CASCADE, verbose_name='MaestroCargoOcupacion')
    maestroseccion = models.ForeignKey(erpp.gen.models.Maestroseccion, on_delete=models.CASCADE, verbose_name='MaestroSeccion')
    maestrotipocontrato = models.ForeignKey(erpp.gen.models.Maestrotipocontrato, on_delete=models.CASCADE, verbose_name='MaestroTipoContrato')
    maestrobancopagoplanillas = models.ForeignKey(erpp.gen.models.Maestrobancos, on_delete=models.CASCADE, verbose_name='MaestroBancoPagoPlanillas')
    funcionario = models.BooleanField(verbose_name='¿Funcionario?', default=False)
    afectoalsenati = models.BooleanField(verbose_name='¿Afecto Al SENATI?', default=False)
    ies = models.BooleanField(verbose_name='¿Impuesto Especial de Solidaridad?', default=False)
    maestrosituacion = models.ForeignKey(erpp.per.models.Maestrosituacion, on_delete=models.CASCADE, verbose_name='MaestroSituacion')
    fechainiciosituacion = models.DateField(label='Fecha Inicio De Situación')
    fechaterminosituacion = models.DateField(label='Fecha Termino De Situación')
    segurovidaessalud = models.BooleanField(verbose_name='¿Seguro De Vida ESSALUD?', default=False)
    sueldobasico = models.DecimalField(label='Sueldo Básico', max_digits=11, decimal_places=2)
    asignacionfamiliar = models.BooleanField(verbose_name='¿Asignación Familiar?', default=False)
    fechaingresoplanilla = models.DateField(label='Fecha Ingreso Planilla')
    fechainiciocontrato = models.DateField(label='Fecha Inicio Contrato')
    fechaterminocontrato = models.DateField(label='Fecha Termino Contrato')
    fechacese = models.DateField(label='Fecha Cese')
    movilidadporasistencia = models.DecimalField(label='Movilidad Por Asistencia', max_digits=11, decimal_places=2)
    numerocarnetessalud = models.CharField(label='Número Carnet ESSALUD', max_length=50)
    vidaley = models.BooleanField(verbose_name='¿Vida Ley?', default=False)
    segurocomplementario = models.BooleanField(verbose_name='¿Seguro Complementario?', default=False)
    numerorocarnetafp = models.CharField(label='Número Carnet AFP', max_length=50)
    fechaafiliacionafp = models.DateField(label='Fecha Afiliación AFP')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    cuentabancariapagoplanillas = models.CharField(label='Cuenta Bancaria Pago Planillas', max_length=50)
    cuentabancariadepositocts = models.CharField(label='Cuenta Bancaria Deposito CTS', max_length=50)
    dl25897porcentaje1023 = models.DecimalField(label='D.L. 25897 Porcentaje 1023', max_digits=18, decimal_places=2)
    dl25897porcentaje300 = models.DecimalField(label='D.L. 25897 Porcentaje 300', max_digits=18, decimal_places=2)
    dl26504porcentaje33 = models.DecimalField(label='D.L. 26504 Porcentaje 33', max_digits=18, decimal_places=2)
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    tiposervidor = models.ForeignKey(erpp.serv.models.Tipobienoservicio, on_delete=models.CASCADE, verbose_name='TipoServidor', blank=True, null=True)
    importe01 = models.DecimalField(label='Importe 01', max_digits=18, decimal_places=2, blank=True, null=True)
    importe02 = models.DecimalField(label='Importe 02', max_digits=18, decimal_places=2, blank=True, null=True)
    importe03 = models.DecimalField(label='Importe 03', max_digits=18, decimal_places=2, blank=True, null=True)
    importe04 = models.DecimalField(label='Importe 04', max_digits=18, decimal_places=2, blank=True, null=True)
    importe05 = models.DecimalField(label='Importe 05', max_digits=18, decimal_places=2, blank=True, null=True)
    importe06 = models.DecimalField(label='Importe 06', max_digits=18, decimal_places=2, blank=True, null=True)
    importe07 = models.DecimalField(label='Importe 07', max_digits=18, decimal_places=2, blank=True, null=True)
    importe08 = models.DecimalField(label='Importe 08', max_digits=18, decimal_places=2, blank=True, null=True)
    comisionmixta = models.BooleanField(verbose_name='¿Comisión Mixta?', blank=True, null=True)
    essindicalizado = models.BooleanField(verbose_name='¿Es Sindicalizado?', blank=True, null=True)
    montoasignacionfamiliar = models.DecimalField(label='Monto Asignación Familiar', max_digits=18, decimal_places=2, blank=True, null=True)
    importetotaldeudacc = models.DecimalField(label='Importe Total Deuda Cuenta Corriente', max_digits=18, decimal_places=2, blank=True, null=True)
    importetotalremper = models.DecimalField(label='Importe Total Remisión Personal', max_digits=18, decimal_places=2, blank=True, null=True)
    importeretencion5 = models.DecimalField(label='Importe Retención 5', max_digits=18, decimal_places=2, blank=True, null=True)
    redondeoant = models.DecimalField(label='Redondeo Anterior', max_digits=18, decimal_places=2, blank=True, null=True)
    redondeoactual = models.DecimalField(label='Redondeo Actual', max_digits=18, decimal_places=2, blank=True, null=True)
    jornaldiario = models.DecimalField(label='Jornal Diario', max_digits=18, decimal_places=2, blank=True, null=True)
    maestrobancocts = models.ForeignKey(erpp.gen.models.Maestrobancos, on_delete=models.CASCADE, verbose_name='MaestroBancoCts', blank=True, null=True)
    quintaactiva = models.BooleanField(verbose_name='¿Quinta Activa?', blank=True, null=True)
    empresaquinta = models.IntegerField(verbose_name='Empresa Quinta', blank=True, null=True)
    beneficiostrabajador = models.BooleanField(verbose_name='¿Beneficios Del Trabajador?', blank=True, null=True)
    calculoempresaextra = models.BooleanField(verbose_name='¿Cálculo De Empresa Extra?', blank=True, null=True)

    class Meta:
        db_table = 'datosplanilla'


class Feriados(models.Model):
    idferiado = models.AutoField(label='IDFeriado', primary_key=True)
    descripcion = models.CharField(label='Descripción', max_length=200)
    fechainicio = models.DateField(label='Fecha De Inicio')
    fechafin = models.DateField(label='Fecha De Finalización')
    usuario = models.CharField(label='Usuario', max_length=36)
    autorizado = models.CharField(label='Autorizado', max_length=50)
    activo = models.BooleanField()
    maestrotipocambio = models.ForeignKey(erpp.gen.models.Maestrotipodecambio, on_delete=models.CASCADE, verbose_name='Maestrotipocambio', blank=True, null=True)

    class Meta:
        db_table = 'feriados'


class Maestroaccidentetrabajo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoaccidentetrabajo = models.CharField(label='Código Accidente De Trabajo', max_length=20)
    clasetabla = models.CharField(label='Clase Tabla', max_length=5)
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroaccidentetrabajo'


class Maestroafp(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoafp = models.CharField(label='Codigo AFP', max_length=20)
    ubigeo = models.ForeignKey(erpp.gen.models.Maestroubigeo, on_delete=models.CASCADE, verbose_name='Ubigeo')
    razonsocial = models.CharField(label='Razón Social', max_length=75)
    direccion = models.CharField(label='Dirección', max_length=500)
    telefono = models.CharField(label='Teléfono', max_length=25)
    aportesolidaridadsoles = models.DecimalField(label='Aporte De Solidaridad En Soles', max_digits=11, decimal_places=2)
    aportefondopensionsoles = models.DecimalField(label='Aporte De Fondo De Pensión En Soles', max_digits=11, decimal_places=2)
    comisionfijasoles = models.DecimalField(label='Comisión Fija En Soles', max_digits=11, decimal_places=2)
    comisionporcentual = models.DecimalField(label='Comisión Porcentual', max_digits=5, decimal_places=2)
    seguroinvalidezsoles = models.DecimalField(label='Seguro Invalidez Soles', max_digits=11, decimal_places=2)
    cuentacontabledebe = models.IntegerField(verbose_name='Cuenta Contable Debe')
    cuentacontablehaber = models.IntegerField(verbose_name='Cuenta Contable Haber')
    anexocontable = models.IntegerField(verbose_name='Anexo Contable')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    comisionvariable = models.DecimalField(label='Comisión Variable', max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'maestroafp'
        unique_together = (('idmaestroempresa', 'razonsocial'),)


class Maestroapoderado(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestropersonal = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    nombrescompletos = models.CharField(label='Nombres Completos', max_length=200)
    dni = models.CharField(label='DNI', max_length=20)
    ruc = models.CharField(label='RUC', max_length=20)
    otros = models.CharField(label='Otros', max_length=20, blank=True, null=True)
    numeropartida = models.CharField(label='Número De Partida', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroapoderado'


class Maestrobeneficiario(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestrobancos = models.ForeignKey(erpp.gen.models.Maestrobancos, on_delete=models.CASCADE, verbose_name='MaestroBancos')
    maestropersonal = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    cuentabancariadepositoretencion = models.CharField(label='Cuenta Bancaria De Deposito/Retencion', max_length=50)
    apellidosnombres = models.CharField(label='Apellidos y Nombres', max_length=500)
    dni = models.CharField(label='DNI', max_length=8)
    sustentoretencion = models.CharField(label='Sustento De La Retención', max_length=70)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrobeneficiario'


class Maestrocargoocupacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigocargoocupacion = models.CharField(label='Código Cargo/Ocupacion', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=100)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrocargoocupacion'


class Maestrocentroasistencial(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigocentroasistencial = models.CharField(label='Código Centro Asistencial', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrocentroasistencial'


class Maestroconceptospdt(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoconceptospdt = models.CharField(label='Código Conceptos PDT', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=150)
    conceptospdtplanilla = models.ForeignKey(erpp.per.models.Personalconceptospdtplanilla, on_delete=models.CASCADE, verbose_name='ConceptosPDTPlanilla', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    sistemaprivadopensiones = models.BooleanField(verbose_name='¿Sistema Privado De Pensiones?', blank=True, null=True)
    sistemanacionalpensiones = models.BooleanField(verbose_name='¿Sistema Nacional De Pensiones?', blank=True, null=True)
    vacaciones118 = models.BooleanField(verbose_name='¿Vacaciones 118?', blank=True, null=True)
    gratificacion406 = models.BooleanField(verbose_name='¿Gratificación 406?', blank=True, null=True)

    class Meta:
        db_table = 'maestroconceptospdt'


class Maestroderechohabientes(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestropersonal = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    maestrovinculofamiliar = models.ForeignKey(erpp.per.models.Maestrovinculofamiliar, on_delete=models.CASCADE, verbose_name='MaestroVinculoFamiliar')
    maestrosituacion = models.ForeignKey(erpp.per.models.Maestrosituacion, on_delete=models.CASCADE, verbose_name='MaestroSituacion')
    maestrodomicilio = models.ForeignKey(erpp.per.models.Maestrodomicilio, on_delete=models.CASCADE, verbose_name='MaestroDomicilio')
    apellidopaterno = models.CharField(label='Apellido Paterno', max_length=75)
    apellidomaterno = models.CharField(label='Apellido Materno', max_length=75)
    nombres = models.CharField(label='Nombres', max_length=75)
    fechanacimiento = models.DateTimeField(label='Fecha De Nacimiento')
    sexo = models.CharField(label='Sexo', max_length=10)
    maestrodocumentoidentidad = models.IntegerField(verbose_name='IDMaestroDocumentoIdentidad')
    numerodocumentoidentidad = models.CharField(label='Número De Documento De Identidad', max_length=20)
    fechaalta = models.DateTimeField(label='Fecha De Alta')
    maestrodocumentoacreditapaternidad = models.ForeignKey(erpp.per.models.Maestrodocumentoacreditapaternidad, on_delete=models.CASCADE, verbose_name='MaestroDocumentoAcreditaPaternidad')
    numerodocumentoacreditapaternidad = models.CharField(label='Número De Documento Que Acredita Paternidad', max_length=30)
    maestrotipobaja = models.ForeignKey(erpp.conta.models.Maestrotipobaja, on_delete=models.CASCADE, verbose_name='MaestroTipoBaja')
    fechabaja = models.DateTimeField(label='Fecha De Baja')
    resolucionincapacidadhijomayor = models.CharField(label='ResoluciÓn De Incapacidad Hijo Mayor', max_length=20)
    domiciliodetalle = models.ForeignKey(erpp.fac.models.Domiciliodetalle, on_delete=models.CASCADE, verbose_name='DomicilioDetalle')
    direcciondomicilio = models.CharField(label='Dirección/Domicilio', max_length=200)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroderechohabientes'


class Maestrodocumentoacreditapaternidad(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcion = models.CharField(label='Descripción', max_length=100)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrodocumentoacreditapaternidad'


class Maestrodocumentoidentidad(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigodocumentoidentidad = models.CharField(label='Código Del Documento De Identidad', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=50)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    codigoafp = models.CharField(label='Código AFP', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'maestrodocumentoidentidad'


class Maestrodomicilio(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigodomicilio = models.CharField(label='Código Del Domicilio', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrodomicilio'


class Maestroenfermedad(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcion = models.CharField(label='Descripción', max_length=15)
    trabajadorfamiliar = models.CharField(label='Trabajador Familiar', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroenfermedad'


class Maestrogradoinstruccion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigogradoinstruccion = models.CharField(label='Codigo De Grado De Instrucción', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=70)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrogradoinstruccion'


class Maestronivelcategoria(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigonivelcategoria = models.CharField(label='Código Del Nivel De Categoria', max_length=20)
    clasetabla = models.CharField(label='Clase Tabla', max_length=5)
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestronivelcategoria'


class Maestropensiones(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigopensiones = models.CharField(label='Código Pensiones', max_length=20)
    clasetabla = models.CharField(label='Clase Tabla', max_length=5)
    descripcion = models.CharField(label='Descripción', max_length=70)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestropensiones'


class Maestroperiodicidadremuneracion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoperiodicidadremuneracion = models.CharField(label='Código De Periodicidad De Remuneración', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroperiodicidadremuneracion'


class Maestropersonal(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoservidor = models.CharField(label='Código Del Servidor', max_length=20)
    distribucioncentrodecostos = models.ForeignKey(erpp.conta.models.Distribucioncentrocostocabecera, on_delete=models.CASCADE, verbose_name='DistribucionCentroDeCostos')
    domiciliodetalle = models.ForeignKey(erpp.per.models.Maestrodomicilio, on_delete=models.CASCADE, verbose_name='DomicilioDetalle')
    maestrocentroasistencialessalud = models.ForeignKey(Maestrocentroasistencial, on_delete=models.CASCADE, verbose_name='MaestroCentroAsistencialESSALUD')
    maestroestadocivil = models.ForeignKey(erpp.gen.models.Maestroestadocivil, on_delete=models.CASCADE, verbose_name='MaestroEstadoCivil')
    maestrotiposangre = models.ForeignKey(erpp.gen.models.Maestrotiposangre, on_delete=models.CASCADE, verbose_name='MaestroTipoSangre')
    apellidopaterno = models.CharField(label='Apellido Paterno', max_length=75)
    apellidomaterno = models.CharField(label='Apellido Materno', max_length=75)
    nombres = models.CharField(label='Nombres', max_length=75)
    direccion = models.CharField(label='Dirección', max_length=500)
    telefono = models.CharField(label='Teléfono', max_length=25)
    fechanacimiento = models.DateTimeField(label='Fecha De Nacimiento')
    maestronacionalidad = models.ForeignKey(erpp.gen.models.Maestronacionalidad, on_delete=models.CASCADE, verbose_name='MaestroNacionalidad')
    nacionalidad = models.CharField(label='Nacionalidad', max_length=75)
    maestropaisemisordocumento = models.ForeignKey(erpp.gen.models.Maestropaisemisordocumento, on_delete=models.CASCADE, verbose_name='MaestroPaisEmisorDocumento')
    ubigeonacimiento = models.ForeignKey(erpp.gen.models.Maestroubigeo, on_delete=models.CASCADE, verbose_name='UbigeoNacimiento')
    maestrogradoinstrucciom = models.ForeignKey(Maestrogradoinstruccion, on_delete=models.CASCADE, verbose_name='MaestroGradoInstrucciom')
    lugarnacimiento = models.CharField(label='Lugar Nacimiento', max_length=50)
    sexo = models.CharField(label='Sexo', max_length=10)
    prod91adm94ven95 = models.IntegerField(verbose_name='Prod91Adm94Ven95')
    profesion = models.CharField(label='Profesión', max_length=75)
    documentoidentidad = models.ForeignKey(Maestrodocumentoidentidad, on_delete=models.CASCADE, verbose_name='DocumentoIdentidad')
    numerodocumentoidentidad = models.CharField(label='Número Del Documento De Identidad', max_length=15)
    maestrotipomovimiento = models.ForeignKey(erpp.per.models.Maestrotipomovimiento, on_delete=models.CASCADE, verbose_name='MaestroTipoMovimiento')
    fechatipomovimiento = models.DateTimeField(label='Fecha Tipo De Movimiento')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroperiodicidadremuneracion = models.ForeignKey(Maestroperiodicidadremuneracion, on_delete=models.CASCADE, verbose_name='MaestroPeriodicidadRemuneracion')
    maestrotipopagoremuneracion = models.ForeignKey(erpp.per.models.Maestrotipopagoremuneracion, on_delete=models.CASCADE, verbose_name='MaestroTipoPagoRemuneracion')
    codigocentrocosto = models.CharField(label='Código Del Centro De Costo', max_length=20, blank=True, null=True)
    codigotiposervidor = models.CharField(label='Codigo Del Tipo De Servidor', max_length=50, blank=True, null=True)
    correoelectronico = models.CharField(label='Correo Electrónico', max_length=50, blank=True, null=True)
    fiscalizacion = models.BooleanField(verbose_name='¿Fiscalización?', blank=True, null=True)
    firma = models.CharField(label='Firma', max_length=50, blank=True, null=True)
    detalleextra = models.CharField(label='Detalle Extra', max_length=50, blank=True, null=True)
    obervacion = models.CharField(label='Obervación', max_length=200, blank=True, null=True)
    turnonoche = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'maestropersonal'


class Maestroregimenlaboral(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoregimenlaboral = models.CharField(label='Código Del Regimen Laboral', max_length=20)
    clasetabla = models.CharField(label='Clase Tabla', max_length=5)
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroregimenlaboral'


class Maestroretencion(models.Model):
    id = models.AutoField(label='Id', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    seriedocretencion = models.CharField(label='Serie Del Documento De Retención', max_length=50)
    numerodocretencion = models.CharField(label='Número Del Documento De Retención', max_length=50)
    proveedor = models.ForeignKey(erpp.gen.models.Maestroproveedores, on_delete=models.CASCADE, verbose_name='Proveedor')
    estacontabilizada = models.BooleanField(verbose_name='¿Esta Contabilizada?', default=False)
    estapagada = models.BooleanField(verbose_name='¿Está Pagada?', default=False)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    fechaimpresion = models.DateTimeField(label='Fecha De La Impresión', blank=True, null=True)
    fechaimpresionretencion = models.DateTimeField(label='Fecha De La Impresión De Retención', blank=True, null=True)

    class Meta:
        db_table = 'maestroretencion'


class Maestrosalud(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigosalud = models.CharField(label='Código De Salud', max_length=20)
    clasetabla = models.CharField(label='Clase Tabla', max_length=4)
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrosalud'


class Maestrosituacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigosituacion = models.CharField(label='Código De La Situación', max_length=20)
    clasetabla = models.CharField(label='Clase Tabla', max_length=4)
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrosituacion'


class Maestrotipomovimiento(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigotipomovimiento = models.CharField(label='Código Tipo De Movimiento', max_length=20)
    empresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='Empresa')
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipomovimiento'


class Maestrotipopagoremuneracion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigotipopagoremuneracion = models.CharField(label='Codigo Tipo De Pago Con Remuneración', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipopagoremuneracion'


class Maestrotipoparentesco(models.Model):
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
        db_table = 'maestrotipoparentesco'


class Maestrotipopersonal(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigotipopersonal = models.CharField(label='Código Tipo De Personal', max_length=20)
    clasetabla = models.CharField(label='Clase Tabla', max_length=5)
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipopersonal'


class Maestrotipoplanilla(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigoplanilla = models.CharField(label='Código De La Planilla', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=75)
    tipoplanillaabreviado = models.CharField(label='Tipo De Planilla Abreviada', max_length=1)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipoplanilla'


class Maestrotipoprestamo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigotipoprestamo = models.CharField(label='Codigo De Tipo De Prestamo', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotipoprestamo'


class Maestrotiposervidor(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigotiposervidor = models.CharField(label='Código Del Tipo De Servidor', max_length=20)
    clasetabla = models.CharField(label='Clase Tabla', max_length=5)
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotiposervidor'


class Maestrotiposubsidio(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    codigotiposusidiosunat = models.CharField(label='Código Tipo Subsidio SUNAT', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'maestrotiposubsidio'


class Maestrovariablesentornopersonal(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigovariableentorno = models.CharField(label='Código De La Variable De Entorno', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=75)
    valor1 = models.DecimalField(label='Valor 1', max_digits=11, decimal_places=2)
    valor2 = models.DecimalField(label='Valor 2', max_digits=11, decimal_places=2)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrovariablesentornopersonal'


class Maestrovinculofamiliar(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    codigovinculofamiliar = models.CharField(label='Código Del Vinculo Familiar', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrovinculofamiliar'


class Personaladelantoquincena(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestropersonal = models.ForeignKey(Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    montoadelanto = models.DecimalField(label='Monto De Adelanto', max_digits=11, decimal_places=2)
    vacaciones = models.BooleanField(verbose_name='¿Vacaciones?', default=False)
    personaldatosvariablesplanilla = models.ForeignKey(erpp.per.models.Personaldatosvariablesplanilla, on_delete=models.CASCADE, verbose_name='PersonalDatosVariablesPlanilla')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroplanilla = models.ForeignKey(erpp.fac.models.Maestroplanilla, on_delete=models.CASCADE, verbose_name='MaestroPlanilla')

    class Meta:
        db_table = 'personaladelantoquincena'


class Personaladicionalesgeneraciondeboletas(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    generaciondeboletas = models.ForeignKey(erpp.per.models.Personalgeneraciondeboletas, on_delete=models.CASCADE, verbose_name='GeneracionDeBoletas')
    rangoinferior = models.IntegerField(verbose_name='Rango Inferior')
    rangosuperior = models.IntegerField(verbose_name='Rango Superior')
    numeroinicialdeboleta = models.IntegerField(verbose_name='Número Inicial De Boleta')
    fechapago = models.DateTimeField(label='Fecha De Pago')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personaladicionalesgeneraciondeboletas'


class Personalcalculocts(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa', blank=True, null=True)
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal', blank=True, null=True)
    fechapagocts = models.DateField(label='Fecha De Pago De Cuentas', blank=True, null=True)
    tipodecambio = models.DecimalField(label='Tipo De Cambio', max_digits=12, decimal_places=4, blank=True, null=True)
    fechainicio = models.DateTimeField(label='Fecha De Inicio', blank=True, null=True)
    fechafin = models.DateTimeField(label='Fecha De Fin', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=20, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=80, blank=True, null=True)
    estado = models.IntegerField(verbose_name='Estado', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36, blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    tiposervidor = models.ForeignKey(erpp.per.models.Maestrotiposervidor, on_delete=models.CASCADE, verbose_name='TipoServidor', blank=True, null=True)
    anhio = models.IntegerField(verbose_name='Año', blank=True, null=True)
    mes = models.IntegerField(verbose_name='Mes', blank=True, null=True)
    semestre = models.IntegerField(verbose_name='Semestre', blank=True, null=True)

    class Meta:
        db_table = 'personalcalculocts'


class Personalcalculoctsdetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalcalculocts = models.ForeignKey(erpp.per.models.Personalcalculocts, on_delete=models.CASCADE, verbose_name='PersonalCalculoCts', blank=True, null=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa', blank=True, null=True)
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal', blank=True, null=True)
    maestropersonal = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal', blank=True, null=True)
    cantidadanhio = models.IntegerField(verbose_name='Cantidad De Años', blank=True, null=True)
    cantidadmes = models.IntegerField(verbose_name='Cantidad De Meses', blank=True, null=True)
    cantidaddia = models.IntegerField(verbose_name='Cantidad De Días', blank=True, null=True)
    promediocomision = models.DecimalField(label='Promedio De Comisión', max_digits=11, decimal_places=2, blank=True, null=True)
    promediohoraextra = models.DecimalField(label='Promedio De Horas Extra', max_digits=11, decimal_places=2, blank=True, null=True)
    totalcomputable = models.DecimalField(label='Total Computable', max_digits=11, decimal_places=2, blank=True, null=True)
    promediocomputable = models.DecimalField(label='Promedio Computable', max_digits=11, decimal_places=2, blank=True, null=True)
    gratificacioncomputable = models.DecimalField(label='Gratificación Computable', max_digits=11, decimal_places=2, blank=True, null=True)
    totalremuneracioncomputable = models.DecimalField(label='Total De Remuneración Computable', max_digits=11, decimal_places=2, blank=True, null=True)
    cantidaddiaafectivonotrabajado = models.IntegerField(verbose_name='Cantidad De Días Afectivos No Trabajados', blank=True, null=True)
    importemes = models.DecimalField(label='Importe Del Mes', max_digits=11, decimal_places=2, blank=True, null=True)
    importedia = models.DecimalField(label='Importe Del Día', max_digits=11, decimal_places=2, blank=True, null=True)
    importetotalsoles = models.DecimalField(label='Importe Total En Soles', max_digits=11, decimal_places=2, blank=True, null=True)
    importetotaldolares = models.DecimalField(label='Importe Total En Dólares', max_digits=11, decimal_places=2, blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=20, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=80, blank=True, null=True)
    estado = models.IntegerField(verbose_name='Estado', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36, blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    importebasico = models.DecimalField(label='Importe Básico', max_digits=11, decimal_places=2, blank=True, null=True)
    importeotroconcepto = models.DecimalField(label='Importe Por Otro Concepto', max_digits=11, decimal_places=2, blank=True, null=True)
    correlativo = models.CharField(label='Correlativo', max_length=10, blank=True, null=True)
    pagado = models.BooleanField(verbose_name='¿Pagado?', blank=True, null=True)
    contabilizado = models.BooleanField(verbose_name='¿Contabilizado?', blank=True, null=True)
    simplec = models.BooleanField(verbose_name='¿Cuenta Simple?', blank=True, null=True)

    class Meta:
        db_table = 'personalcalculoctsdetalle'


class Personalcomposicionfamiliar(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(erpp.per.models.Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    nombresapellidos = models.CharField(label='Nombres y Apellidos', max_length=500)
    parentesco = models.CharField(label='Parentesco', max_length=20)
    fechanacimiento = models.DateTimeField(label='Fecha De Nacimiento')
    sexo = models.BooleanField(verbose_name='¿Sexo?', default=False)
    gradoinstruccion = models.CharField(label='Grado De Instrucción', max_length=15)
    ocupacion = models.CharField(label='Ocupación', max_length=20)
    dni = models.IntegerField(verbose_name='DNI')
    estadocivil = models.CharField(label='Estado Civil', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalcomposicionfamiliar'


class Personalconceptospdtplanilla(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigoconceptospdtplanilla = models.CharField(label='Código De Conceptos PDT Planilla', max_length=20)
    codigotipoconcepto = models.CharField(label='Código Del Tipo De Concepto', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=100, blank=True, null=True)
    imaestroconceptospdt = models.ForeignKey(Maestroconceptospdt, models.DO_NOTHING, label='IMaestroConceptosPDT')
    calculovariable = models.BooleanField(verbose_name='¿Cálculo De Variable?', default=False)
    escuentacorriente = models.BooleanField(verbose_name='¿Es Cuenta Corriente?', default=False)
    ctaactivopasivoempleadodebe = models.CharField(label='Cuenta Activa/Pasiva Del Empleado Debe', max_length=8)
    ctaactivopasivoempleadohaber = models.CharField(label='Cuenta Activa/Pasiva Del Empleado Haber', max_length=8)
    ctaactivopasivoobrerodebe = models.CharField(label='Cuenta Activa/Pasiva Del Obrero Debe', max_length=8)
    ctaactivopasivoobrerohaber = models.CharField(label='Cuenta Activa/Pasiva Del Obrero Haber', max_length=8)
    ctagastoproduccionempleadodebe = models.CharField(label='Cuenta Gasto/Producción Del Empleado Debe', max_length=8)
    ctagastoproduccionobrerodebe = models.CharField(label='Cuenta Gasto/Producción Del Obrero Debe', max_length=8)
    ctagastoproduccionhaber = models.CharField(label='Cuenta Gasto/Producción Haber', max_length=8)
    ctagastoadministracionempleadodebe = models.CharField(label='Cuenta Gasto/Administración Del Empleado Debe', max_length=8)
    ctagastoadministracionobrerodebe = models.CharField(label='Cuenta Gasto/Administración Del Obrero Debe', max_length=8)
    ctagastoadministracionhaber = models.CharField(label='Cuenta Gasto/Administración Haber', max_length=8)
    ctagastoventasempleadodebe = models.CharField(label='Cuenta Gasto/Ventas Del Empleado Debe', max_length=8)
    ctagastoventasobrerodebe = models.CharField(label='Cuenta Gasto/Ventas Del Obrero Debe', max_length=8)
    ctagastoventashaber = models.CharField(label='Cuenta Gasto/Ventas Haber', max_length=8)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    nposicion = models.IntegerField(verbose_name='N Posición', blank=True, null=True)
    descripcionconceptosunat = models.TextField(label='Descripción Por Concepto De Sunat', blank=True, null=True)

    class Meta:
        db_table = 'personalconceptospdtplanilla'


class Personalconceptospdtplanilla2(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigoconceptospdtplanilla = models.CharField(label='Código De Conceptos PDT Planilla', max_length=20)
    codigotipoconcepto = models.CharField(label='Código Del Tipo De Concepto', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=100, blank=True, null=True)
    imaestroconceptospdt = models.IntegerField(verbose_name='IMaestroConceptosPDT')
    calculovariable = models.BooleanField(verbose_name='Cálculo De Variable')
    escuentacorriente = models.BooleanField(verbose_name='¿Es Cuenta Corriente?', default=False)
    ctaactivopasivoempleadodebe = models.CharField(label='Cuenta Activo/Pasivo Del Empleado Debe', max_length=8)
    ctaactivopasivoempleadohaber = models.CharField(label='Cuenta Activo/Pasivo Del Empleado Haber', max_length=8)
    ctaactivopasivoobrerodebe = models.CharField(label='Cuenta Activo/Pasivo Del Obrero Debe', max_length=8)
    ctaactivopasivoobrerohaber = models.CharField(label='Cuenta Activo/Pasivo Del Obrero Haber', max_length=8)
    ctagastoproduccionempleadodebe = models.CharField(label='Cuenta Gasto/Producción Del Empleado Debe', max_length=8)
    ctagastoproduccionobrerodebe = models.CharField(label='Cuenta Gasto/Producción Del Obrero Debe', max_length=8)
    ctagastoproduccionhaber = models.CharField(label='Cuenta Gasto/Producción Haber', max_length=8)
    ctagastoadministracionempleadodebe = models.CharField(label='Cuenta Gasto/Administración Del Empleado Debe', max_length=8)
    ctagastoadministracionobrerodebe = models.CharField(label='Cuenta Gasto/Administración Del Obrero Debe', max_length=8)
    ctagastoadministracionhaber = models.CharField(label='Cuenta Gasto/Administración Haber', max_length=8)
    ctagastoventasempleadodebe = models.CharField(label='Cuenta Gasto/Ventas Del Empleado Debe', max_length=8)
    ctagastoventasobrerodebe = models.CharField(label='Cuenta Gasto/Ventas Del Obrero Debe', max_length=8)
    ctagastoventashaber = models.CharField(label='Cuenta Gasto/Ventas Haber', max_length=8)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    posicion = models.IntegerField(verbose_name='Posición', blank=True, null=True)

    class Meta:
        db_table = 'personalconceptospdtplanilla2'


class Personalconceptospdtplanilladetalle(models.Model):
    id = models.AutoField(label='Id', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrotipopersonal = models.ForeignKey(Maestrotipopersonal, on_delete=models.CASCADE, verbose_name='MaestroTipoPersonal')
    personalconceptospdtplanilla = models.ForeignKey(Personalconceptospdtplanilla, on_delete=models.CASCADE, verbose_name='PersonalConceptosPDTPlanilla')
    cuentadebe = models.CharField(label='Cuenta Debe', max_length=20, blank=True, null=True)
    cuentahaber = models.CharField(label='Cuenta Haber', max_length=20, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    cuenta90debe1 = models.CharField(label='Cuenta 90 Debe 1', max_length=50, blank=True, null=True)
    cuenta90debe2 = models.CharField(label='Cuenta 90 Debe 2', max_length=50, blank=True, null=True)
    cuenta90debe3 = models.CharField(label='Cuenta 90 Debe 3', max_length=50, blank=True, null=True)
    cuenta90haber1 = models.CharField(label='Cuenta 90 Haber 1', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'personalconceptospdtplanilladetalle'


class Personalcuentacorrientecabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestropersonal = models.ForeignKey(Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    maestrotipopersonal = models.ForeignKey(erpp.per.models.Maestrotipopersonal, on_delete=models.CASCADE, verbose_name='MaestroTipoPersonal')
    maestrotipoprestamo = models.ForeignKey(Maestrotipoprestamo, on_delete=models.CASCADE, verbose_name='MaestroTipoPrestamo')
    cantidaddecuotas = models.IntegerField(verbose_name='Cantidad De Cuotas')
    montoprestado = models.DecimalField(label='Monto Del Prestado', max_digits=11, decimal_places=2, blank=True, null=True)
    fechaprestamo = models.DateTimeField(label='Fecha Del Prestamo', blank=True, null=True)
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalcuentacorrientecabecera'


class Personalcuentacorrientedetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestropersonal = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    numerodecuota = models.IntegerField(verbose_name='Número De Cuota')
    montocuota = models.DecimalField(label='Monto De La Cuota', max_digits=11, decimal_places=2, blank=True, null=True)
    fechapago = models.DateTimeField(label='Fecha Del Pago', blank=True, null=True)
    saldoactual = models.DecimalField(label='Saldo Actual', max_digits=11, decimal_places=2, blank=True, null=True)
    descripcion = models.CharField(label='Descripción', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    personalcuentacorrientecabecera = models.ForeignKey(Personalcuentacorrientecabecera, on_delete=models.CASCADE, verbose_name='PersonalCuentaCorrienteCabecera')
    personaldatosvariablespalnilla = models.ForeignKey(erpp.per.models.Personaldatosvariablesplanilla, on_delete=models.CASCADE, verbose_name='PersonalDatosVariablesPalnilla')
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalcuentacorrientedetalle'


class Personalcurriculo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestropersonal = models.ForeignKey(Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    documentoescaneado = models.BinaryField(label='Documento Escaneado')
    fecharegistro = models.DateTimeField(label='Fecha De Registro')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalcurriculo'


class Personaldatosadicionales(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(erpp.per.models.Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    religion = models.CharField(label='Religión', max_length=50)
    idioma = models.CharField(label='Idioma', max_length=30)
    otrosidiomas = models.CharField(label='Otros Idiomas', max_length=75)
    fechacaducidaddni = models.DateTimeField(label='Fecha De Caducidad Del DNI')
    numeropasaporte = models.CharField(label='Número Del Pasaporte', max_length=20)
    numeromesavotacion = models.CharField(label='Número De Mesa De Votación', max_length=10)
    numerobrevete = models.CharField(label='Número Del Brevete', max_length=15)
    codigo_usuario = models.CharField(label='Código Del Usuario', max_length=36)
    fecha_creacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personaldatosadicionales'


class Personaldatosvariablesplanilla(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    personalplanilla = models.ForeignKey(erpp.per.models.Personalplanilla, on_delete=models.CASCADE, verbose_name='PersonalPlanilla')
    conceptospdtplanilla = models.ForeignKey(Personalconceptospdtplanilla, on_delete=models.CASCADE, verbose_name='ConceptosPDTPlanilla')
    montoconceptospdtplanilla = models.DecimalField(label='Monto De Conceptos PDT Planilla', max_digits=10, decimal_places=2)
    descripcion = models.CharField(label='Descripción', max_length=100)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personaldatosvariablesplanilla'


class Personaldespistajerealizado(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(erpp.per.models.Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    enfermedad = models.CharField(label='Enfermedad', max_length=50)
    trabajadorfamiliar = models.CharField(label='Trabajador Familiar', max_length=75)
    entidadsalud = models.CharField(label='Entidad Salud', max_length=50)
    fechadespistaje = models.DateTimeField(label='Fecha De Despistaje')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personaldespistajerealizado'


class Personaldistribucioncentrodecostos(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigodistribucioncentrodecostos = models.CharField(label='Codigo De Distribución Del Centro De Costos', max_length=20)
    clasetabla = models.CharField(label='Clase Tabla', max_length=5)
    descripcion = models.CharField(label='Descripción', max_length=30)
    totalimporte = models.DecimalField(label='Total Del Importe', max_digits=11, decimal_places=2)
    totalporcentaje = models.DecimalField(label='Total Del Porcentaje', max_digits=5, decimal_places=2)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personaldistribucioncentrodecostos'


class Personalegresofamiliar(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(erpp.per.models.Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    descripcion = models.CharField(label='Descripción', max_length=50)
    monto = models.DecimalField(label='Monto', max_digits=11, decimal_places=2)
    referencia = models.CharField(label='Referencia', max_length=50)
    codigo_usuario = models.CharField(label='Código De Usuario', max_length=36)
    fecha_creacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalegresofamiliar'


class Personalentidadcontingencia(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(erpp.per.models.Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    maestrotipoparentesco = models.ForeignKey(Maestrotipoparentesco, on_delete=models.CASCADE, verbose_name='MaestroTipoParentesco')
    nombreentidad = models.CharField(label='Nombre De La Entidad', max_length=75)
    codigo_usuario = models.CharField(label='Código De Usuario', max_length=36)
    fecha_creacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalentidadcontingencia'


class Personalestudioscomplementarios(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(erpp.per.models.Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    institucion = models.CharField(label='Institución', max_length=75)
    especialidad = models.CharField(label='Especialidad', max_length=50)
    grado = models.CharField(label='Grado', max_length=30)
    periodo = models.CharField(label='Periodo', max_length=10)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalestudioscomplementarios'


class Personalexperiencialaboral(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(erpp.per.models.Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    nombreempresa = models.CharField(label='Nombre De La Empresa', max_length=75)
    cargo = models.CharField(label='Cargo', max_length=30)
    motivocese = models.CharField(label='Motivo Del Cese', max_length=30)
    periodo = models.CharField(label='Periodo', max_length=10)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalexperiencialaboral'


class Personalfichacompartevivienda(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(erpp.per.models.Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    maestrotipoparentesco = models.ForeignKey(Maestrotipoparentesco, on_delete=models.CASCADE, verbose_name='MaestroTipoParentesco')
    especifiquecompartevivienda = models.CharField(label='Especificación De Vivienda Compartida', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalfichacompartevivienda'


class Personalfichapersonasacargo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestrotipoparentesco = models.ForeignKey(Maestrotipoparentesco, on_delete=models.CASCADE, verbose_name='MaestroTipoParentesco')
    personalfichasocioeconomica = models.ForeignKey(erpp.per.models.Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    especifiquepersonasacargo = models.CharField(label='Especificación De Personas A Cargo', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalfichapersonasacargo'


class Personalfichaproblematicafamiliar(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(erpp.per.models.Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    descripcion = models.CharField(label='Descripción', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalfichaproblematicafamiliar'


class Personalfichasocioeconomica(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    ubigeo = models.ForeignKey(erpp.gen.models.Maestroubigeo, on_delete=models.CASCADE, verbose_name='Ubigeo')
    maestropersonal = models.ForeignKey(Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    personalentidadcontingencia = models.ForeignKey(Personalentidadcontingencia, on_delete=models.CASCADE, verbose_name='PersonalEntidadContingencia')
    personalgradoacademico = models.ForeignKey(erpp.per.models.Personalgradoacademico, on_delete=models.CASCADE, verbose_name='PersonalGradoAcademico')
    personalpersonascasoemergencia1 = models.ForeignKey(erpp.per.models.Personalpersonascasoemergencia, models.DO_NOTHING, label='IDPersonalPersonasCasoEmergencia1')
    personalpersonascasoemergencia2 = models.ForeignKey(erpp.per.models.Personalpersonascasoemergencia, on_delete=models.CASCADE, verbose_name='PersonalPersonasCasoEmergencia2')
    participaciontomadecisiones = models.CharField(label='Participación De Toma De Decisiones', max_length=20)
    gradocomunicacion = models.CharField(label='Grado De Comunicación', max_length=20)
    gradoconfianza = models.CharField(label='Grado De Confianza', max_length=20)
    controlmedico = models.CharField(label='Control Médico', max_length=50)
    poseeelectricidad = models.BooleanField(verbose_name='Posee Electricidad')
    compartehorasdiarias = models.TimeField(label='Comparte Horas Diarias')
    compartehorassemanales = models.TimeField(label='Comparte Horas Semanales')
    compartemotivodiario = models.CharField(label='Comparte Motivo Diario', max_length=30)
    compartemotivosemanal = models.CharField(label='Comparte Motivo Semanal', max_length=30)
    afiliacion = models.CharField(label='Afiliación', max_length=5)
    afpcussp = models.CharField(label='AFP CUSSP', max_length=15)
    centroessalud = models.CharField(label='Centro ESSALUD', max_length=50)
    numeroautogenerado = models.CharField(label='Número Autogenerado', max_length=20)
    essaludvida = models.BooleanField(verbose_name='¿ESSALUD Vida?', default=False)
    seguroadicional = models.CharField(label='Seguro Adicional', max_length=50)
    desayunocasa = models.BooleanField(verbose_name='¿Desayuno En Casa?', default=False)
    almuerzocasa = models.BooleanField(verbose_name='¿Almuerzo En Casa?', default=False)
    cenacasa = models.BooleanField(verbose_name='¿Cena En Casa?', default=False)
    desayunofueracasa = models.BooleanField(verbose_name='¿Desayuno Fuera Casa?', default=False)
    almuerzofueracasa = models.BooleanField(verbose_name='¿Almuerzo Fuera Casa?', default=False)
    cenafueracasa = models.BooleanField(verbose_name='¿Cena Fuera Casa?', default=False)
    cantidaddormitorio = models.CharField(label='Cantidad De Dormitorios', max_length=5)
    cantidadfamilias = models.CharField(label='Cantidad De Familias', max_length=5)
    aseguradoconyuge = models.CharField(label='Asegurado Con Conyuge', max_length=20)
    aseguradohijos = models.CharField(label='Asegurado Con Hijos', max_length=20)
    tipofamilia = models.CharField(label='Tipo De Familia', max_length=30)
    tipovivienda = models.CharField(label='Tipo De Vivienda', max_length=30)
    tipozona = models.CharField(label='Tipo De Zona', max_length=30)
    tipoagua = models.CharField(label='Tipo De Agua', max_length=30)
    tiposshh = models.CharField(label='Tipo SSHH', max_length=30)
    maestromaterialconstruccionpiso = models.ForeignKey(erpp.gen.models.Maestromaterialconstruccion, on_delete=models.CASCADE, verbose_name='MaestroMaterialConstruccionPiso')
    maestromaterialconstruccionpared = models.ForeignKey(erpp.gen.models.Maestromaterialconstruccion, on_delete=models.CASCADE, verbose_name='MaestroMaterialConstruccionPared')
    maestromaterialconstrucciontecho = models.ForeignKey(erpp.gen.models.Maestromaterialconstruccion, on_delete=models.CASCADE, verbose_name=' MaestroMaterialConstruccionTecho')
    observacionlaboral = models.CharField(label='Observación Laboral', max_length=500)
    observacionfamiliar = models.CharField(label='Observación Familiar', max_length=500)
    observacioneconomica = models.CharField(label='Observación Económica', max_length=500)
    observacionvivienda = models.CharField(label='Observación Vivienda', max_length=500)
    observacionsalud = models.CharField(label='Observación De Salud', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalfichasocioeconomica'


class Personalgeneraciondeboletas(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroplanilla = models.ForeignKey(erpp.fac.models.Maestroplanilla, on_delete=models.CASCADE, verbose_name='MaestroPlanilla')
    tituloplanilla = models.CharField(label='Título De Planilla', max_length=100)
    subtituloplanilla = models.CharField(label='SubTítulo De Planilla', max_length=100)
    fechainicio = models.DateTimeField(label='Fecha De Inicio')
    fechatermino = models.DateTimeField(label='Fecha De Termino')
    comentariofinboleta = models.CharField(label='Comentario Fin De Boleta', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalgeneraciondeboletas'


class Personalgradoacademico(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    institucion = models.CharField(label='Institución', max_length=75)
    grado = models.CharField(label='Grado', max_length=20)
    periodo = models.CharField(label='Periodo', max_length=10)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalgradoacademico'


class Personalhogarambientecomun(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    descripcion = models.CharField(label='Descripción', max_length=15)
    cantidad = models.IntegerField(verbose_name='Cantidad')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalhogarambientecomun'


class Personalingresofamiliar(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    aportanteresponsable = models.CharField(label='Aportante Responsable', max_length=75)
    actividad = models.CharField(label='Actividad', max_length=50)
    monto = models.DecimalField(label='Monto', max_digits=11, decimal_places=2)
    codigo_usuario = models.CharField(label='Código De Usuario', max_length=36)
    fecha_creacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalingresofamiliar'


class Personalliquidacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    salariomensual = models.DecimalField(label='Salario Mensual', max_digits=11, decimal_places=2, blank=True, null=True)
    promediohoraextra = models.DecimalField(label='Promedio De Horas Extra', max_digits=11, decimal_places=2, blank=True, null=True)
    promediocomision = models.DecimalField(label='Promedio De Comisiones', max_digits=11, decimal_places=2, blank=True, null=True)
    asignacionfamiliar = models.DecimalField(label='Asignación Familiar', max_digits=11, decimal_places=2, blank=True, null=True)
    otrosafecto = models.DecimalField(label='Otros Afectos', max_digits=11, decimal_places=2, blank=True, null=True)
    totalremuneracion = models.DecimalField(label='Total De Remuneración', max_digits=11, decimal_places=2, blank=True, null=True)
    motivoretiro = models.CharField(label='Motivo De Retiro', max_length=100, blank=True, null=True)
    esafecto = models.BooleanField(verbose_name='¿Es Afecto?', blank=True, null=True)
    remuneracionasegurable = models.DecimalField(label='Remuneración Asegurable', max_digits=11, decimal_places=2, blank=True, null=True)
    cantidaddiaremuneracionasegurable = models.IntegerField(verbose_name='Cantidad De Días De Remuneración Asegurable', blank=True, null=True)
    totalremuneracionasegurable = models.DecimalField(label='Total De Remuneración Asegurable', max_digits=11, decimal_places=2, blank=True, null=True)
    gratificaciontrunca = models.DecimalField(label='Gratificación Trunca', max_digits=11, decimal_places=2, blank=True, null=True)
    gratificacionafectacts = models.DecimalField(label='Gratificación Afecta Cuentas', max_digits=11, decimal_places=2, blank=True, null=True)
    porcentajecompensacion = models.DecimalField(label='Porcentaje Compensación', max_digits=11, decimal_places=2, blank=True, null=True)
    porcentajeresulremuneracionasegurable = models.DecimalField(label='Porcentaje De Resultados De Remuneración Asegurable', max_digits=11, decimal_places=2, blank=True, null=True)
    porcentajeresulgratificacionafectacts = models.DecimalField(label='Porcentaje De Resultados De Gratificación Afecta Cuentas', max_digits=11, decimal_places=2, blank=True, null=True)
    porcentajeresulgratificaciontrunca = models.DecimalField(label='Porcentaje De Resultados De Gratificación Trunca', max_digits=11, decimal_places=2, blank=True, null=True)
    totalcompensacionportiemposervicio = models.DecimalField(label='Total De Compensación Por Tiempo De Servicio', max_digits=11, decimal_places=2, blank=True, null=True)
    cantidadmesgratificaciontrunca = models.DecimalField(label='Cantidad De Meses De Gratificación Trunca', max_digits=11, decimal_places=2, blank=True, null=True)
    cantidadanhiovacaciontrunca = models.DecimalField(label='Cantidad De Años De Vacación Trunca', max_digits=11, decimal_places=2, blank=True, null=True)
    cantidadmesvacaciontrunca = models.DecimalField(label='Cantidad De Meses De Vacación Trunca', max_digits=11, decimal_places=2, blank=True, null=True)
    cantidaddiavacaciontrunca = models.DecimalField(label='Cantidad De Días De Vacación Trunca', max_digits=11, decimal_places=2, blank=True, null=True)
    importemesgratificaciontrunca = models.DecimalField(label='Importe De Mes De Gratificación Trunca', max_digits=11, decimal_places=2, blank=True, null=True)
    importeanhiovacaciontrunca = models.DecimalField(label='Importe De Año De Vacación Trunca', max_digits=11, decimal_places=2, blank=True, null=True)
    importemesvacaciontrunca = models.DecimalField(label='Importe De Mes De Vacación Trunca', max_digits=11, decimal_places=2, blank=True, null=True)
    importediavacaciontrunca = models.DecimalField(label='Importe De Día De Vacación Trunca', max_digits=11, decimal_places=2, blank=True, null=True)
    bonificacionexttemporal = models.DecimalField(label='Bonificación Extensiva Temporal', max_digits=11, decimal_places=2, blank=True, null=True)
    subtotalsoles = models.DecimalField(label='Subtotal En Soles', max_digits=11, decimal_places=2, blank=True, null=True)
    descuentosnp = models.DecimalField(label='Descuento Por Snp', max_digits=11, decimal_places=2, blank=True, null=True)
    descuentofondopension = models.DecimalField(label='Descuento Por Fondo De Pension', max_digits=11, decimal_places=2, blank=True, null=True)
    descuentosobrevivencia = models.DecimalField(label='Descuento Por Sobrevivencia', max_digits=11, decimal_places=2, blank=True, null=True)
    descuentocomision = models.DecimalField(label='Descuento De Comisión', max_digits=11, decimal_places=2, blank=True, null=True)
    totaldescuentoley = models.DecimalField(label='Total De Descuento Por Ley', max_digits=11, decimal_places=2, blank=True, null=True)
    importequintacategoria = models.DecimalField(label='Importe De Quinta Categoría', max_digits=11, decimal_places=2, blank=True, null=True)
    importecuentacorriente = models.DecimalField(label='Importe De Cuenta Corriente', max_digits=11, decimal_places=2, blank=True, null=True)
    otrosinafecto = models.DecimalField(label='Otros Inafecto', max_digits=11, decimal_places=2, blank=True, null=True)
    totalpago = models.DecimalField(label='Total De Pago', max_digits=11, decimal_places=2, blank=True, null=True)
    maestropersonal = models.ForeignKey(Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal', blank=True, null=True)
    mesesreciboshonorarios = models.IntegerField(verbose_name='Meses De Recibos Por Honorarios', blank=True, null=True)
    remuneracionreciboshonorarios = models.IntegerField(verbose_name='Remuneración De Recibos Por Honorarios', blank=True, null=True)
    promedioreciboshonorarios = models.IntegerField(verbose_name='Promedio De Recibos Por Honorarios', blank=True, null=True)
    faltas = models.IntegerField(verbose_name='Faltas', blank=True, null=True)

    class Meta:
        db_table = 'personalliquidacion'


class Personalmantenimientotablas(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigotabla = models.CharField(label='Código De La Tabla', max_length=20)
    descripciontabla = models.CharField(label='Descripción De La Tabla', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalmantenimientotablas'


class Personalpadeceenfermedad(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    enfermedad = models.CharField(label='Enfermedad', max_length=50)
    trabajadorfamiliar = models.CharField(label='Trabajador Familiar', max_length=75)
    codigo_usuario = models.CharField(label='Código De Usuario', max_length=36)
    fecha_creacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalpadeceenfermedad'


class Personalperiodovacaciones(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    periodovacaciones = models.CharField(label='Periodo De Vacaciones', max_length=8)
    maestropersonal = models.ForeignKey(Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    fechasalida = models.DateTimeField(label='Fecha De Salida')
    fecharetorno = models.DateTimeField(label='Fecha De Retorno')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    periodovacacioneshasta = models.CharField(label='Periodo De Vacaciones Hasta', max_length=50, blank=True, null=True)
    reduccion = models.BooleanField(verbose_name='¿Reducción?', blank=True, null=True)

    class Meta:
        db_table = 'personalperiodovacaciones'


class Personalpersonascasoemergencia(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    apellidopaterno = models.CharField(label='Apellido Paterno', max_length=20)
    apellidomaterno = models.CharField(label='Apellido Materno', max_length=20)
    nombres = models.CharField(label='Nombres', max_length=30)
    direccion = models.CharField(label='Dirección', max_length=500)
    distrito = models.CharField(label='Distrito', max_length=20)
    referenciavivienda = models.CharField(label='Referencia De Vivienda', max_length=30)
    parentesco = models.CharField(label='Parentesco', max_length=15)
    fijocelular = models.CharField(label='Celular Fijo', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalpersonascasoemergencia'


class Personalplanilla(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestropersonal = models.ForeignKey(Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    maestroplanilla = models.ForeignKey(erpp.fac.models.Maestroplanilla, on_delete=models.CASCADE, verbose_name='MaestroPlanilla')
    numeroboleta = models.CharField(label='Número De Boleta', max_length=20)
    codigoservidor = models.CharField(label='Código Del Servidor', max_length=20)
    numerocarnetessalud = models.CharField(label='Número De Carnet ESSALUD', max_length=50)
    numerorocarnetafp = models.CharField(label='Número De Carnet AFP', max_length=50)
    maestroafp = models.ForeignKey(Maestroafp, on_delete=models.CASCADE, verbose_name='MaestroAFP')
    numerodocumentoidentidad = models.CharField(label='Número De Documento De Identidad', max_length=10)
    nombrepaisemisor = models.CharField(label='Nombre Del País Emisor', max_length=75)
    fechaingresoplanilla = models.DateField(label='Fecha De Ingreso Planilla')
    sueldobasico = models.DecimalField(label='Sueldo Básico', max_digits=11, decimal_places=2)
    segurovidaessalud = models.BooleanField(verbose_name='¿Seguro De Vida ESSALUD?', default=False)
    asignacionfamiliar = models.BooleanField(verbose_name='¿Asignación Familiar?', default=False)
    afectoalsenati = models.BooleanField(verbose_name='¿Afecto Al SENATI?', default=False)
    movilidadporasistencia = models.DecimalField(label='Movilidad Por Asistencia', max_digits=11, decimal_places=2)
    maestrovariablesentornopersonal = models.ForeignKey(Maestrovariablesentornopersonal, on_delete=models.CASCADE, verbose_name='MAestroVariablesEntornoPersonal')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'personalplanilla'


class Personalplantillaadelantoquincena(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestropersonal = models.ForeignKey(Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    montoadelanto = models.DecimalField(label='Monto De Adelanto', max_digits=10, decimal_places=2)
    porcentajeadelanto = models.DecimalField(label='Porcentaje De Adelanto', max_digits=5, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(label='Descuento', max_digits=10, decimal_places=2, blank=True, null=True)
    flagvacaciones = models.BooleanField(verbose_name='¿Flag De Vacaciones?', default=False)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'personalplantillaadelantoquincena'


class Personalposeebienes(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    descripcion = models.CharField(label='Descripción', max_length=50)
    codigo_usuario = models.CharField(label='Código De Usuario', max_length=36)
    fecha_creacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    personalfichasocioeconomica = models.ForeignKey(Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalposeebienes'


class Personalquintaacumulado(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    maestropersonal = models.ForeignKey(Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    fecha = models.DateTimeField(label='Fecha')
    descripcion = models.CharField(label='Descripción', max_length=200, blank=True, null=True)
    montorentaquinta = models.DecimalField(label='Monto De Renta Quinta', max_digits=18, decimal_places=2)
    montosueldo = models.DecimalField(label='Monto Del Sueldo', max_digits=18, decimal_places=2)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'personalquintaacumulado'


class Personalreferencialaboral(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    personalfichasocioeconomica = models.ForeignKey(Personalfichasocioeconomica, on_delete=models.CASCADE, verbose_name='PersonalFichaSocioEconomica')
    nombresapellidos = models.CharField(label='Nombres y Apellidos', max_length=500)
    cargo = models.CharField(label='Cargo', max_length=30)
    fijocelular = models.CharField(label='Celular Fijo', max_length=20)
    relacion = models.CharField(label='Relación', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalreferencialaboral'


class Personalregistroasistencia(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestropersonal = models.ForeignKey(Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    maestroplanilla = models.ForeignKey(erpp.fac.models.Maestroplanilla, on_delete=models.CASCADE, verbose_name='MaestroPlanilla')
    maestroseccion = models.ForeignKey(erpp.gen.models.Maestroseccion, on_delete=models.CASCADE, verbose_name='MaestroSeccion')
    maestrocentrodecostos = models.ForeignKey(erpp.gen.models.Maestrocentrosdecostos, on_delete=models.CASCADE, verbose_name='MaestroCentroDeCostos')
    maestroafp = models.ForeignKey(Maestroafp, on_delete=models.CASCADE, verbose_name='MaestroAFP')
    dias = models.DecimalField(label='Días', max_digits=12, decimal_places=4)
    dominical = models.IntegerField(verbose_name='Dominical')
    promediohorasextra1 = models.DecimalField(label='Promedio De Horas Extra 1', max_digits=12, decimal_places=4)
    promediohorasextra2 = models.DecimalField(label='Promedio De Horas Extra 2', max_digits=12, decimal_places=4)
    promediohorasextra3 = models.DecimalField(label='Promedio De Horas Extra 3', max_digits=12, decimal_places=4)
    sobretasa = models.DecimalField(label='Sobre Tasa', max_digits=12, decimal_places=4)
    minutospermiso = models.IntegerField(verbose_name='Minutos De Permiso')
    minutostardanza = models.IntegerField(verbose_name='Minutos De Tardanza')
    horassuspencion = models.IntegerField(verbose_name='Horas De Suspención')
    horasinasistencia = models.IntegerField(verbose_name='Horas De Inasistencia')
    personaldatosvariablesplanilla = models.ForeignKey(Personaldatosvariablesplanilla, on_delete=models.CASCADE, verbose_name='PersonalDatosVariablesPlanilla')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    horasnocturnas0507 = models.DecimalField(label='Horas Nocturnas 0507', max_digits=12, decimal_places=4, blank=True, null=True)
    horasnocturnas1921 = models.DecimalField(label='Horas Nocturnas 1921', max_digits=12, decimal_places=4, blank=True, null=True)
    horasnocturnas2105 = models.DecimalField(label='Horas Nocturnas 2105', max_digits=12, decimal_places=4, blank=True, null=True)
    horastrabajadas = models.DecimalField(label='Horas Trabajadas', max_digits=12, decimal_places=4, blank=True, null=True)
    descuentotardanzassoles = models.DecimalField(label='Descuento Por Tardanzas En Soles', max_digits=12, decimal_places=4, blank=True, null=True)
    horasferiados = models.DecimalField(label='Horas Feriados', max_digits=12, decimal_places=4, blank=True, null=True)
    numeroviajes = models.IntegerField(verbose_name='Número De Viajes', blank=True, null=True)

    class Meta:
        db_table = 'personalregistroasistencia'


class Personalretencionesjudiciales(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestropersonal = models.ForeignKey(Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    maestrobeneficiario = models.ForeignKey(Maestrobeneficiario, on_delete=models.CASCADE, verbose_name='MaestroBeneficiario')
    porcentaje = models.BooleanField(verbose_name='¿Porcentaje?', default=False)
    porcentajeimporte = models.DecimalField(label='Porcentaje De Importe', max_digits=5, decimal_places=2)
    descuentosobrebrutoneto = models.CharField(label='Descuento Sobre Bruto Neto', max_length=10)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalretencionesjudiciales'


class Personalsubsidio(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    datospalnilla = models.ForeignKey(Datosplanilla, on_delete=models.CASCADE, verbose_name='DatosPalnilla')
    maestrotiposubsidio = models.ForeignKey(Maestrotiposubsidio, on_delete=models.CASCADE, verbose_name='MaestroTipoSubsidio')
    numerocitt = models.CharField(label='Número CITT', max_length=25)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')
    fechainicio = models.DateTimeField(label='Fecha De Inicio')
    fechafin = models.DateTimeField(label='Fecha De Finalización')

    class Meta:
        db_table = 'personalsubsidio'


class Personalturnopersonalcabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestropersonal = models.ForeignKey(Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal')
    turnofijo = models.BooleanField(verbose_name='TurnoFijo')
    codigomarcadoprincipal = models.CharField(label='Código De Marcado Principal', max_length=20)
    maestrohorarioturnopersonal = models.ForeignKey(erpp.fac.models.Maestrohorarioturnopersonal, on_delete=models.CASCADE, verbose_name='MaestroHorarioTurnoPersonal')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='MaestroEmpresa')
    maestrosucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'personalturnopersonalcabecera'
