# Este arquivo tem a resposabilidade de receber as requisições e dizer quais conteudos 
# as páginas terão
from django.shortcuts import render




# Create your views here.
def index(request): 
    return render(request, 'core\index.html')
