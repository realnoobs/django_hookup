from django.contrib import admin
from django.urls import path, include
import django_hookup

hooks = django_hookup.get_hooks("register_foobar")

text = ""
for func in hooks:
    text += func(func.__name__)
print(text)

urlpatterns = [
    path("admin/hooks/", include("django_hookup.urls")),
    path("admin/", admin.site.urls),
]
