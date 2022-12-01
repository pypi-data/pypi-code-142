# Generated by Django 4.0.2 on 2022-02-28 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketmanager', '0007_alter_order_is_buy_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('', ''), ('cancelled', 'Cancelled'), ('expired ', 'Expired')], help_text='Current order state, Only valid for Authenticated order History. Will not update from Public Market Data.', max_length=20, verbose_name='Order State'),
        ),
    ]
