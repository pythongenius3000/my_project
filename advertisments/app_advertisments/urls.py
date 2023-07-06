from django.urls import path
from .views import index

urlpatterns = [
    path('', index) #на запрос "" получаем ответ из функции index из views
]