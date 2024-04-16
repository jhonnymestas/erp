from django import forms


from .models import Marcaciondetalle, Marcarpersonal


class MarcaciondetalleForm(forms.ModelForm):
    class Meta:
        model = Marcaciondetalle
        fields = ['idmarcaciondetalle', 'idmarcacion', 'dni', 'nombre', 'fechamarcacion', 'titulohorario',
                  'fechahorainiciomarcacion', 'fechahorasalidamarcacion', 'fechahoraentrada', 'fechahorasalidad',
                  'fechacreacion', 'codigousuario', 'accion', 'activo']


class MarcarpersonalForm(forms.ModelForm):
    class Meta:
        model = Marcarpersonal
        fields = ['idmarcarpersonal', 'nombresapellidos', 'fecha', 'horaentrada', 'horasalida', 'falta',
                  'salidarefrigerio', 'ingresorefrigerio', 'tolerancia', 'horarefrigerio', 'sobretiempo25porcentaje',
                  'sobretiempo35porcentaje', 'sobretiempo100porcentaje', 'diferenciaingreso', 'diferenciasalida',
                  'marcaringresotareo', 'marcarsalidatareo', 'permiso', 'descripcion', 'horatrabajo', 'calificacion',
                  'activo', 'idempresa', 'fechademodificacion', 'usuario', 'idmaestropersonal', 'horaingresoreal',
                  'horasalirreal', 'documentoidentidad', 'horasextra', 'horstnocturna']
