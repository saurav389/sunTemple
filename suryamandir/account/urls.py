from django.urls import path
from .views import ExpenseView


urlpatterns = [
    path('',ExpenseView,name='account')

]