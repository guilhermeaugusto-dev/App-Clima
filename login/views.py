from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from cadastro.models import User


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        try:
            user = User.objects.get(email=email)
            print(user)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Email ou senha incorretos'})

        if check_password(password, user.password):
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            request.session['user_first_name'] = user.first_name
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Email ou senha incorretos'})

    return render(request, 'login.html')