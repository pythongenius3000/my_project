from django.urls import path
from .views import answer

urlpatterns = [
    path('', answer), #на запрос "" получаем ответ из функции index из views
    path('lesson_4', answer),
]