from django import forms

from .models import Aprobaciones, Aprobacionesdetalle, Aprobacionesfacturadetalle, \
    Aprobacionesfacturacion, Aprobacionesordencompra, Aprobacionesordencompradetalle, \
    Aprobacionespedidos, Aprobacionespedidosdetalle


class AprobacionesForm(forms.ModelForm):
    class Meta:
        model = Aprobaciones
        fields = ['id', 'esgrupal', 'taller', 'valortaller', 'ventas',
                  'valorventas', 'logistica', 'valorlogistica', 'almacen',
                  'valoralmacen', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'idmaestroempresa',
                  'idmaestrosucursal']


class AprobacionesdetalleForm(forms.ModelForm):
    class Meta:
        model = Aprobacionesdetalle
        fields = ['id', 'idcargotrabajador', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa',
                  'idmaestrosucursal', 'idaprobacion']


class AprobacionesfacturacionForm(forms.ModelForm):
    class Meta:
        model = Aprobacionesfacturacion
        fields = ['id', 'idfactura', 'idaprobacion', 'aprobadogeneral',
                  'fechaaprobaciongeneral', 'montogeneral', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class AprobacionesfacturadetalleForm(forms.ModelForm):
    class Meta:
        model = Aprobacionesfacturadetalle
        fields = ['id', 'idaprobacionfactura', 'idaprobaciondetalle', 'aprobado', 'motivo',
                  'fechaaprobacion', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo']


class AprobacionesordencompraForm(forms.ModelForm):
    class Meta:
        model = Aprobacionesordencompra
        fields = ['id', 'idordencompra', 'idaprobacion', 'aprobadogeneral',
                  'fechaaprobaciongeneral', 'montogeneral', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class AprobacionesordencompradetalleForm(forms.ModelForm):
    class Meta:
        model = Aprobacionesordencompradetalle
        fields = ['id', 'idaprobacionordencompra', 'idaprobaciondetalle', 'aprobado',
                  'motivo', 'fechaaprobacion', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo']


class AprobacionespedidosForm(forms.ModelForm):
    class Meta:
        model = Aprobacionespedidos
        fields = ['id', 'idpedido', 'idaprobacion', 'aprobadogeneral',
                  'fechaaprobaciongeneral', 'idtiposolicitud', 'idviaaprobacion',
                  'montogeneral', 'logistica', 'taller', 'ventas', 'almacen',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo']


class AprobacionespedidosdetalleForm(forms.ModelForm):
    class Meta:
        model = Aprobacionespedidosdetalle
        fields = ['id', 'idaprobacionpedido', 'idaprobaciondetalle', 'aprobado',
                  'motivo', 'fechaaprobacion', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo']
