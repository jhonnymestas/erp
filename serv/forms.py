from django import forms


from .models import Guiaservicio, Historiaalertasistema, Historiaclinicadetalle, \
    Maestroactividadtaller, Maestroserviciorepuesto, Maestroserviciotaller, \
    Maestroservicios, Maestrotecnico, Ordenpedido, Ordenpedidocliente, Ordenpedidodetalle, Ordenserviciocabecera, \
    Ordenserviciodetalle, Ordenservicionivelcombustible, Ordenservicioproductosdetalle, Ordenserviciotipoaveria, \
    Ordenserviciotrabajoadicional, Servicioportercerocabecera, Servicioportercerodetalle, Tallerasesores, \
    Tallerkilometraje, Tallerordenservicioimagen, Tallervehiculo, Tipobienoservicio, Tiposolicitud


class GuiaservicioForm(forms.ModelForm):
    class Meta:
        model = Guiaservicio
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'numero', 'idmaestroproveedor', 'numerofactura',
                  'unidad', 'idcotizacion', 'idmaestromoneda', 'idmaestrotipocambio', 'utilidadsoles',
                  'utilidaddolares', 'costosoles', 'costodolares', 'idmaestroproducto', 'observacion', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class HistoriaalertasistemaForm(forms.ModelForm):
    class Meta:
        model = Historiaalertasistema
        fields = ['id', 'nombremodulo', 'asunto', 'idusuario', 'fechacreacion', 'accion', 'estado', 'activo']


class HistoriaclinicadetalleForm(forms.ModelForm):
    class Meta:
        model = Historiaclinicadetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroalmacen', 'codigalmacen',
                  'idordenserviciocabecera', 'numeroordenservicio', 'esservicio', 'idmaestrotiposdocumentos',
                  'tipomovimiento', 'nrodocumento', 'codigoproducto', 'cantidad', 'moneda', 'preciounitario',
                  'valorventa', 'porcentajedescuento', 'descuentomonto', 'impuesto', 'totalventa',
                  'preciounitariodolares', 'valorventadolares', 'descuentomontodolares', 'impuestodolares',
                  'totalventadolares', 'realizadopor', 'fechaoperacion', 'descripcionservicioproducto',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'idalmacencabecera',
                  'valorcomprasoles', 'valorcompradolares', 'esmigracion']


class MaestroactividadtallerForm(forms.ModelForm):
    class Meta:
        model = Maestroactividadtaller
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoservicio', 'nombre', 'preciosoles',
                  'preciodolar', 'modelo', 'tiempo', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado',
                  'activo', 'codigocuentacontable', 'orden']


class MaestroserviciorepuestoForm(forms.ModelForm):
    class Meta:
        model = Maestroserviciorepuesto
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'idmaestroactividadtaller',
                  'idmaestroproducto', 'cantidad', 'fechamodificado', 'codigousuario', 'accion', 'fechacreacion',
                  'autorizado', 'estado', 'activo', 'idmaestrosmodelo', 'nombremodelo', 'version', 'numeromotor',
                  'transmision', 'idpreciario']


class MaestroserviciotallerForm(forms.ModelForm):
    class Meta:
        model = Maestroserviciotaller
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroactividadtaller', 'idmaestrotrabajotaller',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class MaestroserviciosForm(forms.ModelForm):
    class Meta:
        model = Maestroservicios
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoservicio', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotecnicoForm(forms.ModelForm):
    class Meta:
        model = Maestrotecnico
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotecnico', 'nombretecnico', 'direccion',
                  'telefono', 'fecharegistro', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado',
                  'activo', 'libre', 'tiniciados']


class OrdenpedidoForm(forms.ModelForm):
    class Meta:
        model = Ordenpedido
        fields = [
            'id', 'idmaestroempresa', 'idmaestrosucursal', 'numeropedido', 'idmaestrovendedor', 'codigovendedor',
            'idmaestrocliente', 'idmaestroclientey_o', 'codigocliente', 'idmaestroalmacen', 'idmaestroproducto',
            'partenissan', 'codigoproducto', 'idmaestrotipopago', 'condicionpago', 'color', 'clase', 'modelo', 'anho',
            'carroceria', 'marca', 'numeroserie', 'numeromotor', 'ejes', 'cilindros', 'ruedas', 'pasajeros', 'asientos',
            'puertas', 'pesoseco', 'pesobruto', 'cargautil', 'largo', 'alto', 'ancho', 'idmaestrovehiculocombustible',
            'combustible', 'distancia_ejes', 'cilindrada', 'preciocontado', 'otrosgastos', 'registrofiscal',
            'descuentos', 'totalprecioventa', 'saldofinanciadomes', 'observaciones', 'idmaestrodocumentosunat', 'serie',
            'numerodocumento', 'numerovehiculo', 'valorcompradolares', 'idtipoformadepago', 'codigoformadepago',
            'descripcionotrosgastos', 'observacionespedido', 'p_operacion', 'potencia', 'capacidadm3', 'desplazamiento',
            'accesorios', 'dua', 'fechasolicitud', 'pedidonissan', 'fechallegadaapuerto', 'factura_boleta',
            'codigocomercial', 'numerodeseparacion', 'codigocolorexterior', 'codigocolorinterior', 'imprimir1',
            'imprimir2', 'placaoval', 'idmaestromoneda', 'moneda', 'usuariomodificacion', 'fechamodificacion',
            'numeroseparacion', 'numeroembarque', 'numerocase', 'placa', 'codigousuario', 'fechacreacion', 'accion',
            'autorizado', 'estado', 'activo', 'estadodocumento', 'facturada', 'km', 'fecha', 'llave', 'lote',
            'idmaestrocliente2', 'notacreditonumero', 'notacreditoserie', 'notacreditomonto',
            'idcaracteristicavehiculo', 'idmaestroproveedor', 'importeflete', 'importetramitetarjetaplaca',
            'idmaestroalmacenequipamiento', 'fechallegadavehiculo', 'horallegadavehiculo', 'fechaentregavehiculo',
            'horaentregavehiculo', 'codigomvc', 'idmaestroequipamiento'
        ]


class OrdenpedidoclienteForm(forms.ModelForm):
    class Meta:
        model = Ordenpedidocliente
        fields = [
            'idordenpedido', 'idmaestrocliente', 'codigousuario', 'fechacreacion', 'accion', 'estado', 'activo', 'id'
        ]


class OrdenpedidodetalleForm(forms.ModelForm):
    class Meta:
        model = Ordenpedidodetalle
        fields = [
            'idordenpedidodetalle', 'idordenpedidocabecera', 'cantidad', 'descripcion', 'idmaestroproducto',
            'preciounitarioventasoles', 'preciounitarioventadolares', 'fechacreacion', 'activo'
        ]


class OrdenserviciocabeceraForm(forms.ModelForm):
    class Meta:
        model = Ordenserviciocabecera
        fields = [
            'id', 'idmaestroempresa', 'idmaestrosucursal', 'numerotarjeta', 'idmaestrotipoorden', 'idmaestrocliente',
            'idmaestroclientefactura', 'idrecepcionadopor', 'fecharecepcion', 'descripcion', 'numerocono',
            'idmaestroestadosdeatencion', 'idmaestrovehiculo', 'idmaestromoneda', 'idmaestrotipodecambio',
            'fechaentrega', 'horaentrega', 'idmaestroformasdepago', 'totalsoles', 'totaldolares', 'anulado',
            'numeroorden', 'kilometraje', 'niveldecombustible', 'codigousuario', 'fechacreacion', 'accion',
            'autorizado', 'estado', 'activo', 'terminado', 'lavado', 'secado', 'controlcalidad', 'revisionasesor',
            'listo', 'porordende', 'estadodocumento', 'codigotecnico', 'horatentativaentrega', 'numerodecono',
            'observacion', 'cita', 'esfactura', 'tiempo', 'hojadiagn1', 'hojadiagn2', 'hojadiagn3', 'hojadiagn4',
            'hojadiagn5', 'hojadiagn6', 'hojadiagn7', 'hojadiagn8', 'hojadiagn9', 'porordendetelefono', 'porordendedni',
            'porordendecorreo', 'usuario', 'idpreciario', 'montoproductosservicio', 'montomateriales',
            'mantenimientoreal', 'idtallercitas', 'observaciondocumentoreferencia'
        ]


class OrdenserviciodetalleForm(forms.ModelForm):
    class Meta:
        model = Ordenserviciodetalle
        fields = [
            'id', 'idmaestroempresa', 'idmaestrosucursal', 'idordenserviciocabecera', 'idmaestrotrabajotaller',
            'idmaestroserviciotaller', 'idmaestrotescnico', 'cantidad', 'subtotalsoles', 'subtotaldolares',
            'preciosoles', 'preciodolares', 'observacion', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
            'estado', 'activo', 'duracionminutos', 'descripcion', 'esproducto', 'descuento', 'precioprodref',
            'preciomaterialesref'
        ]


class OrdenservicionivelcombustibleForm(forms.ModelForm):
    class Meta:
        model = Ordenservicionivelcombustible
        fields = [
            'id', 'idmaestroempresa', 'idmaestrosucursal', 'x', 'y', 'idmaestrovehiculo', 'observacion',
            'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo'
        ]


class OrdenservicioproductosdetalleForm(forms.ModelForm):
    class Meta:
        model = Ordenservicioproductosdetalle
        fields = [
            'id', 'idmaestroempresa', 'idmaestrosucursal', 'idordenserviciodetalle', 'idmaestroactividadtaller',
            'idmaestroproducto', 'cantidad', 'subtotalsoles', 'subtotaldolares', 'preciosoles', 'preciodolares',
            'recogido', 'cantidadrecogida', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo'
        ]


class OrdenserviciotipoaveriaForm(forms.ModelForm):
    class Meta:
        model = Ordenserviciotipoaveria
        fields = [
            'id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrotipoaveria', 'x', 'y', 'idorderserviciocabecera',
            'idmaestrovehiculo', 'observacion', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado',
            'activo'
        ]


class OrdenserviciotrabajoadicionalForm(forms.ModelForm):
    class Meta:
        model = Ordenserviciotrabajoadicional
        fields = [
            'id', 'idmaestroempresa', 'idmaestrosucursal', 'idordenserviciocabecera', 'numeroordenserviciocabecera',
            'personaqueautoriza', 'descripciontrabajo', 'telefono', 'aprobacion', 'formacomunicaciontelefono',
            'formacomunicacioncorreo', 'nuevafechahoraentrega', 'preciosoles', 'preciodolares', 'tiempotabla',
            'codigousuario', 'fechacreacion', 'autorizado', 'estado', 'activo', 'preciosolesmanoobra',
            'preciosolesrepuesto'
        ]


class ServicioportercerocabeceraForm(forms.ModelForm):
    class Meta:
        model = Servicioportercerocabecera
        fields = [
            'id', 'idmaestroempresa', 'idmaestrosucursal', 'idordenserviciocabecera', 'nombreproveedor',
            'rucproveedor', 'idmaestrodocumentosunat', 'idmaestromoneda', 'idmaestrotipocambio',
            'porcentajeadicional', 'totalsoles', 'totaldolares', 'totalcompletosoles', 'totalcompletodolares',
            'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
            'numerodocumentoreferido', 'seriedocumentoreferido', 'idmaestromonedaventa', 'fechadocumento'
        ]


class ServicioportercerodetalleForm(forms.ModelForm):
    class Meta:
        model = Servicioportercerodetalle
        fields = [
            'id', 'idmaestroempresa', 'idmaestrosucursal', 'idservicioportercabecera', 'cantidad',
            'preciounitariosoles', 'preciounitariodolares', 'descripcion', 'subtotalsoles', 'subtotaldolares',
            'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
            'fechahorainicioservicio', 'fechahorafinservicio', 'horainicio', 'horafin', 'idmaestroproveedor',
            'porcentajeadicional'
        ]


class TallerasesoresForm(forms.ModelForm):
    class Meta:
        model = Tallerasesores
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'nombres', 'apellido_paterno', 'apellido_materno',
                  'nombre_completo', 'id_estacion', 'imagen', 'codigousuario', 'accion', 'fechacreacion', 'autorizado',
                  'estado', 'activo', 'idmaestropersonal']


class TallerkilometrajeForm(forms.ModelForm):
    class Meta:
        model = Tallerkilometraje
        fields = ['id', 'km']


class TallerordenservicioimagenForm(forms.ModelForm):
    class Meta:
        model = Tallerordenservicioimagen
        fields = ['id', 'descripcion', 'rutaimagen', 'idordenserviciocabecera', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo', 'codigousuario']


class TallervehiculoForm(forms.ModelForm):
    class Meta:
        model = Tallervehiculo
        fields = ['id', 'marca', 'modelo', 'placa']


class TipobienoservicioForm(forms.ModelForm):
    class Meta:
        model = Tipobienoservicio
        fields = ['id', 'usuarioid', 'codigo', 'nombre', 'descripcion', 'estadoregistro', 'fechahoraregistro']


class TiposolicitudForm(forms.ModelForm):
    class Meta:
        model = Tiposolicitud
        fields = ['id', 'descripcion', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']
