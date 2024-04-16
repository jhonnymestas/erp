from django import forms

from .models import Activosfijos, Amarrecabecera, Amarredetalle, \
    Balancecabecera, Balancedetalle, Cajacabecera, Cajachicacabecera, \
    Cajachicadetalle, Cierreanualcontable, Cierrecajafin, Configuracionplancuentas, \
    Controlcontable, Correntistas, Cuentasbancos, Cuentaslibrescheques, \
    Distribucioncentrocostocabecera, Distribucioncentrocostodetalle, \
    Estadoperdidaganaciacabecera, Estadoperdidaganaciadetalle, \
    Flujosdeefectivocabecera, Flujosdeefectivodetalle, Licenciaconducirpersonal, \
    Lugarbal8Column, Maestroaccionnotadecredito, Maestroactivosfijos, Maestrobienes, \
    Maestromotivoanulacionnotadecredito, Maestrotipobaja, Maestrotipodediario, Mayor, Meses, \
    Notascreditocabecera, Notascreditodetalle, Notasdebito, Numerocorrelativoc, Numerosdocumentos, \
    Observaciondocumento, Pagos4Tacategoria, Pagos4Tacategoriadetalle, Plandecuentas, TiposDeDocumentos, \
    Unidadimpositivatributaria, Valecabecera, Valedetalle, Vehiculomarca, Vehiculomarcalogo, Vehiculomodelo, \
    Vouchercabecera, Voucherdetalle, Vouchernumeroreabierto


class ActivosFijosForm(forms.ModelForm):
    class Meta:
        model = Activosfijos
        fields = ['id', 'codigo', 'cuentacontable', 'descripcion', 'marca', 'modelo', 'numeroplaca',
                  'saldoinicial', 'adquisiciones', 'mejoras', 'retirosbajas', 'ajustes', 'valorhistorico',
                  'ajusteinflacion', 'valorajustado', 'fechaadquisicion', 'fechainicio', 'metodo',
                  'nrodocumento', 'porcentajedepreciacion', 'depreciacionacumulada', 'depreciacionejercicio',
                  'depreciacionretiros', 'depreciacionotros', 'depreciacionhistorica', 'ajustedepreciacion',
                  'depreciacioninflacion', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class AmarrecabeceraForm(forms.ModelForm):
    class Meta:
        model = Amarrecabecera
        fields = ['id', 'idplandecuentas', 'descripcion', 'fechahoraregistro',
                  'activo', 'estado', 'uusarioid', 'idmaestroempresa',
                  'idmaestrosucursal']


class AmarredetalleForm(forms.ModelForm):
    class Meta:
        model = Amarredetalle
        fields = ['id', 'idamarrecabecera', 'idplandecuentasdebe', 'idplandecuentashaber',
                  'porcentaje', 'estado', 'activo', 'fechahoraregistro', 'usuarioid',
                  'idmaestroempresa', 'idmaestrosucursal']


class BalancecabeceraForm(forms.ModelForm):
    class Meta:
        model = Balancecabecera
        fields = ['id', 'anhio', 'idmaestroempresa', 'codigoempresa', 'posicion', 'linea',
                  'signo', 'titulodetalle', 'titulogeneral', 'titulototales',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class BalancedetalleForm(forms.ModelForm):
    class Meta:
        model = Balancedetalle
        fields = ['id', 'idmaestrocabecera', 'idmaestroempresa', 'codigoempresa', 'posicion', 'linea',
                  'cuenta', 'condicion', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo']


class CajacabeceraForm(forms.ModelForm):
    class Meta:
        model = Cajacabecera
        fields = ['codempresa', 'codcaja', 'numerocaja', 'fecha', 'moneda', 'transferencia',
                  'totaldebe', 'totalhaber', 'nrocomprobante', 'glosa', 'items', 'asientogenerado',
                  'asientorevisado', 'saldoinicial', 'saldofinla', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo', 'codigocuenta', 'idmaestrocaja']


class CajachicacabeceraForm(forms.ModelForm):
    class Meta:
        model = Cajachicacabecera
        fields = ['id', 'codempresa', 'numerocaja', 'refcaja', 'fecha', 'fechacontabilizacion',
                  'totalsolesdebe', 'totalsoleshaber', 'glosa', 'items', 'asientogenerado',
                  'asientorevisado', 'nrocomprobante', 'saldoinicial', 'saldofinal',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado',
                  'activo', 'codigocuenta', 'idmaestroempresa', 'codigocaja']


class CajachicadetalleForm(forms.ModelForm):
    class Meta:
        model = Cajachicadetalle
        fields = ['id', 'idcajachicacabecera', 'codempresa', 'nrocaja', 'item', 'codproveedor',
                  'codcentrodecostos', 'tipodocumento', 'serie', 'numero', 'debeohaber',
                  'moneda', 'basesoles', 'igvsoles', 'totalsoles', 'basedolares',
                  'igvdolares', 'totaldolares', 'glosa', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo', 'codcuenta', 'codcaja',
                  'fechadoc', 't_c', 'hora', 'usuario']


class CierreanualcontableForm(forms.ModelForm):
    class Meta:
        model = Cierreanualcontable
        fields = ['id', 'idempresa', 'idsucursal', 'anio', 'cerrado', 'fechacierre', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class CierrecajafinForm(forms.ModelForm):
    class Meta:
        model = Cierrecajafin
        fields = ['id', 'idformadepago', 'precioventadeclaradosoles', 'diferenciasoles', 'idcajero',
                  'fechacreacion', 'usuario', 'activo']


class ConfiguracionplancuentasForm(forms.ModelForm):
    class Meta:
        model = Configuracionplancuentas
        fields = ['idcomponente', 'idmaestroproductopadre', 'idmaestroproducto', 'cantidad', 'observaciones',
                  'estadoregistro', 'fechacreacion', 'idarea', 'descripcionimpresion']


class ControlcontableForm(forms.ModelForm):
    class Meta:
        model = Controlcontable
        fields = ['id', 'idmaestroempresa', 'controlactivo', 'mes', 'anhio', 'ultimodiario', 'dolarizado',
                  'tipocambiodolar', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo',
                  'idusuariogeneradosis']


class CorrentistasForm(forms.ModelForm):
    class Meta:
        model = Correntistas
        fields = ['correlativo', 'id', 'nombre', 'identificador', 'tipo']


class CuentasbancosForm(forms.ModelForm):
    class Meta:
        model = Cuentasbancos
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigobanco', 'idmaestrobanco', 'numerocuenta',
                  'moneda', 'idmaestromoneda', 'codigocuentacontable', 'idplandecuentas', 'numerofijocheque',
                  'correlativocheque', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class CuentaslibreschequesForm(forms.ModelForm):
    class Meta:
        model = Cuentaslibrescheques
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigocuenta', 'idplandecuentas', 'pideproveedor',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class DistribucioncentrocostocabeceraForm(forms.ModelForm):
    class Meta:
        model = Distribucioncentrocostocabecera
        fields = ['id', 'idmaestroempresa', 'codigoempresa', 'codigodistribucioncentrocosto', 'descripcion',
                  'porcentaje', 'total', 'totalimporte', 'estadodcc', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'codigocuentacontable']


class DistribucioncentrocostodetalleForm(forms.ModelForm):
    class Meta:
        model = Distribucioncentrocostodetalle
        fields = ['id', 'idmaestroempresa', 'codigoempresa', 'iddistribucioncentrocostoscabecera',
                  'codigodistribucioncentrocosto', 'idmaestrocentrosdecostos', 'codigocentrocosto', 'porcentaje',
                  'valor', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class EstadoperdidaganaciacabeceraForm(forms.ModelForm):
    class Meta:
        model = Estadoperdidaganaciacabecera
        fields = ['id', 'anhio', 'idmaestroempresa', 'codigoempresa', 'posicion', 'linea', 'signo', 'titulodetalle',
                  'titulogeneral', 'titulototal', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado',
                  'activo']


class EstadoperdidaganaciadetalleForm(forms.ModelForm):
    class Meta:
        model = Estadoperdidaganaciadetalle
        fields = ['id', 'idestadoperdidasgananciacabecera', 'idmaestroempresa', 'codigoempresa', 'posicion', 'linea',
                  'cuenta', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class FlujosdeefectivocabeceraForm(forms.ModelForm):
    class Meta:
        model = Flujosdeefectivocabecera
        fields = ['id', 'anhio', 'idmaestroempresa', 'codigoempresa', 'posicion', 'linea', 'signo', 'titulodetalle',
                  'titulogeneral', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class FlujosdeefectivodetalleForm(forms.ModelForm):
    class Meta:
        model = Flujosdeefectivodetalle
        fields = ['id', 'idcabecera', 'idmaestroempresa', 'codigoempresa', 'posicion', 'linea', 'cuenta',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class LicenciaconducirpersonalForm(forms.ModelForm):
    class Meta:
        model = Licenciaconducirpersonal
        fields = ['id', 'idmaestropersonal', 'numbrevete', 'tipo', 'fechaemision', 'fechavencimiento',
                  'fechaemisionpermiso1', 'fechaemisionpermiso2', 'fechaemisionpermiso3', 'fechacesepermiso1',
                  'fechacesepermiso2', 'fechacesepermiso3', 'fechacreacion', 'estado', 'activo', 'usuario']


class Lugarbal8ColumnForm(forms.ModelForm):
    class Meta:
        model = Lugarbal8Column
        fields = ['id', 'codigo', 'descripcion', 'usuarioid', 'fecharhoraregistro', 'idmaestroempresa',
                  'idmaestrosucursal', 'activo', 'estado']


class MaestroaccionnotadecreditoForm(forms.ModelForm):
    class Meta:
        model = Maestroaccionnotadecredito
        fields = ['id', 'codigoaccion', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'fechacreacion',
                  'activo', 'cuentacontable']


class MaestroactivosfijosForm(forms.ModelForm):
    class Meta:
        model = Maestroactivosfijos
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoempresa', 'tipoactivo', 'codigoactivo',
                  'descripcion', 'fechacompra', 'ajustadosoles', 'costocomprasoles', 'retirossoles', 'adicionessoles',
                  'tipocambio', 'idmaestrotipocambio', 'ajustadodolares', 'costocompradolares', 'retirosdolares',
                  'adicionesdolares', 'montodepreciacionsoles', 'fechaultimadepreciacion', 'fechamodificado',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrobienesForm(forms.ModelForm):
    class Meta:
        model = Maestrobienes
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestromotivoanulacionnotadecreditoForm(forms.ModelForm):
    class Meta:
        model = Maestromotivoanulacionnotadecredito
        fields = ['id', 'codigomotivo', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'fechacreacion',
                  'activo']


class MaestrotipobajaForm(forms.ModelForm):
    class Meta:
        model = Maestrotipobaja
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotipobaja', 'clasetabla', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipodediarioForm(forms.ModelForm):
    class Meta:
        model = Maestrotipodediario
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'tipodiario', 'descripcion', 'tipodolar',
                  'fechamodificado', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo',
                  'sunattipolibro']


class MayorForm(forms.ModelForm):
    class Meta:
        model = Mayor
        fields = ['id', 'idmaestroempresa', 'codigoempresa', 'idplandecuentas', 'codigocuenta', 'anhio',
                  'aperturadebesoles', 'aperturahabersoles', 'enerodebesoles', 'enerohabersoles', 'febrerodebesoles',
                  'febrerohabersoles', 'marzodebesoles', 'marzohabersoles', 'abrildebesoles', 'abrilhabersoles',
                  'mayodebesoles', 'mayohabersoles', 'juniodebesoles', 'juniohabersoles', 'juliodebesoles',
                  'juliohabersoles', 'agostodebesoles', 'agostohabersoles', 'setiembredebesoles', 'setiembrehabersoles',
                  'octubredebesoles', 'octubrehabersoles', 'noviembredebesoles', 'noviembrehabersoles',
                  'diciembredebesoles', 'diciembrehabersoles', 'aperturadebedolares', 'aperturahaberdolares',
                  'enerodebedolares', 'enerohaberdolares', 'febrerodebedolares', 'febrerohaberdolares',
                  'marzodebedolares', 'marzohaberdolares', 'abrildebedolares', 'abrilhaberdolares', 'mayodebedolares',
                  'mayohaberdolares', 'juniodebedolares', 'juniohaberdolares', 'juliodebedolares', 'juliohaberdolares',
                  'agostodebedolares', 'agostohaberdolares', 'setiembredebedolares', 'setiembrehaberdolares',
                  'octubredebedolares', 'octubrehaberdolares', 'noviembredebedolares', 'noviembrehaberdolares',
                  'diciembredebedolares', 'diciembrehaberdolares', 'codigousuario', 'accion', 'fechacreacion',
                  'autorizado', 'estado', 'activo']


class MesesForm(forms.ModelForm):
    class Meta:
        model = Meses
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'meses', 'anno', 'descripcion', 'cerro', 'modifico',
                  'mesreal', 'anioreal', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class NotascreditocabeceraForm(forms.ModelForm):
    class Meta:
        model = Notascreditocabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'numeroseriec', 'numerodocumentoc', 'idmaestrocliente',
                  'codigocliente', 'concepto', 'precioventasoles', 'valorventasoles', 'precioventadolares',
                  'valorventadolares', 'igv', 'recepciona', 'fechaemision', 'fecharecepcionado', 'idmaestroalmacen',
                  'codigoalmacen', 'codigosucursal', 'idfacturaclientecabecera', 'numeroseriefb', 'numerodocumentofb',
                  'numerooperacion', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class NotascreditodetalleForm(forms.ModelForm):
    class Meta:
        model = Notascreditodetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idnotacreditocabecera', 'numeroseriec',
                  'numerodocumentoc', 'idmaestroalmacen', 'codigoalmacen', 'codigosucursal', 'idmaestroproducto',
                  'codigoproducto', 'cantidad', 'preciounitariosoles', 'preciounitariodolares', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class NotasdebitoForm(forms.ModelForm):
    class Meta:
        model = Notasdebito
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'numeroseried', 'numerodocumentod', 'idmaestrocliente',
                  'codigocliente', 'concepto', 'precioventasoles', 'valorventasoles', 'precioventadolares',
                  'valorventadolares', 'igv', 'recepciona', 'fechaemision', 'fecharecepcionado', 'codigoalmacen',
                  'codigosucursal', 'idfacturaclientecabecera', 'numeroseriefb', 'numerodocumentofb', 'numerooperacion',
                  'fechamodificado', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class NumerocorrelativocForm(forms.ModelForm):
    class Meta:
        model = Numerocorrelativoc
        fields = ['id', 'numerooperacion', 'id1', 'nrocomprobante']


class NumerosdocumentosForm(forms.ModelForm):
    class Meta:
        model = Numerosdocumentos
        fields = ['id', 'idmaestroempresa', 'idmaestrotipodocumento', 'codigotipodocumento', 'idmaestrocajero',
                  'codigocajero', 'serie', 'correlativo', 'codigousuario', 'fechamodificacion', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo']


class ObservaciondocumentoForm(forms.ModelForm):
    class Meta:
        model = Observaciondocumento
        fields = ['id', 'idmaestroempresa', 'observacionordenpedido', 'observacioncotizacion', 'observacionfactura',
                  'observacionordentrabajo']


class Pagos4TacategoriaForm(forms.ModelForm):
    class Meta:
        model = Pagos4Tacategoria
        fields = [
            'id', 'idmaestroempresa', 'anhio', 'mes', 'cancelada', 'contabilizada', 'codigousuario', 'fechacreacion',
            'autorizado', 'activo', 'estado', 'idtipoproveedor'
        ]


class Pagos4TacategoriadetalleForm(forms.ModelForm):
    class Meta:
        model = Pagos4Tacategoriadetalle
        fields = [
            'id', 'idpagos4tacategoria', 'idmaestroproveedores', 'monto', 'cancelado', 'contabilizada',
            'codigousuario', 'fechacreacion', 'autorizado', 'activo', 'estado', 'idtipoproveedor',
            'bonificacion1', 'bonificacion2', 'horas', 'descuentos', 'bonificaciongrado', 'grado',
            'sinrecibo', 'remuneracion', 'diasfalta', 'descuentodiasfalta', 'descuentootrasfaltas'
        ]


class PlandecuentasForm(forms.ModelForm):
    class Meta:
        model = Plandecuentas
        fields = ['id', 'idmaestroempresa', 'codigocuenta', 'descripcion', 'esmayor', 'codigocuentamayor', 'tipo',
                  'tipocuenta', 'flagctacte', 'flagcostos', 'itemsrelacionados', 'lugarbal8column', 'ruc',
                  'codigocuentadebe', 'debe', 'codigocuentahaber', 'haber', 'anhio', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo']


class TiposDeDocumentosForm(forms.ModelForm):
    class Meta:
        model = TiposDeDocumentos
        fields = ['id', 'tipdoc_codigo', 'tipdoc_descripcion', 'tipdoc_sunat', 'tipdoc_resta', 'tipdoc_referencia',
                  'tipdoc_file', 'tipdoc_fechavto', 'tipo_equi', 'tipdoc_fechavto_vta']


class UnidadimpositivatributariaForm(forms.ModelForm):
    class Meta:
        model = Unidadimpositivatributaria
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'anhio', 'valor', 'baselegal', 'observacion',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class ValecabeceraForm(forms.ModelForm):
    class Meta:
        model = Valecabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idtrabajador', 'idautorizadopor', 'recogido',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'idpedido', 'codigo',
                  'idalmacen', 'codcliente', 'iddocreferencia', 'seriereferencia', 'numeroreferencia',
                  'entregacompleta', 'costocero']


class ValedetalleForm(forms.ModelForm):
    class Meta:
        model = Valedetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idvalecabecera', 'idmaestroproducto', 'cantidad',
                  'idmaestrocentrodecostos', 'idmaestroalmacen', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'motivo', 'cantidadrecojida']


class VehiculomarcaForm(forms.ModelForm):
    class Meta:
        model = Vehiculomarca
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigomarca', 'nombremarca', 'mostrarencita',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class VehiculomarcalogoForm(forms.ModelForm):
    class Meta:
        model = Vehiculomarcalogo
        fields = ['id', 'logomarca', 'nombremarca', 'idmaestromarca']


class VehiculomodeloForm(forms.ModelForm):
    class Meta:
        model = Vehiculomodelo
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idvehiculomarca', 'codigomodelo', 'nombremodelo',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class VouchercabeceraForm(forms.ModelForm):
    class Meta:
        model = Vouchercabecera
        fields = ['id', 'idmaestrosucursal', 'idmaestroempresa', 'codempresa', 'nrocomprobante', 'tipodiario', 'anhio',
                  'mes', 'fecha', 'glosa', 'totaldebesoles', 'totalhabersoles', 'totaldebedolares', 'totalhaberdolares',
                  'tipodecambio', 'itemsrelacionados', 'codproveedor', 'idtipodocsunat', 'nrofactura', 'seriefactura',
                  'tipooperacion', 'fechadoc', 'codigousuario', 'fechamodificado', 'accion', 'fechacreacion',
                  'autorizado', 'estado', 'activo', 'tipoigv', 'procedencia']


class VoucherdetalleForm(forms.ModelForm):
    class Meta:
        model = Voucherdetalle
        fields = ['id', 'idvoucher', 'idmaestrosucursal', 'idmaestroempresa', 'codempresa', 'nrocomprobante',
                  'tipodiario', 'nroitem', 'nroitempadre', 'anhio', 'mes', 'codcuenta', 'item1', 'item2',
                  'tipocorrentista', 'codcuentacorriente', 'codcentrodecostos', 'idtipodocsunat', 'nrodocumento',
                  'fecha', 'debeohaber', 'tipomoneda', 'idtipomoneda', 'linea', 'montodebesoles', 'montohabersoles',
                  'montodebedolares', 'montohaberdolares', 'cdda', 'nrocheque', 'idtipodocreferencia',
                  'seriedocreferencia', 'nrodocreferencia', 'glosaii', 'codigousuario', 'fechamodificado', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo', 'iddistribucioncentrodecostocabecera',
                  'codigoproducto']


class VouchernumeroreabiertoForm(forms.ModelForm):
    class Meta:
        model = Vouchernumeroreabierto
        fields = ['id', 'idregistro', 'nrovoucher', 'anhio', 'mes', 'tipoprocedencia', 'activo', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'codigousuario', 'activoregistromaestro', 'estadonumero']
