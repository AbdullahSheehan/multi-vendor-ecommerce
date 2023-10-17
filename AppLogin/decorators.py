from functools import wraps
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

def seller_required():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(req, *args, **kwargs):
            if not req.user.is_seller:
                messages.warning(req, "You are not allowed to view this page!")
                return HttpResponseRedirect(reverse('homepage'))
            return view(req, *args, **kwargs)
        return _wrapped_view
    return decorator
