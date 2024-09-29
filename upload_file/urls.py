from django.urls import path
from .views import upload_file_views
# importação para a pasta onde contem os arquivos de media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', upload_file_views, name="upload_file"),
]



# adiciona a nova url com as ja existentes
# quando o arquivo é de midia a gente nao utiliza o path mas sim o static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# MEDIA_ROOT FOI INICIALIZADO NO FINAL DO ARQUIVO SETTINGS E É ONDE TEM O CAMINHO DO MEDIA
# para ir até a midia que eu coloquei o random-forest:
# http://127.0.0.1:8000/media/random-forest.png