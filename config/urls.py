from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("exerciseHabitsRecord.urls")),
    path('staffroom/', include("staffroom.urls", namespace="staffroom")),
]
