# Generated by Django 2.2 on 2019-09-12 13:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('site_settings', '0001_initial'),
        ('voucher', '0001_initial'),
        ('cart', '0001_initial'),
        ('catalogue', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Friendly ID')),
                ('title', models.CharField(max_length=150, verbose_name='Τίτλος')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('date_expired', models.DateField(default=datetime.date(2019, 9, 12), verbose_name='Ημερομηνία')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Αρχική Αξία')),
                ('taxes_modifier', models.CharField(choices=[('1', 13), ('2', 23), ('3', 24), ('4', 0)], default='3', max_length=1, verbose_name='ΦΠΑ')),
                ('paid_value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Πληρωτέο Ποσό')),
                ('final_value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Αξία')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Έκπτωση')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Πληρωμένο')),
                ('printed', models.BooleanField(default=False, verbose_name='Εκτυπωμένο')),
                ('number', models.SlugField(blank=True, max_length=128)),
                ('status', models.CharField(choices=[('1', 'Νέα Παραγγελία'), ('2', 'Σε επεξεργασία'), ('3', 'Έτοιμη προς αποστολή'), ('4', 'Απεστάλη'), ('5', 'Επιστράφηκε'), ('6', 'Ακυρώθηκε'), ('7', 'Εισπράκτηκε'), ('8', 'Ολοκληρώθηκε')], default='1', max_length=1, verbose_name='Κατάσταση')),
                ('order_type', models.CharField(choices=[('r', 'Λιανική Πώληση'), ('e', 'Πώληση Eshop'), ('b', 'Παραστατικό Επιστροφής'), ('c', 'Ακυρωμένη Παραγγελία'), ('wa', 'Παραστατικό Εισαγωγής'), ('wr', 'Παραστατικό Εξαγωγής')], default='r', max_length=1, verbose_name='Είδος')),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Συνολικο Κόστος')),
                ('shipping_method_cost', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Μεταφορικά')),
                ('payment_cost', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Κόστος Αντικαταβολής')),
                ('day_sent', models.DateTimeField(blank=True, null=True, verbose_name='Ημερομηνία Αποστολής')),
                ('eshop_session_id', models.CharField(blank=True, max_length=50, null=True)),
                ('voucher_discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('guest_email', models.EmailField(blank=True, max_length=254)),
                ('cart_related', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='cart.Cart')),
                ('order_related', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='point_of_sale.Order')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='site_settings.PaymentMethod', verbose_name='Τρόπος Πληρωμής')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile_orders', to='accounts.Profile', verbose_name='Πελάτης')),
                ('shipping_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_settings.Shipping', verbose_name='Τρόπος Μεταφοράς')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='User Account')),
                ('user_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('vouchers', models.ManyToManyField(blank=True, to='voucher.Voucher')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': '1. Orders',
                'ordering': ['-date_expired', 'status', '-id'],
            },
            managers=[
                ('my_query', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('qty', models.PositiveIntegerField(default=1, verbose_name='Ποσότητα')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Αξία Προϊόντων')),
                ('discount_value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Έκπτωση %')),
                ('final_value', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Αξία')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('is_find', models.BooleanField(default=False)),
                ('is_return', models.BooleanField(default=False)),
                ('attribute', models.BooleanField(default=False)),
                ('total_value', models.DecimalField(decimal_places=2, default=0, help_text='qty*final_value', max_digits=20)),
                ('total_cost_value', models.DecimalField(decimal_places=0, default=0, help_text='qty*cost', max_digits=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='point_of_sale.Order', verbose_name='Παραστατικό')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='retail_items', to='catalogue.Product', verbose_name='Προϊόν')),
            ],
            options={
                'verbose_name_plural': '2. Προϊόντα Πωληθέντα',
                'ordering': ['-order__timestamp'],
                'unique_together': {('title', 'order')},
            },
            managers=[
                ('broswer', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Last Name')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('zip_code', models.IntegerField(blank=True, null=True, verbose_name='Postal')),
                ('phone', models.CharField(blank=True, max_length=10, verbose_name='Phone')),
                ('cellphone', models.CharField(blank=True, max_length=10, verbose_name='Cell Phone')),
                ('order_related', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='point_of_sale.Order')),
            ],
        ),
        migrations.CreateModel(
            name='SendReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sent', models.BooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('shipping_code', models.CharField(blank=True, max_length=240)),
                ('order_related', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_voucher', to='point_of_sale.Order')),
                ('shipping_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_settings.Shipping')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('is_found', models.BooleanField(default=False)),
                ('attribute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.Attribute')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='point_of_sale.OrderItem')),
            ],
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Last Name')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('zip_code', models.IntegerField(blank=True, null=True, verbose_name='Postal')),
                ('phone', models.CharField(blank=True, max_length=10, verbose_name='Phone')),
                ('cellphone', models.CharField(blank=True, max_length=10, verbose_name='Cell Phone')),
                ('need_invoice', models.BooleanField(default=False)),
                ('is_retail', models.BooleanField(default=True)),
                ('is_eshop', models.BooleanField(default=True)),
                ('vat', models.CharField(blank=True, max_length=9, verbose_name='ΑΦΜ')),
                ('vat_city', models.CharField(blank=True, max_length=100, null=True)),
                ('company_detail', models.CharField(blank=True, max_length=200, null=True)),
                ('order_related', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='point_of_sale.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('first_name', models.CharField(max_length=100, verbose_name='Ονομα')),
                ('last_name', models.CharField(max_length=100, verbose_name='Επιθετο')),
                ('address', models.CharField(max_length=100, verbose_name='Διευθυνση')),
                ('city', models.CharField(max_length=100, verbose_name='Πολη')),
                ('zip_code', models.CharField(max_length=5, verbose_name='Ταχυδρομικος Κωδικας')),
                ('cellphone', models.CharField(max_length=10, verbose_name='Κινητό')),
                ('phone', models.CharField(blank=True, max_length=10, verbose_name='Σταθερο Τηλεφωνο')),
                ('notes', models.TextField(blank=True, verbose_name='Σημειωσεις')),
                ('order_type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], default='shipping', max_length=50)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='site_settings.Country')),
                ('order_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_profiles', to='point_of_sale.Order')),
            ],
            options={
                'unique_together': {('order_related', 'order_type')},
            },
        ),
    ]
