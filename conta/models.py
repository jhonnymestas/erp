from django.db import models

import erpp.cita.models
import erpp.cmp.models
import erpp.fac.models
import erpp.gen.models
import erpp.inv.models
import erpp.marca.models
import erpp.per.models


class Activosfijos(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigo = models.CharField(label='Código', max_length=50)
    cuentacontable = models.CharField(label='Cuenta Contable', max_length=50)
    descripcion = models.CharField(label='Descripción', max_length=500)
    marca = models.CharField(label='Marca', max_length=50)
    modelo = models.CharField(label='Modelo', max_length=50)
    numeroplaca = models.CharField(label='Número De Placa', max_length=50)
    saldoinicial = models.DecimalField(label='Saldo Inicial', max_digits=18, decimal_places=2)
    adquisiciones = models.DecimalField(label='Adquisiciones', max_digits=18, decimal_places=2)
    mejoras = models.DecimalField(label='Mejoras', max_digits=18, decimal_places=2)
    retirosbajas = models.DecimalField(label='Retiros Bajas', max_digits=18, decimal_places=2)
    ajustes = models.DecimalField(label='Ajustes', max_digits=18, decimal_places=2)
    valorhistorico = models.DecimalField(label='Valor Historico', max_digits=18, decimal_places=2)
    ajusteinflacion = models.DecimalField(label='Ajuste De Inflacion', max_digits=18, decimal_places=2)
    valorajustado = models.DecimalField(label='Valor Ajustado', max_digits=18, decimal_places=2)
    fechaadquisicion = models.DateTimeField(label='Fecha De Adquisicion')
    fechainicio = models.DateTimeField(label='Fecha De Inicio')
    metodo = models.CharField(label='Método', max_length=50)
    nrodocumento = models.CharField(label='Número de Documento', max_length=50)
    porcentajedepreciacion = models.IntegerField(verbose_name='Porcentaje De Depreciacion')
    depreciacionacumulada = models.DecimalField(label='Depreciacion Acumulada', max_digits=18, decimal_places=2)
    depreciacionejercicio = models.DecimalField(label='Depreciacion Ejercicio', max_digits=18, decimal_places=2)
    depreciacionretiros = models.DecimalField(label='Depreciacion Retiros', max_digits=18, decimal_places=2)
    depreciacionotros = models.DecimalField(label='DepreciacionOtros', max_digits=18, decimal_places=2)
    depreciacionhistorica = models.DecimalField(label='Depreciacion Historica', max_digits=18, decimal_places=2)
    ajustedepreciacion = models.DecimalField(label='Ajuste De Depreciacion', max_digits=18, decimal_places=2)
    depreciacioninflacion = models.DecimalField(label='Depreciación Inflación', max_digits=18, decimal_places=2)
    codigousuario = models.CharField(label='Codigo De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?', default=False)
    maestroempresas = models.IntegerField(verbose_name='MaestroEmpresas')
    maestrosucursales = models.IntegerField(verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'activosfijos'


class Plandecuentas(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.IntegerField(verbose_name='MaestroEmpresas')
    codigocuenta = models.CharField(label='Código De Cuenta', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=255)
    esmayor = models.BooleanField(verbose_name='¿Es Mayor?')
    codigocuentamayor = models.CharField(label='Código De Cuenta Mayor', max_length=20)
    tipo = models.BooleanField(verbose_name='¿Tipo?', blank=True, null=True)
    tipocuenta = models.IntegerField(verbose_name='Tipo De Cuenta', blank=True, null=True)
    flagctacte = models.BooleanField(verbose_name='¿Flag Cuenta Cliente?')
    flagcostos = models.BooleanField(verbose_name='¿Flag Costos?')
    itemsrelacionados = models.IntegerField(verbose_name='Ítems Relacionados', blank=True, null=True)
    lugarbal8column = models.IntegerField(verbose_name='Lugar Bal 8 Column A')
    ruc = models.CharField(label='RUC', max_length=11, blank=True, null=True)
    codigocuentadebe = models.CharField(label='Código De Cuenta Debe', max_length=20, blank=True, null=True)
    debe = models.IntegerField(verbose_name='Debe', blank=True, null=True)
    codigocuentahaber = models.CharField(label='Código De CuentaHaber', max_length=20, blank=True, null=True)
    haber = models.IntegerField(verbose_name='Haber', blank=True, null=True)
    anhio = models.IntegerField(verbose_name='Año')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'plandecuentas'


class Amarrecabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    plandecuentas = models.ForeignKey(Plandecuentas, on_delete=models.CASCADE, verbose_name='PlanDeCuentas')
    descripcion = models.CharField(label='Descripción', max_length=250)
    fechahoraregistro = models.DateTimeField(label='Fecha y Hora De Registro')
    activo = models.BooleanField(verbose_name='¿Activo?')
    estado = models.IntegerField(verbose_name='Estado')
    uusarioid = models.IntegerField(verbose_name='UusarioID')
    maestroempresas = models.IntegerField(verbose_name='MaestroEmpresas')
    maestrosucursal = models.IntegerField(verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'amarrecabecera'


class Amarredetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    amarrecabecera = models.ForeignKey(Amarrecabecera, on_delete=models.CASCADE, verbose_name='AmarreCabecera')
    plandecuentasdebe = models.ForeignKey(Plandecuentas, on_delete=models.CASCADE, verbose_name='PlanDeCuentasDebe')
    plandecuentashaber = models.ForeignKey(Plandecuentas, on_delete=models.CASCADE, verbose_name='PlanDeCuentasHaber')
    porcentaje = models.DecimalField(label='Porcentaje', max_digits=5, decimal_places=2)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')
    fechahoraregistro = models.DateTimeField(label='Fecha y Hora De Registro')
    usuarioid = models.IntegerField(verbose_name='UsuarioID')
    maestroempresas = models.IntegerField(verbose_name='MaestroEmpresas')
    maestrosucursal = models.IntegerField(verbose_name='MaestroSucursal')

    class Meta:
        db_table = 'AmarreDetalle'


class Balancecabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    anhio = models.IntegerField(verbose_name='Año')
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    codigoempresa = models.CharField(label='Código Empresa', max_length=20)
    posicion = models.IntegerField(verbose_name='Posición')
    linea = models.IntegerField(verbose_name='Línea')
    signo = models.IntegerField(verbose_name='Signo')
    titulodetalle = models.CharField(label='Título Detalle', max_length=250, blank=True, null=True)
    titulogeneral = models.CharField(label='Título General', max_length=250, blank=True, null=True)
    titulototales = models.CharField(label='Titulo Totales', max_length=250, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'balancecabecera'


class Balancedetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestrocabecera = models.ForeignKey(
        Balancecabecera,
        on_delete=models.CASCADE,
        verbose_name='MaestroCabecera',
        blank=True,
        null=True
    )
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20)
    posicion = models.IntegerField(verbose_name='Posición')
    linea = models.IntegerField(verbose_name='Línea')
    cuenta = models.CharField(label='Cuenta', max_length=250)
    condicion = models.CharField(label='Condición', max_length=5)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'balancedetalle'


class Cajacabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codempresa = models.IntegerField(verbose_name='Código De Empresa', blank=True, null=True)
    codcaja = models.CharField(label='Código De Caja', max_length=20, blank=True, null=True)
    numerocaja = models.IntegerField(verbose_name='Número De Caja', blank=True, null=True)
    fecha = models.DateTimeField(label='Fecha', blank=True, null=True)
    moneda = models.TextField(label='Moneda', blank=True, null=True)
    transferencia = models.BooleanField(verbose_name='¿Transferencia?', blank=True, null=True)
    totaldebe = models.DecimalField(label='Total Debe', max_digits=11, decimal_places=2, blank=True, null=True)
    totalhaber = models.DecimalField(label='Total Haber', max_digits=11, decimal_places=2, blank=True, null=True)
    nrocomprobante = models.IntegerField(verbose_name='Número Comprobante', blank=True, null=True)
    glosa = models.TextField(label='Glosa', blank=True, null=True)
    items = models.IntegerField(verbose_name='Items', blank=True, null=True)
    asientogenerado = models.BooleanField(verbose_name='¿Asiento Generado?', blank=True, null=True)
    asientorevisado = models.BooleanField(verbose_name='¿Asiento Revisado?', blank=True, null=True)
    saldoinicial = models.DecimalField(label='Saldo Inicial', max_digits=12, decimal_places=4)
    saldofinla = models.DecimalField(label='Saldo Final', max_digits=12, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')
    codigocuenta = models.CharField(label='CodigoCuenta', max_length=50, blank=True, null=True)
    maestrocaja = models.ForeignKey(
        erpp.fac.models.Maestrocajas,
        on_delete=models.CASCADE,
        verbose_name='MaestroCajas',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'cajacabecera'


class Cajachicacabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codempresa = models.IntegerField(verbose_name='Código De Empresa', blank=True, null=True)
    numerocaja = models.CharField(label='Número Caja', max_length=20, blank=True, null=True)
    refcaja = models.TextField(label='Referencia Caja', blank=True, null=True)
    fecha = models.DateTimeField(label='Fecha', blank=True, null=True)
    fechacontabilizacion = models.DateTimeField(label='Fecha Contabilización', blank=True, null=True)
    totalsolesdebe = models.DecimalField(
        label='Total Soles Debe',
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True
    )
    totalsoleshaber = models.DecimalField(
        label='Total Soles Haber',
        max_digits=11,
        decimal_places=2,
        blank=True,
        null=True
    )
    glosa = models.TextField(label='Glosario', blank=True, null=True)
    items = models.IntegerField(verbose_name='Ítems', blank=True, null=True)
    asientogenerado = models.BooleanField(verbose_name='¿Asiento Generado?', blank=True, null=True)
    asientorevisado = models.BooleanField(verbose_name='¿Asiento Revisado?', blank=True, null=True)
    nrocomprobante = models.IntegerField(verbose_name='Número Comprobante', blank=True, null=True)
    saldoinicial = models.DecimalField(label='Saldo Inicial', max_digits=12, decimal_places=4)
    saldofinal = models.DecimalField(label='Saldo Final', max_digits=12, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')
    codigocuenta = models.CharField(label='Código De Cuenta', max_length=50, blank=True, null=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='maestroempresas',
        blank=True,
        null=True
    )
    codigocaja = models.CharField(label='Código Caja', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'cajachicacabecera'


class Cajachicadetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    cajachicacabecera = models.ForeignKey(Cajachicacabecera, on_delete=models.CASCADE, verbose_name='CajaChicaCabecera')
    codempresa = models.IntegerField(verbose_name='Código De Empresa', blank=True, null=True)
    nrocaja = models.CharField(label='Número De Caja', max_length=20, blank=True, null=True)
    item = models.IntegerField(verbose_name='Ítem', blank=True, null=True)
    codproveedor = models.CharField(label='Código Proveedor', max_length=20, blank=True, null=True)
    codcentrodecostos = models.TextField(label='Código CentrodeCostos', blank=True, null=True)
    tipodocumento = models.CharField(label='Tipo De Documento', max_length=5, blank=True, null=True)
    serie = models.CharField(label='Serie', max_length=20, blank=True, null=True)
    numero = models.CharField(label='Número', max_length=20, blank=True, null=True)
    debeohaber = models.BooleanField(verbose_name='¿Debe o Haber?', blank=True, null=True)
    moneda = models.TextField(label='Moneda', blank=True, null=True)
    basesoles = models.DecimalField(label='Base En Soles', max_digits=11, decimal_places=2, blank=True, null=True)
    igvsoles = models.DecimalField(label='Igv En Soles', max_digits=11, decimal_places=2, blank=True, null=True)
    totalsoles = models.DecimalField(label='Total En Soles', max_digits=11, decimal_places=2, blank=True, null=True)
    basedolares = models.DecimalField(label='Base En Dólares', max_digits=11, decimal_places=2, blank=True, null=True)
    igvdolares = models.DecimalField(label='Igv En Dólares', max_digits=11, decimal_places=2, blank=True, null=True)
    totaldolares = models.DecimalField(label='Total En Dólares', max_digits=11, decimal_places=2, blank=True, null=True)
    glosa = models.TextField(label='Glosa', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')
    codcuenta = models.CharField(label='Código De Cuenta', max_length=50, blank=True, null=True)
    codcaja = models.CharField(label='Código De Caja', max_length=20, blank=True, null=True)
    fechadoc = models.DateTimeField(label='Fecha De Documentación', blank=True, null=True)
    t_c = models.DecimalField(label='T_C', max_digits=13, decimal_places=4, blank=True, null=True)
    hora = models.TimeField(label='Hora', blank=True, null=True)
    usuario = models.TextField(label='Usuario', blank=True, null=True)

    class Meta:
        db_table = 'cajachicadetalle'


class Cierreanualcontable(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    empresa = models.ForeignKey(erpp.gen.models.Maestroempresas, on_delete=models.CASCADE, verbose_name='Empresas')
    sucursal = models.ForeignKey(erpp.gen.models.Maestrosucursales, on_delete=models.CASCADE, verbose_name='Sucursales')
    anio = models.IntegerField(verbose_name='Año')
    cerrado = models.BooleanField(verbose_name='¿Cerrado?')
    fechacierre = models.DateTimeField(label='Fecha De Cierre')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=50)
    autorizado = models.CharField(label='Autorizado', max_length=250)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'cierreanualcontable'


class Cierrecajafin(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    formadepago = models.ForeignKey(
        erpp.gen.models.Maestroformasdepago,
        on_delete=models.CASCADE,
        verbose_name='FormaDePago',
        blank=True,
        null=True
    )
    precioventadeclaradosoles = models.DecimalField(
        label='Precio De Venta Declarado En Soles',
        max_digits=18,
        decimal_places=0,
        blank=True,
        null=True
    )
    diferenciasoles = models.DecimalField(
        label='Diferencia En Soles',
        max_digits=18,
        decimal_places=0,
        blank=True,
        null=True
    )
    cajero = models.ForeignKey(
        erpp.fac.models.Maestrocajas,
        on_delete=models.CASCADE,
        verbose_name='Cajero',
        blank=True,
        null=True
    )
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    usuario = models.CharField(label='Usuario', max_length=36, blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)

    class Meta:
        db_table = 'cierrecajafin'


class Configuracionplancuentas(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    cuentaigv = models.CharField(label='Cuenta IGV', max_length=50)
    fecharegistro = models.DateTimeField(label='Fecha De Registro')
    cuentaproveedornacional = models.CharField(
        label='Cuenta De Proveedor Nacional',
        max_length=50,
        blank=True,
        null=True
    )
    cuentsproveedorextranjera = models.CharField(
        label='Cuenta De proveedor Extranjero',
        max_length=50,
        blank=True,
        null=True
    )
    porcentajeigv = models.DecimalField(
        label='Porcentaje IGV',
        max_digits=18,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'configuracionplancuentas'


class Controlcontable(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    controlactivo = models.BooleanField(verbose_name='¿Control Activo?')
    mes = models.IntegerField(verbose_name='Mes')
    anhio = models.IntegerField(verbose_name='Año')
    ultimodiario = models.CharField(label='Último Diario', max_length=20, blank=True, null=True)
    dolarizado = models.BooleanField(verbose_name='¿Dolarizado?')
    tipocambiodolar = models.DecimalField(label='Tipo Cambio De Dolar', max_digits=5, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')
    usuariogeneradosis = models.ForeignKey(
        erpp.cita.models.Usuarioweb,
        on_delete=models.CASCADE,
        verbose_name='UsuarioGeneradoSiS',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'controlcontable'


class Correntistas(models.Model):
    correlativo = models.AutoField(label='Correlativo', primary_key=True)
    id = models.AutoField(label='ID', primary_key=True)
    nombre = models.CharField(label='Nombre', max_length=200)
    identificador = models.CharField(label='Identificador', max_length=100)
    tipo = models.CharField(label='Tipo', max_length=10)

    class Meta:
        db_table = 'correntistas'


class Cuentasbancos(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    codigobanco = models.CharField(label='Código De Banco', max_length=20)
    maestrobanco = models.ForeignKey(
        erpp.gen.models.Maestrobancos,
        on_delete=models.CASCADE,
        verbose_name='MaestroBancos'
    )
    numerocuenta = models.CharField(label='Número De Cuenta', max_length=20, blank=True, null=True)
    moneda = models.CharField(label='Moneda', max_length=10)
    maestromoneda = models.ForeignKey(
        erpp.gen.models.Maestromoneda,
        on_delete=models.CASCADE,
        verbose_name='MaestroMoneda'
    )
    codigocuentacontable = models.CharField(label='Código De Cuenta Contable', max_length=20)
    plandecuentas = models.ForeignKey(Plandecuentas, on_delete=models.CASCADE, verbose_name='PlanDeCuentas')
    numerofijocheque = models.CharField(label='Número Fijo Cheque', max_length=100, blank=True, null=True)
    correlativocheque = models.IntegerField(verbose_name='Correlativo Cheque')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'cuentasbancos'


class Cuentaslibrescheques(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    codigocuenta = models.CharField(label='Código De Cuenta', max_length=20, blank=True, null=True)
    plandecuentas = models.ForeignKey(Plandecuentas, on_delete=models.CASCADE, verbose_name='PlanDeCuentas')
    pideproveedor = models.BooleanField(verbose_name='¿Pide Proveedor?')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'cuentaslibrescheques'


class Distribucioncentrocostocabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas',
        blank=True,
        null=True
    )
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20, blank=True, null=True)
    codigodistribucioncentrocosto = models.CharField(
        label='Código Distribución Centro Costo',
        max_length=20,
        blank=True,
        null=True
    )
    descripcion = models.CharField(label='Descripción', max_length=100, blank=True, null=True)
    porcentaje = models.BooleanField(verbose_name='¿Porcentaje?', blank=True, null=True)
    total = models.DecimalField(label='Total', max_digits=5, decimal_places=2, blank=True, null=True)
    totalimporte = models.DecimalField(label='Total De Importe', max_digits=8, decimal_places=2, blank=True, null=True)
    estadodcc = models.CharField(label='Estado De Cuenta Contable', max_length=20, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')
    codigocuentacontable = models.CharField(label='Código Cuenta Contable', max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'distribucioncentrocostocabecera'


class Distribucioncentrocostodetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas',
        blank=True,
        null=True
    )
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20, blank=True, null=True)
    distribucioncentrocostoscabecera = models.ForeignKey(
        Distribucioncentrocostocabecera,
        on_delete=models.CASCADE,
        verbose_name='DistribucionCentroCostosCabecera',
        blank=True,
        null=True
    )
    codigodistribucioncentrocosto = models.CharField(
        label='Código Distribución Centro Costo',
        max_length=20,
        blank=True,
        null=True
    )
    maestrocentrosdecostos = models.ForeignKey(
        erpp.gen.models.Maestrocentrosdecostos,
        on_delete=models.CASCADE,
        verbose_name='MaestroCentrosDeCostos',
        blank=True,
        null=True
    )
    codigocentrocosto = models.CharField(label='Código Centro Costo', max_length=20, blank=True, null=True)
    porcentaje = models.DecimalField(label='Porcentaje', max_digits=5, decimal_places=2, blank=True, null=True)
    valor = models.DecimalField(label='Valor', max_digits=8, decimal_places=2, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36, blank=True, null=True)
    fechacreacion = models.DateTimeField(label='Fecha De Creación', blank=True, null=True)
    accion = models.CharField(label='Acción', max_length=20, blank=True, null=True)
    autorizado = models.CharField(label='Autorizado', max_length=80, blank=True, null=True)
    estado = models.IntegerField(verbose_name='Estado', blank=True, null=True)
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)

    class Meta:
        db_table = 'distribucioncentrocostodetalle'


class Estadoperdidaganaciacabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    anhio = models.IntegerField(verbose_name='Año')
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20)
    posicion = models.IntegerField(verbose_name='Posición')
    linea = models.IntegerField(verbose_name='Línea')
    signo = models.IntegerField(verbose_name='Signo')
    titulodetalle = models.CharField(label='Título Detalle', max_length=250, blank=True, null=True)
    titulogeneral = models.CharField(label='Título General', max_length=250, blank=True, null=True)
    titulototal = models.CharField(label='Título Total', max_length=250, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'estadoperdidaganaciacabecera'


class Estadoperdidaganaciadetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    estadoperdidasgananciacabecera = models.ForeignKey(
        Estadoperdidaganaciacabecera,
        on_delete=models.CASCADE,
        verbose_name='EstadoPerdidasGananciaCabecera',
        blank=True,
        null=True
    )
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20)
    posicion = models.IntegerField(verbose_name='Posición')
    linea = models.IntegerField(verbose_name='Línea')
    cuenta = models.CharField(label='Cuenta', max_length=250, blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'estadoperdidaganaciadetalle'


class Flujosdeefectivocabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    anhio = models.IntegerField(verbose_name='Año')
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20)
    posicion = models.IntegerField(verbose_name='Posición')
    linea = models.IntegerField(verbose_name='Línea')
    signo = models.IntegerField(verbose_name='Signo')
    titulodetalle = models.CharField(label='Título Detalle', max_length=250)
    titulogeneral = models.CharField(label='Título General', max_length=250)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'flujosdeefectivocabecera'


class Flujosdeefectivodetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    cabecera = models.ForeignKey(Flujosdeefectivocabecera, on_delete=models.CASCADE, verbose_name='Cabecera')
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20)
    posicion = models.IntegerField(verbose_name='Posición')
    linea = models.IntegerField(verbose_name='Línea')
    cuenta = models.CharField(label='Cuenta', max_length=250)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'flujosdeefectivodetalle'


class Licenciaconducirpersonal(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestropersonal = models.ForeignKey(
        erpp.per.models.Maestropersonal,
        on_delete=models.CASCADE,
        verbose_name='MaestroPersonal'
    )
    numbrevete = models.CharField(label='Número Del Brevete', max_length=500, blank=True, null=True)
    tipo = models.CharField(label='Tipo', max_length=50, blank=True, null=True)
    fechaemision = models.DateField(label='Fecha De Emisión', blank=True, null=True)
    fechavencimiento = models.DateField(label='Fecha De Vencimiento', blank=True, null=True)
    fechaemisionpermiso1 = models.DateField(label='Fecha De Emisión Permiso 1', blank=True, null=True)
    fechaemisionpermiso2 = models.DateField(label='Fecha De Emisión Permiso 2', blank=True, null=True)
    fechaemisionpermiso3 = models.DateField(label='Fecha De Emisión Permiso 3', blank=True, null=True)
    fechacesepermiso1 = models.DateField(label='Fecha De Cese Permiso 1', blank=True, null=True)
    fechacesepermiso2 = models.DateField(label='Fecha De Cese Permiso 2', blank=True, null=True)
    fechacesepermiso3 = models.DateField(label='Fecha De Cese Permiso 3', blank=True, null=True)
    fechacreacion = models.DateField(label='Fecha De Creación')
    estado = models.CharField(label='Estado', max_length=10)
    activo = models.BooleanField(verbose_name='¿Activo?')
    usuario = models.CharField(label='Usuario', max_length=36)

    class Meta:
        db_table = 'licenciaconducirpersonal'


class Lugarbal8Column(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigo = models.CharField(label='Codigo', max_length=4, blank=True, null=True)
    descripcion = models.CharField(label='Descripción', max_length=250, blank=True, null=True)
    usuarioid = models.IntegerField(verbose_name='UsuarioID', blank=True, null=True)
    fecharhoraregistro = models.DateTimeField(label='Fecha y Hora De Registro', blank=True, null=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas',
        blank=True,
        null=True
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal',
        blank=True,
        null=True
    )
    activo = models.BooleanField(verbose_name='¿Activo?', blank=True, null=True)
    estado = models.IntegerField(verbose_name='Estado', blank=True, null=True)

    class Meta:
        db_table = 'lugarbal8column'


class Maestroaccionnotadecredito(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigoaccion = models.IntegerField(verbose_name='Código De Acción')
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    descripcion = models.CharField(label='Descripción', max_length=200)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    activo = models.BooleanField(verbose_name='¿Activo?')
    cuentacontable = models.CharField(label='Cuenta Contable', max_length=20)

    class Meta:
        db_table = 'maestroaccionnotadecredito'


class Maestroactivosfijos(models.Model):
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
    codigoempresa = models.CharField(label='Código De Empresa', max_length=20)
    tipoactivo = models.CharField(label='Tipo Activo', max_length=20)
    codigoactivo = models.CharField(label='Código Activo', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    fechacompra = models.DateTimeField(label='Fecha De Compra')
    ajustadosoles = models.DecimalField(label='Ajustado En Soles', max_digits=11, decimal_places=2)
    costocomprasoles = models.DecimalField(label='Costo De Compra En Soles', max_digits=11, decimal_places=2)
    retirossoles = models.DecimalField(label='Retiros En Soles', max_digits=11, decimal_places=2)
    adicionessoles = models.DecimalField(label='Adiciones En Soles', max_digits=11, decimal_places=2)
    tipocambio = models.DecimalField(label='Tipo De Cambio', max_digits=13, decimal_places=4)
    maestrotipocambio = models.ForeignKey(
        erpp.gen.models.Maestrotipodecambio,
        on_delete=models.CASCADE,
        verbose_name='MaestroTipoCambio'
    )
    ajustadodolares = models.DecimalField(label='Ajustado Dólares', max_digits=13, decimal_places=4)
    costocompradolares = models.DecimalField(label='Costo De Compra DÓlares', max_digits=13, decimal_places=4)
    retirosdolares = models.DecimalField(label='Retiros De Dólares', max_digits=13, decimal_places=4)
    adicionesdolares = models.DecimalField(label='Adiciones Dólares', max_digits=13, decimal_places=4)
    montodepreciacionsoles = models.DecimalField(
        label='Monto De Depreciación En Soles',
        max_digits=11,
        decimal_places=2
    )
    fechaultimadepreciacion = models.DateTimeField(label='Fecha De Última Depreciación')
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'maestroactivosfijos'
        unique_together = (('codigoactivo', 'idmaestroempresas', 'tipoactivo'),)


class Maestrobienes(models.Model):
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
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'maestrobienes'


class Maestromotivoanulacionnotadecredito(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    codigomotivo = models.IntegerField(verbose_name='CodigoMotivo')
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrosucursal = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursal'
    )
    descripcion = models.CharField(label='Descripción', max_length=200)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'maestromotivoanulacionnotadecredito'


class Maestrotipobaja(models.Model):
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
    codigotipobaja = models.CharField(label='Código Tipo De Baja', max_length=20)
    clasetabla = models.CharField(label='Clase Tabla', max_length=5)
    descripcion = models.CharField(label='Descripción', max_length=30)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'maestrotipobaja'


class Maestrotipodediario(models.Model):
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
    tipodiario = models.CharField(label='Tipo De Diario', max_length=20)
    descripcion = models.CharField(label='Descripción', max_length=60)
    tipodolar = models.CharField(label='Tipo De Dólar', max_length=20)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')
    sunattipolibro = models.IntegerField(verbose_name='Sunat Tipo De Libro', blank=True, null=True)

    class Meta:
        db_table = 'maestrotipodediario'
        unique_together = (('idmaestroempresas', 'tipodiario'),)


class Mayor(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    codigoempresa = models.IntegerField(verbose_name='Código De Empresa')
    plandecuentas = models.ForeignKey(
        Plandecuentas,
        on_delete=models.CASCADE,
        verbose_name='PlanDeCuentas',
        blank=True,
        null=True
    )
    codigocuenta = models.CharField(label='Código De Cuenta', max_length=20)
    anhio = models.IntegerField(verbose_name='Año')
    aperturadebesoles = models.FloatField(verbose_name='Apertura que Debe En Soles', blank=True, null=True)
    aperturahabersoles = models.FloatField(verbose_name='Apertura que Hay En Soles', blank=True, null=True)
    enerodebesoles = models.FloatField(verbose_name='Para Enero Se Debe En Soles', blank=True, null=True)
    enerohabersoles = models.FloatField(verbose_name='Para Enero Hay En Soles', blank=True, null=True)
    febrerodebesoles = models.FloatField(verbose_name='Para Febrero Se Debe En Soles', blank=True, null=True)
    febrerohabersoles = models.FloatField(verbose_name='Para Febrero Hay En Soles', blank=True, null=True)
    marzodebesoles = models.FloatField(verbose_name='Para Marzo Se Debe En Soles', blank=True, null=True)
    marzohabersoles = models.FloatField(verbose_name='Para Marzo Hay En Soles', blank=True, null=True)
    abrildebesoles = models.FloatField(verbose_name='Para Abril Se Debe En Soles', blank=True, null=True)
    abrilhabersoles = models.FloatField(verbose_name='Para Abril Hay En Soles', blank=True, null=True)
    mayodebesoles = models.FloatField(verbose_name='Para Mayo Se Debe En Soles', blank=True, null=True)
    mayohabersoles = models.FloatField(verbose_name='Para Mayo Hay En Soles', blank=True, null=True)
    juniodebesoles = models.FloatField(verbose_name='Para Junio Se Debe En Soles', blank=True, null=True)
    juniohabersoles = models.FloatField(verbose_name='Para Junio Hay En Soles', blank=True, null=True)
    juliodebesoles = models.FloatField(verbose_name='Para Julio Se Debe En Soles', blank=True, null=True)
    juliohabersoles = models.FloatField(verbose_name='Para Julio Hay En Soles', blank=True, null=True)
    agostodebesoles = models.FloatField(verbose_name='Para Agosto Se Debe En Soles', blank=True, null=True)
    agostohabersoles = models.FloatField(verbose_name='Para Agosto Hay En Soles', blank=True, null=True)
    setiembredebesoles = models.FloatField(verbose_name='Para Setiembre Se Debe En Soles', blank=True, null=True)
    setiembrehabersoles = models.FloatField(verbose_name='Para Setiembre Hay En Soles', blank=True, null=True)
    octubredebesoles = models.FloatField(verbose_name='Para Octubre Se Debe En Soles', blank=True, null=True)
    octubrehabersoles = models.FloatField(verbose_name='Para Octubre Hay En Soles', blank=True, null=True)
    noviembredebesoles = models.FloatField(verbose_name='Para Noviembre Se Debe En Soles', blank=True, null=True)
    noviembrehabersoles = models.FloatField(verbose_name='Para Noviembre Hay En Soles', blank=True, null=True)
    diciembredebesoles = models.FloatField(verbose_name='Para Diciembre Se Debe En Soles', blank=True, null=True)
    diciembrehabersoles = models.FloatField(verbose_name='Para Diciembre Hay En Soles', blank=True, null=True)
    aperturadebedolares = models.FloatField(verbose_name='Apertura Se Debe En Dólares', blank=True, null=True)
    aperturahaberdolares = models.FloatField(verbose_name='Apertura Hay En Dólares', blank=True, null=True)
    enerodebedolares = models.FloatField(verbose_name='Para Enero Se Debe En Dólares', blank=True, null=True)
    enerohaberdolares = models.FloatField(verbose_name='Para Enero Hay En Dólares', blank=True, null=True)
    febrerodebedolares = models.FloatField(verbose_name='Para Febrero Se Debe En Dólares', blank=True, null=True)
    febrerohaberdolares = models.FloatField(verbose_name='Para Febrero Hay En Dólares', blank=True, null=True)
    marzodebedolares = models.FloatField(verbose_name='Para Marzo Se Debe En Dólares', blank=True, null=True)
    marzohaberdolares = models.FloatField(verbose_name='Para Marzo Hay En Dólares', blank=True, null=True)
    abrildebedolares = models.FloatField(verbose_name='Para Abril Se Debe En Dólares', blank=True, null=True)
    abrilhaberdolares = models.FloatField(verbose_name='Para Abril Hay En Dólares', blank=True, null=True)
    mayodebedolares = models.FloatField(verbose_name='Para Mayo Se Debe En Dólares', blank=True, null=True)
    mayohaberdolares = models.FloatField(verbose_name='Para Mayo Hay En Dólares', blank=True, null=True)
    juniodebedolares = models.FloatField(verbose_name='Para Junio Se Debe En Dólares', blank=True, null=True)
    juniohaberdolares = models.FloatField(verbose_name='Para Junio Hay En Dólares', blank=True, null=True)
    juliodebedolares = models.FloatField(verbose_name='Para Julio Se Debe En Dólares', blank=True, null=True)
    juliohaberdolares = models.FloatField(verbose_name='Para Julio Hay En Dólares', blank=True, null=True)
    agostodebedolares = models.FloatField(verbose_name='Para Agosto Se Debe En Dólares', blank=True, null=True)
    agostohaberdolares = models.FloatField(verbose_name='Para Agosto Hay En Dólares', blank=True, null=True)
    setiembredebedolares = models.FloatField(verbose_name='Para Setiembre Se Debe En Dólares', blank=True, null=True)
    setiembrehaberdolares = models.FloatField(verbose_name='Para Setiembre Hay En Dólares', blank=True, null=True)
    octubredebedolares = models.FloatField(verbose_name='Para Octubre Se Debe En Dólares', blank=True, null=True)
    octubrehaberdolares = models.FloatField(verbose_name='Para Octubre Hay En Dólares', blank=True, null=True)
    noviembredebedolares = models.FloatField(verbose_name='Para Noviembre Se Debe En Dólares', blank=True, null=True)
    noviembrehaberdolares = models.FloatField(verbose_name='Para Noviembre Hay En Dólares', blank=True, null=True)
    diciembredebedolares = models.FloatField(verbose_name='Para Diciembre Se Debe En Dólares', blank=True, null=True)
    diciembrehaberdolares = models.FloatField(verbose_name='Para Diciembre Hay En Dólares', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'mayor'


class Meses(models.Model):
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
    meses = models.IntegerField(verbose_name='Meses')
    anno = models.IntegerField(verbose_name='Año')
    descripcion = models.CharField(label='Descripción', max_length=200)
    cerro = models.BooleanField(verbose_name='Cerró')
    modifico = models.BooleanField(verbose_name='Modificó')
    mesreal = models.IntegerField(verbose_name='Mes Real')
    anioreal = models.IntegerField(verbose_name='Año Real')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'meses'


class Notascreditocabecera(models.Model):
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
    numeroseriec = models.CharField(label='Número De Serie De La Cabecera', max_length=20)
    numerodocumentoc = models.CharField(label='Número De Documento De La Cabecera', max_length=20)
    maestrocliente = models.ForeignKey(
        erpp.fac.models.Maestroclientes,
        on_delete=models.CASCADE,
        verbose_name='MaestroClientes'
    )
    codigocliente = models.CharField(label='Código Del Cliente', max_length=20)
    concepto = models.CharField(label='Concepto', max_length=200)
    precioventasoles = models.DecimalField(label='Precio De Venta En Soles', max_digits=11, decimal_places=2)
    valorventasoles = models.DecimalField(label='Valor De Venta En Soles', max_digits=11, decimal_places=2)
    precioventadolares = models.DecimalField(label='Precio De Venta En Dólares', max_digits=13, decimal_places=4)
    valorventadolares = models.DecimalField(label='Valor De Venta En Dólares', max_digits=13, decimal_places=4)
    igv = models.DecimalField(label='IGV', max_digits=5, decimal_places=2)
    recepciona = models.CharField(label='Recepciona', max_length=100)
    fechaemision = models.DateTimeField(label='Fecha De Emision')
    fecharecepcionado = models.DateTimeField(label='Fecha De Recepcionado')
    maestroalmacen = models.ForeignKey(
        erpp.gen.models.Maestroalmacenes,
        on_delete=models.CASCADE,
        verbose_name='MaestroAlmacenes'
    )
    codigoalmacen = models.CharField(label='Código Del Almacen', max_length=20)
    codigosucursal = models.CharField(label='Código De La Sucursal', max_length=20)
    facturaclientecabecera = models.ForeignKey(
        erpp.fac.models.Facturaclientecabecera,
        on_delete=models.CASCADE,
        verbose_name='FacturaClienteCabecera'
    )
    numeroseriefb = models.CharField(label='Número De Serie Factura/Boleta', max_length=20)
    numerodocumentofb = models.CharField(label='Número De Documento Factura/Boleta', max_length=20)
    numerooperacion = models.CharField(label='Número De Operación', unique=True, max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'notascreditocabecera'


class Notascreditodetalle(models.Model):
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
    notacreditocabecera = models.ForeignKey(
        Notascreditocabecera,
        on_delete=models.CASCADE,
        verbose_name='NotaCreditoCabecera'
    )
    numeroseriec = models.CharField(label='Número De Serie Crédito', max_length=20)
    numerodocumentoc = models.CharField(label='Número Documento De Crédito', max_length=20)
    maestroalmacen = models.ForeignKey(
        erpp.gen.models.Maestroalmacenes,
        on_delete=models.CASCADE,
        verbose_name='MaestroAlmacen'
    )
    codigoalmacen = models.CharField(label='Código Del Almacen', max_length=20)
    codigosucursal = models.CharField(label='Código De La Sucursal', max_length=20)
    maestroproducto = models.ForeignKey(
        erpp.inv.models.Maestroproductos,
        on_delete=models.CASCADE,
        verbose_name='MaestroProducto'
    )
    codigoproducto = models.CharField(label='Código Del Producto', max_length=20)
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    preciounitariosoles = models.DecimalField(label='Precio Unitario En Soles', max_digits=11, decimal_places=2)
    preciounitariodolares = models.DecimalField(label='Precio Unitario En Dólares', max_digits=13, decimal_places=4)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'notascreditodetalle'


class Notasdebito(models.Model):
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
    numeroseried = models.CharField(label='Número De Serie De Débito', max_length=20)
    numerodocumentod = models.CharField(label='Número De Documento De Débito', max_length=20)
    maestrocliente = models.ForeignKey(
        erpp.fac.models.Maestroclientes,
        on_delete=models.CASCADE,
        verbose_name='MaestroClientes'
    )
    codigocliente = models.CharField(label='Código Del Cliente', max_length=20)
    concepto = models.CharField(label='Concepto', max_length=200)
    precioventasoles = models.DecimalField(label='Precio De Venta En Soles', max_digits=11, decimal_places=2)
    valorventasoles = models.DecimalField(label='Valor De Venta En Soles', max_digits=11, decimal_places=2)
    precioventadolares = models.DecimalField(label='Precio De Venta En Dólares', max_digits=13, decimal_places=4)
    valorventadolares = models.DecimalField(label='Valor De Venta En Dólares', max_digits=13, decimal_places=4)
    igv = models.DecimalField(label='IGV', max_digits=18, decimal_places=2)
    recepciona = models.CharField(label='Recepciona', max_length=100)
    fechaemision = models.DateTimeField(label='Fecha De Emisión')
    fecharecepcionado = models.DateTimeField(label='Fecha De Recepcionado', blank=True, null=True)
    codigoalmacen = models.CharField(label='Código Del Almacen', max_length=20)
    codigosucursal = models.CharField(label='Código De La Sucursal', max_length=20)
    facturaclientecabecera = models.ForeignKey(
        erpp.fac.models.Facturaclientecabecera,
        on_delete=models.CASCADE,
        verbose_name='FacturaClienteCabecera'
    )
    numeroseriefb = models.CharField(label='Número De Serie Factura/Boleta', max_length=5)
    numerodocumentofb = models.CharField(label='Número De Documento Factura/Boleta', max_length=20)
    numerooperacion = models.CharField(label='Número De La Operación', max_length=20)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'notasdebito'


class Numerocorrelativoc(models.Model):
    id = models.AutoField(label='ID', primary_key=True, blank=True, null=True)
    numerooperacion = models.FloatField(verbose_name='Número De Operación', blank=True, null=True)
    id1 = models.FloatField(verbose_name='ID1', blank=True, null=True)
    nrocomprobante = models.FloatField(verbose_name='Número De Comprobante', blank=True, null=True)

    class Meta:
        db_table = 'numerocorrelativoc'


class Numerosdocumentos(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    maestrotipodocumento = models.ForeignKey(
        erpp.gen.models.Maestrotiposdocumentos,
        on_delete=models.CASCADE,
        verbose_name='MaestroTipoDocumento'
    )
    codigotipodocumento = models.CharField(label='Código Del Tipo De Documento', max_length=20, blank=True, null=True)
    maestrocajero = models.ForeignKey(
        erpp.fac.models.Maestrocajeros,
        on_delete=models.CASCADE,
        verbose_name='MaestroCajero'
    )
    codigocajero = models.CharField(label='Código Del Cajero', max_length=20)
    serie = models.CharField(label='Serie', max_length=20)
    correlativo = models.CharField(label='Correlativo', max_length=20)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechamodificacion = models.DateTimeField(label='Fecha De Modificación')
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'numerosdocumentos'


class Observaciondocumento(models.Model):
    id = models.IntegerField(verbose_name='ID', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas',
        blank=True,
        null=True
    )
    observacionordenpedido = models.TextField(label='Observación De Orden/Pedido', blank=True, null=True)
    observacioncotizacion = models.TextField(label='Observación De Cotización', blank=True, null=True)
    observacionfactura = models.TextField(label='Observación De Factura', blank=True, null=True)
    observacionordentrabajo = models.TextField(label='Observación De Orden/Trabajo', blank=True, null=True)

    class Meta:
        db_table = 'observaciondocumento'


class Pagos4Tacategoria(models.Model):
    id = models.IntegerField(verbose_name='Id', primary_key=True)
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    anhio = models.IntegerField(verbose_name='Año')
    mes = models.CharField(label='Mes', max_length=20)
    cancelada = models.BooleanField(verbose_name='¿Cancelada?', blank=True, null=True)
    contabilizada = models.BooleanField(verbose_name='¿Contabilizada?', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    activo = models.BooleanField(verbose_name='¿Activo?')
    estado = models.IntegerField(verbose_name='Estado', blank=True, null=True)
    tipoproveedor = models.ForeignKey(
        erpp.cmp.models.Maestrotipoproveedores,
        on_delete=models.CASCADE,
        verbose_name='IdTipoProveedor',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'pagos4tacategoria'


class Pagos4Tacategoriadetalle(models.Model):
    id = models.IntegerField(verbose_name='Id', primary_key=True)
    pagos4tacategoria = models.ForeignKey(Pagos4Tacategoria, on_delete=models.CASCADE, verbose_name='Pagos4taCategoria')
    maestroproveedores = models.ForeignKey(
        erpp.gen.models.Maestroproveedores,
        on_delete=models.CASCADE,
        verbose_name='MaestroProveedores'
    )
    monto = models.DecimalField(label='Monto', max_digits=14, decimal_places=2)
    cancelado = models.DecimalField(label='Cancelado', max_digits=14, decimal_places=2, blank=True, null=True)
    contabilizada = models.BooleanField(verbose_name='¿Contabilizada?', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    activo = models.BooleanField(verbose_name='¿Activo?')
    estado = models.IntegerField(verbose_name='Estado', blank=True, null=True)
    tipoproveedor = models.ForeignKey(
        erpp.cmp.models.Maestrotipoproveedores,
        on_delete=models.CASCADE,
        verbose_name='TipoProveedor',
        blank=True,
        null=True
    )
    bonificacion1 = models.DecimalField(label='Bonificación 1', max_digits=18, decimal_places=4, blank=True, null=True)
    bonificacion2 = models.DecimalField(label='Bonificación 2', max_digits=18, decimal_places=4, blank=True, null=True)
    horas = models.DecimalField(label='Horas', max_digits=18, decimal_places=2, blank=True, null=True)
    descuentos = models.DecimalField(label='Descuentos', max_digits=18, decimal_places=2, blank=True, null=True)
    bonificaciongrado = models.DecimalField(
        label='Grado De Bonificación',
        max_digits=18,
        decimal_places=2,
        blank=True,
        null=True
    )
    grado = models.IntegerField(verbose_name='Grado', blank=True, null=True)
    sinrecibo = models.BooleanField(verbose_name='¿Sin Recibo?', blank=True, null=True)
    remuneracion = models.DecimalField(label='Remuneración', max_digits=11, decimal_places=2, blank=True, null=True)
    diasfalta = models.IntegerField(verbose_name='Días De Falta', blank=True, null=True)
    descuentodiasfalta = models.DecimalField(
        label='Descuento Por Días De Falta',
        max_digits=18,
        decimal_places=2,
        blank=True,
        null=True
    )
    descuentootrasfaltas = models.DecimalField(
        label='Descuento Por Otras Faltas',
        max_digits=18,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'pagos4tacategoriadetalle'


class TiposDeDocumentos(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    tipdoc_codigo = models.CharField(label='Tipo C De Código', max_length=2)
    tipdoc_descripcion = models.CharField(label='Tipo C De Descripción', max_length=25, blank=True, null=True)
    tipdoc_sunat = models.CharField(label='Tipo C SUNAT', max_length=2, blank=True, null=True)
    tipdoc_resta = models.BooleanField(verbose_name='Tipo C Resta')
    tipdoc_referencia = models.BooleanField(verbose_name='Tipo C Referencia')
    tipdoc_file = models.CharField(label='Tipo C File', max_length=8, blank=True, null=True)
    tipdoc_fechavto = models.BooleanField(verbose_name='Tipo C Fecha VTO')
    tipo_equi = models.CharField(label='Tipo equivo', max_length=3, blank=True, null=True)
    tipdoc_fechavto_vta = models.BooleanField(verbose_name='Tipo C Fecha VTO VTA', blank=True, null=True)

    class Meta:
        db_table = 'tipos_de_documentos'


class Unidadimpositivatributaria(models.Model):
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
    anhio = models.IntegerField(verbose_name='Año')
    valor = models.DecimalField(label='Valor', max_digits=11, decimal_places=2)
    baselegal = models.CharField(label='Base Legal', max_length=20)
    observacion = models.CharField(label='Observación', max_length=200)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'unidadimpositivatributaria'


class Valecabecera(models.Model):
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
    trabajador = models.ForeignKey(erpp.per.models.Maestropersonal, on_delete=models.CASCADE, verbose_name='Trabajador')
    idautorizadopor = models.IntegerField(verbose_name='Autorizado Por')
    recogido = models.BooleanField(verbose_name='¿Recogido?')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')
    pedido = models.ForeignKey(
        erpp.inv.models.Pedidocabecera,
        on_delete=models.CASCADE,
        verbose_name='Pedido',
        blank=True,
        null=True
    )
    codigo = models.CharField(label='Código', max_length=20, blank=True, null=True)
    almacen = models.ForeignKey(
        erpp.gen.models.Maestroalmacenes,
        on_delete=models.CASCADE,
        verbose_name='Almacen',
        blank=True,
        null=True
    )
    codcliente = models.CharField(label='Código Del Cliente', max_length=50, blank=True, null=True)
    docreferencia = models.ForeignKey(
        erpp.per.models.Maestrodocumentoidentidad,
        on_delete=models.CASCADE,
        verbose_name='DocReferencia',
        blank=True,
        null=True
    )
    seriereferencia = models.CharField(label='Serie De Referencia', max_length=50, blank=True, null=True)
    numeroreferencia = models.CharField(label='Número De Referencia', max_length=50, blank=True, null=True)
    entregacompleta = models.BooleanField(verbose_name='¿Entrega Completa?', blank=True, null=True)
    costocero = models.BooleanField(verbose_name='Costo Cero', blank=True, null=True)

    class Meta:
        db_table = 'valecabecera'


class Valedetalle(models.Model):
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
    valecabecera = models.ForeignKey(Valecabecera, on_delete=models.CASCADE, verbose_name='ValeCabecera')
    maestroproducto = models.ForeignKey(
        erpp.inv.models.Maestroproductos,
        on_delete=models.CASCADE,
        verbose_name='MaestroProducto'
    )
    cantidad = models.DecimalField(label='Cantidad', max_digits=12, decimal_places=5)
    maestrocentrodecostos = models.ForeignKey(
        erpp.gen.models.Maestrocentrosdecostos,
        on_delete=models.CASCADE,
        verbose_name='MaestroCentroDeCostos'
    )
    maestroalmacen = models.ForeignKey(
        erpp.gen.models.Maestroalmacenes,
        on_delete=models.CASCADE,
        verbose_name='MaestroAlmacen'
    )
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')
    motivo = models.CharField(label='Motivo', max_length=500, blank=True, null=True)
    cantidadrecojida = models.IntegerField(verbose_name='Cantidad Recojida', blank=True, null=True)

    class Meta:
        db_table = 'valedetalle'


class Vehiculomarca(models.Model):
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
    codigomarca = models.CharField(label='Código De La Marca', max_length=20)
    nombremarca = models.CharField(label='Nombre De La Marca', max_length=30)
    mostrarencita = models.BooleanField(verbose_name='¿Mostrar En Cita?', blank=True, null=True)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'vehiculomarca'


class Vehiculomarcalogo(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    logomarca = models.BinaryField(label='Logo De La Marca')
    nombremarca = models.CharField(label='Nombre De La Marca', max_length=30, blank=True, null=True)
    maestromarca = models.ForeignKey(
        erpp.marca.models.Marcaciondetalle,
        on_delete=models.CASCADE,
        verbose_name='MaestroMarca'
    )

    class Meta:
        db_table = 'vehiculomarcalogo'


class Vehiculomodelo(models.Model):
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
    vehiculomarca = models.ForeignKey(Vehiculomarca, on_delete=models.CASCADE, verbose_name='VehiculoMarca')
    codigomodelo = models.CharField(label='Código Del Modelo', max_length=200)
    nombremodelo = models.CharField(label='Nombre Del Modelo', max_length=100)
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')

    class Meta:
        db_table = 'vehiculomodelo'


class Vouchercabecera(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    codempresa = models.CharField(label='Código De La Empresa', max_length=20)
    nrocomprobante = models.IntegerField(verbose_name='NroComprobante')
    tipodiario = models.CharField(label='Tipo De Diario', max_length=20)
    anhio = models.IntegerField(verbose_name='Año')
    mes = models.IntegerField(verbose_name='Mes')
    fecha = models.DateTimeField(label='Fecha')
    glosa = models.TextField(label='Glosa')
    totaldebesoles = models.DecimalField(label='Total Se Debe En Soles', max_digits=11, decimal_places=2)
    totalhabersoles = models.DecimalField(label='Total Hay En Soles', max_digits=11, decimal_places=2)
    totaldebedolares = models.DecimalField(label='Total Se Debe En Dólares', max_digits=13, decimal_places=4)
    totalhaberdolares = models.DecimalField(label='Total Hay En Dólares', max_digits=13, decimal_places=4)
    tipodecambio = models.DecimalField(label='Tipo De Cambio', max_digits=13, decimal_places=4)
    itemsrelacionados = models.IntegerField(verbose_name='Ítems Relacionados')
    codproveedor = models.CharField(label='Código Del Proveedor', max_length=20)
    tipodocsunat = models.ForeignKey(TiposDeDocumentos, on_delete=models.CASCADE, verbose_name='TipoDocSunat')
    nrofactura = models.CharField(label='Número De La Factura', max_length=20)
    seriefactura = models.CharField(label='Serie De La Factura', max_length=20, blank=True, null=True)
    tipooperacion = models.IntegerField(verbose_name='Tipo De Operación')
    fechadoc = models.DateTimeField(label='Fecha Del Documento')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')
    tipoigv = models.CharField(label='Tipo Igv', max_length=50, blank=True, null=True)
    procedencia = models.IntegerField(verbose_name='Procedencia', blank=True, null=True)

    class Meta:
        db_table = 'vouchercabecera'


class Voucherdetalle(models.Model):
    id = models.AutoField(label='ID', primary_key=True)
    voucher = models.ForeignKey(Vouchercabecera, on_delete=models.CASCADE, verbose_name='Voucher')
    maestrosucursales = models.ForeignKey(
        erpp.gen.models.Maestrosucursales,
        on_delete=models.CASCADE,
        verbose_name='MaestroSucursales'
    )
    maestroempresas = models.ForeignKey(
        erpp.gen.models.Maestroempresas,
        on_delete=models.CASCADE,
        verbose_name='MaestroEmpresas'
    )
    codempresa = models.CharField(label='Código De Empresa', max_length=20)
    nrocomprobante = models.IntegerField(verbose_name='Número Del Comprobante')
    tipodiario = models.CharField(label='Tipo De Diario', max_length=20)
    nroitem = models.IntegerField(verbose_name='Número De Ítem')
    nroitempadre = models.IntegerField(verbose_name='Número De Ítem Padre', blank=True, null=True)
    anhio = models.IntegerField(verbose_name='Año')
    mes = models.IntegerField(verbose_name='Mes')
    codcuenta = models.CharField(label='Código Cuenta', max_length=20)
    item1 = models.IntegerField(verbose_name='Ítem 1')
    item2 = models.IntegerField(verbose_name='Ítem 2')
    tipocorrentista = models.CharField(label='Tipo Correntista', max_length=20)
    codcuentacorriente = models.CharField(label='Código De Cuenta Corriente', max_length=20)
    codcentrodecostos = models.CharField(label='Código De Centro De Costos', max_length=20)
    tipodocsunat = models.ForeignKey(
        erpp.gen.models.Maestrodocumentossunat,
        on_delete=models.CASCADE,
        verbose_name='TipoDocSunat'
    )
    nrodocumento = models.CharField(label='Número De Documento', max_length=20)
    fecha = models.DateTimeField(label='Fecha')
    debeohaber = models.BooleanField(verbose_name='¿Debe o Haber?')
    tipomoneda = models.CharField(label='Tipo De Moneda', max_length=30)
    tipomonedaid = models.ForeignKey(erpp.gen.models.Maestromoneda, on_delete=models.CASCADE, verbose_name='TipoMoneda')
    linea = models.CharField(label='Línea', max_length=5)
    montodebesoles = models.DecimalField(label='Monto Se Debe En Soles', max_digits=11, decimal_places=2)
    montohabersoles = models.DecimalField(label='Monto Hay En Soles', max_digits=11, decimal_places=2)
    montodebedolares = models.DecimalField(label='Monto Se Debe En Dólares', max_digits=13, decimal_places=4)
    montohaberdolares = models.DecimalField(label='Monto Hay En Dólares', max_digits=13, decimal_places=4)
    cdda = models.CharField(label='CDDA', max_length=50)
    nrocheque = models.CharField(label='Número De Cheque', max_length=20)
    tipodocreferencia = models.ForeignKey(TiposDeDocumentos, on_delete=models.CASCADE, verbose_name='TipoDocReferencia')
    seriedocreferencia = models.CharField(label='Serie De Documento Referencia', max_length=20, blank=True, null=True)
    nrodocreferencia = models.CharField(label='Número De Documento Referencia', max_length=20)
    glosaii = models.TextField(label='Glosa II')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    fechamodificado = models.DateTimeField(label='Fecha De Modificación')
    accion = models.CharField(label='Acción', max_length=20)
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    activo = models.BooleanField(verbose_name='¿Activo?')
    distribucioncentrodecostocabecera = models.ForeignKey(
        Distribucioncentrocostocabecera,
        on_delete=models.CASCADE,
        verbose_name='DistribucionCentroDeCostoCabecera',
        blank=True,
        null=True
    )
    codigoproducto = models.CharField(label='Código Del Producto', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'voucherdetalle'


class Vouchernumeroreabierto(models.Model):
    id = models.AutoField(label='Id', primary_key=True)
    registro = models.ForeignKey(Vouchercabecera, on_delete=models.CASCADE, verbose_name='Registro')
    nrovoucher = models.IntegerField(verbose_name='Número Del Voucher')
    anhio = models.IntegerField(verbose_name='Año')
    mes = models.IntegerField(verbose_name='Mes')
    tipoprocedencia = models.CharField(label='Tipo De Procedencia', max_length=150)
    activo = models.BooleanField(verbose_name='¿Activo?')
    fechacreacion = models.DateTimeField(label='Fecha De Creación')
    accion = models.CharField(label='Acción', max_length=20)
    autorizado = models.CharField(label='Autorizado', max_length=80)
    estado = models.IntegerField(verbose_name='Estado')
    codigousuario = models.CharField(label='Código De Usuario', max_length=36)
    activoregistromaestro = models.BooleanField(verbose_name='¿Registro Maestro Activo?', blank=True, null=True)
    estadonumero = models.CharField(label='Estado Del Número', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'vouchernumeroreabierto'
