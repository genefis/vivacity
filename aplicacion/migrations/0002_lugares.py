# Generated by Django 4.2.7 on 2024-01-15 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lugares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre_lugar', models.CharField(max_length=225, null=True)),
                ('fotolugar', models.ImageField(null=True, upload_to='')),
                ('direccionlugar', models.URLField(null=True)),
                ('horario', models.DateTimeField(null=True)),
                ('tipo_lugar', models.CharField(max_length=225, null=True)),
                ('canton_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.canton')),
            ],
            options={
                'verbose_name': 'lugares',
                'verbose_name_plural': 'lugares',
                'ordering': ['nombre_lugar'],
            },
        ),
    ]
