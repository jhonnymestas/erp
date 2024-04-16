# from dataclasses import fields

from django import forms

from .models import Cliente

# Implementando Las clases FAC
from .models import (Cajadetalle, Cajeroserie, Cierrefacturacion, Cierrefacturaciondetalle, Cierreordenservicio,
                     Clientedireccion, Clientesmigrar, Controlventa, Cotizacion, Cotizacionclientecabecera,
                     Cotizacionclientedetalle, Datoclientedelivey, Documentofactura, Domiciliodetalle,
                     Ejecucionserviciocabecera, Facturacioncaja, Facturaclientecabecera, Facturaclientedetalle,
                     Maestrocajas, Maestrocajeros, Maestroclientetipo, Maestroclientes, Maestrogastoscaja,
                     Maestrohorarioturnopersonal, Maestroimpresora, Maestroplanilla, Maestroplantillaalmacenpedido,
                     Maestroplats, Maestroprecios, Maestrotipocliente, Maestroturnoscaja, Maestrovehiculo,
                     Maestrovehiculoaccesorios, Maestrovehiculoestado, Maestrovendedores, Maestroversionmodelo,
                     Ordencompraclientecabecera, Ordencompraclientedetalle, Maestrovehiculocombustible, Preciario,
                     Recetas, Saldoscaja, Solicituddeproductocabecera, Solicituddeproductodetalle,
                     Solicitudhotlinecabecera, Solicitudhotlinedetalle, Solicitudnotacredito,
                     Solicitudnotacreditoproductounitarioimagen, Tallerfactura, Vendedormetaobjetivo, Ventadescuento,
                     Viaaprobacion)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombres', 'apellidos', 'tipo',
                  'celular', 'estado']
        exclude = ['um', 'fm', 'uc', 'fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-


class CajadetalleForm(forms.ModelForm):
    class Meta:
        model = Cajadetalle
        fields = ['id', 'idcajacabecera', 'codempresa', 'codcaja', 'nrocaja', 'item', 'tipodocumento',
                  'serie', 'numero', 'fechadoc', 'codcuenta', 'codcentrodecostos', 'debe',
                  'glosa', 'moneda', 't_c', 'totalsoles', 'totaldolares', 'hora', 'usuario',
                  'tipocorrentista', 'codproveedor', 'coddistcc', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo', 'tcorrentista', 'procedencia',
                  'diferenciacambio']


class CajeroserieForm(forms.ModelForm):
    class Meta:
        model = Cajeroserie
        fields = ['id', 'idmaestrocajero', 'serie', 'tipodocumento', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class CierrefacturacionForm(forms.ModelForm):
    class Meta:
        model = Cierrefacturacion
        fields = ['id', 'fecha', 'cerrado', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'idtrabajador', 'idempresa', 'idsucursal',
                  'saldoinical', 'fechacierre', 'cajachicadeclara', 'efectivodeclara', 'visadeclara',
                  'masterdeclara', 'valesalimenticiosdeclara', 'valesdeclara', 'creditodeclara',
                  'conspersonaldeclara', 'connopagadodeclara', 'otrosdeclara', 'cajachica', 'efectivo',
                  'visa', 'master', 'valesalimenticios', 'vales', 'credito', 'conspersonal', 'connopagado',
                  'otros', 'codigocajero', 'cajachicasis', 'efectivosis', 'visasis', 'mastersis',
                  'valesalimenticiossis', 'valessis', 'creditosis', 'conspersonalsis', 'connopagadosis', 'otrossil']


class CierrefacturaciondetalleForm(forms.ModelForm):
    class Meta:
        model = Cierrefacturaciondetalle
        fields = ['idcierrefacturaciondetalle', 'idcierrefacturacion', 'idmaestroformadepago',
                  'totaldeclara', 'totalsistema', 'diferencia', 'fecharegistro', 'estado', 'activo']


class CierreordenservicioForm(forms.ModelForm):
    class Meta:
        model = Cierreordenservicio
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idordenserviciocabecera',
                  'idespecialista', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo']


class ClientedireccionForm(forms.ModelForm):
    class Meta:
        model = Clientedireccion
        fields = ['id', 'idmaestrocliente', 'iddomiciliodetalle']


class ClientesmigrarForm(forms.ModelForm):
    class Meta:
        model = Clientesmigrar
        fields = ['tipo_persona', 'tipo_de_documento_de_identidad_del_cliente',
                  'ruc', 'razon_social']


class ControlventaForm(forms.ModelForm):
    class Meta:
        model = Controlventa
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idfacturacabecera', 'numerofactura', 'fecha',
                  'montosoles', 'montodolares', 'idmaestromoneda', 'idmaestrotipocambio', 'porcentaje', 'utilidadsoles',
                  'utilidaddolares', 'idlugar', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado',
                  'activo']


class ContizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idpedidocabecera', 'idpedidodetalle', 'cantidad',
                  'cotizado', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
                  'imagenscaneada']


class CotizacionclientecabeceraForm(forms.ModelForm):
    class Meta:
        model = Cotizacionclientecabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idsolicituddeproductodetalle', 'fechacotizacion',
                  'numero', 'idmaestrocliente', 'servicio', 'equipo', 'modelo', 'anhio', 'unidad', 'placa', 'coloquial',
                  'serie', 'tiempoentrega', 'idlugar', 'valorventasoles', 'valorventadolares', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class CotizacionclientedetalleForm(forms.ModelForm):
    class Meta:
        model = Cotizacionclientedetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idcotizacionclientecabecera', 'idproductoservicio',
                  'producto', 'cantidad', 'preciounitariosoles', 'preciounitariodolares', 'porcentajedescuento',
                  'subtotalsoles', 'subtotaldolares', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo']


class DatoclientedeliveyForm(forms.ModelForm):
    class Meta:
        model = Datoclientedelivey
        fields = ['iddatoclientedelivery', 'telefono', 'numerodocumentoidentidad', 'nombrecliente', 'direccioncliente',
                  'referenciadireccioncliente', 'nombretransportista']


class DocumentofacturaForm(forms.ModelForm):
    class Meta:
        model = Documentofactura
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigosucursal', 'numerodocumentofacbol',
                  'tipomovimiento', 'idtipomovimiento', 'numerodocumentoalmacen', 'idfacturaclientecabecera',
                  'idalmacencabecera', 'idordencompraclientecabecera', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'idordenpedido', 'idtallercabecera', 'texto']


class DomiciliodetalleForm(forms.ModelForm):
    class Meta:
        model = Domiciliodetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrotipovia', 'nombrevia', 'numerovia',
                  'departamento', 'interior', 'manzana', 'lote', 'kilometro', 'block', 'etapa', 'idmaestrotipozona',
                  'nombrezona', 'referenciavivienda', 'idubigeodireccion', 'direccioncompleta', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'idpersonal']


class EjecucionserviciocabeceraForm(forms.ModelForm):
    class Meta:
        model = Ejecucionserviciocabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'numerotarjeta', 'idmaestrotrabajotaller',
                  'idmaestroserviciotaller', 'tiempo', 'tiempotablalavadosecado', 'tiempotablacontrolcalidad',
                  'tiempotablarevisionasesor', 'porcentaje', 'terminado', 'idordenserviciocabecera', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'observacioncontrolista']


class FacturacioncajaForm(forms.ModelForm):
    class Meta:
        model = Facturacioncaja
        fields = ['id', 'descripcion', 'idmaestroempresa', 'idmaestrosucursal', 'activo', 'fechacreacion', 'autorizado',
                  'idmaestrocajero']


class FacturaclientecabeceraForm(forms.ModelForm):
    class Meta:
        model = Facturaclientecabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrodocumentosunat', 'fechaemision',
                  'numeroserie', 'numerodocumentofb', 'idmaestrocliente', 'nombrecliente',
                  'idordencompraclientecabecera', 'idordenpedido', 'factura', 'numerodocumento', 'tipodocumrequerido',
                  'seriedocumentorequerido', 'numerodocumentorequerido', 'tipodocumentooc', 'numerodocumentooc',
                  'diferenciasoles', 'numerodocumentoformapago', 'concepto', 'idmaestrovendedor', 'idmaestrocaja',
                  'tipofactura', 'guiadespacho', 'referenciapresupuesto', 'idmaestrobanco', 'saldopendientesoles',
                  'saldopendientedolares', 'idmaestrocentrodecosto', 'idmaestromoneda', 'idmaestrotipocambio',
                  'totalsoles', 'totaldolares', 'totaligvsoles', 'totaligvdolares', 'idmaestroformapago',
                  'descuentosoles', 'descuentodolares', 'fechavencimiento', 'idcobrador', 'codigocobrador',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'imprimida', 'detalle',
                  'anulada', 'estadodocumento', 'tipodecambio', 'afectoigv', 'importecanceladosoles',
                  'importecanceladodolares', 'items', 'usuario', 'imprimedocumento', 'requesicion', 'adelanto',
                  'tienedetraccion', 'esformatolargo', 'numerocontable', 'idvouchercabecera', 'idmaestrocajero',
                  'fechaimpresion', 'idtipodocumentoimprimeen', 'seriedocumentoimprimeen', 'numerodocumentoimprimeen',
                  'noesfacturadetallada', 'idaccionnotadecredito', 'idmotivonotadecredito', 'idmaestroturnocaja',
                  'idmaestrovehiculo', 'idmaestroalmacen', 'condescargoporalmacen', 'direccioncliente',
                  'totalvaletarjetasoles', 'iddatoclientedelivery', 'efectivovale', 'tipoventa',
                  'telefonodatoclienteref', 'clienteallamardatoclienteref', 'clientedirecciondatoclienteref',
                  'clientedireccionreferenciadatoclienteref', 'transportistadatoclienteref', 'firma', 'bolsas']


class FacturaclientedetalleForm(forms.ModelForm):
    class Meta:
        model = Facturaclientedetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idfacturaclientecabecera', 'trabajotaller',
                  'serviciotaller', 'producto', 'idproductoservicio', 'cantidad', 'subtotalsoles', 'subtotaldolares',
                  'preciosoles', 'preciodolares', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado',
                  'activo', 'productolibre', 'requesicion']


class MaestrocajasForm(forms.ModelForm):
    class Meta:
        model = Maestrocajas
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigosucursal', 'codigocaja', 'numerocaja',
                  'tipocaja', 'idmaestromoneda', 'moneda', 'nombre', 'fechamodificado', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo', 'codigocuentacontable']


class MaestrocajerosForm(forms.ModelForm):
    class Meta:
        model = Maestrocajeros
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigocajero', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo', 'id_usuario']


class MaestroclientetipoForm(forms.ModelForm):
    class Meta:
        model = Maestroclientetipo
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotipocliente', 'descripcion', 'fechamodificado',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo', 'descripcionadicional']


class MaestroclientesForm(forms.ModelForm):
    class Meta:
        model = Maestroclientes
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrotipocliente', 'codigotipocliente',
                  'codigosucursal', 'codigocliente', 'razonsocial', 'nombres', 'primerapellido', 'segundoapellido',
                  'fechanacimiento', 'nombrepadre', 'nombremadre', 'viatipo', 'vianombre', 'numero', 'interior', 'zona',
                  'idubigeo', 'codigociudad', 'idmaestrotipodocumento', 'numerodocumentoidentificacion',
                  'personajuridica', 'ruc', 'contacto', 'telefono1', 'telefono2', 'telefonocelular', 'email', 'fax',
                  'fecharegistro', 'limitecreditosoles', 'limitecreditodolares', 'montototaldeudasoles',
                  'montototaldeudadolares', 'observaciones', 'codigocobrador', 'codigozona', 'codigoestado',
                  'agenteretencion', 'fechamodificado', 'numeromaximoordenservicio', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo', 'direccioncompleta', 'listaaprobda',
                  'idclienteempresa']


class MaestrogastoscajaForm(forms.ModelForm):
    class Meta:
        model = Maestrogastoscaja
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigogasto', 'nombregasto', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrohorarioturnopersonalForm(forms.ModelForm):
    class Meta:
        model = Maestrohorarioturnopersonal
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'lunesingeso', 'martesingeso', 'miercolesingeso',
                  'juevesingeso', 'viernesingeso', 'sabadoingeso', 'domingoingeso', 'lunessalida', 'martessalida',
                  'miercolessalida', 'juevessalida', 'viernessalida', 'sabadosalida', 'domingosalida', 'lunesingesoii',
                  'martesingesoii', 'miercolesingesoii', 'juevesingesoii', 'viernesingesoii', 'sabadoingesoii',
                  'domingoingesoii', 'lunessalidaii', 'martessalidaii', 'miercolessalidaii', 'juevessalidaii',
                  'viernessalidaii', 'sabadosalidaii', 'domingosalidaii', 'codigousuario', 'accion', 'fechacreacion',
                  'autorizado', 'estado', 'activo']


class MaestroimpresoraForm(forms.ModelForm):
    class Meta:
        model = Maestroimpresora
        fields = ['idimpresora', 'nombreimpresora', 'idalmacen', 'activo', 'fechamodificado', 'idarea',
                  'idmaestroempresa']


class MaestroplanillaForm(forms.ModelForm):
    class Meta:
        model = Maestroplanilla
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoplanilla', 'idtipoplanilla',
                  'idmaestrotiposervidor', 'idcentrodecostos', 'tituloplanilla', 'tituloplanillaabreviado',
                  'fechainicio', 'fechatermino', 'anio', 'mes', 'semana', 'diasnormales', 'dominical',
                  'porcentajedescuentocuentacorriente', 'cerrada', 'pagosegurovida', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo', 'numeroasientoctb', 'boletagenerada',
                  'fechacontabilizacion', 'conboleta']


class MaestroplantillaalmacenpedidoForm(forms.ModelForm):
    class Meta:
        model = Maestroplantillaalmacenpedido
        fields = ['idplantilla', 'idmaestroempresa', 'idmaestroalmacen', 'idmaestroarea', 'idmaestroproducto',
                  'cantidad', 'fechahoraregistro']


class MaestroplatsForm(forms.ModelForm):
    class Meta:
        model = Maestroplats
        fields = ['id', 'descripccionplato', 'idunidadmedida', 'idgrupo', 'idproducto1', 'idproducto2', 'idproducto3',
                  'idproducto', 'lunes', 'luneshoraini1', 'luneshorafin1', 'luneshoraini2', 'luneshorafin2', 'martes',
                  'marteshoraini1', 'marteshorafin1', 'marteshoraini2', 'marteshorafin2', 'miercoles',
                  'miercoleshoraini1', 'miercoleshorafin1', 'miercoleshoraini2', 'miercoleshorafin2', 'jueves',
                  'jueveshoraini1', 'jueveshorafin1', 'jueveshoraini2', 'jueveshorafin2', 'viernes', 'vierneshoraini1',
                  'vierneshorafin1', 'vierneshoraini2', 'vierneshorafin2', 'sabado', 'sabhoraini1', 'sabhorafin1',
                  'sabhoraini2', 'sabhorafin2', 'domingo', 'domhoraini1', 'domhorafin1', 'domhoraini2', 'domhorafin2',
                  'activo', 'idmaestroempresa']


class MaestropreciosForm(forms.ModelForm):
    class Meta:
        model = Maestroprecios
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigosucursal', 'idmaestroproducto',
                  'codigoproducto', 'fechavigencia', 'descripcion', 'precioventasoles', 'fechamodificado',
                  'precioventadolares', 'porcentaje1', 'porcentaje2', 'porcentaje3', 'preciototalsoles',
                  'preciototaldolares', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipoclienteForm(forms.ModelForm):
    class Meta:
        model = Maestrotipocliente
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotipocliente', 'descripcion', 'fechamodificado',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroturnoscajaForm(forms.ModelForm):
    class Meta:
        model = Maestroturnoscaja
        fields = ['id', 'idmaestrocajero', 'idmaestroempresa', 'descripcion', 'fechainicio', 'fechafin', 'horainicio',
                  'horafin', 'autorizado', 'activo', 'fechacreacion', 'accion', 'turnocerrado']


class MaestrovehiculoForm(forms.ModelForm):
    class Meta:
        model = Maestrovehiculo
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'placarodaje', 'color', 'tipo', 'idmaestromarca',
                  'motor', 'modelo', 'chasis', 'nrounidad', 'kilometraje', 'anhiofabricacion', 'placaoval',
                  'idmaestrocliente', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo',
                  'idtallerasesores', 'coordenadax', 'coordenaday', 'pisoid', 'idmaestrooperacion', 'pertenencia']


class MaestrovehiculoaccesoriosForm(forms.ModelForm):
    class Meta:
        model = Maestrovehiculoaccesorios
        fields = ['id', 'descripcion', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class MaestrovehiculocombustibleForm(forms.ModelForm):
    class Meta:
        model = Maestrovehiculocombustible
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrovehiculoestadoForm(forms.ModelForm):
    class Meta:
        model = Maestrovehiculoestado
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrovendedoresForm(forms.ModelForm):
    class Meta:
        model = Maestrovendedores
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigosucursal', 'codigovendedor', 'nombrevendedor',
                  'direccion', 'telefono', 'fechaingreso', 'tipo', 'metaventasoles', 'metaventadolares',
                  'metacobranzasoles', 'metacobranzadolares', 'comisionsoles', 'comisiondolares', 'garantias',
                  'fechamodificado', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo',
                  'codigoservidor', 'idusuariosistema']


class MaestroversionmodeloForm(forms.ModelForm):
    class Meta:
        model = Maestroversionmodelo
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'nombreversion', 'idvehiculomodelo', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class OrdencompraclientecabeceraForm(forms.ModelForm):
    class Meta:
        model = Ordencompraclientecabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'fechadocumento', 'numerodocumento',
                  'idsolicituddeproductocabecera', 'idmaestrocliente', 'idmaestromoneda', 'idmaestrotipocambio',
                  'totaligvsoles', 'totaligvdolares', 'totalsoles', 'totaldolares', 'tiempoentrega', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'estadodocumento', 'observacion']


class OrdencompraclientedetalleForm(forms.ModelForm):
    class Meta:
        model = Ordencompraclientedetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idordencompraclientecabecera',
                  'idcotizacionclientedetalle', 'preciounitariosoles', 'preciounitariodolares', 'idmaestroproducto',
                  'cantidad', 'porcentajedescuento', 'descuentomontosoles', 'descuentomontodolares', 'subtotalsoles',
                  'subtotaldolares', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
                  'esproducto']


class PreciarioForm(forms.ModelForm):
    class Meta:
        model = Preciario
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrosmodelo', 'nombremodelo', 'version',
                  'numeromotor', 'transmision', 'idmaestrotrabajotaller', 'mantenimiento', 'montoproductos',
                  'montomanoobra', 'montomateriales', 'idmaestroactividadtaller', 'tiempominutos', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class RecetasForm(forms.ModelForm):
    class Meta:
        model = Recetas
        fields = [
            'idprincipal', 'idcomponente', 'cantidad', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
            'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20',
            'f21', 'f22', 'f23', 'f24', 'f25', 'f26'
        ]


class SaldoscajaForm(forms.ModelForm):
    class Meta:
        model = Saldoscaja
        fields = [
            'id', 'idmaestroempresa', 'codigoempresa', 'esdebe', 'importesoles', 'importedolares',
            'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo'
        ]


class SolicituddeproductocabeceraForm(forms.ModelForm):
    class Meta:
        model = Solicituddeproductocabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrocliente', 'fechasolicitud', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class SolicituddeproductodetalleForm(forms.ModelForm):
    class Meta:
        model = Solicituddeproductodetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idsolicituddeproductocabecera', 'cantidad',
                  'idmaestroproducto', 'modelo', 'numero', 'anhio', 'unidad', 'chasis', 'motor', 'observacion',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class SolicitudhotlinecabeceraForm(forms.ModelForm):
    class Meta:
        model = Solicitudhotlinecabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrocliente', 'fechasolicitud',
                  'numerosolicitud', 'solicitante', 'prioridad', 'ordentaller', 'tipoordentaller', 'asesor', 'tecnico',
                  'idmaestrovehiculo', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class SolicitudhotlinedetalleForm(forms.ModelForm):
    class Meta:
        model = Solicitudhotlinedetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idsolicitudhotlinecabecera', 'idmaestroproducto',
                  'idalmacenubicacionproducto', 'cf', 'cantidad', 'observacion', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo']


class SolicitudnotacreditoForm(forms.ModelForm):
    class Meta:
        model = Solicitudnotacredito
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'fechasolicitud', 'motivo', 'otromotivo',
                  'detallemotivo', 'idmaestroproducto', 'idfacturaproveedordetalle', 'idproductounitarioimagen',
                  'cantidad', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'empresa',
                  'direccion', 'ruc', 'telefono', 'email', 'contacto', 'fechafactura', 'producto']


class SolicitudnotacreditoproductounitarioimagenForm(forms.ModelForm):
    class Meta:
        model = Solicitudnotacreditoproductounitarioimagen
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idproductounitarioimagen', 'idsolicitudnotacredito',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class TallerfacturaForm(forms.ModelForm):
    class Meta:
        model = Tallerfactura
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idfacturaclientecabecera', 'idordenserviciocabecera',
                  'idservicioportercerocabecera', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado',
                  'activo']


class VendedormetaobjetivoForm(forms.ModelForm):
    class Meta:
        model = Vendedormetaobjetivo
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrovendedor', 'idvehiculomodelo',
                  'cantidadplanificada', 'cantidadalcanzada', 'fechainicio', 'fechafin', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class VentadescuentoForm(forms.ModelForm):
    class Meta:
        model = Ventadescuento
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'porcentaje', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class ViaaprobacionForm(forms.ModelForm):
    class Meta:
        model = Viaaprobacion
        fields = ['id', 'descripcion', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']
