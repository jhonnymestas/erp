from django import forms

from .models import Controlgasto, Presupuesto, Presupuestoanuales, Presupuestodetalle


class ControlgastoForm(forms.ModelForm):
    class Meta:
        model = Controlgasto
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'fecha', 'idmaestroproveedor', 'idfacturacabecera',
                  'numerofactura', 'idmaestroproducto', 'preciosoles', 'preciodolares', 'idarea', 'observacion',
                  'motivo', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class PresupuestoForm(forms.ModelForm):
    class Meta:
        nombre = Presupuesto
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigopresupuesto', 'descripcion', 'mayor',
                  'codigocuentamayor', 'itemsrelacionados', 'cuenta', 'cuentaii', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo']


class PresupuestoanualesForm(forms.ModelForm):
    class Meta:
        nombre = Presupuestoanuales
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigopresupuesto', 'tipo', 'codigopresupuestopadre',
                  'descripcion', 'idcentrocostos', 'centrocostos', 'idcuentacontable', 'cuentacontable', 'enero',
                  'porcentajeenero', 'febrero', 'porcentajefebrero', 'marzo', 'porcentajemarzo', 'abril',
                  'porcentajeabril', 'mayo', 'porcentajemayo', 'junio', 'porcentajejunio', 'julio', 'porcentajejulio',
                  'agosto', 'porcentajeagosto', 'septiembre', 'porcentajeseptiembre', 'octubre', 'porcentajeoctubre',
                  'noviembre', 'porcentajenoviembre', 'diciembre', 'porcentajediciembre', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'anhio']


class PresupuestodetalleForm(forms.ModelForm):
    class Meta:
        model = Presupuestodetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigopresupuesto', 'periodomes', 'periodoanhio',
                  'montopresupuestadosoles', 'montopresupuestadodolares', 'idmaestrotipocambio', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']
