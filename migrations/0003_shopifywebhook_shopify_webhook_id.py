# Generated by Django 3.2.4 on 2021-10-18 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopifyIntegrationPlugin', '0002_shopifywebhook'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopifywebhook',
            name='shopify_webhook_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
