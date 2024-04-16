from django import forms

from .models import Chequecabecera, Chequedetalle, Ctacteproveedor, Maestrocuentaslibresparacheques


class ChequecabeceraForm(forms.ModelForm):
    class Meta:
        model = Chequecabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoempresa', 'numerocomprobante',
                  'tipo', 'fecha', 'codigobanco', 'idmaestrobanco', 'numerocuenta', 'codigocuenta',
                  'idplandecuentas', 'numerocheque', 'giradoa', 'tipomoneda', 'tipodecambio',
                  'montosoles', 'montodolares', 'acumuladosoles', 'acumuladodolares',
                  'numerocomprobantecont', 'glosa', 'estadocheque', 'fechadigitacion',
                  'fechaaceptacion', 'usuariodigitacion', 'usuarioaceptacion', 'transferencia',
                  'debesoles', 'habersoles', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'idmaestroretencion', 'idcajachica', 'imprimiren']


class ChequedetalleForm(forms.ModelForm):
    class Meta:
        model = Chequedetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idchequecabecera', 'codigoempresa',
                  'tipo', 'numerocomprobante', 'item', 'tipodocumentosunat', 'numerofactura',
                  'codigoproveedor', 'idmaestroproveedor', 'codigocuenta', 'idplandecuentas',
                  'numerocheque', 'tipomoneda', 'monto', 'glosa', 'estadocheque', 'fechadigitacion',
                  'fechaaceptacion', 'usuario', 'seriedocumento', 'numerodocumento', 'debehaber',
                  'codigodistribucioncentrocosto', 'iddistribucioncentrocosto', 'codigocentrocostos',
                  'idmaestrocentrocosto', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo', 'idfacturaproveedor']


class CtacteproveedorForm(forms.ModelForm):
    class Meta:
        model = Ctacteproveedor
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'cargoabono', 'fechaemisioncaja', 'codigoproveedor',
                  'idmaestroproveedor', 'tipodocorigen', 'numdocorigen', 'itemorigen', 'fechadocorigen',
                  'fechadevencimiento', 'codigobanco', 'idmaestrobanco', 'numerodecheque', 'idfacturaproveedor',
                  'idtipodocref', 'numdocref', 'seriedocref', 'fechaliquidacionca', 'moneda', 'tipodecambio',
                  'importesoles', 'importedolares', 'saldodocumento', 'saldodolares', 'lineaproduccion',
                  'codigocentrocostos', 'codigocuenta', 'idplandecuentas', 'anulado', 'fechacancelacion',
                  'facturacancelada', 'empresactb', 'anhioctb', 'mesctb', 'tipodiarioctb', 'nrocomprobctb', 'glosa',
                  'cajaref', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
                  'tipoconceptopdt']


class MaestrocuentaslibresparachequesForm(forms.ModelForm):
    class Meta:
        model = Maestrocuentaslibresparacheques
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigocuenta', 'pideproveedor', 'fechamodificado',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']
