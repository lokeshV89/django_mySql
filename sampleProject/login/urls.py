from login import views
from django.urls import path, include
urlpatterns = [
    path('',views.login_index,name="login"),

]
