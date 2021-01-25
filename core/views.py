import json
import requests
import re

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Endereco
from .forms import EnderecoForm


# Create your views here.
def home(request):
    pesquisa = request.GET.get('search', '')

    pesquisa_replace = re.sub('\D', '', pesquisa)

    if pesquisa:
        enderecos = Endereco.objects.filter(Q(cep__iregex=pesquisa_replace))
    else:
        enderecos = Endereco.objects.all()

    paginator = Paginator(enderecos, 10)
    numero_pagina = request.GET.get('pagina', 1)
    pagina = paginator.get_page(numero_pagina)

    if pagina.has_next():
        proxima_url = f'?pagina={pagina.next_page_number()}'
    else:
        proxima_url = ''

    if pagina.has_previous():
        url_anterior = f'?pagina={pagina.previous_page_number()}'
    else:
        url_anterior = ''

    return render(request, 'index.html', context={
        'pagina': pagina,
        'proxima_pagina_url': proxima_url,
        'pagina_anterior_url': url_anterior
    })


def cadastrar_endereco(request):
    form = EnderecoForm(request.POST or None)

    get_cep_data = request.POST.dict()
    cep = get_cep_data.get("cep")

    if (request.POST) and (not form.is_valid()):

        if cep == None or cep == "":
            pass
        else:
            cep_replace = re.sub('\D', '', cep)

        try:
            endereco: Endereco = Endereco.objects.get(Q(cep__exact=cep_replace))
        except:
            endereco: Endereco = Endereco.objects.filter(Q(cep__exact=cep_replace))
        if endereco:
            return JsonResponse(model_to_dict(endereco), status=200)
        else:
            dados_cep = ViaCEP(cep_replace)
            obj_cep: dict = dados_cep.getDadosCEP()
            obj_cep['cep'] = cep_replace
            return JsonResponse(obj_cep, status=200)
    else:
        try:
            endereco: Endereco = Endereco.objects.get(Q(cep__exact=cep))
            if request.method == 'POST':
                atualizar_endereco(request, endereco.id)
                return redirect('home')
        except:
            form = EnderecoForm(request.POST or None)

            if form.is_valid():
                form.save()
                return redirect('home')

            return render(request, 'endereco-form.html', {'form': form})


def atualizar_endereco(request, id):
    endereco = Endereco.objects.get(id=id)
    form = EnderecoForm(request.POST or None, instance=endereco)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'endereco-form.html', {'form': form, 'endereco': endereco})


def deletar_endereco(request, id):
    endereco = Endereco.objects.get(id=id)

    if request.method == 'POST':
        endereco.delete()
        return redirect('home')
    return render(request, 'endereco-delete-confirm.html', {'endereco': endereco})


class ViaCEP:

    def __init__(self, cep):
        self.cep = cep

    def getDadosCEP(self):
        url_api = ('http://www.viacep.com.br/ws/%s/json' % self.cep)
        req = requests.get(url_api)
        if req.status_code == 200:
            dados_json = json.loads(req.text)
            return dados_json
