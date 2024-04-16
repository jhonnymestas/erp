from django.db import models

import erpp.conta.models
import erpp.fac.models
import erpp.gen.models


class Ctactecliente(models.Model):
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
    cargo = models.BooleanField(verbose_name='¿Cargo?', blank=True, null=True)
    fechageneracion = models.DateTimeField(label='Fecha De Generación', blank=True, null=True)
    codigocliente = models.CharField(label='Código De Cliente', max_length=20, blank=True, null=True)
    maestrocliente = models.ForeignKey(
        erpp.fac.models.Maestroclientes,
        on_delete=models.CASCADE,
        verbose_name='MaestroCliente',
        blank=True,
        null=True
    )
    codigoconcepto = models.CharField(label='Código De Concepto', max_length=20, blank=True, null=True)
    obligacion = models.ForeignKey(
        erpp.fac.models.Facturaclientecabecera,
        on_delete=models.CASCADE,
        verbose_name='Obligacion',
        blank=True,
        null=True
    )
    codigotipocliente = models.CharField(label='Código Tipo De Cliente', max_length=20, blank=True, null=True)
    maestrotipocliente = models.ForeignKey(
        erpp.fac.models.Maestrotipocliente,
        on_delete=models.CASCADE,
        verbose_name='MaestroTipoCliente',
        blank=True,
        null=True
    )
    codigoestado = models.CharField(label='Código De Estado', max_length=20, blank=True, null=True)
    tipodocorigen = models.CharField(label='Tipo De Documento Origen', max_length=5, blank=True, null=True)
    numserorigen = models.CharField(label='Número De Serie Origen', max_length=25, blank=True, null=True)
    numdocorigen = models.DecimalField(
        label='Número Documento Origen',
        max_digits=18,
        decimal_places=0,
        blank=True,
        null=True
    )
    itemorigen = models.IntegerField(verbose_name='Ítem Origen', blank=True, null=True)
    fechadocorigen = models.DateTimeField(label='Fecha Documento Origen', blank=True, null=True)
    fechadevencimiento = models.DateTimeField(label='Fecha De Vencimiento', blank=True, null=True)
    codigodebanco = models.IntegerField(verbose_name='Código De Banco', blank=True, null=True)
    maestrobanco = models.ForeignKey(
        erpp.gen.models.Maestrobancos,
        on_delete=models.CASCADE,
        verbose_name='MaestroBanco',
        blank=True,
        null=True
    )
    cuentabanco = models.CharField(label='Cuenta De Banco', max_length=100, blank=True, null=True)
    numerocheque = models.CharField(label='Número De Cheque', max_length=100, blank=True, null=True)
    tipodocref = models.CharField(label='Tipo Documento Referido', max_length=5, blank=True, null=True)
    serdocref = models.CharField(label='Serie De Documento Referido', max_length=25, blank=True, null=True)
    numdocref = models.IntegerField(verbose_name='Número Documento Referido', blank=True, null=True)
    fechaliquidacionca = models.DateTimeField(label='Fecha Liquidación Ca', blank=True, null=True)
    moneda = models.CharField(label='Moneda', max_length=100, blank=True, null=True)
    maestrotipocambio = models.ForeignKey(
        erpp.gen.models.Maestrotipodecambio,
        on_delete=models.CASCADE,
        verbose_name='MaestroTipoCambio',
        blank=True,
        null=True
    )
    tipodecambio = models.DecimalField(label='Tipo de Cambio', max_digits=5, decimal_places=4, blank=True, null=True)
    importesoles = models.DecimalField(label='Importe En Soles', max_digits=11, decimal_places=2, blank=True, null=True)
    importedolares = models.DecimalField(
        label='Importe En Dólares',
        max_digits=13,
        decimal_places=4,
        blank=True,
        null=True
    )
    saldodocumento = models.DecimalField(
        label='Saldo Documento',
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True
    )
    centrodecostos = models.CharField(label='Centro De Costos', max_length=100, blank=True, null=True)
    codigocuenta = models.CharField(label='Código De Cuenta', max_length=20, blank=True, null=True)
    plandecuentas = models.ForeignKey(
        erpp.conta.models.Plandecuentas,
        on_delete=models.CASCADE,
        verbose_name='PlanDeCuentas',
        blank=True,
        null=True
    )
    anulado = models.BooleanField(verbose_name='¿Anulado?', blank=True, null=True)
    edoletras = models.IntegerField(verbose_name='Edo Letras', blank=True, null=True)
    fechacancelacion = models.DateTimeField(label='Fecha De Cancelación', blank=True, null=True)
    doccancelado = models.BooleanField(verbose_name='¿Documento Cancelado?', blank=True, null=True)
    empresactb = models.IntegerField(verbose_name='Empresa CTB', blank=True, null=True)
    anhioctb = models.IntegerField(verbose_name='Año CTB', blank=True, null=True)
    mesctb = models.IntegerField(verbose_name='Mes CTB', blank=True, null=True)
    tipodiarioctb = models.CharField(label='Tipo Diario CTB', max_length=100, blank=True, null=True)
    nrocomprobctb = models.IntegerField(verbose_name='Número Comprobante CTB', blank=True, null=True)
    glosa = models.CharField(label='Glosa', max_length=100, blank=True, null=True)
    depctacte = models.BooleanField(verbose_name='¿Depósito Cuenta Cliente?', blank=True, null=True)
    cancelacion = models.BooleanField(verbose_name='¿Cancelación?', blank=True, null=True)
    fill = models.CharField(label='Fill', max_length=20, blank=True, null=True)
    codigocaja = models.CharField(label='Código De Caja', max_length=20, blank=True, null=True)
    castigado = models.BooleanField(verbose_name='¿Castigado?', blank=True, null=True)
    fechacastigo = models.DateTimeField(label='Fecha De Castigo', blank=True, null=True)
    porcentajeinteres = models.DecimalField(
        label='Porcentaje De Interés',
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )
    gastosadministrativos = models.DecimalField(
        label='Gastos Administrativos',
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True
    )
    gastosbancarios = models.DecimalField(
        label='Gastos Bancarios',
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True
    )
    intereses = models.DecimalField(label='Intereses', max_digits=11, decimal_places=2, blank=True, null=True)
    pagooficina = models.BooleanField(verbose_name='¿Pago Oficina?', blank=True, null=True)
    diferenciacambio = models.DecimalField(
        label='Diferencia Cambio',
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True
    )
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    cobrador = models.ForeignKey(
        erpp.fac.models.Maestrovendedores,
        on_delete=models.CASCADE,
        verbose_name='Cobrador',
        blank=True,
        null=True
    )
    maestroturnocaja = models.ForeignKey(
        erpp.fac.models.Maestroturnoscaja,
        on_delete=models.CASCADE,
        verbose_name='MaestroTurnoCaja',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'ctactecliente'
