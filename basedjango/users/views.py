from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm

@login_required(login_url="/accounts/login/")
def index(request):
    context = {
        'title': 'Base Django',
        'user': request.user
    }
    template = loader.get_template('users/index.html')
    return HttpResponse(template.render(context, request))

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return index(request)
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})
