from django.urls import path
from .views import index, top_sellers

urlpatterns = [
    path("", index, name='main-page'), #на запрос "" получаем ответ из функции index из views
    path("top-sellers/", top_sellers, name='top-sellers')
]