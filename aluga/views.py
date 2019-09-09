from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, TelForm, ItemForm
from django.contrib.auth.models import User
from .models import Telefone, Item
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def main(request):
        #pega os últimos 9 itens cadastrados e inverte a sua ordem de apresentação
        #para tornar visivelmente mais agradavel
        lista = list(Item.objects.all())[::-1]
        itens = []
        for i in range(9):
            try:
                itens.append(lista[i])
            except Exception as e:
                break
        return render(request, 'inicio.html',{'itens':itens})

def cadastro(request):
        if request.method == "POST":
                form1 = UserForm(request.POST)
                form2 = TelForm(request.POST)
                if form1.is_valid() and form2.is_valid():
                        usuario = form1.save(commit=False)


                        #verifica se o email já foi cadastrado
                        if User.objects.filter(email=usuario.email):
                                messages.error(request, 'Email já está em uso!')
                                return render(request, 'cadastro.html', {'form1':form1, 'form2':form2})

                        #verifica se a confirmação de senha bate com a senha cadastrada
                        if usuario.password != request.POST.get('confirmar'):
                                messages.error(request, 'confimação de senha incorreta!')
                                return render(request, 'cadastro.html', {'form1':form1, 'form2':form2})

                        #passa a senha para o padrão do django
                        usuario.set_password(form1.cleaned_data['password'])

                        usuario.save()
                        salvar = form2.save(commit=False)
                        salvar.user = User.objects.get(email=usuario.email)
                        salvar.save()
                        return redirect('inicio')
                else:
                        return render(request, 'cadastro.html', {'form1':form1, 'form2':form2})
        form1 = UserForm()
        form2 = TelForm()
        return render(request, 'cadastro.html', {'form1':form1, 'form2':form2})

@login_required
def itemcadastro(request):
        if request.method == 'POST':
                form = ItemForm(request.POST, request.FILES)
                if form.is_valid():
                        if not(request.FILES.get('imagem')):
                                messages.error(request, 'adicione uma imagem para o produto!')
                                return render(request, 'item.html',{'form':form, 'texto': 'Cadastrar', 'usuario': request.user})
                        salvar = form.save(commit=False)
                        salvar.user = request.user
                        salvar.save()
                        return redirect('inicio')
        form = ItemForm()
        return render(request, 'item.html',{'form':form, 'texto': 'Cadastrar', 'usuario': request.user})

def itemver(request, id):
        item = Item.objects.get(pk=id)

        #habilita a opção de editar/excluir se o usuário for o mesmo que cadastrou o item
        if request.user == item.user:
                return render(request,'itemver.html',{'item':item, 'editar': True,
                 'url':request.META.get('HTTP_REFERER')})
        
        return render(request,'itemver.html',{'item':item, 'editar': False,
         'url':request.META.get('HTTP_REFERER')})

@login_required
def itemeditar(request, id):
        try:
                item = Item.objects.get(pk=id)
        except Item.DoesNotExist as e:
                messages.error(request, 'Item inválido!')
                return redirect('inicio')

        #verifica se o usuário que pediu para editar o item é o mesmo que o cadastrou
        if request.user != item.user:
                return redirect('inicio')

        if request.method == 'POST':
                form = ItemForm(request.POST, request.FILES, instance=item)
                if form.is_valid():
                        salvar = form.save(commit=False)
                        salvar.user = item.user
                        if not(salvar.imagem):
                                salvar.imagem = item.imagem.url
                        salvar.save()
                        return redirect('itemver', id=id)
        form = ItemForm(instance=item)
        return render(request, 'item.html',{'form':form, 'texto': 'Editar', 'usuario': request.user})

@login_required
def itemexcluir(request, id):
        try:
                item = Item.objects.get(pk=id)
        except Item.DoesNotExist as e:
                messages.error(request, 'Item inválido!')
                return redirect('inicio')

        #verifica se o usuário que pediu para excluir o item é o mesmo que o cadastrou
        if request.user != item.user:
                return redirect('inicio')

        #deleta a imagem da pasta /media/itens
        item.imagem.delete()
        #deleta o item do banco de dados
        item.delete()
        return redirect('meusitens')

def procura(request):
        if request.method=='POST':
                #seleciona todos os itens que tem o nome procurado em seu nome
                nome = Item.objects.filter(nome=request.POST.get('procura'))

                #seleciona todos os itens que tem o nome procurado em sua descrição
                #é transformado em lista para poder utilizar o método list.remove()
                des = list(Item.objects.filter(descricao=request.POST.get('procura')))

                #remove os itens repetidos na listagem
                for i in nome:
                        if i in des:
                                des.remove(i)

                return render(request, 'procura.html', {'nome':nome, 'des':des, 
                        'procura':request.POST.get('procura')})
        return redirect('inicio')
        
@login_required        
def meusitens(request):
        itens = Item.objects.filter(user=request.user)
        return render(request, 'meusitens.html', {'itens':itens, 'usuario': request.user})

