from django.shortcuts import render
from .models import MyFile
# Create your views here.
def upload_file_views(request):
    if request.method == 'GET':
        return render (request, 'index.html')
    elif request.method == 'POST':
        # my_file -> se refere ao NAME que eu dei no input do HTML
        file = request.FILES.get("my_file")

        # instancia a classe MyFile e coloca o titulo original do arquivo do usuario
        mf = MyFile(title="minha_imagem", arq=file)
        # salva no banco de dados
        mf.save()
        return render(request, 'index.html', {'success': True})

    