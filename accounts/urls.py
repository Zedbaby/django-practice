from django.urls import path
from .views import signup , change_user_info

app_name = 'accounts'

urlpatterns = [
    path('signup/' , signup , name='signup'),
    path('change_user_info/' , change_user_info , name='change_user_info'),
]
