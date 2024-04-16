from django import forms

from .models import Clientecita, Ejecucionserviciodetalle, Horariotaller, \
    Horariotallerweb, Maestroconfiguracioncita, Maestroestadocita, Maestrotrabajotaller, Tallercitas, \
    Tallerclientevehiculo, Tallerestacion, Tallerhorario, Usuarioweb, Vehiculoaccesorios


class ClientecitaForm(forms.ModelForm):
    class Meta:
        model = Clientecita
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrocliente',
                  'cargocliente', 'lugarentrevista', 'idmaestroproducto', 'fechacita',
                  'horacita', 'observacion', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo']


class MaestrotrabajotallerForm(forms.ModelForm):
    class Meta:
        model = Maestrotrabajotaller
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'nombre', 'mostrarencita', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class EjecucionserviciodetalleForm(forms.ModelForm):
    class Meta:
        model = Ejecucionserviciodetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idejecucionserviciocabecera', 'numerotarjeta',
                  'idmaestrotrabajotaller', 'idmaestroserviciotaller', 'idmaestrotecnico', 'idordenserviciodetalle',
                  'accionejecucion', 'observacion', 'hora', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo', 'horastranscurridas', 'porcentaje', 'descripcion', 'estrabajoadicional',
                  'idordenserviciotrabajoadicional', 'esservicioportercero', 'idservicioportercerodetalle']


class HorariotallerForm(forms.ModelForm):
    class Meta:
        model = Horariotaller
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'hora', 'cantidadcitasportruno', 'tipodia',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'id_marca']


class HorariotallerwebForm(forms.ModelForm):
    class Meta:
        model = Horariotallerweb
        fields = ['hora', 'cantidad']


class MaestroconfiguracioncitaForm(forms.ModelForm):
    class Meta:
        model = Maestroconfiguracioncita
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'minutosdeactualizacion', 'dimensionpantallaancho',
                  'dimensionpantallaalto', 'comprobaciondefacturapendiente', 'numerodediasmaximofacturapendiente',
                  'diashabilescalendarios', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado',
                  'activo']


class MaestroestadocitaForm(forms.ModelForm):
    class Meta:
        model = Maestroestadocita
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'nombre', 'color', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class TallerestacionForm(forms.ModelForm):
    class Meta:
        model = Tallerestacion
        fields = ['id', 'nombre', 'direccion', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado',
                  'activo', 'idmaestroempresa', 'idmaestrosucursal']


class TallercitasForm(forms.ModelForm):
    class Meta:
        model = Tallercitas
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'id_cliente', 'id_vehiculo', 'id_estacion',
                  'id_asesor', 'idmaestrotrabajotaller', 'idmaestroestadocita', 'carroceriapintura', 'fecha', 'hora',
                  'taxi', 'informacion', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo',
                  'citaefectiva', 'horaterminocita', 'tecnico', 'fechaentregatentativa', 'anulada',
                  'horainicioatencion']


class TallerclientevehiculoForm(forms.ModelForm):
    class Meta:
        model = Tallerclientevehiculo
        fields = ['id', 'id_cliente', 'id_vehiculo']


class TallerhorarioForm(forms.ModelForm):
    class Meta:
        model = Tallerhorario
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idtallerestacion', 'entrada', 'salida',
                  'horastrabajadas', 'descripcion', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado',
                  'activo']


class UsuariowebForm(forms.ModelForm):
    class Meta:
        model = Usuarioweb
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'usuario', 'password', 'observacion', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class VehiculoaccesoriosForm(forms.ModelForm):
    class Meta:
        model = Vehiculoaccesorios
        fields = ['id', 'idmaestrovehiculo', 'idmaestroaccesorios', 'idordenserviciocabecera', 'estadoaccesorios',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']
