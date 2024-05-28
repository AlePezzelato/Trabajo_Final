from django.urls import path
from  core.views import index, CustomLoginView, registro
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("login/", CustomLoginView.as_view(), name = "login"),
    path("logout/", LogoutView.as_view(template_name = "core/logout.html"), name= "logout"),
    path("registro/", registro, name= "registro"),
]

urlpatterns += staticfiles_urlpatterns()