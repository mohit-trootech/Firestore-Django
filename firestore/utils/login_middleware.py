from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from quickreads.utils.constants import Constants, Urls
from django.contrib.messages import info


class LoginMiddleware:
    LOGIN_NOT_REQUIRED_PATHS = [
        reverse_lazy(Urls.LOGIN_REVERSE.value),
        reverse_lazy(Urls.REGISTER_REVERSE.value),
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path not in self.LOGIN_NOT_REQUIRED_PATHS:
            if request.session.get("uid") is None:
                info(request, Constants.NOT_AUTHENTICATED.value)
                return HttpResponseRedirect(reverse_lazy(Urls.LOGIN_REVERSE.value))
        return response
