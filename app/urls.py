from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('predict',views.predict,name='predict'),
    path('result',views.result,name='result'),
    
]
