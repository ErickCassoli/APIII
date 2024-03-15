from django.shortcuts import render
from django.http import JsonResponse
from .models import Books
import json

def manipular_dados(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sensor = data.get('Sensor', False)
        botao = data.get('Botao', False)
        liga_robo = data.get('LigaRobo', False)
        reset_contador = data.get('ResetContador', False)
        valor_contagem = data.get('ValorContagem', 0)

        # Salvar os dados no banco de dados
        book = Books.objects.create(
            sensor=sensor,
            botao=botao,
            ligaRobo=liga_robo,
            resetContador=reset_contador,
            valorContagem=valor_contagem
        )
        book.save()
        return JsonResponse({'status': 'Dados salvos com sucesso!'})
    elif request.method == 'GET':
        # Buscar o último registro do banco de dados
        ultimo_dado = Books.objects.last()
        context = {'ultimo_dado': ultimo_dado}
        return render(request, 'exibir_dados.html', context)
    else:
        return JsonResponse({'error': 'Método não permitido.'}, status=405)
