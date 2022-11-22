from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.main),
    path('detail/<int:movie_pk>/', views.movie_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:movie_pk>/comments/', views.comment_create),
    # path('mypageMovie/<str:username>', views.mypageMovie)
    path('mbti/<int:mbti_pk>/', views.mbti_detail),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
]