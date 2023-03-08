from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('graph', views.graph, name='graph'),
    path('education', views.education, name='education'),
    path('upload/', views.upload, name='upload'),
    path('research/', views.research_list, name='research_list'),
    path('research/<int:pk>/', views.delete_research, name = 'delete_research'),
    path('research/upload/', views.upload_research, name='upload_research'),
    path('register', views.registerUser, name='registerUser'),
    path('login', views.loginUser, name='loginUser'),
    path('logout_user', views.logoutUser, name='logoutUser'),
    path('graph_years', views.graphToYear, name='graphYears'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)