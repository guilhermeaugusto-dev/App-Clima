import requests
from django.shortcuts import render, redirect

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    contexto = {}
    cidade_pesquisada = request.GET.get('cidade')

    if cidade_pesquisada:
        pais = 'BR'
        api_key = '8521319558e38c23140c95b9c38a1207'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade_pesquisada},{pais}&appid={api_key}&units=metric&lang=pt_br'
        try:
            response = requests.get(url).json()
            if response.get('cod') == 200:
                contexto = {
                    'clima': {
                        'cidade': response['name'],
                        'pais': response['sys']['country'],
                        'temperatura': round(response['main']['temp']),
                        'descricao': response['weather'][0]['description'],
                        'icone': response['weather'][0]['icon'],
                    },
                    'cidade_pesquisada': cidade_pesquisada
                }
            else:
                contexto['error'] = 'Cidade não encontrada.'

        except requests.exceptions.RequestException:
            contexto['error'] = 'Não foi possível conectar ao serviço de clima.'

    return render(request, 'dashboard.html', contexto)