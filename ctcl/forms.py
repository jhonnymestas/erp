from django import forms

from .models import Ctactecliente


class CtacteclienteForm(forms.ModelForm):
    class Meta:
        model = Ctactecliente
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'cargo', 'fechageneracion', 'codigocliente',
                  'idmaestrocliente', 'codigoconcepto', 'idobligacion', 'codigotipocliente', 'idmaestrotipocliente',
                  'codigoestado', 'tipodocorigen', 'numserorigen', 'numdocorigen', 'itemorigen', 'fechadocorigen',
                  'fechadevencimiento', 'codigodebanco', 'idmaestrobanco', 'cuentabanco', 'numerocheque', 'tipodocref',
                  'serdocref', 'numdocref', 'fechaliquidacionca', 'moneda', 'idmaestrotipocambio', 'tipodecambio',
                  'importesoles', 'importedolares', 'saldodocumento', 'centrodecostos', 'codigocuenta',
                  'idplandecuentas', 'anulado', 'edoletras', 'fechacancelacion', 'doccancelado', 'empresactb',
                  'anhioctb', 'mesctb', 'tipodiarioctb', 'nrocomprobctb', 'glosa', 'depctacte', 'cancelacion', 'fill',
                  'codigocaja', 'castigado', 'fechacastigo', 'porcentajeinteres', 'gastosadministrativos',
                  'gastosbancarios', 'intereses', 'pagooficina', 'diferenciacambio', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo', 'idcobrador', 'idmaestroturnocaja']
