from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contas/", include("contas.urls")),
    path("homepage/", include("homepage.urls")),
    path("servicos/", include("servicos.urls")),
]
