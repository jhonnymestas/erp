from django.db import models

import erpp.cmp.models
import erpp.conta.models
import erpp.gen.models
import erpp.per.models


class Chequecabecera(models.Model):
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
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20, blank=True, null=True)
    numerocomprobante = models.CharField(label='Número Comprobante', max_length=20, blank=True, null=True)
    tipo = models.CharField(label='Tipo', max_length=1, blank=True, null=True)
    fecha = models.DateTimeField(label='Fecha', blank=True, null=True)
    codigobanco = models.CharField(label='Código Banco', max_length=20, blank=True, null=True)
    maestrobanco = models.ForeignKey(
        erpp.gen.models.Maestrobancos,
        on_delete=models.CASCADE,
        verbose_name='MaestroBanco',
        blank=True,
        null=True
    )
    numerocuenta = models.CharField(label='Número De Cuenta', max_length=20, blank=True, null=True)
    codigocuenta = models.CharField(label='Código De Cuenta', max_length=20, blank=True, null=True)
    plandecuentas = models.ForeignKey(
        erpp.conta.models.Plandecuentas,
        on_delete=models.CASCADE,
        verbose_name='PlanDeCuentas',
        blank=True,
        null=True
    )
    numerocheque = models.IntegerField(verbose_name='Número De Cheque')
    giradoa = models.CharField(label='Girado A', max_length=20, blank=True, null=True)
    tipomoneda = models.CharField(label='Tipo Moneda', max_length=10, blank=True, null=True)
    tipodecambio = models.DecimalField(label='Tipo De Cambio', max_digits=5, decimal_places=4, blank=True, null=True)
    montosoles = models.DecimalField(label='Monto En Soles', max_digits=11, decimal_places=2, blank=True, null=True)
    montodolares = models.DecimalField(label='Monto En Dólares', max_digits=13, decimal_places=4, blank=True, null=True)
    acumuladosoles = models.DecimalField(
        label='Acumulado En Soles',
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True
    )
    acumuladodolares = models.DecimalField(
        label='Acumulado En Dólares',
        max_digits=13,
        decimal_places=4,
        blank=True,
        null=True
    )
    numerocomprobantecont = models.IntegerField(verbose_name='Número De Comprobante Cont', blank=True, null=True)
    glosa = models.CharField(label='Glosa', max_length=100, blank=True, null=True)
    estadocheque = models.CharField(label='Estado De Cheque', max_length=20, blank=True, null=True)
    fechadigitacion = models.DateTimeField(label='Fecha De Digitación', blank=True, null=True)
    fechaaceptacion = models.DateTimeField(label='Fecha De Aceptación', blank=True, null=True)
    usuariodigitacion = models.CharField(label='Usuario De Digitación', max_length=20, blank=True, null=True)
    usuarioaceptacion = models.CharField(label='Usuario De Aceptación', max_length=20, blank=True, null=True)
    transferencia = models.BooleanField(verbose_name='¿Transferencia?', blank=True, null=True)
    debesoles = models.DecimalField(label='Se Debe En Soles', max_digits=11, decimal_places=2, blank=True, null=True)
    habersoles = models.DecimalField(label='Hay En Soles', max_digits=11, decimal_places=2, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroretencion = models.ForeignKey(
        erpp.per.models.Maestroretencion,
        on_delete=models.CASCADE,
        verbose_name='MaestroRetencion',
        blank=True,
        null=True
    )
    cajachica = models.ForeignKey(
        erpp.conta.models.Cajachicacabecera,
        on_delete=models.CASCADE,
        verbose_name='CajaChica',
        blank=True,
        null=True
    )
    imprimiren = models.TextField(label='Imprimir En', blank=True, null=True)

    class Meta:
        db_table = 'chequecabecera'


class Chequedetalle(models.Model):
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
    chequecabecera = models.ForeignKey(
        Chequecabecera,
        on_delete=models.CASCADE,
        verbose_name='ChequeCabecera',
        blank=True,
        null=True
    )
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20, blank=True, null=True)
    tipo = models.BooleanField(blank=True, null=True)
    numerocomprobante = models.CharField(label='Número De Comprobante', max_length=20, blank=True, null=True)
    item = models.IntegerField(verbose_name='Ítem', blank=True, null=True)
    tipodocumentosunat = models.IntegerField(verbose_name='Tipo De Documento Sunat', blank=True, null=True)
    numerofactura = models.CharField(label='Número De Factura', max_length=20, blank=True, null=True)
    codigoproveedor = models.CharField(label='Código De Proveedor', max_length=20, blank=True, null=True)
    maestroproveedor = models.ForeignKey(
        erpp.gen.models.Maestroproveedores,
        on_delete=models.CASCADE,
        verbose_name='MaestroProveedor',
        blank=True,
        null=True
    )
    codigocuenta = models.CharField(label='Código De Cuenta', max_length=20, blank=True, null=True)
    plandecuentas = models.ForeignKey(
        erpp.conta.models.Plandecuentas,
        on_delete=models.CASCADE,
        verbose_name='PlanDeCuentas',
        blank=True,
        null=True
    )
    numerocheque = models.CharField(label='Número De Cheque', max_length=20, blank=True, null=True)
    tipomoneda = models.CharField(label='Tipo De Moneda', max_length=20, blank=True, null=True)
    monto = models.DecimalField(label='Monto', max_digits=11, decimal_places=2, blank=True, null=True)
    glosa = models.CharField(label='Glosa', max_length=100, blank=True, null=True)
    estadocheque = models.CharField(label='Estado De Cheque', max_length=20, blank=True, null=True)
    fechadigitacion = models.DateTimeField(label='Fecha De Digitación', blank=True, null=True)
    fechaaceptacion = models.DateTimeField(label='Fecha De Aceptación', blank=True, null=True)
    usuario = models.CharField(label='Usuario', max_length=20, blank=True, null=True)
    seriedocumento = models.CharField(label='Serie De Documento', max_length=20, blank=True, null=True)
    numerodocumento = models.CharField(label='Número De Documento', max_length=20, blank=True, null=True)
    debehaber = models.CharField(label='Debe Haber', max_length=20, blank=True, null=True)
    codigodistribucioncentrocosto = models.CharField(
        label='CodigoDistribucionCentroCosto',
        max_length=20,
        blank=True,
        null=True
    )
    distribucioncentrocosto = models.ForeignKey(
        erpp.conta.models.Distribucioncentrocostocabecera,
        on_delete=models.CASCADE,
        verbose_name='DistribucionCentroCosto',
        blank=True,
        null=True
    )
    codigocentrocostos = models.CharField(label='Código Del Centro De Costos', max_length=20, blank=True, null=True)
    maestrocentrocosto = models.ForeignKey(
        erpp.gen.models.Maestrocentrosdecostos,
        on_delete=models.CASCADE,
        verbose_name='MaestroCentroCosto',
        blank=True,
        null=True
    )
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=True)
    facturaproveedor = models.ForeignKey(
        erpp.cmp.models.Facturasproveedorescabecera,
        on_delete=models.CASCADE,
        verbose_name='FacturaProveedor',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'chequedetalle'


class Ctacteproveedor(models.Model):
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
    cargoabono = models.BooleanField(verbose_name='¿Cargo Abono?', blank=True, null=True)
    fechaemisioncaja = models.DateTimeField(label='Fecha De Emisión Caja', blank=True, null=True)
    codigoproveedor = models.CharField(label='Código De Proveedor', max_length=20)
    maestroproveedor = models.ForeignKey(
        erpp.gen.models.Maestroproveedores,
        on_delete=models.CASCADE,
        verbose_name='MaestroProveedor'
    )
    tipodocorigen = models.IntegerField(verbose_name='Tipo Documento Origen', blank=True, null=True)
    numdocorigen = models.CharField(label='Número Documento Origen', max_length=20)
    itemorigen = models.IntegerField(verbose_name='Ítem Origen')
    fechadocorigen = models.DateTimeField(label='Fecha De Documento Origen', blank=True, null=True)
    fechadevencimiento = models.DateTimeField(label='Fecha De Vencimiento', blank=True, null=True)
    codigobanco = models.CharField(label='Código De Banco', max_length=20)
    maestrobanco = models.ForeignKey(
        erpp.gen.models.Maestrobancos,
        on_delete=models.CASCADE,
        verbose_name='MaestroBanco'
    )
    numerodecheque = models.CharField(label='Número De Cheque', max_length=20)
    facturaproveedor = models.ForeignKey(
        erpp.cmp.models.Facturasproveedorescabecera,
        on_delete=models.CASCADE,
        verbose_name='FacturaProveedor',
        blank=True,
        null=True
    )
    tipodocref = models.ForeignKey(
        erpp.gen.models.Maestrotiposdocumentos,
        on_delete=models.CASCADE,
        verbose_name='TipoDocumentoReferido',
        blank=True,
        null=True
    )
    numdocref = models.CharField(label='Número Documento Referido', max_length=20)
    seriedocref = models.CharField(label='Serie Documento Referido', max_length=20, blank=True, null=True)
    fechaliquidacionca = models.DateTimeField(label='Fecha Liquidacion Ca', blank=True, null=True)
    moneda = models.CharField(label='Moneda', max_length=20)
    tipodecambio = models.DecimalField(label='Tipo De Cambio', max_digits=10, decimal_places=4, blank=True, null=True)
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
    saldodolares = models.DecimalField(label='Saldo En Dólares', max_digits=13, decimal_places=4, blank=True, null=True)
    lineaproduccion = models.IntegerField(verbose_name='Línea De Producción', blank=True, null=True)
    codigocentrocostos = models.CharField(label='Código De Centro De Costos', max_length=20)
    codigocuenta = models.CharField(label='Código De Cuenta', max_length=20, blank=True, null=True)
    plandecuentas = models.ForeignKey(
        erpp.conta.models.Plandecuentas,
        on_delete=models.CASCADE,
        verbose_name='PlanDeCuentas',
        blank=True,
        null=True
    )
    anulado = models.BooleanField(verbose_name='¿Anulado?', blank=True, null=True)
    fechacancelacion = models.DateTimeField(label='Fecha De Cancelación', blank=True, null=True)
    facturacancelada = models.BooleanField(verbose_name='¿Factura Cancelada?', blank=True, null=True)
    empresactb = models.IntegerField(verbose_name='Empresa CTB', blank=True, null=True)
    anhioctb = models.IntegerField(verbose_name='Año CTB', blank=True, null=True)
    mesctb = models.IntegerField(verbose_name='Mes CTB', blank=True, null=True)
    tipodiarioctb = models.IntegerField(verbose_name='Tipo Diario CTB', blank=True, null=True)
    nrocomprobctb = models.CharField(label='Número Comprobante CTB', max_length=20, blank=True, null=True)
    glosa = models.TextField(label='Glosa', blank=True, null=True)
    cajaref = models.IntegerField(verbose_name='Caja Referencia', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    tipoconceptopdt = models.CharField(label='Tipo De Concepto Pdt', max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'ctacteproveedor'


class Maestrocuentaslibresparacheques(models.Model):
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
    codigocuenta = models.CharField(label='Código De Cuenta', max_length=20)
    pideproveedor = models.BooleanField(verbose_name='¿Pide Proveedor?', default=False)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)

    class Meta:
        db_table = 'maestrocuentaslibresparacheques'
        unique_together = (('codigocuenta', 'idmaestroempresa'),)
