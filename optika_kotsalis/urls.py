from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls')),
    path('en/', include('frontend.urls_eng')),
    path('', include('frontend.urls')),

    path('accounts/', include('accounts.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),

    # admin  dashboard

    path('dashboard-catalogue/', include('catalogue.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard-pos/', include('point_of_sale.urls')),
    path('dashboard-cart/', include('cart.urls')),
    path('dashboard-voucher/', include('voucher.urls')),
    path('dashboard-settings/', include('site_settings.urls')),
    path('dashboard-newsletter/', include('newsletter.urls')),
    path('dashboard-contact/', include('contact.urls')),
    path('dashboard-size-chart/', include('chartsize.urls')),


    path('social-auth/', include('social_django.urls', namespace="social")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'frontend.views.error_404'