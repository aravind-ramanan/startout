from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

#from hackathon

from rest_framework import viewsets, mixins

#scripts
from scripts.googlePlus import *

# Python
import oauth2 as oauth
import simplejson as json
import requests

# Models
from allocator.models import *
from allocator.serializers import SnippetSerializer
from allocator.forms import UserForm

app_name='allocator'

profile_track = None

getGoogle = GooglePlus(settings.GOOGLE_PLUS_APP_ID, settings.GOOGLE_PLUS_APP_SECRET)

		
def index(request):
    print "index: " + str(request.user)

    if not request.user.is_active:
        if request.GET.items():

            if profile_track == 'google':
                code = request.GET['code']
                state = request.GET['state']
                getGoogle.get_access_token(code, state)
                userInfo = getGoogle.get_user_info()
                username = userInfo['given_name'] + userInfo['family_name']

                try:
                    user = User.objects.get(username=username+'_google')
                except User.DoesNotExist:
                    new_user = User.objects.create_user(username+'_google', username+'@madewithgoogleplus', 'password')
                    new_user.save()

                    try:
                        profile = GoogleProfile.objects.get(user = new_user.id)
                        profile.access_token = getGoogle.access_token
                    except:
                        profile = GoogleProfile()
                        profile.user = new_user
                        profile.google_user_id = userInfo['id']
                        profile.access_token = getGoogle.access_token
                        profile.profile_url = userInfo['link']
                    profile.save()
                user = authenticate(username=username+'_google', password='password')
                login(request, user)

    context = {'hello': 'world'}
    return render(request, 'allocator/index.html', context)


def api_examples(request):
    if request.method == 'POST':
        project_name = request.POST.get('projectname')
        project_logo = request.POST.get('project_logo')
        project_desc = request.POST.get('description')
        project_cat = request.POST.get('category')
        project_skill = request.POST.get('skills_reqd')
        project_back = request.POST.get('edu_background_reqd')
        project_payment = request.POST.get('payment')
        new_project = Project(project_name = project_name)
        new_project.project_logo = project_logo
        new_project.description = project_desc
        new_project.category = project_cat
        new_project.skills_reqd = project_skill
        new_project.edu_background_reqd = project_back
        new_project.payment = project_payment
        new_project.date_created = timezone.now()
        new_project.status = "working"
        new_project.save()
        context = {'title' : "The project has been created"}
    context = {'title': 14}
    return render(request, 'allocator/api_examples.html', context)

def googlePlus(request):
    userInfo = getGoogle.get_user_info()
    return render(request, 'allocator/googlePlus.html', {'userInfo' : userInfo})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect('/allocator/login/')
        else:
            print user_form.errors
    else:
        user_form = UserForm()


    return render(request,
            'allocator/register.html',
            {'user_form': user_form, 'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/allocator/api/')
            else:
                return HttpResponse("Your Project allocator account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'allocator/login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/allocator/login/')

class CRUDBaseView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    pass

class SnippetView(CRUDBaseView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()


def google_login(request):
    global profile_track
    profile_track = 'google'
    google_url = getGoogle.get_authorize_url()
    return HttpResponseRedirect(google_url)

def searchproject(request):
    if request.method == 'GET':
        projectname = request.GET['projectname']
        projects = Project.objects.filter(project_name = 'projectname')
        print projects
        context['p']= projects
        return render(request, 'allocator/searchproject.html', context)
    else:
        return HttpResponse("Invalid request")

def createproject(request):
    return render(request, 'allocator/createproject.html', {})