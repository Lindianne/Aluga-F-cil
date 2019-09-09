# Generated by Django 2.0.7 on 2019-08-24 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aluga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('tamanho', models.DecimalField(decimal_places=2, default=1, max_digits=5)),
                ('marca', models.CharField(max_length=15)),
                ('preco', models.DecimalField(decimal_places=2, default=1, max_digits=5)),
                ('descricao', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to='itens')),
                ('categoria', models.CharField(choices=[('calcados', 'Calcados'), ('roupas', 'Roupas'), ('eletro', 'Eletrodomésticos'), ('imoveis', 'Imóveis'), ('outros', 'Outros')], default='calcados', max_length=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]