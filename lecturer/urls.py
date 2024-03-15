from django.urls import path
from . import views

urlpatterns = [
    path('lec/', views.lecturerformview, name="lecturer_url"),
    path('lecshow/', views.lecshowview, name='lecshow_url'),
    path('lecup/<int:lid>', views.updateview, name='lecupdate_url'),
    path('lecdel/<int:lid>', views.deleteview, name='lecdelete_url'),
]