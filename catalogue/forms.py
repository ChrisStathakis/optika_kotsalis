from django import forms
from .models import *
from .product_attritubes import CharacteristicsValue, Characteristics, AttributeClass, AttributeTitle, ProductCharacteristics, Attribute
from .models import Product, ProductPhotos
from .product_details import Vendor, Color

from dal import autocomplete


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CreateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'eng_title', 'product_class']

    def __init__(self, *args, **kwargs):
        super(CreateProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CreateProductClassForm(forms.ModelForm):

    class Meta:
        model = ProductClass
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateProductClassForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CategorySiteForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['active', 'name', 'eng_title', 'parent', 'image', 'content', 'meta_description', 'slug', 'order' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class WarehouseCategoryForm(BaseForm, forms.ModelForm):

    class Meta:
        model = WarehouseCategory
        fields = '__all__'


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = ['active', 'title', 'eng_title', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CharacteristicsValueForm(BaseForm, forms.ModelForm):
    char_related = forms.ModelChoiceField(queryset=Characteristics.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = CharacteristicsValue
        fields = ['title', 'eng_title', 'char_related', 'custom_ordering']


class CharacteristicsForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Characteristics
        fields = ['active', 'title', 'eng_title', 'custom_ordering', 'is_filter']


class AttributeClassForm(BaseForm, forms.ModelForm):

    class Meta:
        model = AttributeClass
        fields = '__all__'


class AttributeTitleForm(BaseForm, forms.ModelForm):
    attri_by = forms.ModelChoiceField(queryset=AttributeClass.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = AttributeTitle
        fields = ['name', 'attri_by']


class ProductForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'sku',
                  'vendor', 'order_code',
                  'brand', 'slug',
                  'price', 'price_discount',
                  'qty', 'qty_measure',
                  'site_text',
                  'active', 'featured_product'
                   ]


class ProductPhotoUploadForm(forms.Form):
    image = forms.ImageField()


class ProductCharacteristicForm(BaseForm, forms.ModelForm):
    product_related = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())
    title = forms.ModelChoiceField(queryset=Characteristics.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = ProductCharacteristics
        fields = '__all__'


class AttributeForm(forms.ModelForm):

    class Meta:
        model = Attribute
        fields = '__all__'


class VendorForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Vendor
        fields = '__all__'
        exclude = ['balance', 'output_value', 'input_value']


class ColorForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Color
        fields = ['active', 'title', 'eng_title']
