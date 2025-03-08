from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student_delete/<int:student_id>/', views.student_delete, name='student_delete'),
    path('student_edit/', views.student_edit, name='student_edit'),
]
