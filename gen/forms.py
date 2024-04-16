from django import forms

from .models import Configuracionreportes, Maestrocontrolcalidad, Hojacalidad, Maestroalmacenes, Maestrobancos, \
    Maestrocentrosdecostos, Maestrociudades, Maestrodatosgenerales, Maestrodocumentossunat, \
    Maestroempresadatosadicionales, Maestroempresas, Maestroestadocivil, Maestroformasdepago, \
    Maestrolineascomerciales, Maestromoneda, Maestromotivo, Maestromotor, Maestronacionalidad, Maestrooperacion, \
    Maestropaisemisordocumento, Maestroproveedores, Maestrorepresentantedelbanco, Maestroseccion, \
    Maestrosucursales, Maestrotipocontrato, Maestrotipodecambio, Maestrotipoempresa, Maestrotipofinanciamiento, \
    Maestrotipoformapago, Maestrotipooperacion, Maestrotipoorden, Maestrotiposangre, Maestrotiposdocumentos, \
    Maestrotiposdocumentostabla12, Maestrotipovia, Maestrotipozona, Maestrotransportistas, Maestroubigeo, \
    Maestrounidadesdemedida, Maestrounidadesdemedidatabla6, Maestrousuario, Maestrousuarionotasventas, \
    Maestrozonas, Maestroestadosdeatencion, Maestromaterialconstruccion, Reniec, Reportegenerados, Secuencias, \
    Maestrocubiculo, Maestroexpediente, Maestroexpedientesituacion, UsuarioSistemas, Componentebase, Maestrotipoaveria


class ConfiguracionreportesForm(forms.ModelForm):
    class Meta:
        model = Configuracionreportes
        fields = ['id', 'nombrearchivo', 'nombrevisual', 'modulo', 'maestro', 'ruta',
                  'icono', 'abreviacion']


class MaestroempresasForm(forms.ModelForm):
    class Meta:
        model = Maestroempresas
        fields = ['id', 'idmaestrotipoempresa', 'codigoempresa', 'codigotipoempresa', 'representantelegal', 'contacto',
                  'descripcion', 'descripcionlarga', 'direccion', 'ruc', 'telefono', 'fax', 'fechamodificado',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo', 'contabautomatico',
                  'tipocontab1as2cc3tod4otr', 'firmadigital']


class MaestrosucursalesForm(forms.ModelForm):
    class Meta:
        model = Maestrosucursales
        fields = ['id', 'idmaestroempresa', 'codigoempresa', 'codigosucursal', 'descripcion', 'direccion',
                  'codigociudad', 'responsable', 'fechamodificado', 'idubigeo', 'numero', 'interior', 'zona',
                  'telefono', 'celular', 'email', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado',
                  'activo', 'direccioncompleta', 'lcsunat']


class MaestrocontrolcalidadForm(forms.ModelForm):
    class Meta:
        model = Maestrocontrolcalidad
        fields = ['id', 'maestroempresa', 'maestrosucursal', 'nombre', 'tipocontrol', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class HojacalidadForm(forms.ModelForm):
    class Meta:
        model = Hojacalidad
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idordenserviciocabecera', 'idmaestrocontrolcalidad',
                  'resultado', 'etapa', 'observaciones', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo', 'fechaingreso']


class MaestroalmacenesForm(forms.ModelForm):
    class Meta:
        model = Maestroalmacenes
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigosucursal', 'codigoalmacen', 'descripcion',
                  'viatipo', 'vianombre', 'numero', 'interior', 'zona', 'idubigeo', 'direccion', 'fechamodificado',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo', 'tipoalm']


class MaestrobancosForm(forms.ModelForm):
    class Meta:
        model = Maestrobancos
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigobanco', 'nombrebanco', 'fechamodificado', 'ruc',
                  'direccion', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrocentrosdecostosForm(forms.ModelForm):
    class Meta:
        model = Maestrocentrosdecostos
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigocentrocostos', 'descripcion', 'mayor',
                  'codigocuentamayor', 'fechamodificado', 'codigousuario', 'accion', 'fechacreacion', 'autorizado',
                  'estado', 'activo']


class MaestrociudadesForm(forms.ModelForm):
    class Meta:
        model = Maestrociudades
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idubigeo', 'codigociudad', 'nombreciudad',
                  'nombrepais', 'fechamodificado', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado',
                  'activo']


class MaestrodatosgeneralesForm(forms.ModelForm):
    class Meta:
        model = Maestrodatosgenerales
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'fld1', 'porcentajeigv', 'mensajeenfacturas',
                  'porcentajeinteresletrasnormal', 'porcentajeinteresletrasatrazado', 'descuentomayoristasoles',
                  'descuentomayoristadolares', 'gastosadministrativosletrassoles', 'gastosadministrativosletrasdolares',
                  'fechamodificado', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo',
                  'descuentorepuestos', 'descuentotaller', 'importeretencion', 'porcentajeretencion', 'saldosnegativos',
                  'horastrabajo', 'porcentajeutilidadproductoalmacen', 'porcentajeutilidadproductoventa',
                  'porcentajedescuentoflotas', 'cuentacontableigv', 'cuentacontablerenta',
                  'cuentacontablefacturacliente', 'cuentacontableretencion', 'idmaestroclientestockordenpedido',
                  'cuentacontablecierrecaja']


class MaestrodocumentossunatForm(forms.ModelForm):
    class Meta:
        model = Maestrodocumentossunat
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'tipodocumento', 'descripcion', 'fechamodificado',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo', 'essunat']


class MaestroempresadatosadicionalesForm(forms.ModelForm):
    class Meta:
        model = Maestroempresadatosadicionales
        fields = ['id', 'logofondo', 'logoreporte', 'colorbarra', 'colorfondo', 'colorreportes', 'tipodeletra',
                  'fechainicio', 'fechatermino', 'nrousuariosmax', 'tamanhobdmb', 'email']


class MaestroestadosdeatencionForm(forms.ModelForm):
    class Meta:
        model = Maestroestadosdeatencion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'color', 'descripcion', 'cantidadmaxima', 'prioridad',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class MaestroestadocivilForm(forms.ModelForm):
    class Meta:
        model = Maestroestadocivil
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoestadocivil', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroformasdepagoForm(forms.ModelForm):
    class Meta:
        model = Maestroformasdepago
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoformapago', 'descripcion', 'diascredito',
                  'tasainteressoles', 'tasainteresdolares', 'fechamodificado', 'idmaestrotipoformapago',
                  'tipoformapago', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrolineascomercialesForm(forms.ModelForm):
    class Meta:
        model = Maestrolineascomerciales
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigolineacomercial', 'descripcion',
                  'fechamodificado', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestromaterialconstruccionForm(forms.ModelForm):
    class Meta:
        model = Maestromaterialconstruccion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestromonedaForm(forms.ModelForm):
    class Meta:
        model = Maestromoneda
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigomoneda', 'nombre', 'descripcion',
                  'fechamodificado', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestromotivoForm(forms.ModelForm):
    class Meta:
        model = Maestromotivo
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestromotorForm(forms.ModelForm):
    class Meta:
        model = Maestromotor
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcionmotor', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo']


class MaestronacionalidadForm(forms.ModelForm):
    class Meta:
        model = Maestronacionalidad
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigonacionalidad', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrooperacionForm(forms.ModelForm):
    class Meta:
        model = Maestrooperacion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'nombreoperacion', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestropaisemisordocumentoForm(forms.ModelForm):
    class Meta:
        model = Maestropaisemisordocumento
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigopaisemisordocumento', 'nombrepaisemisor',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroproveedoresForm(forms.ModelForm):
    class Meta:
        model = Maestroproveedores
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'nombrecomercial', 'propietario', 'pais', 'viatipo',
                  'vianombre', 'numero', 'interior', 'zona', 'idubigeo', 'direccion', 'personajuridica', 'telefono',
                  'fax', 'ruc', 'tipoproveedor', 'email', 'paginaweb', 'codigolinea', 'fechamodificado',
                  'idtipoproveedor', 'marca', 'detraccion', 'observacion', 'codigousuario', 'accion', 'fechacreacion',
                  'autorizado', 'estado', 'activo', 'primerapellido', 'segundoapellido', 'nombres',
                  'codigocuentacontable', 'codigocuentacontabledolar']


class MaestrorepresentantedelbancoForm(forms.ModelForm):
    class Meta:
        model = Maestrorepresentantedelbanco
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrobanco', 'nombres', 'apellidopaterno',
                  'apellidomaterno', 'dni', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado',
                  'activo']


class MaestroseccionForm(forms.ModelForm):
    class Meta:
        model = Maestroseccion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoseccion', 'clasetabla', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipocontratoForm(forms.ModelForm):
    class Meta:
        model = Maestrotipocontrato
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotipocontrato', 'clasetabla', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipodecambioForm(forms.ModelForm):
    class Meta:
        model = Maestrotipodecambio
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'fechacambio', 'codigomoneda', 'dolarpromedio',
                  'dolarcompra', 'dolarventa', 'fechamodificado', 'codigousuario', 'accion', 'fechacreacion',
                  'autorizado', 'estado', 'activo']


class MaestrotipoempresaForm(forms.ModelForm):
    class Meta:
        model = Maestrotipoempresa
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotipoempresa', 'descripcion', 'fechamodificado',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipofinanciamientoForm(forms.ModelForm):
    class Meta:
        model = Maestrotipofinanciamiento
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigofinanciamiento', 'nombrefinanciamiento',
                  'descripcion', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipoformapagoForm(forms.ModelForm):
    class Meta:
        model = Maestrotipoformapago
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idcentrodecosto', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipooperacionForm(forms.ModelForm):
    class Meta:
        model = Maestrotipooperacion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'tipooperacion', 'descripcion', 'fechamodificado',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipoordenForm(forms.ModelForm):
    class Meta:
        model = Maestrotipoorden
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'nombre', 'codigousuario', 'accion', 'fechacreacion',
                  'autorizado', 'estado', 'activo']


class MaestrotiposangreForm(forms.ModelForm):
    class Meta:
        model = Maestrotiposangre
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripciontiposangre', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotiposdocumentosForm(forms.ModelForm):
    class Meta:
        model = Maestrotiposdocumentos
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'tipomovimiento', 'descripcion', 'nacional', 'ingreso',
                  'factura', 'creditofiscal', 'operacionresta', 'valorado', 'otros', 'tipodocumento', 'fechamodificado',
                  'proveedorcliente', 'pertenecientea', 'tipooperacionsunat', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class Maestrotiposdocumentostabla12Form(forms.ModelForm):
    class Meta:
        model = Maestrotiposdocumentostabla12
        fields = ['id', 'tipooperacion', 'descripcion']


class MaestrotipoviaForm(forms.ModelForm):
    class Meta:
        model = Maestrotipovia
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotipovia', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipozonaForm(forms.ModelForm):
    class Meta:
        model = Maestrotipozona
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotipozona', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotransportistasForm(forms.ModelForm):
    class Meta:
        model = Maestrotransportistas
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigosucursal', 'codigotransportista', 'razonsocial',
                  'ruc', 'direccion', 'certificadoinscripcion', 'nombrecomercial', 'tipo', 'fechamodificado',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo', 'idmaestrosucursales']


class MaestroubigeoForm(forms.ModelForm):
    class Meta:
        model = Maestroubigeo
        fields = ['id', 'codigoregion', 'codigodepartamento', 'codigoprovincia', 'codigodistrito', 'nombreregion',
                  'nombredepartamento', 'nombreprovincia', 'nombredistrito']


class MaestrounidadesdemedidaForm(forms.ModelForm):
    class Meta:
        model = Maestrounidadesdemedida
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigounidadmedida', 'descripcion', 'valor',
                  'fechamodificado', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo',
                  'idunidaddemedidasunat']


class Maestrounidadesdemedidatabla6Form(forms.ModelForm):
    class Meta:
        model = Maestrounidadesdemedidatabla6
        fields = ['id', 'codigounidadmedida', 'descripcion', 'abreviacion']


class MaestrousuarioForm(forms.ModelForm):
    class Meta:
        model = Maestrousuario
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigo', 'descripcion', 'codigoresponsabilidad',
                  'usuario', 'fechamodificado', 'codigosucursal', 'codigoalmacen', 'numeroseriegr', 'numeroguiar',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrousuarionotasventasForm(forms.ModelForm):
    class Meta:
        model = Maestrousuarionotasventas
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrousuario', 'idmaestroalmacen',
                  'codigosucursal', 'codigoalmacen', 'numeroseried', 'numerodocumentod', 'numeroseriec',
                  'numerodocumentoc', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrozonasForm(forms.ModelForm):
    class Meta:
        model = Maestrozonas
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigozona', 'descripcion', 'idmaestrociudades',
                  'codigociudad', 'idmaestrovendedor', 'codigovendedor', 'metaventassoles', 'metaventasdolares',
                  'metacobranzasoles', 'metacobranzadolares', 'fechamodificado', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class ReniecForm(forms.ModelForm):
    class Meta:
        model = Reniec
        fields = ['dni', 'apellidopaterno', 'apellidomaterno', 'nombre', 'sexo']


class ReportegeneradosForm(forms.ModelForm):
    class Meta:
        model = Reportegenerados
        fields = ['idreporte', 'rutafisica', 'archivo', 'fechacreacion']


class SecuenciasForm(forms.ModelForm):
    class Meta:
        model = Secuencias
        fields = ['nombresecuencia', 'semilla', 'incremento', 'valoractual']


class UsuariosistemasForm(forms.ModelForm):
    class Meta:
        model = UsuarioSistemas
        fields = ['id', 'empresa', 'surcursal', 'almacen']


class MaestrocubiculoForm(forms.ModelForm):
    class Meta:
        model = Maestrocubiculo
        fields = ['id', 'maestroempresa', 'maestrosucursal', 'codigocubiculo', 'descripcion', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroexpedienteForm(forms.ModelForm):
    class Meta:
        model = Maestroexpediente
        fields = ['id', 'maestroempresa', 'maestrosucursal', 'maestroexpedientesituacion', 'ordenpedido',
                  'maestroformapago', 'numerooperacion', 'tarjetapropiedad', 'fechallegadatarjetapropiedad', 'placa',
                  'fechallegadaplaca', 'inscripcionmunicipalidad', 'numerorecibomunicipalidad', 'leasing',
                  'numerocuotas', 'declaracionjurada', 'cartapodertarjeta', 'cartapoderplaca', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroexpedientesituacionForm(forms.ModelForm):
    class Meta:
        model = Maestroexpedientesituacion
        fields = ['id', 'maestroempresa', 'maestrosucursal', 'descripcion', 'codigousuario', 'accion', 'fechacreacion',
                  'autorizado', 'estado', 'activo']


class ComponentebaseForm(forms.ModelForm):
    class Meta:
        model = Componentebase
        fields = ['idcompbase', 'codigocompbase', 'descripcion', 'autorizado', 'fechacreacion', 'activo', 'accion']


class MaestrotipoaveriaForm(forms.ModelForm):
    class Meta:
        model = Maestrotipoaveria
        fields = ['id', 'maestroempresa', 'maestrosucursal', 'descripcion', 'codigousuario', 'accion', 'fechacreacion',
                  'autorizado', 'estado', 'activo']
