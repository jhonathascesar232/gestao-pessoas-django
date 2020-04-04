
from django.urls import path
#
# Conf.. para arquivos estáticos
from django.conf import settings
from django.conf.urls.static import static

from .views import hello, list_person, person_new, update, delete

urlpatterns = [
    # path('', hello),
    path('listar/', list_person, name = 'list_person'),
    path('person/', person_new, name = 'person_new'),
    path('update/<int:id>/', update, name = 'update_person'),
    path('delete/<int:id>/', delete, name = 'delete_person'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Conf.. para arquivos estáticos
