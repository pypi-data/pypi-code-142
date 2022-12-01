# Generated by Django 4.0.3 on 2022-03-13 14:17

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveuniverse', '0005_type_materials_and_sections'),
        ('marketmanager', '0011_alter_privateconfig_failed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='structure',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.RemoveField(
            model_name='watchconfig',
            name='type',
        ),
        migrations.AddField(
            model_name='watchconfig',
            name='type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='eveuniverse.evetype', verbose_name='EVE Type'),
            preserve_default=False,
        ),
    ]
