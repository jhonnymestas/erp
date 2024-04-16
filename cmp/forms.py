from django import forms

from .models import Proveedor, ComprasEnc


# Importando Tablas
from .models import Facturasproveedorescabecera, Facturasproveedoresdetalle, Maestroformasdepagocompras, \
    Maestromotivosfacturaproveedor, Maestroporcentajedetraccion, Maestrotipoproveedores, Maestroestadosordencompra, \
    Ordencompracabecera, Ordencompradetalle, Proveedoresmigracion, Proveedorlinea


class ProveedorForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = Proveedor
        exclude = ['um', 'fm', 'uc', 'fc']
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean(self):
        try:
            sc = Proveedor.objects.get(
                descripcion=self.cleaned_data["descripcion"].upper()
            )

            if not self.instance.pk:
                print("Registro ya existe")
                raise forms.ValidationError("Registro Ya Existe")
            elif self.instance.pk != sc.pk:
                print("Cambio no permitido")
                raise forms.ValidationError("Cambio No Permitido")
        except Proveedor.DoesNotExist:
            pass
        return self.cleaned_data


class ComprasEncForm(forms.ModelForm):
    fecha_compra = forms.DateInput()
    fecha_factura = forms.DateInput()
    
    class Meta:
        model = ComprasEnc
        fields = ['proveedor', 'fecha_compra', 'observacion',
                  'no_factura', 'fecha_factura', 'sub_total',
                  'descuento', 'total']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fecha_compra'].widget.attrs['readonly'] = True
        self.fields['fecha_factura'].widget.attrs['readonly'] = True
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True


class FacturasproveedorescabeceraForm(forms.ModelForm):
    class Meta:
        model = Facturasproveedorescabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idordencompracabecera', 'idmaestroformadepago',
                  'periodo', 'numerooperacion', 'idmaestroproveedor', 'codigoproveedor',
                  'idmaestromotivofacturaproveedor', 'idmaestrotipomovimiento', 'tipomovimiento', 'seriedocumentofb',
                  'numerodocumentofb', 'idmaestrodocumentosunat', 'documentosunat', 'fechadocumento', 'conceptocompra',
                  'igv', 'solidaridad', 'asientogenerado', 'idmaestromoneda', 'moneda', 'fechacancelacion',
                  'idmaestrotipodecambio', 'tipocambio', 'montosoles', 'montodolares', 'igvsoles', 'igvdolares',
                  'otrosmontossoles', 'otrosmontosdolares', 'fechacontabilizacion', 'montototalsoles',
                  'montototaldolares', 'codigocuentatotalventa', 'voucher', 'refcaja', 'anulada', 'fechallegada',
                  'glosa', 'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo',
                  'idmaestrocentrocosto', 'aprobado', 'tipoigv', 'idordenpedido', 'fechadetraccion', 'id_docreferencia',
                  'seriereferencia', 'numeroreferencia', 'numerocomprobantedetraccion', 'seriedocretencion',
                  'numerodocretencion', 'retencion', 'montoretencion', 'fechavencimiento', 'montodetraccion',
                  'montopercepcion', 'iddistribucioncentrocosto', 'esgasto', 'observaciones', 'idalmacencabecera',
                  'bolsas', 'igvporcentaje']


class FacturasproveedoresdetalleForm(forms.ModelForm):
    class Meta:
        model = Facturasproveedoresdetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idfacturaproveedorcabecera', 'numerodocumentofb',
                  'seriedocumentofb', 'idmaestroproducto', 'codigoproducto', 'cantidad', 'preciounitariosoles',
                  'preciounitariodolares', 'numerooperacion', 'numeroembarque', 'numerocase', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'subtotaldolares', 'subtotalsoles',
                  'idcentrocosto', 'ctactbdiscentrocosto', 'iddistribucioncentrocosto', 'conceptolibre', 'sinigvcheck',
                  'idamarrecabecera']


class MaestroformasdepagocomprasForm(forms.ModelForm):
    class Meta:
        model = Maestroformasdepagocompras
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'codigoformapago', 'descripcion', 'codigousuario',
                  'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestromotivosfacturaproveedorForm(forms.ModelForm):
    class Meta:
        model = Maestromotivosfacturaproveedor
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'motivo', 'fechamodificado', 'codigousuario', 'accion',
                  'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroporcentajedetraccionForm(forms.ModelForm):
    class Meta:
        model = Maestroporcentajedetraccion
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'descripcion', 'porcentaje', 'normativa',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo', 'esdetraccion']


class MaestrotipoproveedoresForm(forms.ModelForm):
    class Meta:
        model = Maestrotipoproveedores
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'tipoproveedor', 'descripcion', 'fechamodificado',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class MaestroestadosordencompraForm(forms.ModelForm):
    class Meta:
        model = Maestroestadosordencompra
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'estadoordencompra', 'fechamodificado',
                  'codigousuario', 'accion', 'fechacreacion', 'autorizado', 'estado', 'activo']


class OrdencompracabeceraForm(forms.ModelForm):
    class Meta:
        model = Ordencompracabecera
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'serieorden', 'numeroorden', 'idalmacencabecera',
                  'idmaestroalmacendestino', 'numerorequerimiento', 'fechaoperacion', 'fechaentrega', 'idmaestromoneda',
                  'idmaestrotipocambio', 'totalsoles', 'totaldolares', 'idmaestroproveedor', 'idmaestrocaja',
                  'idmaestrocajachica', 'condicionespago', 'montopagoadelantadosoles', 'montopagoadelantadodolares',
                  'numerodiascredito', 'numeroletrascredito', 'tipocompra', 'glosa', 'idcotizacion',
                  'idmaestroestadoordencompra', 'sincotizacion', 'idmaestrocentrodecosto', 'anulado', 'codigousuario',
                  'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'facturada', 'codigo', 'recibida',
                  'aprobado', 'servicio', 'idmaestroformadepago', 'igvsoles', 'igvdolares', 'ventasoles',
                  'ventadolares', 'igv', 'atencion', 'firma', 'idautorizadofirma', 'porcentajedescuento',
                  'lugaresentrega']


class OrdencompradetalleForm(forms.ModelForm):
    class Meta:
        model = Ordencompradetalle
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idordencompracabecera', 'preciounitariosoles',
                  'preciounitariodolares', 'idmaestroproducto', 'cantidad', 'subtotalsoles', 'subtotaldolares',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo', 'facturada',
                  'cantidadfacturada', 'idcentrocosto', 'cantidadrecibida', 'recibida', 'idpedidodetalle',
                  'ctactbdiscentrocosto', 'descripcionproductoref', 'idunidadmedida', 'observacion', 'codprodref',
                  'descuento']


class ProveedoresmigracionForm(forms.ModelForm):
    class Meta:
        model = Proveedoresmigracion
        fields = ['tipo_persona', 'tipo_de_documento_de_identidad_del_proveedor', 'ruc',
                  'apellidos_y_nombres_denominacion_o_razon_social_del_proveedor_field', 'cuenta']


class ProveedorlineaForm(forms.ModelForm):
    class Meta:
        model = Proveedorlinea
        fields = ['id', 'idmaestroempresa', 'idmaestrosucursal', 'idmaestroprovedor', 'idmaestrolineacomercial',
                  'codigousuario', 'fechacreacion', 'accion', 'autorizado', 'estado', 'activo']
