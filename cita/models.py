from django.db import models


import erpp.fac.models
import erpp.gen.models
import erpp.inv.models
import erpp.serv.models


class Clientecita(models.Model):
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
    maestroclientes = models.ForeignKey(
        erpp.fac.models.Maestroclientes,
        on_delete=models.CASCADE,
        verbose_name='MaestroClientes'
    )
    cargocliente = models.CharField(label='Cargo Cliente', max_length=50)
    lugarentrevista = models.CharField(label='Lugar De Entrevista', max_length=50)
    maestroproductos = models.ForeignKey(
        erpp.inv.models.Maestroproductos,
        on_delete=models.CASCADE,
        verbose_name='MaestroProductos'
    )
    fechacita = models.DateField(label='Fecha De Cita')
    horacita = models.DateTimeField(label='Hora De Cita')
    observacion = models.CharField(label='Observación', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'clientecita'


class Maestrotrabajotaller(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    nombre = models.CharField(label='Nombre', max_length=75)
    mostrarencita = models.BooleanField(verbose_name='Mostrar En Cita')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrotrabajotaller'


class Ejecucionserviciodetalle(models.Model):
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
    ejecucionserviciocabecera = models.ForeignKey(
        erpp.fac.models.Ejecucionserviciocabecera,
        on_delete=models.CASCADE,
        verbose_name='EjecucionServicioCabecera'
    )
    numerotarjeta = models.CharField(label='Número De Tarjeta', max_length=75)
    maestrotrabajotaller = models.ForeignKey(
        Maestrotrabajotaller,
        on_delete=models.CASCADE,
        verbose_name='MaestroTrabajoTaller'
    )
    maestroserviciotaller = models.ForeignKey(
        erpp.serv.models.Maestroserviciotaller,
        on_delete=models.CASCADE,
        verbose_name='MaestroServicioTaller'
    )
    maestrotecnico = models.ForeignKey(
        erpp.serv.models.Maestrotecnico,
        on_delete=models.CASCADE,
        verbose_name='MaestroTecnico'
    )
    ordenserviciodetalle = models.ForeignKey(
        erpp.serv.models.Ordenserviciodetalle,
        on_delete=models.CASCADE,
        verbose_name='OrdenServicioDetalle',
        blank=True,
        null=True
    )
    accionejecucion = models.CharField(label='Acción De Ejecución', max_length=50)
    observacion = models.CharField(label='Observación', max_length=500)
    hora = models.CharField(label='Hora', max_length=50)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    horastranscurridas = models.CharField(label='Horas Transcurridas', max_length=50, blank=True, null=True)
    porcentaje = models.DecimalField(label='Porcentaje', max_digits=18, decimal_places=2, blank=True, null=True)
    descripcion = models.CharField(label='Descripción', max_length=200, blank=True, null=True)
    estrabajoadicional = models.BooleanField(verbose_name='¿Es Trabajo Adicional?', blank=True, null=True)
    ordenserviciotrabajoadicional = models.ForeignKey(
        erpp.serv.models.Ordenserviciotrabajoadicional,
        on_delete=models.CASCADE,
        verbose_name='OrdenServicioTrabajoAdicional',
        blank=True,
        null=True
    )
    esservicioportercero = models.BooleanField(verbose_name='¿Es Servicio Por Tercero?', blank=True, null=True)
    servicioportercerodetalle = models.ForeignKey(
        erpp.serv.models.Servicioportercerodetalle,
        on_delete=models.CASCADE,
        verbose_name='ServicioPorTerceroDetalle',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'ejecucionserviciodetalle'


class Horariotaller(models.Model):
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
    hora = models.CharField(label='Hora', max_length=10)
    cantidadcitasportruno = models.IntegerField(verbose_name='Cantidad De Citas Por Turno')
    tipodia = models.CharField(label='Tipo Día', max_length=50, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    marca = models.ForeignKey(
        erpp.inv.models.Marca,
        on_delete=models.CASCADE,
        verbose_name='Marca',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'horariotaller'


class Horariotallerweb(models.Model):
    hora = models.CharField(max_length=10, blank=True, null=True)
    cantidad = models.IntegerField(verbose_name='Cantidad', blank=True, null=True)

    class Meta:
        db_table = 'horariotallerweb'


class Maestroconfiguracioncita(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresa'
    )
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    minutosdeactualizacion = models.IntegerField(verbose_name='Minutos De Actualización')
    dimensionpantallaancho = models.IntegerField(verbose_name='Dimensión Pantalla Ancho')
    dimensionpantallaalto = models.IntegerField(verbose_name='Dimensión Pantalla Alto')
    comprobaciondefacturapendiente = models.BooleanField(verbose_name='Comprobación De Factura Pendiente')
    numerodediasmaximofacturapendiente = models.IntegerField(
        verbose_name='Número De Días Máximo Para La Factura Pendiente'
    )
    diashabilescalendarios = models.BooleanField(verbose_name='Días Hábiles Calendarios')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroconfiguracioncita'


class Maestroestadocita(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    nombre = models.CharField(label='Nombre', max_length=50)
    color = models.CharField(label='Color', max_length=50)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestroestadocita'


class Tallerestacion(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    nombre = models.CharField(label='Nombre', max_length=50)
    direccion = models.CharField(label='Dirección', max_length=150)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
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

    class Meta:
        db_table = 'tallerestacion'


class Tallercitas(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresa = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    cliente = models.ForeignKey(
        erpp.fac.models.Maestroclientes,
        on_delete=models.CASCADE,
        verbose_name='MaestroClientes'
    )
    vehiculo = models.ForeignKey(
        erpp.fac.models.Maestrovehiculo,
        on_delete=models.CASCADE,
        label='MaestroVehiculo'
    )
    estacion = models.ForeignKey(
        Tallerestacion,
        on_delete=models.CASCADE,
        verbose_name='TalleresEstacion'
    )
    asesor = models.ForeignKey(
        erpp.serv.models.Tallerasesores,
        on_delete=models.CASCADE,
        verbose_name='TallerAsesores'
    )
    maestrotrabajotaller = models.ForeignKey(
        Maestrotrabajotaller,
        on_delete=models.CASCADE,
        verbose_name='MaestroTrabajoTaller'
    )
    maestroestadocita = models.ForeignKey(Maestroestadocita, on_delete=models.CASCADE, verbose_name='MaestroEstadoCita')
    carroceriapintura = models.BooleanField(verbose_name='Carrocería Pintura')
    fecha = models.DateField(label='Fecha')
    hora = models.CharField(label='Hora', max_length=10)
    taxi = models.BooleanField(verbose_name='¿Taxi?', default=False)
    informacion = models.CharField(label='Información', max_length=500)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    citaefectiva = models.BooleanField(verbose_name='¿Cita Efectiva?', blank=True, null=True)
    horaterminocita = models.CharField(label='Hora De Termino De La Cita', max_length=12, blank=True, null=True)
    tecnico = models.CharField(label='Técnico', max_length=100, blank=True, null=True)
    fechaentregatentativa = models.DateField(label='Fecha De Entrega Tentativa', blank=True, null=True)
    anulada = models.BooleanField(verbose_name='¿Anulada?', blank=True, null=True)
    horainicioatencion = models.DateTimeField(label='Hora De Inicio De Atención', blank=True, null=True)

    class Meta:
        db_table = 'tallercitas'


class Tallerclientevehiculo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    cliente = models.ForeignKey(
        erpp.fac.models.Maestroclientes,
        on_delete=models.CASCADE,
        verbose_name='MaestroCliente'
    )
    vehiculo = models.ForeignKey(
        erpp.fac.models.Maestrovehiculo,
        on_delete=models.CASCADE,
        verbose_name='MaestroVehiculo'
    )

    class Meta:
        db_table = 'tallerclientevehiculo'


class Tallerhorario(models.Model):
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
    tallerestacion = models.ForeignKey(
        Tallerestacion,
        on_delete=models.CASCADE,
        verbose_name='TallerEstacion'
    )
    entrada = models.CharField(label='Entrada', max_length=5)
    salida = models.CharField(label='Salida', max_length=5)
    horastrabajadas = models.IntegerField(verbose_name='Horas Trabajadas')
    descripcion = models.CharField(label='Descripción', max_length=200)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'tallerhorario'


class Usuarioweb(models.Model):
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
    usuario = models.CharField(label='Usuario', max_length=50)
    password = models.CharField(label='Contraseña', max_length=50)
    observacion = models.CharField(label='Observación', max_length=100, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'usuarioweb'


class Vehiculoaccesorios(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestrovehiculo = models.ForeignKey(
        erpp.fac.models.Maestrovehiculo,
        on_delete=models.CASCADE,
        verbose_name='MaestroVehiculo'
    )
    maestroaccesorios = models.ForeignKey(
        erpp.fac.models.Maestrovehiculoaccesorios,
        on_delete=models.CASCADE,
        verbose_name='MaestroAccesorios'
    )
    ordenserviciocabecera = models.ForeignKey(
        erpp.serv.models.Ordenserviciocabecera,
        on_delete=models.CASCADE,
        verbose_name='OrdenServicioCabecera'
    )
    estadoaccesorios = models.IntegerField(verbose_name='Estado De Los Accesorios')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'vehiculoaccesorios'
