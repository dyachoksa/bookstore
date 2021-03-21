# Generated by Django 3.1.7 on 2021-03-21 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_shoppingcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address_line', models.CharField(max_length=250, verbose_name='address')),
                ('zip_code', models.CharField(max_length=12)),
                ('is_default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_addresses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'shipping address',
                'verbose_name_plural': 'shipping addresses',
            },
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='shipping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.shippingaddress'),
        ),
    ]