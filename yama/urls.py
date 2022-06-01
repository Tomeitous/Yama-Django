from django.contrib import admin
from django.urls import path
from yamanians import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('yamanians/', views.YamanianListView.as_view()),
    path('yamanians/<int:pk>', views.YamanianDetailView.as_view()),
    path('yamanians/<int:pk>/update', views.YamanianUpdateView.as_view()), 
    path('yamanians/<int:pk>/delete', views.YamanianDeleteView.as_view()),
    path('yamanians/create', views.YamanianCreateView.as_view()),
    path('anime/', views.AnimeListView.as_view()),
    path('anime/<int:pk>', views.AnimeDetailView.as_view()),
    path('anime/create', views.AnimeCreateView.as_view()),
    path('yamanians/<int:pk>/update', views.YamanianUpdateView.as_view()),
    path('comment/create', views.CommentCreateView.as_view()),
    
    path('accounts/login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view(next_page="/yamanians/")),
    path('register/', views.RegisterView.as_view()),
]

