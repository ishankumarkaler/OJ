from django.urls import path

from . import views

urlpatterns = [
    path('', views.displayProblems, name='problem_list_page'),
    path('<int:prob_id>/', views.problemDescriptions, name='problem_description')
]