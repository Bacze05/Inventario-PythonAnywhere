# Generated by Django 4.2.7 on 2024-02-24 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cajas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_inicial', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Monto Inicial')),
                ('cantidad_vendida', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cantidad Vendida')),
                ('fecha_apertura', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Apertura')),
                ('fecha_cierre', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Cierre')),
                ('cerrada', models.BooleanField(default=False, verbose_name='Caja Cerrada')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('caja', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Venta.cajas')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('nombre', models.CharField(db_index=True, max_length=100, verbose_name='Nombre del Reporte')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción del Reporte')),
                ('datos', models.JSONField(default=dict, verbose_name='Datos del Reporte')),
            ],
            options={
                'indexes': [models.Index(fields=['nombre'], name='idx_nombre_length')],
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventario.descuento')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='Inventario.product')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='Venta.venta')),
            ],
        ),
    ]
