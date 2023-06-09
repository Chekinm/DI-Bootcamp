"""
URL configuration for students project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from students_app.views import StudentsList, StudentDetails, StudentsLookUp
from students_app.views import StudentsLookUpGeneral
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('students/', StudentsList.as_view(), name ='students-list'),
    path('students/<int:pk>', StudentDetails.as_view(), name ='student-details'),
    path('students_q/', StudentsLookUp.as_view(), name ='students-search'),
    path('students_q_all/', StudentsLookUpGeneral.as_view(), name ='students-search-all'),
    path('__debug__/', include('debug_toolbar.urls')),

]
