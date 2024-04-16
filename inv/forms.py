# from builtins import classmethod

from django import forms

from .models import Categoria, SubCategoria, Marca, \
    UnidadMedida, Producto


# Importación correspondiente de las tablas tipo: ALMACEN
from .models import Ajustealmacen, AlmAreas, Almacencabecera, Almacenconfiguracion, Almacendetalle, \
    Almacenubicacionproducto, Areagrupo, Areas, Cierrealmacen, Componenteproducto, Detallegrupo, \
    Expedientedetalleregistrospublico, Experiencialaboralpersonal, Formagrupo, Guiaremisioncabecera, \
    Guiaremisiondetalle, Maestroaccesoriosequipamiento, Maestroalmacenoperaciones, Maestrogrupos, \
    Maestromotivosingresoalmacen, Maestromotivossalidaalmacen, Maestroproductocomplementario, Maestroproductoimagen, \
    Maestroproductokit, Maestroproductos, Maestroproductosustituto, Maestrotipolinea, Maestrotiporotacion, Pedplant, \
    Pedidocabecera, Pedidodetalle, Pedidogenericodetalle, Pedidogenericodetalleanulacion, Principalgrupo, Produc, \
    Productoazar, Productodescuento, Productos5Dec, Productounitarioimagen, Saldoareahistorial, Saldosdelanhio, \
    Saldosxalmacenes, Saldosxarea, Stock, Tablaimagen, Tamaniogrupo, Tipogrupo, Transformacioncabecera, \
    Transformaciondetalle, Trasladounidad, Usuarioalmacen


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción de la Categoría",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )

    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado']
        labels = {'descripcion': "Sub Categoría",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['categoria'].empty_label = "Seleccione Categoría"


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción de la Marca",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class UMForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción de la Marca",
                  "estado": "Estado"}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'codigo_barra', 'descripcion', 'estado',
                  'precio', 'existencia', 'ultima_compra',
                  'marca', 'subcategoria', 'unidad_medida', 'foto']
        exclude = ['um', 'fm', 'uc', 'fc']
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True


# *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*


class MaestromotivosingresoalmacenForm(forms.ModelForm):
    class Meta:
        model = Maestromotivosingresoalmacen
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestromotivossalidaalmacenForm(forms.ModelForm):
    class Meta:
        model = Maestromotivossalidaalmacen
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class AlmAreasForm(forms.ModelForm):
    class Meta:
        model = AlmAreas
        fields = ['idalm_area', 'idempresa', 'idsucursal', 'idalmacen', 'descripcion', 'activo']


class TipogrupoForm(forms.ModelForm):
    class Meta:
        model = Tipogrupo
        fields = ['idtipogrupo', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroalmacen', 'codigotipogrupo',
                  'descripcion', 'autorizado', 'fechacreacion', 'activo', 'accion']


class TamaniogrupoForm(forms.ModelForm):
    class Meta:
        model = Tamaniogrupo
        fields = ['idtamaniogrupo', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroalmacen', 'codigotamaniogrupo',
                  'descripcion', 'autorizado', 'fechacreacion', 'activo', 'accion']


class PrincipalgrupoForm(forms.ModelForm):
    class Meta:
        model = Principalgrupo
        fields = ['idprincipalgrupo', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroalmacen',
                  'codigoprincipalgrupo', 'descripcion', 'autorizado', 'fechacreacion', 'activo', 'accion']


class FormagrupoForms(forms.ModelForm):
    class Meta:
        model = Formagrupo
        fields = ['idformagrupo', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroalmacen', 'codigoformagrupo',
                  'descripcion', 'autorizado', 'fechacreacion', 'activo', 'accion']


class DetallegrupoForm(forms.ModelForm):
    class Meta:
        model = Detallegrupo
        fields = ['iddetallegrupo', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroalmacen', 'codigodetallegrupo',
                  'descripcion', 'autorizado', 'fechacreacion', 'activo', 'accion']


class AreagrupoForm(forms.ModelForm):
    class Meta:
        model = Areagrupo
        fields = ['idmaestroempresa', 'idmaestrosucursal', 'idmaestroalmacen',
                  'codigoareagrupo', 'descripcion', 'autorizado', 'fechacreacion',
                  'activo', 'accion']


class AreasForm(forms.ModelForm):
    class Meta:
        model = Areas
        fields = ['id', 'codigoarea', 'descripcion', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo', 'idmaestroempresa',
                  'idmaestrosucursal']


class MaestroproductosForm(forms.ModelForm):
    class Meta:
        model = Maestroproductos
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoproducto', 'nombrecomercial', 'descripcion',
                  'idmaestrounidadesdemedida', 'codigounidadmedida', 'medida', 'idmaestrolineascomerciales',
                  'codigolineacomercial', 'procedencia', 'codigoubicacion', 'codigogrupo', 'costopromediosoles',
                  'costopromediodolares', 'fechacostopromedio', 'ultimocostosoles', 'ultimocostodolares',
                  'fechaultimocosto', 'fechaultimomovimiento', 'precioventasoles', 'precioventadolares',
                  'totalingresos', 'totalsalidas', 'stockmaximo', 'stockminimo', 'saldo', 'recalcular', 'desdemes',
                  'desdeanhio', 'margen', 'ingresosvencidos', 'salidasvencidas', 'saldovencidos', 'loteproduccion',
                  'codigoaplicacion', 'kilos', 'fechamodificado', 'numeroparte', 'equipoproteccionp',
                  'tipoactualizacion', 'rotacion', 'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado',
                  'activo', 'servicio', 'clasificacion', 'cantidadsugerida', 'precioventamanual', 'manodeobra',
                  'unidadmedidaentero', 'factordeconversion', 'controlasaldo', 'idareagrupo', 'iddetallegrupo',
                  'idformagrupo', 'idprincipalgrupo', 'idtaminiogrupo', 'idtipogrupo', 'idcomponentebase']


class ProductodescuentoForm(forms.ModelForm):
    class Meta:
        model = Productodescuento
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroproducto', 'descripcion', 'porcentaje',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class AjustealmacenForm(forms.ModelForm):
    class Meta:
        model = Ajustealmacen
        fields = ['id', 'codigoajuste', 'idmaestroproducto', 'cantidad', 'tipoajuste',
                  'fechamovimientoreferencial', 'idareaorigen', 'idareadestino', 'motivo',
                  'comentario', 'codigousuario', 'fechahoraregistro', 'estadoregistro',
                  'idmaestrosucursal', 'tiposucursal', 'idobservaciontipo']


class AlmacencabeceraForm(forms.ModelForm):
    class Meta:
        model = Almacencabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroalmacen', 'codigoalmacen',
                  'idmaestromotivosingresoalmacen', 'idmaestromotivossalidaalmacen', 'tipomovimiento',
                  'numerooperacion', 'fechaoperacion', 'idmaestroproveedor', 'codigoproveedor',
                  'tipodocumentoreferido', 'numeroserie', 'numerodocumentoreferido', 'idmaestrocliente',
                  'codigocliente', 'idmaestromoneda', 'moneda', 'idmaestrotipocambio', 'tipocambio',
                  'totaldescuentosoles', 'totaldescuentodolares', 'importetotalsoles', 'importetotaldolares',
                  'completada', 'procesado', 'idmaestroformadepago', 'codigoformapago', 'idmaestrovendedor',
                  'codigovendedor', 'anulado', 'codigousuario', 'fechacreacion', 'accion', 'autorizado',
                  'estado', 'activo', 'estadodocumento', 'codigocentrocosto', 'conigv', 'fechavencimiento',
                  'idordendecompra', 'tieneextorno']


class AlmacenconfiguracionForm(forms.ModelForm):
    class Meta:
        model = Almacenconfiguracion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigosolicitudhotline',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class AlmacendetalleForm(forms.ModelForm):
    class Meta:
        model = Almacendetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idalmacencabecera', 'idmaestroalmacen',
                  'codigoalmacen', 'numerooperacion', 'idtipomovimiento', 'movimiento', 'almacenorigendestino',
                  'idmaestroproducto', 'codigoproducto', 'cantidad', 'saldooperacion', 'costosoles', 'costodolares',
                  'preciocostosoles', 'preciocostodolares', 'precioventasoles', 'precioventadolares',
                  'idproductodescuento', 'porcentajedescuento', 'descuentodolares', 'descuentosoles',
                  'desglosefacturas', 'entregafutura', 'numerodesglose', 'fletesoles', 'fletedolares',
                  'gastosadministracionsoles', 'gastosadministraciondolares', 'codigousuario', 'fechacreacion',
                  'accion', 'autorizado', 'estado', 'activo', 'descuentoporcentajeflota', 'idmaestrocentrodecosto',
                  'costoacumuladosoles', 'costoacumuladodolares', 'iddetallereferencia', 'cantidadenteros',
                  'idareaorigen', 'idareaprocedencia', 'costooperativosoles', 'costooperativodolares']


class AlmacenubicacionproductoForm(forms.ModelForm):
    class Meta:
        model = Almacenubicacionproducto
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroproducto',
                  'idmaestroalmacendetalle', 'idmaestrocubiculo', 'idmaestrovehiculo',
                  'fechaproduccion', 'codigocubiculo', 'loteproduccion',
                  'caracteristicalote', 'placarodaje', 'color', 'tipo',
                  'idvehiculomarca', 'idvehiculomodelo', 'motor', 'chasis',
                  'numerounidad', 'kilometraje', 'anhiofabricacion', 'placaoval',
                  'clavecomercial', 'idmaestrocliente', 'idordenpedido',
                  'idmaestrovehiculoestado', 'idmaestrovendedor',
                  'idmaestrovehiculocombustible', 'fechallegada', 'valorsoles',
                  'valordolares', 'llavero', 'placa', 'numeromotor', 'recogida',
                  'numeropoliza', 'fechallegadapoliza', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class CierrealmacenForm(forms.ModelForm):
    class Meta:
        model = Cierrealmacen
        fields = ['id', 'idmaestroalmacen', 'idmaestroempresa', 'idmaestrosucursal', 'numeroalmacen',
                  'fechacierrealmacen', 'glosa', 'numerooperacioningreso', 'numerooperacionsalida',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class ComponenteproductoForm(forms.ModelForm):
    class Meta:
        model = Componenteproducto
        fields = ['idcomponente', 'idmaestroproductopadre', 'idmaestroproducto', 'cantidad', 'observaciones',
                  'estadoregistro', 'fechacreacion', 'idarea', 'descripcionimpresion']


class ExpedientedetalleregistrospublicoForm(forms.ModelForm):
    class Meta:
        model = Expedientedetalleregistrospublico
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroexpediente', 'titulo', 'fecharecepcion',
                  'cargo', 'descripcionobservacion', 'observacion', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo']


class ExperiencialaboralpersonalForm(forms.ModelForm):
    class Meta:
        model = Experiencialaboralpersonal
        fields = ['idexperiencialaboralpersonal', 'fechainicio', 'fechacese', 'motivo', 'institucion', 'observacion',
                  'cargo', 'idmaestropersonal', 'activo', 'usuario', 'fechacreacion']


class GuiaremisioncabeceraForm(forms.ModelForm):
    class Meta:
        model = Guiaremisioncabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idtrabajador', 'numero', 'idsucursalorigen',
                  'idsucursaldestino', 'idmaestrocliente', 'idmaestrotransportista', 'fechatraslado', 'idmaestromotivo',
                  'marca', 'placa', 'licenciaconducir', 'iddocumentopago', 'numeropago', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'tipoguiaremision', 'idalmacenorigen',
                  'idmaestroempresadestino', 'serie', 'idmarcavehiculo', 'idalmacendestino', 'direcciondestino',
                  'estadoguiaremision', 'esguiaexterna', 'seriepago', 'direccionorigen', 'pesototal']


class GuiaremisiondetalleForm(forms.ModelForm):
    class Meta:
        model = Guiaremisiondetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idguiaremisioncabecera', 'idmaestroproducto',
                  'cantidad', 'cantidadentero', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado',
                  'activo', 'productolibre', 'idareadestino', 'idareaorigen', 'cantidadactualizada']


class MaestroaccesoriosequipamientoForm(forms.ModelForm):
    class Meta:
        model = Maestroaccesoriosequipamiento
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcionaccesorioequipamiento', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class MaestroalmacenoperacionesForm(forms.ModelForm):
    class Meta:
        model = Maestroalmacenoperaciones
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigooperacion', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrogruposForm(forms.ModelForm):
    class Meta:
        model = Maestrogrupos
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroalmacen', 'codigogrupo', 'codigoalmacen',
                  'descripcion', 'cuentacontable', 'porcentajedescuento', 'fechamodificado', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo', 'porcentajeganancia', 'cuentactbventas']


class MaestroproductocomplementarioForm(forms.ModelForm):
    class Meta:
        model = Maestroproductocomplementario
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idproducto', 'idcomplementario', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroproductoimagenForm(forms.ModelForm):
    class Meta:
        model = Maestroproductoimagen
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroproducto', 'foto', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroproductokitForm(forms.ModelForm):
    class Meta:
        model = Maestroproductokit
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idproducto', 'idproductokit', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroproductosustitutoForm(forms.ModelForm):
    class Meta:
        model = Maestroproductosustituto
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroproducto', 'idmaestroproductosustituto',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotipolineaForm(forms.ModelForm):
    class Meta:
        model = Maestrotipolinea
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigotipolinea', 'nombretipolinea', 'descripcion',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestrotiporotacionForm(forms.ModelForm):
    class Meta:
        model = Maestrotiporotacion
        fields = ['id', 'codigorotacion', 'nombre', 'descripcion']


class PedplantForm(forms.ModelForm):
    class Meta:
        model = Pedplant
        fields = ['id', 'idalmarea', 'idproducto', 'idunidadmedida', 'cantidad']


class PedidocabeceraForm(forms.ModelForm):
    class Meta:
        model = Pedidocabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestrocentrodecosto', 'idtrabajador', 'anulado',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'aprobado',
                  'observacion', 'fechanecesidad', 'tipoproducto', 'tiempoatencion', 'tiposuministro', 'totaldolares',
                  'totalsoles', 'idtipocambio', 'tipocambio', 'servicio', 'solicitaraprobacion', 'fechallegada',
                  'valegenerado', 'idmaestroalmacen']


class PedidodetalleForm(forms.ModelForm):
    class Meta:
        model = Pedidodetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idpedidocabecera', 'idmaestroproducto', 'cantidad',
                  'motivo', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'cotizado',
                  'calificado', 'comprado', 'especificacion', 'dolares', 'soles', 'nuevodolares', 'nuevosoles',
                  'cantidadaprobada', 'aprobado', 'descripcionproductoref']


class PedidogenericodetalleForm(forms.ModelForm):
    class Meta:
        model = Pedidogenericodetalle
        fields = ['idpedidogenericodetalle', 'idfacturacabecera', 'idmaestroplato', 'tipoplato', 'precioventaunitario',
                  'cantidad', 'fechahoraregistro', 'estadoregistro', 'codigousuario', 'observaciondetalle',
                  'impresacomanda']


class PedidogenericodetalleanulacionForm(forms.ModelForm):
    class Meta:
        model = Pedidogenericodetalleanulacion
        fields = ['idpedidogenericodetalleanulacion', 'idpedidogenericodetalle', 'idfacturacabecera', 'idmaestroplato',
                  'tipoplato', 'precioventaunitario', 'cantidad', 'fechahoraregistro', 'estadoregistro',
                  'codigousuario', 'observaciondetalle', 'impresacomanda']


class ProducForm(forms.ModelForm):
    class Meta:
        model = Produc
        fields = ['id', 'f2']


class ProductoazarForm(forms.ModelForm):
    class Meta:
        model = Productoazar
        fields = ['id', 'idmaestroproducto', 'codigoproducto', 'idmaestroalmacen', 'codigoalmacen', 'saldo', 'fecha',
                  'tipo']


class Productos5DecForm(forms.ModelForm):
    class Meta:
        model = Productos5Dec
        fields = ['codigo', 'descripcion', 'precio_unitario', 'ruta']


class ProductounitarioimagenForm(forms.ModelForm):
    class Meta:
        model = Productounitarioimagen
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idalmacenubicacionproducto', 'foto', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'nombrefoto', 'idsolicitudnotacredito',
                  'idpedidocabecera', 'idordencompradetalle']


class SaldoareahistorialForm(forms.ModelForm):
    class Meta:
        model = Saldoareahistorial
        fields = ['id', 'idmaestroproducto', 'idarea', 'fechasaldo', 'saldoinicial', 'saldofinal']


class SaldosdelanhioForm(forms.ModelForm):
    class Meta:
        model = Saldosdelanhio
        fields = [
            'id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroalmacen', 'codigoalmacen',
            'idmaestroproducto', 'codigoproducto', 'fecha', 'saldomes', 'costopromediosoles',
            'costopromediodolares', 'codigousuario', 'accion', 'fechacreacion', 'autorizado',
            'estado', 'activo'
        ]


class SaldosxalmacenesForm(forms.ModelForm):
    class Meta:
        model = Saldosxalmacenes
        fields = [
            'id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroalmacen', 'codigoalmacen',
            'idmaestroproducto', 'codigoproducto', 'numerooperacion', 'cantidadingresosalmacen',
            'cantidadsalidasalmacen', 'saldoalmacen', 'entregafutura', 'saldofisico', 'codigoubicacion',
            'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'rotacion',
            'ultimocostodolares', 'ultimocostosoles', 'costopromediodolares', 'costopromediosoles',
            'importeacumuladodolares', 'importeacumuladosoles'
        ]


class SaldosxareaForm(forms.ModelForm):
    class Meta:
        model = Saldosxarea
        fields = [
            'id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroarea', 'idmaestroproducto',
            'codigoproducto', 'numerooperacion', 'cantidadingresosalmacen', 'cantidadsalidasalmacen',
            'saldoalmacen', 'entregafutura', 'saldofisico', 'codigousuario', 'fechacreacion',
            'accion', 'autorizado', 'estado', 'activo', 'rotacion'
        ]


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroalmacen', 'idmaestroproducto', 'stockactual',
                  'stockminimo', 'stockmaximo', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado',
                  'activo']


class TablaimagenForm(forms.ModelForm):
    class Meta:
        model = Tablaimagen
        fields = ['id', 'imagen']


class TransformacioncabeceraForm(forms.ModelForm):
    class Meta:
        model = Transformacioncabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'idmaestroproducto', 'cantidad', 'motivo', 'precioventasoles',
                  'precioventadolares', 'fechatransformacion', 'idmestroalmacen', 'idalmaceningreso', 'idalmacensalida',
                  'tipotransformacion']


class TransformaciondetalleForm(forms.ModelForm):
    class Meta:
        model = Transformaciondetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigousuario', 'fechacreacion', 'accion',
                  'autorizado', 'estado', 'activo', 'idtransformacioncabecera', 'idmaestroproducto', 'cantidad',
                  'costosoles', 'costodolares', 'esiingreso', 'conceptolibre', 'idalmacencabecera']


class TrasladounidadForm(forms.ModelForm):
    class Meta:
        model = Trasladounidad
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idalmacenubicacionproducto', 'fechallegada',
                  'idmaestrocliente', 'numerofactura', 'numeroembarque', 'numerocase', 'revisado', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']


class UsuarioalmacenForm(forms.ModelForm):
    class Meta:
        model = Usuarioalmacen
        fields = ['id', 'iduser', 'codigousuario', 'idmaestroalmacen']
