from django.urls import path
from . import views

urlpatterns = [
    path('crs/', views.coursesformview, name="courses_url"),
    path('crsv/', views.showView, name='show_url'),
    path('up/<int:cid>', views.updateview, name='update_url'),
    path('del/<int:cid>', views.deleteview, name='delete_url'),
]
