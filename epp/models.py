from django.db import models

import erpp.gen.models
import erpp.inv.models
import erpp.per.models


class Operacioneppcabecera(models.Model):
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
    maestropersonal = models.ForeignKey(
        erpp.per.models.Maestropersonal,
        on_delete=models.CASCADE,
        verbose_name='MaestroPersonal'
    )
    area = models.ForeignKey(erpp.inv.models.Areas, on_delete=models.CASCADE, verbose_name='Area')
    numeroguia = models.IntegerField(verbose_name='Número De Guía')
    fechaenvio = models.DateField(label='Fecha De Envío')
    numerocargo = models.CharField(label='Número De Cargo', max_length=75)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    serieguia = models.CharField(label='Serie De Guía', max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'operacioneppcabecera'


class Operacioneppdetalle(models.Model):
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
    cabecera = models.ForeignKey(Operacioneppcabecera, on_delete=models.CASCADE, verbose_name='Cabecera')
    maestroproducto = models.ForeignKey(
        erpp.inv.models.Maestroproductos,
        on_delete=models.CASCADE,
        verbose_name='MaestroProducto'
    )
    cantidad = models.DecimalField(label='Cantidad', max_digits=18, decimal_places=2)
    controlcambio = models.DateField(label='Control De Cambio')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    diasaviso = models.CharField(label='DiasAviso', max_length=4, blank=True, null=True)

    class Meta:
        db_table = 'operacioneppdetalle'
