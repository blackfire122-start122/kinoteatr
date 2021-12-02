from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound,JsonResponse,HttpResponseRedirect
from users.models import *
from films.models import *
from films.views import user_ret
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

str_url_type = 'all'
str_url_genre = 'all'
year = 'all'

years = [i for i in range(2010,2022)]
years.append("all")
years = years[::-1]

def friend_no_index(request):
    user_account = user_ret(request)
    if request.is_ajax():
        try:
            user_account.friends.remove(User.objects.get(pk=int(request.GET['id'])))
        except:
            return JsonResponse({"data_text":"Error"}, status=400)
        return JsonResponse({"data_text":"OK"}, status=200)
    return JsonResponse({"data_text":"Error"}, status=400)


def dont_like(request):
    user_account = user_ret(request)
    if request.is_ajax():
        try:
            user_account.like_films.remove(Films.objects.get(pk=int(request.GET['id']))) 
        except:
            return JsonResponse({"data_text":"Error"}, status=400)
        return JsonResponse({"data_text":"OK"}, status=200)
    return JsonResponse({"data_text":"Error"}, status=400)

def friend_no_add_index(request):
    user_account = user_ret(request)
    if request.is_ajax():
        try:
            user_account.friends_want_add.remove(User.objects.get(pk=int(request.GET['id'])))
            return JsonResponse({"data_text":"OK"}, status=200)
        except:
            return JsonResponse({"data_text":"Error"}, status=400)
    return JsonResponse({"data_text":"Error"}, status=400)

def friend_add_index(request):
    user_account = user_ret(request)
    if request.is_ajax():
        try:
            friend = User.objects.get(pk=int(request.GET['id']))
            user_account.friends.add(friend)
            user_account.friends_want_add.remove(User.objects.get(pk=int(request.GET['id'])))
            return JsonResponse({"data_text":"OK"}, status=200)
        except:
            return JsonResponse({"data_text":"Error"}, status=400)
    return JsonResponse({"data_text":"Error"}, status=400)

def friend_add(request):
    user_account = user_ret(request)
    if request.is_ajax():
        try:
            User.objects.get(pk=int(request.GET['id'])).friends_want_add.add(user_account)
            return JsonResponse({"data_text":"Submit"}, status=200)
        except:
            return JsonResponse({"data_text":"Error"}, status=400)
    else:
        return JsonResponse({"data_text":"No ajax"}, status=400)

def all_users(request):
    user_account = user_ret(request)
    value_find = 'all'
    if request.method == "POST":
        try:
            users=User.objects.filter(name=request.POST['find_name'])
            value_find = request.POST['find_name']
        except:
            users = {}
        if request.POST['find_name'] == 'all':
            users = User.objects.all()[:50]
    else:
        users = User.objects.all()[:50]

    return render(request,
    "users/all_users.html",
    {"genre":Genre.objects.all(),
    "type":Type.objects.all(),
    "years": years,
    "str_type":str_url_type,
    "str_genre":str_url_genre,
    "year":year,
    "reg":user_account,
    "all_users": users,
    "value_find":value_find,
    }
)

def exit(request):
    user_account = user_ret(request)
    if request.is_ajax():
        request.session["id"] = None
        return JsonResponse({'status': 200, 'url':'/'})

def user(request,user_name):
    user_account = user_ret(request)
    error = ""
    try:
        if user_name!=user_account.username:
            return HttpResponseNotFound("Нема такого користувача")  
    except:
        return HttpResponseNotFound("Нема такого користувача")  

    
    if request.method == "POST":
        form = ChangeForm(request.POST,request.FILES,instance=user_account)
        if form.is_valid():
            form.save()
        else:
            error = form.errors
        
    form = ChangeForm()
    return render(request,
        "users/index.html",
        {"genre":Genre.objects.all(),
        "type":Type.objects.all(),
        "years": years,
        "str_type":str_url_type,
        "str_genre":str_url_genre,
        "year":year,
        "form":form,
        "user":user_account,
        'error':error
        }
)

def login(request):
    error = ""
    if request.method == "POST":
        form = Users_login_Form(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'],password=request.POST['password'])
            request.session["id"]=user.id
            return redirect('/users/account/'+user.username)
        else:
            error = "error data"

    form = Users_login_Form()
    return render(request, 
        "users/login.html",
        {'form':form,
        'country':Country.objects.all(),
        'error':error,
        "genre":Genre.objects.all(),
        "type":Type.objects.all(),
        "years": years,
        "str_type":str_url_type,
        "str_genre":str_url_genre,
        "year":year,
        }
)

def sigin(request):
    error = ""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username'])
            request.session["id"] = user.id
            return redirect('/users/account/'+str(user.username))
        else:
            form.error = error
    form = RegisterForm()

    return render(request, 
        "users/sigin.html",
        {'form':form,
        'country':Country.objects.all(),
        'error':error,
        "genre":Genre.objects.all(),
        "type":Type.objects.all(),
        "years": years,
        "str_type":str_url_type,
        "str_genre":str_url_genre,
        "year":year,
        }
)