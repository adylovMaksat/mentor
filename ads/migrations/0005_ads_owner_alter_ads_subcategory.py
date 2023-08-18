# Generated by Django 4.2.4 on 2023-08-18 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0004_category_alter_ads_created_at_alter_ads_updated_ad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ads',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='ads.subcategory'),
        ),
    ]
