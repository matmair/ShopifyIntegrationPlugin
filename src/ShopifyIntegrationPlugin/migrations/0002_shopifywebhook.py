# Generated by Django 3.2.4 on 2021-10-18 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_auto_20210912_1804'),
        ('ShopifyIntegrationPlugin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopifyWebhook',
            fields=[
                ('webhookendpoint_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.webhookendpoint')),
            ],
            bases=('common.webhookendpoint',),
        ),
    ]
