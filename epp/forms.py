from django import forms

from .models import Operacioneppcabecera, Operacioneppdetalle


class OperacioneppcabeceraForm(forms.ModelForm):
    class Meta:
        model = Operacioneppcabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestropersonal', 'idarea', 'numeroguia',
                  'fechaenvio', 'numerocargo', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado',
                  'activo', 'serieguia']


class OperacioneppdetalleForm(forms.ModelForm):
    class Meta:
        model = Operacioneppdetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idcabecera', 'idmaestroproducto', 'cantidad',
                  'controlcambio', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
                  'diasaviso']
