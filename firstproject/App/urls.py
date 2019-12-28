from django.urls import path
from App import views
urlpatterns = [
         path('',views.project_index,name="project_index"), #for all 
         path('<int:pk>/',views.project_detail,name="project_detail"), #primary key like a SSN, one project 
         
     ]

