# Generated by Django 5.0.4 on 2024-04-21 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('documento', models.FileField(upload_to='documentos')),
                ('consulta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='paciente.consulta')),
            ],
        ),
    ]
