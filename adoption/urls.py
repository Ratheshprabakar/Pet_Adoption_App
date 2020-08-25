from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('adoption/<int:pet_id>/',views.pet_details,name='details'),
]
