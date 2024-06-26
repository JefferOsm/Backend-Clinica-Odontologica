# Generated by Django 5.0.4 on 2024-04-20 01:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("consulta_api", "0007_facturamodel"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="facturamodel",
            name="fecha_emision",
            field=models.DateField(
                blank=True, null=True, verbose_name="Fecha de Emision"
            ),
        ),
        migrations.AlterField(
            model_name="facturamodel",
            name="monto",
            field=models.FloatField(default=0, verbose_name="Monto"),
        ),
        migrations.AlterField(
            model_name="facturamodel",
            name="recepcionista",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Recepcionista que Emite la factura",
            ),
        ),
    ]
