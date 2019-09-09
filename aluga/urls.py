from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', views.main, name='inicio'),
	path('cadastro/', views.cadastro, name='cadastro'),
	path('item/cadastro/', views.itemcadastro, name='itemcadastro'),
	path('item/ver/<int:id>', views.itemver, name='itemver'),
	path('item/editar/<int:id>', views.itemeditar, name='itemeditar'),
	path('item/excluir/<int:id>', views.itemexcluir, name='itemexcluir'),
	path('procura/', views.procura, name='procura'),
	path('meusitens/', views.meusitens, name='meusitens'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)