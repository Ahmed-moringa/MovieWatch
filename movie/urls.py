from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='setadmin'

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('addmovie/', views.AddMovies.as_view(), name='addmovie'),
    path('setmovie/', views.SetMovies.as_view(), name='setmovie'),
    path('', views.LoiginAdmin.as_view(), name='adminlogin'),
    path('logout/', views.adminLogout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)