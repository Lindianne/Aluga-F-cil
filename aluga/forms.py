from django import forms
from django.contrib.auth.models import User
from .models import Telefone, Item

class UserForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = True
		self.fields['username'].required = True
		self.fields['password'].required = True	
		self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder':"Email"}
		self.fields['username'].widget.attrs = {'class': 'form-control', 'placeholder':"Username"}
		self.fields['password'].widget.attrs = {'class': 'form-control', 'placeholder':"Senha"}
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password']
		widgets = {
			'password': forms.PasswordInput(),
		}
		error_messages = {
			'username': {
				'unique': 'Esse nome de usuário já está em uso'
			},
		}
		

class TelForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(TelForm, self).__init__(*args, **kwargs)
		self.fields['telefone'].required = False
		self.fields['telefone'].widget.attrs = {'class': 'form-control', 'placeholder':"Telefone" }
		self.fields['cpf'].widget.attrs = {'class': 'form-control', 'placeholder':"CPF"}
		self.fields['endereco'].widget.attrs = {'class': 'form-control', 'placeholder':"Endereço"}

	class Meta:
		model = Telefone
		fields = ['telefone', 'cpf', 'endereco']
		error_messages = {
			'telefone': {
				'unique': 'Esse telefone já está cadastrado',
				'min_length': 'O telefone precisa ter 9 digitos'
			},
			'cpf': {
				'unique': 'Esse CPF já está cadastrado',
				'min_length': 'O CPF precisa ter 11 digitos'
			}
		}

class ItemForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ItemForm, self).__init__(*args, **kwargs)
		self.fields['nome'].required = True
		self.fields['preco'].required = True
		self.fields['descricao'].required = True
		self.fields['imagem'].widget = forms.FileInput()
		self.fields['categoria'].required = True
		self.fields['nome'].widget.attrs = {'class': 'form-control', 'placeholder':"Nome"}
		self.fields['preco'].widget.attrs = {'class': 'form-control', 'placeholder':"Preço"}
		self.fields['descricao'].widget.attrs = {'class': 'form-control', 'placeholder':"Descrição"}
		self.fields['imagem'].widget.attrs = {'class': 'form-control'}
		self.fields['categoria'].widget.attrs = {'class': 'form-control'}

	class Meta:
		model = Item
		fields = ['nome', 'preco', 'descricao','imagem', 'categoria']
