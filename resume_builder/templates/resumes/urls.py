from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_resumes, name='list_resumes'),
    path('create/', views.create_resume, name='create_resume'),
    path('<int:resume_id>/edit/', views.edit_resume, name='edit_resume'),
    path('<int:resume_id>/add_section/', views.add_section, name='add_section'),
    path('<int:resume_id>/delete/', views.delete_resume, name='delete_resume'),
]