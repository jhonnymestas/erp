from django.db import models

import erpp.gen.models
import erpp.per.models


class Marcaciondetalle(models.Model):
    idmarcaciondetalle = models.AutoField(label='IdMarcacionDetalle', primary_key=True)
    marcacion = models.ForeignKey(erpp.marca.models.Marcaciondetalle, on_delete=models.CASCADE, verbose_name='Marcacion', blank=True, null=True)
    dni = models.CharField(label='DNI', max_length=15, blank=True, null=True)
    nombre = models.CharField(label='Nombre', max_length=200, blank=True, null=True)
    fechamarcacion = models.DateField(label='Fecha De Marcación', blank=True, null=True)
    titulohorario = models.CharField(label='Título Del Horario', max_length=100, blank=True, null=True)
    fechahorainiciomarcacion = models.DateTimeField(label='Fecha y Hora De Inicio De Marcación', blank=True, null=True)
    fechahorasalidamarcacion = models.DateTimeField(label='Fecha y Hora De Salida De Marcación', blank=True, null=True)
    fechahoraentrada = models.DateTimeField(label='Fecha y Hora De Entrada', blank=True, null=True)
    fechahorasalidad = models.DateTimeField(label='Fecha y Hora De Salidad', blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36, blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=200, blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)

    class Meta:
        db_table = 'marcaciondetalle'


class Marcarpersonal(models.Model):
    idmarcarpersonal = models.AutoField(label='IdMarcarPersonal')
    nombresapellidos = models.TextField(label='Nombres y Apellidos')
    fecha = models.DateTimeField(label='Fecha')
    horaentrada = models.TimeField(label='Hora De Entrada', blank=True, null=True)
    horasalida = models.TimeField(label='Hora De Salida', blank=True, null=True)
    falta = models.BooleanField(verbose_name='¿Falta?', default=models.CASCADE)
    salidarefrigerio = models.TimeField(label='Salida De Refrigerio', blank=True, null=True)
    ingresorefrigerio = models.TimeField(label='Ingreso De Refrigerio', blank=True, null=True)
    tolerancia = models.TimeField(label='Tolerancia', blank=True, null=True)
    horarefrigerio = models.TimeField(label='Hora De Refrigerio', blank=True, null=True)
    sobretiempo25porcentaje = models.DecimalField(label='Sobre Tiempo 25 porcentaje', max_digits=10, decimal_places=2)
    sobretiempo35porcentaje = models.DecimalField(label='Sobre Tiempo 35 porcentaje', max_digits=10, decimal_places=2)
    sobretiempo100porcentaje = models.DecimalField(label='Sobre Tiempo 100 porcentaje', max_digits=10, decimal_places=2)
    diferenciaingreso = models.TimeField(label='Diferencia De Ingreso', blank=True, null=True)
    diferenciasalida = models.TimeField(label='Diferencia De Salida', blank=True, null=True)
    marcaringresotareo = models.TimeField(label='Marcar Ingreso De Tareo', blank=True, null=True)
    marcarsalidatareo = models.TimeField(label='Marcar Salida De Tareo', blank=True, null=True)
    permiso = models.CharField(label='Permiso', max_length=25)
    descripcion = models.TextField(label='Descripción')
    horatrabajo = models.TimeField(label='HoraTrabajo', blank=True, null=True)
    calificacion = models.BooleanField(verbose_name='¿Calificacion?', default=models.CASCADE)
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    empresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='Empresa', blank=True, null=True)
    fechademodificacion = models.DateTimeField(label='Fecha De Modificación')
    usuario = models.CharField(label='Usuario', max_length=36)
    maestropersonal = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='MaestroPersonal', blank=True, null=True)
    horaingresoreal = models.TimeField(label='Hora De Ingreso Real', blank=True, null=True)
    horasalirreal = models.TimeField(label='Hora De Salida Real', blank=True, null=True)
    documentoidentidad = models.CharField(label='Documento De Identidad', max_length=15, blank=True, null=True)
    horasextra = models.TimeField(label='Horas Extra', blank=True, null=True)
    horstnocturna = models.DecimalField(label='Horas Servicio Tipo Nocturno', max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'marcarpersonal'