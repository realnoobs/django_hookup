from django.urls import path
from operator import itemgetter
from django.views.generic import TemplateView
from django.contrib import admin
from django_hookup.core import _django_hookup


class HookRegistryView(TemplateView):
    template_name = "admin/hooks_registry.html"

    def build_hook_info(self, func, order):
        info = {
            "order": order,
            "module": func.__module__,
            "function": func.__name__,
            "documentation": func.__doc__,
        }
        return info

    def get_hooks_data(self):
        hooks_data = dict()
        for name, hooks in _django_hookup.items():
            hooks_data[name] = [self.build_hook_info(*func) for func in sorted(hooks, key=itemgetter(1))]
        return hooks_data

    def get_context_data(self, **kwargs):
        kwargs.update(
            {
                "title": "Django Hooks Registry",
                "hook_list": self.get_hooks_data(),
                **admin.site.each_context(self.request),
            }
        )
        return super().get_context_data(**kwargs)


urlpatterns = [path("", admin.site.admin_view(HookRegistryView.as_view()), name="history_view")]
