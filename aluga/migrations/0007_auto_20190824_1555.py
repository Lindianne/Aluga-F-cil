# Generated by Django 2.0.7 on 2019-08-24 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluga', '0006_auto_20190824_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='item',
            name='tamanho',
        ),
        migrations.AddField(
            model_name='telefone',
            name='cpf',
            field=models.CharField(max_length=11, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.RegexValidator('^[0-9]*$', 'Apenas números.')]),
        ),
        migrations.AddField(
            model_name='telefone',
            name='endereco',
            field=models.TextField(null=True),
        ),
    ]