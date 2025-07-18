from django.contrib import admin
from django.urls import path
from core import views
from usuarios import views as usuarios_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("login/", usuarios_views.login_view, name="login"),
    path("register/", usuarios_views.register_view, name="register"),
    path("logout/", usuarios_views.logout_view, name="logout"),
    path("about/", views.about, name="about"),
    path("profile/", usuarios_views.profile_view, name="profile"),
]