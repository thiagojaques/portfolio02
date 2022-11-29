from portfolio.tarefas import views
from django.urls.conf import path


app_name = 'tarefas'

urlpatterns = [
    path('', views.home, name='home'),
    
]