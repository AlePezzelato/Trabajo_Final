from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from  core.views import index, CustomLoginView, registro, nosotros
from django.contrib.auth.views import LogoutView


app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("login/", CustomLoginView.as_view(), name = "login"),
    path("logout/", LogoutView.as_view(template_name = "core/logout.html"), name= "logout"),
    path("registro/", registro, name= "registro"),
    path("nosotros/", nosotros, name= "nosotros")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
