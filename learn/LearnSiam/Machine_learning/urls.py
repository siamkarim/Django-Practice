from django.urls import path
from . import views 

urlpatterns = [
 
  path('',views.machine),
  path('deep/',views.deep),

]
