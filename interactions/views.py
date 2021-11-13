""" Views for interactions app """
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import FutureRequest


@login_required
def future(request):
    """ View function for request page """

    user = request.user.get_username
    context = {'user': user}

    return render(request, 'request.html')
