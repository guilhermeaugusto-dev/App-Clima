from django.shortcuts import render
from .forms import CadastroForm
from .models import User
from django.contrib.auth.hashers import make_password 

def verificar_senha(request):
    password = request.POST.get('password')
    confirmar_senha = request.POST.get('confirmar_senha')
    if password != confirmar_senha:
        return False
    return True
def cadastro_view(request):
  if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
          email = request.POST.get('email')
          email_exists = User.objects.filter(email=email).exists()
          if not verificar_senha(request=request):
                form.add_error('confirmar_senha', 'As senhas não conferem')
                return render(request, 'cadastro.html', {'form': form})
          elif email_exists:
                return render(request, 'cadastro.html', {'form': form})
          else:
            user = form.save(commit=False)
            user.password = make_password(request.POST.get('password'))
            user.save()
            return render(request, 'login.html')
        else:

            return render(request, 'cadastro.html', {'form': form})
  else:
        form = CadastroForm()
        return render(request, 'cadastro.html', {'form': form})