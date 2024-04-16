from django import forms

from .models import Cargos, Cargostrabajador, Datosplanilla, \
    Feriados, Maestroaccidentetrabajo, Maestroafp, Maestroapoderado, \
    Maestrobeneficiario, Maestrocargoocupacion, Maestrocentroasistencial, \
    Maestroconceptospdt, Maestroderechohabientes, Maestrodocumentoacreditapaternidad, \
    Maestrodocumentoidentidad, Maestrodomicilio, Maestroenfermedad, Maestrogradoinstruccion, \
    Maestronivelcategoria, Maestropensiones, Maestroperiodicidadremuneracion, Maestropersonal, \
    Maestroregimenlaboral, Maestroretencion, Maestrosalud, Maestrosituacion, Maestrotipomovimiento, \
    Maestrotipopagoremuneracion, Maestrotipoparentesco, Maestrotipopersonal, Maestrotipoplanilla, \
    Maestrotipoprestamo, Maestrotiposervidor, Maestrotiposubsidio, Maestrovariablesentornopersonal, \
    Maestrovinculofamiliar, Personaladelantoquincena, Personaladicionalesgeneraciondeboletas, Personalcalculocts, \
    Personalcalculoctsdetalle, Personalcomposicionfamiliar, Personalconceptospdtplanilla, \
    Personalconceptospdtplanilla2, Personalconceptospdtplanilladetalle, Personalcuentacorrientecabecera, \
    Personalcuentacorrientedetalle, Personalcurriculo, Personaldatosadicionales, Personaldatosvariablesplanilla, \
    Personaldespistajerealizado, Personaldistribucioncentrodecostos, Personalegresofamiliar, \
    Personalentidadcontingencia, Personalestudioscomplementarios, Personalexperiencialaboral, \
    Personalfichacompartevivienda, Personalfichapersonasacargo, Personalfichaproblematicafamiliar, \
    Personalfichasocioeconomica, Personalgeneraciondeboletas, Personalgradoacademico, Personalhogarambientecomun, \
    Personalingresofamiliar, Personalliquidacion, Personalmantenimientotablas, Personalpadeceenfermedad, \
    Personalperiodovacaciones, Personalpersonascasoemergencia, Personalplanilla, Personalplantillaadelantoquincena, \
    Personalposeebienes, Personalquintaacumulado, Personalreferencialaboral, Personalregistroasistencia, \
    Personalretencionesjudiciales, Personalsubsidio, Personalturnopersonalcabecera


class CargosForm(forms.ModelForm):
    class Meta:
        model = Cargos
        fields = ['id', 'codigocargo', 'codigocargopadre', 'descripcion', 'idareas',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal',
                  'idmaestroalmacen', 'idmaestrocentrodecosto']


class CargostrabajadorForm(forms.ModelForm):
    class Meta:
        model = Cargostrabajador
        fields = ['id', 'idcargo', 'idtrabajador', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa',
                  'idmaestrosucursal']


class DatosplanillaForm(forms.ModelForm):
    class Meta:
        model = Datosplanilla
        fields = ['id', 'idmaestropersonal', 'idmaestroaccidentetrabajo', 'idmaestronivelcategoria',
                  'idmaestroregimenlaboral', 'idmaestrotipopersonal', 'idmaestrosalud', 'idmaestropensiones',
                  'idmaestroafp', 'idmaestrocargoocupacion', 'idmaestroseccion', 'idmaestrotipocontrato',
                  'idmaestrobancopagoplanillas', 'funcionario', 'afectoalsenati', 'ies', 'idmaestrosituacion',
                  'fechainiciosituacion', 'fechaterminosituacion', 'segurovidaessalud', 'sueldobasico',
                  'asignacionfamiliar', 'fechaingresoplanilla', 'fechainiciocontrato', 'fechaterminocontrato',
                  'fechacese', 'movilidadporasistencia', 'numerocarnetessalud', 'vidaley', 'segurocomplementario',
                  'numerorocarnetafp', 'fechaafiliacionafp', 'codigousuario', 'fechacreacion',
                  'cuentabancariapagoplanillas', 'cuentabancariadepositocts', 'dl25897porcentaje1023',
                  'dl25897porcentaje300', 'dl26504porcentaje33', 'accion', 'autorizado', 'estado', 'activo',
                  'idtiposervidor', 'importe01', 'importe02', 'importe03', 'importe04', 'importe05', 'importe06',
                  'importe07', 'importe08', 'comisionmixta', 'essindicalizado', 'montoasignacionfamiliar',
                  'importetotaldeudacc', 'importetotalremper', 'importeretencion5', 'redondeoant', 'redondeoactual',
                  'jornaldiario', 'idmaestrobancocts', 'quintaactiva', 'empresaquinta', 'beneficiostrabajador',
                  'calculoempresaextra']


class FeriadosForm(forms.ModelForm):
    class Meta:
        model = Feriados
        fields = ['idferiado', 'descripcion', 'fechainicio', 'fechafin', 'usuario', 'autorizado', 'activo',
                  'idmaestrotipocambio']


class MaestroaccidentetrabajoForm(forms.ModelForm):
    class Meta:
        model = Maestroaccidentetrabajo
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoaccidentetrabajo', 'clasetabla', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroafpForm(forms.ModelForm):
    class Meta:
        model = Maestroafp
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoafp', 'idubigeo', 'razonsocial', 'direccion',
                  'telefono', 'aportesolidaridadsoles', 'aportefondopensionsoles', 'comisionfijasoles',
                  'comisionporcentual', 'seguroinvalidezsoles', 'cuentacontabledebe', 'cuentacontablehaber',
                  'anexocontable', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo',
                  'comisionvariable']


class MaestroapoderadoForm(forms.ModelForm):
    class Meta:
        model = Maestroapoderado
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestropersonal', 'nombrescompletos', 'dni', 'ruc',
                  'otros', 'numeropartida', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado',
                  'activo']


class MaestrobeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Maestrobeneficiario
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrobancos', 'idmaestropersonal',
                  'cuentabancariadepositoretencion', 'apellidosnombres', 'dni', 'sustentoretencion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrocargoocupacionForm(forms.ModelForm):
    class Meta:
        model = Maestrocargoocupacion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigocargoocupacion', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrocentroasistencialForm(forms.ModelForm):
    class Meta:
        model = Maestrocentroasistencial
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigocentroasistencial', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroconceptospdtForm(forms.ModelForm):
    class Meta:
        model = Maestroconceptospdt
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoconceptospdt', 'descripcion',
                  'idconceptospdtplanilla', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado',
                  'activo', 'sistemaprivadopensiones', 'sistemanacionalpensiones', 'vacaciones118', 'gratificacion406']


class MaestroderechohabientesForm(forms.ModelForm):
    class Meta:
        model = Maestroderechohabientes
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestropersonal', 'idmaestrovinculofamiliar',
                  'idmaestrosituacion', 'idmaestrodomicilio', 'apellidopaterno', 'apellidomaterno', 'nombres',
                  'fechanacimiento', 'sexo', 'idmaestrodocumentoidentidad', 'numerodocumentoidentidad', 'fechaalta',
                  'idmaestrodocumentoacreditapaternidad', 'numerodocumentoacreditapaternidad', 'idmaestrotipobaja',
                  'fechabaja', 'resolucionincapacidadhijomayor', 'iddomiciliodetalle', 'direcciondomicilio',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrodocumentoacreditapaternidadForm(forms.ModelForm):
    class Meta:
        model = Maestrodocumentoacreditapaternidad
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrodocumentoidentidadForm(forms.ModelForm):
    class Meta:
        model = Maestrodocumentoidentidad
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigodocumentoidentidad', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo', 'codigoafp']


class MaestrodomicilioForm(forms.ModelForm):
    class Meta:
        model = Maestrodomicilio
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigodomicilio', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroenfermedadForm(forms.ModelForm):
    class Meta:
        model = Maestroenfermedad
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'trabajadorfamiliar', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrogradoinstruccionForm(forms.ModelForm):
    class Meta:
        model = Maestrogradoinstruccion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigogradoinstruccion', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestronivelcategoriaForm(forms.ModelForm):
    class Meta:
        model = Maestronivelcategoria
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigonivelcategoria', 'clasetabla', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestropensionesForm(forms.ModelForm):
    class Meta:
        model = Maestropensiones
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigopensiones', 'clasetabla', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroperiodicidadremuneracionForm(forms.ModelForm):
    class Meta:
        model = Maestroperiodicidadremuneracion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoperiodicidadremuneracion', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestropersonalForm(forms.ModelForm):
    class Meta:
        model = Maestropersonal
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoservidor', 'iddistribucioncentrodecostos',
                  'iddomiciliodetalle', 'idmaestrocentroasistencialessalud', 'idmaestroestadocivil',
                  'idmaestrotiposangre', 'apellidopaterno', 'apellidomaterno', 'nombres', 'direccion', 'telefono',
                  'fechanacimiento', 'idmaestronacionalidad', 'nacionalidad', 'idmaestropaisemisordocumento',
                  'idubigeonacimiento', 'idmaestrogradoinstrucciom', 'lugarnacimiento', 'sexo', 'prod91adm94ven95',
                  'profesion', 'iddocumentoidentidad', 'numerodocumentoidentidad', 'idmaestrotipomovimiento',
                  'fechatipomovimiento', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo',
                  'idmaestroperiodicidadremuneracion', 'idmaestrotipopagoremuneracion', 'codigocentrocosto',
                  'codigotiposervidor', 'correoelectronico', 'fiscalizacion', 'firma', 'detalleextra', 'obervacion',
                  'turnonoche']


class MaestroregimenlaboralForm(forms.ModelForm):
    class Meta:
        model = Maestroregimenlaboral
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoregimenlaboral', 'clasetabla', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroretencionForm(forms.ModelForm):
    class Meta:
        model = Maestroretencion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'seriedocretencion', 'numerodocretencion',
                  'idproveedor', 'estacontabilizada', 'estapagada', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'fechaimpresion', 'fechaimpresionretencion']


class MaestrosaludForm(forms.ModelForm):
    class Meta:
        model = Maestrosalud
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigosalud', 'clasetabla', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrosituacionForm(forms.ModelForm):
    class Meta:
        model = Maestrosituacion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigosituacion', 'clasetabla', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipomovimientoForm(forms.ModelForm):
    class Meta:
        model = Maestrotipomovimiento
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotipomovimiento', 'idempresa', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipopagoremuneracionForm(forms.ModelForm):
    class Meta:
        model = Maestrotipopagoremuneracion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotipopagoremuneracion', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipoparentescoForm(forms.ModelForm):
    class Meta:
        model = Maestrotipoparentesco
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipopersonalForm(forms.ModelForm):
    class Meta:
        model = Maestrotipopersonal
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotipopersonal', 'clasetabla', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipoplanillaForm(forms.ModelForm):
    class Meta:
        model = Maestrotipoplanilla
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoplanilla', 'descripcion',
                  'tipoplanillaabreviado', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipoprestamoForm(forms.ModelForm):
    class Meta:
        model = Maestrotipoprestamo
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotipoprestamo', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotiposervidorForm(forms.ModelForm):
    class Meta:
        model = Maestrotiposervidor
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotiposervidor', 'clasetabla', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotiposubsidioForm(forms.ModelForm):
    class Meta:
        model = Maestrotiposubsidio
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo', 'codigotiposusidiosunat']


class MaestrovariablesentornopersonalForm(forms.ModelForm):
    class Meta:
        model = Maestrovariablesentornopersonal
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigovariableentorno', 'descripcion', 'valor1',
                  'valor2', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrovinculofamiliarForm(forms.ModelForm):
    class Meta:
        model = Maestrovinculofamiliar
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigovinculofamiliar', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class PersonaladelantoquincenaForm(forms.ModelForm):
    class Meta:
        model = Personaladelantoquincena
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestropersonal', 'montoadelanto', 'vacaciones',
                  'idpersonaldatosvariablesplanilla', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo', 'idmaestroplanilla']


class PersonaladicionalesgeneraciondeboletasForm(forms.ModelForm):
    class Meta:
        model = Personaladicionalesgeneraciondeboletas
        fields = ['id', 'idgeneraciondeboletas', 'rangoinferior', 'rangosuperior', 'numeroinicialdeboleta', 'fechapago',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa',
                  'idmaestrosucursal']


class PersonalcalculoctsForm(forms.ModelForm):
    class Meta:
        model = Personalcalculocts
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'fechapagocts', 'tipodecambio', 'fechainicio',
                  'fechafin', 'accion', 'autorizado', 'estado', 'activo', 'codigousuario', 'fechacreacion',
                  'idtiposervidor', 'anhio', 'mes', 'semestre']


class PersonalcalculoctsdetalleForm(forms.ModelForm):
    class Meta:
        model = Personalcalculoctsdetalle
        fields = ['id', 'idpersonalcalculocts', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestropersonal',
                  'cantidadanhio', 'cantidadmes', 'cantidaddia', 'promediocomision', 'promediohoraextra',
                  'totalcomputable', 'promediocomputable', 'gratificacioncomputable', 'totalremuneracioncomputable',
                  'cantidaddiaafectivonotrabajado', 'importemes', 'importedia', 'importetotalsoles',
                  'importetotaldolares', 'accion', 'autorizado', 'estado', 'activo', 'codigousuario', 'fechacreacion',
                  'importebasico', 'importeotroconcepto', 'correlativo', 'pagado', 'contabilizado', 'simplec']


class PersonalcomposicionfamiliarForm(forms.ModelForm):
    class Meta:
        model = Personalcomposicionfamiliar
        fields = ['id', 'idpersonalfichasocioeconomica', 'nombresapellidos', 'parentesco', 'fechanacimiento', 'sexo',
                  'gradoinstruccion', 'ocupacion', 'dni', 'estadocivil', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalconceptospdtplanillaForm(forms.ModelForm):
    class Meta:
        model = Personalconceptospdtplanilla
        fields = ['id', 'codigoconceptospdtplanilla', 'codigotipoconcepto', 'descripcion', 'imaestroconceptospdt',
                  'calculovariable', 'escuentacorriente', 'ctaactivopasivoempleadodebe', 'ctaactivopasivoempleadohaber',
                  'ctaactivopasivoobrerodebe', 'ctaactivopasivoobrerohaber', 'ctagastoproduccionempleadodebe',
                  'ctagastoproduccionobrerodebe', 'ctagastoproduccionhaber', 'ctagastoadministracionempleadodebe',
                  'ctagastoadministracionobrerodebe', 'ctagastoadministracionhaber', 'ctagastoventasempleadodebe',
                  'ctagastoventasobrerodebe', 'ctagastoventashaber', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal', 'nposicion',
                  'descripcionconceptosunat']


class Personalconceptospdtplanilla2Form(forms.ModelForm):
    class Meta:
        model = Personalconceptospdtplanilla2
        fields = ['id', 'codigoconceptospdtplanilla', 'codigotipoconcepto', 'descripcion', 'imaestroconceptospdt',
                  'calculovariable', 'escuentacorriente', 'ctaactivopasivoempleadodebe', 'ctaactivopasivoempleadohaber',
                  'ctaactivopasivoobrerodebe', 'ctaactivopasivoobrerohaber', 'ctagastoproduccionempleadodebe',
                  'ctagastoproduccionobrerodebe', 'ctagastoproduccionhaber', 'ctagastoadministracionempleadodebe',
                  'ctagastoadministracionobrerodebe', 'ctagastoadministracionhaber', 'ctagastoventasempleadodebe',
                  'ctagastoventasobrerodebe', 'ctagastoventashaber', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal', 'posicion']


class PersonalconceptospdtplanilladetalleForm(forms.ModelForm):
    class Meta:
        model = Personalconceptospdtplanilladetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrotipopersonal', 'idpersonalconceptospdtplanilla', 'cuentadebe',
                  'cuentahaber', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
                  'cuenta90debe1', 'cuenta90debe2', 'cuenta90debe3', 'cuenta90haber1']


class PersonalcuentacorrientecabeceraForm(forms.ModelForm):
    class Meta:
        model = Personalcuentacorrientecabecera
        fields = ['id', 'idmaestropersonal', 'idmaestrotipopersonal', 'idmaestrotipoprestamo', 'cantidaddecuotas',
                  'montoprestado', 'fechaprestamo', 'descripcion', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalcuentacorrientedetalleForm(forms.ModelForm):
    class Meta:
        model = Personalcuentacorrientedetalle
        fields = ['id', 'idmaestropersonal', 'numerodecuota', 'montocuota', 'fechapago', 'saldoactual', 'descripcion',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
                  'idpersonalcuentacorrientecabecera', 'idpersonaldatosvariablespalnilla', 'idmaestroempresa',
                  'idmaestrosucursal']


class PersonalcurriculoForm(forms.ModelForm):
    class Meta:
        model = Personalcurriculo
        fields = ['id', 'idmaestropersonal', 'documentoescaneado', 'fecharegistro', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonaldatosadicionalesForm(forms.ModelForm):
    class Meta:
        model = Personaldatosadicionales
        fields = ['id', 'idpersonalfichasocioeconomica', 'religion', 'idioma', 'otrosidiomas', 'fechacaducidaddni',
                  'numeropasaporte', 'numeromesavotacion', 'numerobrevete', 'codigo_usuario', 'fecha_creacion',
                  'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonaldatosvariablesplanillaForm(forms.ModelForm):
    class Meta:
        model = Personaldatosvariablesplanilla
        fields = ['id', 'idmaestroempresa', 'idpersonalplanilla', 'idconceptospdtplanilla', 'montoconceptospdtplanilla',
                  'descripcion', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
                  'idmaestrosucursal']


class PersonaldespistajerealizadoForm(forms.ModelForm):
    class Meta:
        model = Personaldespistajerealizado
        fields = ['id', 'idpersonalfichasocioeconomica', 'enfermedad', 'trabajadorfamiliar', 'entidadsalud',
                  'fechadespistaje', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
                  'idmaestroempresa', 'idmaestrosucursal']


class PersonaldistribucioncentrodecostosForm(forms.ModelForm):
    class Meta:
        model = Personaldistribucioncentrodecostos
        fields = ['id', 'codigodistribucioncentrodecostos', 'clasetabla', 'descripcion', 'totalimporte',
                  'totalporcentaje', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
                  'idmaestroempresa', 'idmaestrosucursal']


class PersonalegresofamiliarForm(forms.ModelForm):
    class Meta:
        model = Personalegresofamiliar
        fields = ['id', 'idpersonalfichasocioeconomica', 'descripcion', 'monto', 'referencia', 'codigo_usuario',
                  'fecha_creacion', 'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalentidadcontingenciaForm(forms.ModelForm):
    class Meta:
        model = Personalentidadcontingencia
        fields = ['id', 'idpersonalfichasocioeconomica', 'idmaestrotipoparentesco', 'nombreentidad', 'codigo_usuario',
                  'fecha_creacion', 'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalestudioscomplementariosForm(forms.ModelForm):
    class Meta:
        model = Personalestudioscomplementarios
        fields = ['id', 'idpersonalfichasocioeconomica', 'institucion', 'especialidad', 'grado', 'periodo',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa',
                  'idmaestrosucursal']


class PersonalexperiencialaboralForms(forms.ModelForm):
    class Meta:
        model = Personalexperiencialaboral
        fields = ['id', 'idpersonalfichasocioeconomica', 'nombreempresa', 'cargo', 'motivocese', 'periodo',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa',
                  'idmaestrosucursal']


class PersonalfichacomparteviviendaForms(forms.ModelForm):
    class Meta:
        model = Personalfichacompartevivienda
        fields = ['id', 'idpersonalfichasocioeconomica', 'idmaestrotipoparentesco', 'especifiquecompartevivienda',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa',
                  'idmaestrosucursal']


class PersonalfichapersonasacargoForms(forms.ModelForm):
    class Meta:
        model = Personalfichapersonasacargo
        fields = ['id', 'idmaestrotipoparentesco', 'idpersonalfichasocioeconomica', 'especifiquepersonasacargo',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa',
                  'idmaestrosucursal']


class PersonalfichaproblematicafamiliarForms(forms.ModelForm):
    class Meta:
        model = Personalfichaproblematicafamiliar
        fields = ['id', 'idpersonalfichasocioeconomica', 'descripcion', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalfichasocioeconomicaForms(forms.ModelForm):
    class Meta:
        model = Personalfichasocioeconomica
        fields = ['id', 'idubigeo', 'idmaestropersonal', 'idpersonalentidadcontingencia', 'idpersonalgradoacademico',
                  'idpersonalpersonascasoemergencia1', 'idpersonalpersonascasoemergencia2',
                  'participaciontomadecisiones', 'gradocomunicacion', 'gradoconfianza', 'controlmedico',
                  'poseeelectricidad', 'compartehorasdiarias', 'compartehorassemanales', 'compartemotivodiario',
                  'compartemotivosemanal', 'afiliacion', 'afpcussp', 'centroessalud', 'numeroautogenerado',
                  'essaludvida', 'seguroadicional', 'desayunocasa', 'almuerzocasa', 'cenacasa', 'desayunofueracasa',
                  'almuerzofueracasa', 'cenafueracasa', 'cantidaddormitorio', 'cantidadfamilias', 'aseguradoconyuge',
                  'aseguradohijos', 'tipofamilia', 'tipovivienda', 'tipozona', 'tipoagua', 'tiposshh',
                  'idmaestromaterialconstruccionpiso', 'idmaestromaterialconstruccionpared',
                  'idmaestromaterialconstrucciontecho', 'observacionlaboral', 'observacionfamiliar',
                  'observacioneconomica', 'observacionvivienda', 'observacionsalud', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalgeneraciondeboletasForm(forms.ModelForm):
    class Meta:
        model = Personalgeneraciondeboletas
        fields = ['id', 'idmaestroplanilla', 'tituloplanilla', 'subtituloplanilla', 'fechainicio', 'fechatermino',
                  'comentariofinboleta', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
                  'idmaestroempresa', 'idmaestrosucursal']


class PersonalgradoacademicoForm(forms.ModelForm):
    class Meta:
        model = Personalgradoacademico
        fields = ['id', 'institucion', 'grado', 'periodo', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalhogarambientecomunForm(forms.ModelForm):
    class Meta:
        model = Personalhogarambientecomun
        fields = ['id', 'idpersonalfichasocioeconomica', 'descripcion', 'cantidad', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalingresofamiliarForm(forms.ModelForm):
    class Meta:
        model = Personalingresofamiliar
        fields = ['id', 'idpersonalfichasocioeconomica', 'aportanteresponsable', 'actividad', 'monto', 'codigo_usuario',
                  'fecha_creacion', 'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalliquidacionForm(forms.ModelForm):
    class Meta:
        model = Personalliquidacion
        fields = ['id', 'salariomensual', 'promediohoraextra', 'promediocomision', 'asignacionfamiliar', 'otrosafecto',
                  'totalremuneracion', 'motivoretiro', 'esafecto', 'remuneracionasegurable',
                  'cantidaddiaremuneracionasegurable', 'totalremuneracionasegurable', 'gratificaciontrunca',
                  'gratificacionafectacts', 'porcentajecompensacion', 'porcentajeresulremuneracionasegurable',
                  'porcentajeresulgratificacionafectacts', 'porcentajeresulgratificaciontrunca',
                  'totalcompensacionportiemposervicio', 'cantidadmesgratificaciontrunca', 'cantidadanhiovacaciontrunca',
                  'cantidadmesvacaciontrunca', 'cantidaddiavacaciontrunca', 'importemesgratificaciontrunca',
                  'importeanhiovacaciontrunca', 'importemesvacaciontrunca', 'importediavacaciontrunca',
                  'bonificacionexttemporal', 'subtotalsoles', 'descuentosnp', 'descuentofondopension',
                  'descuentosobrevivencia', 'descuentocomision', 'totaldescuentoley', 'importequintacategoria',
                  'importecuentacorriente', 'otrosinafecto', 'totalpago', 'idmaestropersonal', 'mesesreciboshonorarios',
                  'remuneracionreciboshonorarios', 'promedioreciboshonorarios', 'faltas']


class PersonalmantenimientotablasForm(forms.ModelForm):
    class Meta:
        model = Personalmantenimientotablas
        fields = ['id', 'codigotabla', 'descripciontabla', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalpadeceenfermedadForm(forms.ModelForm):
    class Meta:
        model = Personalpadeceenfermedad
        fields = ['id', 'idpersonalfichasocioeconomica', 'enfermedad', 'trabajadorfamiliar', 'codigo_usuario',
                  'fecha_creacion', 'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalperiodovacacionesForm(forms.ModelForm):
    class Meta:
        model = Personalperiodovacaciones
        fields = ['id', 'periodovacaciones', 'idmaestropersonal', 'fechasalida', 'fecharetorno', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal',
                  'periodovacacioneshasta', 'reduccion']


class PersonalpersonascasoemergenciaForm(forms.ModelForm):
    class Meta:
        model = Personalpersonascasoemergencia
        fields = ['id', 'apellidopaterno', 'apellidomaterno', 'nombres', 'direccion', 'distrito', 'referenciavivienda',
                  'parentesco', 'fijocelular', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado',
                  'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalplanillaForm(forms.ModelForm):
    class Meta:
        model = Personalplanilla
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestropersonal', 'idmaestroplanilla',
                  'numeroboleta', 'codigoservidor', 'numerocarnetessalud', 'numerorocarnetafp', 'idmaestroafp',
                  'numerodocumentoidentidad', 'nombrepaisemisor', 'fechaingresoplanilla', 'sueldobasico',
                  'segurovidaessalud', 'asignacionfamiliar', 'afectoalsenati', 'movilidadporasistencia',
                  'idmaestrovariablesentornopersonal', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo']


class PersonalplantillaadelantoquincenaForm(forms.ModelForm):
    class Meta:
        model = Personalplantillaadelantoquincena
        fields = ['id', 'idmaestroempresa', 'idmaestropersonal', 'monto_adelanto', 'porcentaje_adelanto', 'descuento',
                  'flag_vacaciones', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class PersonalposeebienesForm(forms.ModelForm):
    class Meta:
        model = Personalposeebienes
        fields = ['id', 'descripcion', 'codigo_usuario', 'fecha_creacion', 'accion', 'autorizado', 'estado', 'activo',
                  'idpersonalfichasocioeconomica', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalquintaacumuladoForm(forms.ModelForm):
    class Meta:
        model = Personalquintaacumulado
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestropersonal', 'fecha', 'descripcion',
                  'montorentaquinta', 'montosueldo', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado',
                  'activo']


class PersonalreferencialaboralForm(forms.ModelForm):
    class Meta:
        model = Personalreferencialaboral
        fields = ['id', 'idpersonalfichasocioeconomica', 'nombresapellidos', 'cargo', 'fijocelular', 'relacion',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa',
                  'idmaestrosucursal']


class PersonalregistroasistenciaForm(forms.ModelForm):
    class Meta:
        model = Personalregistroasistencia
        fields = ['id', 'idmaestropersonal', 'idmaestroplanilla', 'idmaestroseccion', 'idmaestrocentrodecostos',
                  'idmaestroafp', 'dias', 'dominical', 'promediohorasextra1', 'promediohorasextra2',
                  'promediohorasextra3', 'sobretasa', 'minutospermiso', 'minutostardanza', 'horassuspencion',
                  'horasinasistencia', 'idpersonaldatosvariablesplanilla', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal', 'horasnocturnas0507',
                  'horasnocturnas1921', 'horasnocturnas2105', 'horastrabajadas', 'descuentotardanzassoles',
                  'horasferiados', 'numeroviajes']


class PersonalretencionesjudicialesForm(forms.ModelForm):
    class Meta:
        model = Personalretencionesjudiciales
        fields = ['id', 'idmaestropersonal', 'idmaestrobeneficiario', 'porcentaje', 'porcentajeimporte',
                  'descuentosobrebrutoneto', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado',
                  'activo', 'idmaestroempresa', 'idmaestrosucursal']


class PersonalsubsidioForm(forms.ModelForm):
    class Meta:
        model = Personalsubsidio
        fields = ['id', 'iddatospalnilla', 'idmaestrotiposubsidio', 'numerocitt', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa', 'idmaestrosucursal', 'fechainicio',
                  'fechafin']


class PersonalturnopersonalcabeceraForm(forms.ModelForm):
    class Meta:
        model = Personalturnopersonalcabecera
        fields = ['id', 'idmaestropersonal', 'turnofijo', 'codigomarcadoprincipal', 'idmaestrohorarioturnopersonal',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa',
                  'idmaestrosucursal']
