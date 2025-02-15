"""
URL configuration for djangoCRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from autenticacion import views as auth_views  # ✅ Alias para autenticacion
from crud import views as crud_views  # ✅ Alias para crud

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.home, name='home'),  # Usa el alias correcto
    path('signup/', auth_views.signup, name='signup'),
    path('logout/', auth_views.signout, name='logout'),
    path('signin/', auth_views.signin, name='signin'),
    path('tasks/', crud_views.tasks, name='tasks'),  # Aquí sí es de "crud"
    path('tasks/create/', crud_views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', crud_views.task_detail, name='task_detail'),
]
