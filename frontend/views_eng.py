from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from catalogue.categories import Category
from catalogue.product_details import Brand
from catalogue.product_attritubes import Attribute, Characteristics, ProductCharacteristics, CharacteristicsValue
from catalogue.models import Product

from site_settings.models import Banner
from .mixins import ListViewMixin
from .tools import category_and_brands_filter_data
from cart.forms import ProductCartForm
from cart.tools import check_or_create_cart
from cart.models import CartItem
from newsletter.models import NewsLetter
from contact.forms import ContactFrontEndEngForm
from .forms import AskForm
import datetime


class HomepageView(TemplateView):
    template_name = 'frontend_eng/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        page_title = 'Homepage'
        banners = Banner.browser.active()
        big_banners, small_banners = [banners.filter(category='a'), banners.filter(category='c')[:4]]
        featured_products = Product.my_query.featured_products()[:8]
        only_info_products = Product.my_query.only_info_products()
        new_products = Product.my_query.index_new_products()
        offers = Product.my_query.products_with_offer()[:4]
        brands = Brand.objects.filter(active=True)
        context.update(locals())
        return context


class NewProductsListView(ListViewMixin, ListView):
    template_name = 'frontend_eng/list_view.html'
    model = Product

    def get_queryset(self):
        self.initial_queryset = Product.my_query.active_for_site().filter(
            timestamp__gt=datetime.datetime.today() - datetime.timedelta(days=60)
        )
        qs = Product.filters_data(self.request, self.initial_queryset)
        if self.request.GET.getlist('attr_name', None):
            qs = Attribute.product_filter_data(self.request, qs)
        if self.request.GET.getlist('char_name', None):
            try:
                ids = ProductCharacteristics.filters_data(self.request,
                                                          ProductCharacteristics.objects.all()).values_list(
                    'product_related__id')
                qs = qs.filter(id__in=ids)
            except:
                qs = qs
        return qs

    def get_context_data(self, **kwargs):
        context = super(NewProductsListView, self).get_context_data(**kwargs)
        page_title, description = ['New Products',
                                   'Discover the latest fashion on sunglasses and glasses, in Optika-Kotsalis'
                                   ]
        new_products = True
        greek_url, eng_url = reverse('new_products_view'), reverse('eng:new_products_view')
        characteristics = Characteristics.objects.filter(is_filter=True)
        product_characteristics = ProductCharacteristics.objects.filter(product_related__in=self.object_list,
                                                                        title__in=characteristics).distinct()
        context.update(locals())
        return context


class OfferView(ListViewMixin, ListView):
    model = Product
    template_name = 'frontend_eng/list_view.html'

    def get_queryset(self):
        self.initial_queryset = Product.my_query.products_with_offer()
        qs = Product.filters_data(self.request, self.initial_queryset)
        if self.request.GET.get('attr_name', None):
            qs = Attribute.product_filter_data(self.request, qs)
        if self.request.GET.getlist('char_name', None):
            try:
                ids = ProductCharacteristics.filters_data(self.request, ProductCharacteristics.objects.all()).values_list('product_related__id')
                qs = qs.filter(id__in=ids)
            except:
                qs = qs
        return qs

    def get_context_data(self, **kwargs):
        context = super(OfferView, self).get_context_data(**kwargs)
        page_title, description = ['Offers',
                                   'Welcome to our store, optika kotsalis.'
                                   'All our offers is here']
        offer = True
        greek_url, eng_url = reverse('offer_view'), reverse('eng:offer_view')
        context.update(locals())
        return context


class CategoryView(ListViewMixin, ListView):
    template_name = 'frontend_eng/list_view.html'
    model = Product

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        qs = Product.my_query.active_for_site().filter(category_site=self.category)
        self.initial_queryset = qs

        qs = self.initial_queryset
        qs = Product.filters_data(self.request, qs)
        if self.request.GET.getlist('char_name', None):
            try:
                ids = ProductCharacteristics.filters_data(self.request,
                                                          ProductCharacteristics.objects.all()).values_list(
                    'product_related__id')
                qs = qs.filter(id__in=ids)
            except:
                qs = qs
        return qs

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        page_title, description = f'{self.category.eng_title}',\
                                  f'Welcome to our store, optika kotsalis. All the products of the category {self.category.eng_title} is here.'
        categories, brands = category_and_brands_filter_data(self.initial_queryset, cate_id=self.category.id)
        low, max = 0, self.queryset.order_by('final_value')[0].final_value if self.queryset else 200
        greek_url, eng_url = self.category.get_absolute_url(), self.category.get_absolute_eng_url()
        context.update(locals())
        return context


class SearchView(ListViewMixin, ListView):
    model = Product
    template_name = 'frontend_eng/list_view.html'

    def get_queryset(self):
        search_name = self.request.GET.get('search_name', None)
        qs = Product.my_query.active_for_site()
        qs = Product.filters_data(self.request, qs) if len(search_name) > 2 else Product.objects.none()
        self.initial_queryset = qs
        if self.request.GET.getlist('char_name', None):
            try:
                ids = ProductCharacteristics.filters_data(self.request,
                                                          ProductCharacteristics.objects.all()).values_list(
                    'product_related__id')
                qs = qs.filter(id__in=ids)
            except:
                qs = qs
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_name = self.request.GET.get('search_name', None)
        page_title = 'Result of the search...  %s' % search_name
        greek_url, eng_url = reverse('search_page'), reverse('eng:search_page')
        context.update(locals())
        return context


class BrandListView(ListView):
    template_name = 'frontend_eng/brand_view.html'
    model = Brand
    queryset = Brand.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super(BrandListView, self).get_context_data(**kwargs)
        greek_url, eng_url = reverse('brands_view'), reverse('eng:brands_view')
        page_title = 'Brand Page'
        context.update(locals())
        return context


class BrandDetailView(ListViewMixin, ListView):
    template_name = 'frontend_eng/list_view.html'
    model = Product
    paginate_by = 4

    def get_queryset(self):
        brand = self.brand = get_object_or_404(Brand, slug=self.kwargs['slug'])
        qs = Product.my_query.active_for_site().filter(brand=brand)
        self.initial_queryset = qs
        qs = Product.filters_data(self.request, qs)
        if self.request.GET.getlist('char_name', None):
            try:
                ids = ProductCharacteristics.filters_data(self.request,
                                                          ProductCharacteristics.objects.all()).values_list(
                    'product_related__id')
                qs = qs.filter(id__in=ids)
            except:
                qs = qs
        return qs

    def get_context_data(self, **kwargs):
        context = super(BrandDetailView, self).get_context_data(**kwargs)
        brand = get_object_or_404(Brand, slug=self.kwargs['slug'])
        page_title, description = f'{brand.eng_title}', \
                                  f'Welcome to our store  optika kotsalis. All the products of ' \
                                  f'the brand {brand.eng_title} is here.'
        greek_url, eng_url = self.brand.get_absolute_url(), self.brand.get_absolute_eng_url()
        context.update(locals())
        return context


class ProductView(DetailView, FormView):
    template_name = 'frontend_eng/product_view.html'
    model = Product
    form_class = ProductCartForm
    queryset = Product.my_query.active_for_site()

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        page_title = product.eng_title
        attributes = None
        if product.have_attr:
            attributes = Attribute.my_query.product_attributes_with_qty(product)
        contact_form = ContactFrontEndEngForm()
        categories_p = self.object.category_site.all()
        same_cate_products = Product.my_query.active_for_site().filter(category_site__in=categories_p).exclude(
            id=self.object.id)[:4]
        related_products = Product.my_query.active_for_site().filter(related_products=product)[:8]
        different_color_products = Product.my_query.active_for_site().filter(different_color_products=product)
        greek_url, eng_url = self.object.get_absolute_url(), self.object.get_absolute_eng_url()
        ask_form = AskForm()
        context.update(locals())
        return context

    def form_valid(self, form):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        qty = form.cleaned_data.get('qty', 1)
        attribute_id = self.request.POST.get('attribute', None)
        cart = check_or_create_cart(self.request)
        result, message = CartItem.create_cart_item(cart, product, qty, attribute_id)
        messages.success(self.request, message)
        return super(ProductView, self).form_valid(form)

    def form_invalid(self, form):
        return super(ProductView, self).form_invalid(form)


def newsletter_form_view(request):
    email = request.POST.get('newsletter_email', None)
    if email:
        new_newsletter, created = NewsLetter.objects.get_or_create(email=email)
        if created:
            new_newsletter.confirm = True
            new_newsletter.save()
            messages.success(request, f'Yor email, {email}  , is saved. Thank you!')
        else:
            messages.warning(request, 'Το email σας is already on our list.')
    else:
        messages.warning(request, 'The process failed. '
                                  'Try again, or try to contact with the adminnistrators.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def demo_only_view_restart_session(request):
    del request.session['cart_id']
    return HttpResponseRedirect('/')


def error_404(request, exception):
    data = {}
    return render(request, 'frontend/extra/404.html', data)
