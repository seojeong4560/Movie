from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.main),
    path('detail/<int:movie_pk>', views.movie_detail),
    # path('mypageMovie/<str:username>', views.mypageMovie)
]