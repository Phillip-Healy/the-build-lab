from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def future(request):
    """ View function for request page """

    return render(request, 'request.html')
