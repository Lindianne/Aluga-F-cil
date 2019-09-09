from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.contrib.auth.models import User


# Create your models here.

class Telefone(models.Model):
	telefone = models.CharField(max_length=9, validators=[MinLengthValidator(9),RegexValidator(r'^[0-9]*$', 'Apenas números.')], unique=True, null=True)
	cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11),RegexValidator(r'^[0-9]*$', 'Apenas números.')], unique=True)
	endereco = models.TextField()
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class Item(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	nome = models.CharField(max_length=30)
	preco = models.DecimalField(max_digits=10, decimal_places=2, default=1)
	descricao = models.CharField(max_length=100)
	imagem = models.ImageField(upload_to='itens', null=True, blank=True)
	categoria_choices = (('Calçados', 'Calçados'), ('Roupas', 'Roupas'), 
		('Eletrodomésticos', 'Eletrodomésticos'), ('Imóveis', 'Imóveis'), ('Outros', 'Outros'))
	categoria = models.CharField(max_length=16, choices=categoria_choices, default='calcados')