# SeuApp/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt
def submit_data(request):
    if request.method == 'POST':
        print("Chegou aqui")
        try:
            #data = json.loads(request.body)
            #name = data.get('name')
            #tempo = data.get('time')
            #preco = data.get('price')
            # Faça o que desejar com os dados, por exemplo, salvar no banco de dados.
            # ...

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