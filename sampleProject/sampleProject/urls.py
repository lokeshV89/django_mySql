
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from login import views as ls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ls.login_index),
    path('login', include('login.urls')),
    path('user_login', ls.user_login, name='user_login'),
    path('home',ls.home,name="home",),
    path('logout',ls.logout_view,name="logout",),
    path('upload_doc',ls.upload_doc,name="upload_doc"),
    path('returnFileData',ls.returnFileData,name="returnFileData"),
    path('delete_doc',ls.delete_doc,name="delete_doc")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

