# Generated by Django 3.1.7 on 2021-03-16 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactdata',
            options={'ordering': ['-created_at'], 'verbose_name': 'contact form data', 'verbose_name_plural': 'contact forms data'},
        ),
        migrations.AddField(
            model_name='contactdata',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
