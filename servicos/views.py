# SeuApp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Service

import servicos.models
from . import models
import json

@csrf_exempt
def submit_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            nome = data.get('nome')
            tempo = data.get('tempo')
            valor = data.get('valor')
            print(nome,tempo,valor)
            services = servicos.models.Service(nome=nome, tempo=tempo, valor=valor)
            services.save()

            return JsonResponse({'message': 'Dados salvos com sucesso!'})
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Erro ao analisar os dados JSON.'}, status=400)

    return JsonResponse({'message': 'Método não permitido.'}, status=405)

@csrf_exempt
def options_submit_data(request):
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'  # Ou especifique as origens permitidas
    response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Content-Type'

    return response

def list_services(request):
    services = Service.objects.all()  # Consulta todos os serviços cadastrados
    service_data = [{'nome': service.nome, 'tempo': service.tempo, 'valor': service.valor} for service in services]

    return JsonResponse(service_data, safe=False)