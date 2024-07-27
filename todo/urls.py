# name o path se lien quan den index.html, reference to the link in index.html
#{% url 'register' %} vi du o trong ''
from django.urls import path

from .import views


urlpatterns = [
    
# -------------------- Home page----------------------------

    path('', views.home, name =""),



# ---------------- Register a user-------------------------

    path('register', views.register, name = "register"),



# ---------------- Login a user----------------------------

    path('my_login', views.my_login, name = "my_login"),



# ---------------- Dashboard page---------------------------

    path('dashboard', views.dashboard, name = "dashboard"),



# ----------------- Profile management ------------------------

    path('profile_management', views.profile_management, name ="profile_management"),


# ----------------- Delete account ------------------------


    path('delete_account', views.deleteAccount, name = "delete_account"),


# ---------------- Create a task ---------------------------

    path('create_task', views.createTask, name = "create_task"),
    


# ----------------- Read tasks ---------------------------

    path('view_tasks', views.viewTask, name ="view_tasks"),



# ----------------- Update task ---------------------------

    path('update_task/<str:pk>/', views.updateTask, name = "update_task"),



# ----------------- Delete task ---------------------------

    path('delete_task/<str:pk>/', views.deleteTask, name = "delete_task"),



# ---------------- Logout a user----------------------------

    path('user_logout', views.user_logout, name = "user_logout"),








]   
























