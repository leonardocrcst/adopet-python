from django.shortcuts import render

# Por padrão, o código html fica em [app]/templates/[app]/[file].html
# Para cada página, uma rota deve ser criada em [root]/urls.py, ou
# ainda melhor, cada app deve possuir seu arquivo urls.py

def home(request):
  return render(request, 'pet/home.html')