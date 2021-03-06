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

    if request.method == 'POST' :
        dateofbirth=request.POST.get('dateofbirth')
        skills = request.POST.get('skills')
        edu_background = request.POST.get('edu_background')
        interests = request.POST.get('interests')
        userid = request.POST.get('userid')
        u=User.objects.filter(id= userid)
        new_user = UserDetail()
        new_user.user = u[0]
        new_user.date_of_birth = dateofbirth
        new_user.skills = skills
        new_user.edu_background = edu_background
        new_user.interests = interests
        userInfo = getGoogle.get_user_info()
        new_user.profile_pic_loc = userInfo['picture']
        new_user.save()
    
    if not request.user.is_active:
        if request.GET.items():

            if profile_track == 'google':
                code = request.GET['code']
                state = request.GET['state']
                getGoogle.get_access_token(code, state)
                userInfo = getGoogle.get_user_info()
                username = userInfo['given_name']

                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    email = username+'@nitc.ac.in'
                    new_user = User.objects.create_user(username, email.lower(), 'password')
                    new_user.first_name = userInfo['given_name']
                    new_user.last_name = userInfo['family_name']
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
                    print "something"        
                    user = authenticate(username=username, password='password')
                    login(request, user)
                    return HttpResponseRedirect('/allocator/adduserdetail/')
                user = authenticate(username=username, password='password')
                login(request, user)

    context = {'hello': 'world'}
    return render(request, 'allocator/index.html', context)

#view to add user detail
def adduserdetail(request):
    return render(request, 'allocator/adduserdetail.html',{})


def googlePlus(request):
    userInfo = getGoogle.get_user_info()
    return render(request, 'allocator/googlePlus.html', {'userInfo' : userInfo})


def api_examples(request):
    context = {'title': 14}
    return render(request, 'allocator/api_examples.html', context)

#views for manager
def viewall(request):
    try:
      rem = request.POST.get('removep')
    except:
      rem = ""
    if rem == "clicked":
      pid = int(request.POST.get('pid'))
      rid = request.POST.get('rid')
      pros = Project.objects.filter(project_id = pid)
      pro= pros[0]        
      s = pro.project_participants
      if s.count(',') == 0:
        s = "0"
      else :
        s = [int(i) for i in s.split(',')]
        s.remove(int(rid))
        s = ','.join([str(i) for i in s])
      pro.project_participants  = s
      pro.save()

    try:
      leave = request.POST.get('leave')
    except:
      leave = ""
    if leave == "clicked":
      pid = int(request.POST.get('pid'))
      uid = int(request.POST.get('uid')) 
      pros=Project.objects.filter(project_id = pid)
      pro= pros[0]
      if pro.project_owner != uid:
        pro.project_manager = pro.project_owner                 
    try:
      status = request.POST.get('status')
    except:
      status = ""
    if status == "working":
      pid = int(request.POST.get('pid'))
      pros=Project.objects.filter(project_id = pid)
      pro= pros[0]
      pro.status = "working"
      pro.save()
    if status == "not working":
      pid = int(request.POST.get('pid'))
      pros=Project.objects.filter(project_id = pid)
      pro= pros[0]
      pro.status = "not working"
      pro.save()
    try:
      rad = request.POST.get('rad')
    except:
      rad = ""
    if rad == "approve":
      xuid = request.POST.get('xuid')
      pid = int(request.POST.get('pid'))
      pros=Project.objects.filter(project_id = pid)
      pro= pros[0]
      s = pro.project_participants
      if s == "0":
        s = xuid
      else :
        s = s + ',' + xuid
      pro.project_participants = s
      s = pro.requests
      if s.count(',') == 0:
        s = "0"
      else :
        s = [int(i) for i in s.split(',')]
        s.remove(int(xuid))
        s = ','.join([str(i) for i in s])
      pro.requests  = s
      pro.save()
    elif rad == "decline":
      xuid = request.POST.get('xuid')
      pid = int(request.POST.get('pid'))
      pros=Project.objects.filter(project_id = pid)
      pro= pros[0]
      s = pro.requests
      if s.count(',') == 0:
        s = "0"
      else :
        s = [int(i) for i in s.split(',')]
        s.remove(int(xuid))
        s = ','.join([str(i) for i in s])
      pro.requests  = s
      pro.save()
      
    uid = int(request.POST.get('uid')) 
    projects = Project.objects.filter(project_manager = uid)
    con = []    
    for p in projects:
      temp = []
      a = p.requests.split(',')
      a = [int(i) for i in a]
      if a[0] == 0:
        assert(p.requests == "0", "p.requests is not 0 ")
        con.append((p,0))
# if project has no requests add ( <project_object>, 0 ) to the con list
      else :
        for idno in a:
          users = User.objects.filter(id = idno)
          u = users[0]
          temp.append((idno, u.username))
        con.append((p,temp))    
# if project has participants add ( <project_object>, [ ( <idno>, <username> ) ... ] )
    projects = Project.objects.filter(project_manager = uid)
    con2 = []    
    for p in projects:
      temp2 = []
      a = p.project_participants.split(',')
      a = [int(i) for i in a]
      if a[0] == 0:
        con2.append((p,0))
      else :
        for idno in a:
          users = User.objects.filter(id = idno)
          u = users[0]
          temp2.append((idno, u.username))
        con2.append((p,temp2)) 
           
    context={'list' : con,'list2' : con2}   
    return render(request, 'allocator/viewall.html', context)


def deleted(request):
    pname = 0
    if request.method == 'POST':
        pname = request.POST.get('del')
    projects = Project.objects.filter(project_name = pname)
    for p in projects:
        p.delete()
    context = {'i':pname}
    return render(request, 'allocator/deleted.html',context)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            u = UserDetail()
            p = User.objects.filter(username = user.username)
            q=p[0]
            q.first_name = request.POST.get('firstname')
            q.last_name = request.POST.get('secondname')
            q.save()
            u.user= user
            u.date_of_birth= request.POST.get('dateofbirth')
            u.skills= request.POST.get('skills')
            u.edu_background= request.POST.get('edu_background')
            u.interests=request.POST.get('interests')

            u.profile_pic_loc= request.POST.get('pro_pic_location')
            u.save()
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
        projects = Project.objects.all()
        pro = []
        for p in projects:
          if projectname in p.project_name:
            pro.append(p)
        #projects = Project.objects.filter(project_name = request.GET['projectname'])
        if len(projects) == 0:
            return HttpResponse("<html><p> No suggestions </p></html>")       
        else :            
            #pro = projects[0]            		
            context={'i': pro }
            return render(request, 'allocator/searchproject.html', context)
    else:
        return HttpResponse("Invalid request")

#project creation views
def createproject(request):
    member_list = User.objects.all()
    context = {'members' : member_list }
    return render(request, 'allocator/createproject.html', context)


def created(request):
    if request.method == 'POST':
        project_name = request.POST.get('projectname')
        project_logo = request.POST.get('project_logo')
        project_desc = request.POST.get('description')
        project_cat = request.POST.get('category')
        project_skill = request.POST.get('skills_reqd')
        project_back = request.POST.get('edu_background_reqd')
        project_payment = request.POST.get('payment')
        userid = request.POST.get('userid')
        new_project = Project(project_name = project_name)
        new_project.project_logo = project_logo
        new_project.description = project_desc
        new_project.category = project_cat
        new_project.skills_reqd = project_skill
        new_project.edu_background_reqd = project_back
        new_project.payment = project_payment
        new_project.date_created = timezone.now()
        new_project.status = "working"
        new_project.project_owner = userid
        member_list = request.POST.getlist('member_list')
        for a in member_list:
          if new_project.project_participants == "0":
            new_project.project_participants = str(a)          
          else :
            new_project.project_participants = new_project.project_participants + ',' + str(a)
        #manager nomination    
        manager_id = request.POST.get('manager')
        new_project.project_manager = manager_id
        new_project.save()
    return render(request, 'allocator/created.html', {})

def recommended(request):
    try:
      pid = request.GET['pid']
    except:
      pid = ""
    if pid != "":
        uid = int(request.GET['uid'])
        pid = int(request.GET['pid'])
        
        projects = Project.objects.filter(project_id = pid)
        pro = projects[0]
        if pro.requests == "0":
           pro.requests = str(uid)
        else :
           pro.requests = pro.requests + ',' + str(uid)
        pro.save()
    if request.method == 'GET':
        uid = int(request.GET['uid'])
    users = UserDetail.objects.all()
    usr = users[0]
    for u in users:
        if u.getid() == uid: 
             usr = u      
    a1 = usr.skills.split(",")
    projects = Project.objects.all()
    con = []
    for p in projects:
     if p.project_owner != uid :
       a2 = p.skills_reqd.split(",")
       l= list(set(a1).intersection(set(a2)))
       a = p.requests.split(',')
       a = [int(i) for i in a]
       if len(l) != 0 : 
             if uid in a:
                con.append((p, 0))
             else :       
                con.append((p, 1))
    context = { 'i': con }
    return render(request, 'allocator/recommended.html',context)

def sendreq(request):
     
     if request.method == 'GET':
        uid = int(request.GET['uid'])
        pid = int(request.GET['pid'])
        
        projects = Project.objects.filter(project_id = pid)
        pro = projects[0]
        if pro.requests == "0":
           pro.requests = str(uid)
        else :
           pro.requests = pro.requests + ',' + str(uid)
        pro.save()
        print pro.requests
        context = { 'i' : pro }
     return render(request, 'allocator/sendreq.html',context)


#views to edit projects
def editproject(request):
  if request.method == 'POST':
    try:
      rid = int(request.POST.get('rid'))
    except:
      rid = ""
    if rid != "":
      pros = Project.objects.filter(project_id = rid)
      pro = pros[0]
      pro.delete()
   
    pid = request.POST.get('project_id')
    print pid
   
    if pid == "#":         
        uid = int(request.POST.get('uid'))
        p = Project.objects.filter(project_owner = uid)
    else :
        project_name = request.POST.get('projectname')
        project_logo = request.POST.get('project_logo')
        project_desc = request.POST.get('description')
        project_cat = request.POST.get('category')
        project_skill = request.POST.get('skills_reqd')
        project_back = request.POST.get('edu_background_reqd')
        project_payment = request.POST.get('payment')
        project_id = int(request.POST.get('project_id'))
        uid = int(request.POST.get('uid'))
        p = Project.objects.filter(project_id = project_id)
        q=p[0]
        q.project_name = project_name
        q.project_logo = project_logo
        q.description = project_desc
        q.category = project_cat
        q.skills_reqd = project_skill
        q.edu_background_reqd = project_back
        q.payment = project_payment
        q.save()

        p = Project.objects.filter(project_owner = uid)
    
    context = {'project_list' : p }
    return render(request, 'allocator/editproject.html', context)
    
def edit(request, project_id):
    project = Project.objects.filter(project_id =project_id)
    project_obj = project[0]
    print project_obj.description
    context = {'project_id' : project_id, 'project_obj': project_obj} 
    return render(request, 'allocator/edit.html', context)
