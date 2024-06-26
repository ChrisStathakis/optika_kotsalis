from django.utils.html import format_html
import django_tables2 as tables
from catalogue.models import Product, ProductClass
from catalogue.categories import WarehouseCategory, Category

from catalogue.product_details import Brand, Color
from catalogue.product_attritubes import Characteristics, Attribute, AttributeClass
from .models import ProductDiscount


class TruncatedTextColumn(tables.Column):
    '''A Column to limit to 100 characters and add an ellipsis'''
    def render(self, value):
        if len(value) > 30:
            return value[0:27] + '...'
        return str(value)


class ImageColumn(tables.Column):

    def render(self, value):
        return format_html('<img class="img img-thumbnail" style="width:50px;height:50px" src="https://optika-kotsalis.s3.amazonaws.com/media/{}" />', value)


class TableProduct(tables.Table):
    tag_image_ = tables.TemplateColumn("<a href='{{ record.get_edit_url }}'><img src='{{ record.image.url }}' class='image' width=200 height=200 /> </a>")
    action = tables.TemplateColumn("<a href='{{ record.get_edit_url }}' class='btn btn-primary btn-round'>"
                                   "<i class='fa fa-edit'> </i></a>",
                                   orderable=False, verbose_name='Επεξεργασια'
                                   )
    #  qty = tables.TemplateColumn('<span class="label label-{{ record.color_qty }}">{{ record.tag_qty }}</span>')
    tag_final_price = tables.Column(orderable=False, verbose_name='Τιμή Πώλησης')
    #  title = TruncatedTextColumn()
    sku = tables.TemplateColumn("<a href='{{ record.get_edit_url }}'>{{ record.sku }}</a>")

    class Meta:
        model = Product
        template_name = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table  table-hover'}
        fields = ['id', 'tag_image_', 'sku', 'title', 'eng_title', 'brand', 'tag_final_price', 'active', 'action']


class ProductClassTable(tables.Table):
    action = tables.TemplateColumn('<a href="{{ record.get_edit_url }}" class="btn btn-info btn-round">Επεξεργασία</a>')

    class Meta:
        model = ProductClass
        template_name = 'django_tables2/bootstrap.html'
        fields = ['id', 'title', 'have_attribute', 'have_transcations', 'is_service']


class WarehouseCategoryTable(tables.Table):
    action = tables.TemplateColumn("<a href='{{ record.get_edit_url }}' class='btn btn-primary'>Επεξεργασία</a>",
                                   orderable=False)

    class Meta:
        model = WarehouseCategory
        template_name = 'django_tables2/bootstrap.html'
        fields = ['id', 'title', 'active']


class CategorySiteTable(tables.Table):
    action = tables.TemplateColumn("<a href='{{ record.get_edit_url }}' class='btn btn-primary btn-round'>"
                                   "<i class='fa fa-edit'> </i></a>",
                                   orderable=False
                                   )

    class Meta:
        model = Category
        template_name = 'django_tables2/bootstrap.html'
        fields = ['id', '__str__', 'eng_title', 'parent', 'active']


class BrandTable(tables.Table):
    action = tables.TemplateColumn("<a href='{{ record.get_edit_url }}' class='btn btn-primary'>Επεξεργασία</a>",
                                   orderable=False)

    class Meta:
        model = Brand
        template_name = 'django_tables2/bootstrap.html'
        fields = ['id', 'title', 'eng_title', 'active']


class CharacteristicsTable(tables.Table):
    action = tables.TemplateColumn("<a href='{{ record.get_edit_url }}' class='btn btn-primary'>Επεξεργασία</a>",
                                   orderable=False)

    class Meta:
        model = Characteristics
        template_name = 'django_tables2/bootstrap.html'
        fields = ['title', 'eng_title', 'active']


class AttributeTable(tables.Table):
    action = tables.TemplateColumn("<a href='{{ record.get_edit_url }}' class='btn btn-primary'>Επεξεργασία</a>",
                                   orderable=False)

    class Meta:
        model = Attribute
        template_name = 'django_tables2/bootstrap.html'
        fields = ['title', 'active']


class AttributeClassTable(tables.Table):
    action = tables.TemplateColumn("<a href='{{ record.get_edit_url }}' class='btn btn-primary'>Επεξεργασία</a>",
                                   orderable=False)

    class Meta:
        model = AttributeClass
        template_name = 'django_tables2/bootstrap.html'
        fields = ['title', 'active']


class ProductTable(tables.Table):
    action = tables.TemplateColumn("<a href='{{ record.get_edit_url }}' class='btn btn-primary'><i class='fa fa-edit'>"
                                   "</i></a>",
                                   orderable=False)

    class Meta:
        model = AttributeClass
        template_name = 'django_tables2/bootstrap.html'
        fields = ['title', 'category', 'vendor', 'active']


class CategorySiteAddToProductTable(tables.Table):
    action = tables.TemplateColumn('<button data-href="{% url "dashboard:ajax_category_site" "add" '
                                   'instance.id ele.id %}" class="btn btn-success ajax_button">Add</button>',
                                   orderable=False)


class ProductDiscountTable(tables.Table):
    action = tables.TemplateColumn("<a href='{{ record.get_edit_url }}' class='btn btn-primary'><i class='fa fa-edit'>"
                                   "</i></a>",
                                   orderable=False)
    tag_range = tables.Column(orderable=False)

    class Meta:
        model = ProductDiscount
        template_name = 'django_tables2/bootstrap.html'
        fields = ['title', 'tag_range', 'discount_type', 'choices', 'active']


class ColorTable(tables.Table):
    action = tables.TemplateColumn(
        "<a href='{{ record.get_edit_url }}' class='btn btn-primary'><i class='fa fa-edit'></i></a>",
        orderable=False)

    class Meta:
        model = Color
        fields = ['title', 'eng_title', 'active', 'action']
        template_name = 'django_tables2/bootstrap.html'
