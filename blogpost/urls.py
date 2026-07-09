from django.urls import path
from .views import HomePage , DetailPage , AddPost , RecentPost

app_name = 'blogpost'

urlpatterns = [
    path('' , HomePage , name='home'),
    path('add/' , AddPost , name='add'),
    path('detail/<int:pk>' , DetailPage , name='detail'),
    path('recent_post' , RecentPost , name="recentpost")
]
