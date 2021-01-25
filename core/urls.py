from django.urls import path
from .views import home, cadastrar_endereco, atualizar_endereco, deletar_endereco

urlpatterns = [
    path('', home, name='home'),
    path('endereco/novo', cadastrar_endereco, name='cadastrar_endereco'),
    path('endereco/<int:id>/atualizar', atualizar_endereco, name='atualizar_endereco'),
    path('endereco/<int:id>/deletar', deletar_endereco, name='deletar_endereco'),

]
