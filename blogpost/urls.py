from django.urls import path
from .views import *

app_name = 'blogpost'

urlpatterns = [
    path('' , HomePage , name='home'),
    path('add/' , AddPost , name='add'),
    path('detail/<int:pk>' , DetailPage , name='detail'),
    path('update/<int:pk>' , UpdatePost , name='update'),
    path('delete/<int:pk>' , DeletePost , name='delete'),
    path('recent_post' , RecentPost , name="recentpost")
]
