# Generated by Django 2.1.1 on 2018-09-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mdlStatusOcorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descricao')),
                ('datacriacao', models.DateTimeField(auto_now_add=True)),
                ('dataalteracao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
    ]
