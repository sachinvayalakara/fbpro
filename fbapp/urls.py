from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.fn_login ),
    path('register/',views.fn_register ),
    path('',views.fn_home),
    path('userprofile/',views.fn_user_profile),
    path('changepassword/',views.fn_changepassword),
    path('log/',views.fn_log)

]