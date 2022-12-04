import itertools
import logging
import logging.config
import urllib.parse

from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.cache import get_conditional_response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.http import etag
from smart_admin.site import SmartAdminSite

from . import conf
from .forms import ConfigForm, FilterLogForm, LoggerConfigFormSet
from .manager import manager

logger = logging.getLogger(__name__)


def smart_logging_debug_panel(admin_site: SmartAdminSite, request, extra_context=None):
    context = admin_site.each_context(request)
    context["conf"] = conf
    context["title"] = "Logging Configuration"
    # if lgr := request.GET.get("logger"):
    #     context["data"] = manager.mapping[lgr]
    # else:
    context["data"] = manager.mapping
    return render(request, "admin/smart_logging/debug.html", context)


def smart_logging_online_panel(admin_site: SmartAdminSite, request, extra_context=None):
    context = admin_site.each_context(request)
    context["title"] = "Logging Configuration"
    context["conf"] = conf
    context["form"] = FilterLogForm()
    context["online_log"] = manager.online_handler.retrieve()
    return render(request, "admin/smart_logging/online.html", context)


def smart_logging_online_logs(admin_site: SmartAdminSite, request, extra_context=None):
    return JsonResponse(manager.online_handler.retrieve(), safe=False)


def smart_logging_debug_clearlog(
        admin_site: SmartAdminSite, request, extra_context=None
):
    manager.online_handler.clear()
    return JsonResponse([], safe=False)


def get_etag_key(*args):
    etag_key = "smart_logging.%s" % manager.get_signature()
    return etag_key


def smart_logging_config(admin_site: SmartAdminSite, request, extra_context=None):
    if response := get_conditional_response(request, etag=get_etag_key()):
        return response
    context = admin_site.each_context(request)
    context["title"] = "Logging Configuration"
    context["conf"] = conf

    initial_config = [
        {
            "logger": n,
            "level": logging._checkLevel(c["level"]),
            "handlers": c["handlers"],
            "propagate": c.get("propagate", True),
        }
        for n, c in manager.get_active_config().items()
    ]
    if request.method == "POST":
        form = ConfigForm(request.POST)
        formset = LoggerConfigFormSet(request.POST, initial=initial_config)
        if request.POST.get("reset"):
            logging.config.dictConfig(settings.LOGGING)
            messages.add_message(request, messages.SUCCESS, "Logging configuration reset")
        elif request.POST.get("config"):
            if formset.is_valid() and form.is_valid():
                updates = formset.save()
                if any(itertools.chain(updates.values())):
                    messages.add_message(
                        request, messages.SUCCESS, f"Configuration saved"
                    )
                    for logger, actions in updates.items():
                        if actions:
                            messages.add_message(
                                request, messages.SUCCESS, f"{logger} {','.join(actions)}"
                            )
                            # messages.add_message(request, messages.SUCCESS, f"{logger}: {';'.join(actions)}")
                else:
                    messages.add_message(request, messages.WARNING, "No changes detected")
                kwargs = urllib.parse.urlencode(form.cleaned_data)
                return redirect(f".?{kwargs}")
            else:
                messages.add_message(request, messages.ERROR, "Fix errors below")
    else:
        form = ConfigForm(initial=request.GET)
        formset = LoggerConfigFormSet(initial=initial_config)

    context["form"] = form
    context["formset"] = formset
    return render(request, "admin/smart_logging/config.html", context)


def smart_logging_panel(admin_site: SmartAdminSite, request, extra_context=None):
    if request.GET.get("page") == "logs":
        return smart_logging_online_logs(admin_site, request)
    if request.GET.get("page") == "online":
        return smart_logging_online_panel(admin_site, request)
    if request.GET.get("page") == "debug":
        return smart_logging_debug_panel(admin_site, request)
    if request.GET.get("page") == "clear":
        return smart_logging_debug_clearlog(admin_site, request)
    return smart_logging_config(admin_site, request)


smart_logging_panel.verbose_name = "Logging Configuration"
