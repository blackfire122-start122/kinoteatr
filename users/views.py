from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound,JsonResponse,HttpResponseRedirect,HttpResponse
from users.models import *
from films.models import *
from films.views import user_ret
from .forms import *
from django.contrib.auth import get_user_model, authenticate

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
            return JsonResponse({"data_text":"Error"}, status=500)
        return JsonResponse({"data_text":"OK"}, status=200)
    return JsonResponse({"data_text":"Error"}, status=500)


def dont_like(request):
    user_account = user_ret(request)
    if request.GET['typefors'] == "Serial":
        try:
            user_account.like_serials.remove(Serials.objects.get(pk=int(request.GET['id']))) 
            return JsonResponse({"data_text":"OK"}, status=200)
        except:
            return JsonResponse({"data_text":"Error"}, status=500)
    else:
        try:
            user_account.like_films.remove(Films.objects.get(pk=int(request.GET['id']))) 
            return JsonResponse({"data_text":"OK"}, status=200)
        except:
            return JsonResponse({"data_text":"Error"}, status=500)

def friend_no_add_index(request):
    user_account = user_ret(request)
    if request.is_ajax():
        try:
            user_account.friends_want_add.remove(User.objects.get(pk=int(request.GET['id'])))
            return JsonResponse({"data_text":"OK"}, status=200)
        except:
            return JsonResponse({"data_text":"Error"}, status=500)
    return JsonResponse({"data_text":"Error"}, status=500)

def friend_add_index(request):
    user_account = user_ret(request)
    if request.is_ajax():
        try:
            friend = User.objects.get(pk=int(request.GET['id']))
            user_account.friends.add(friend)
            user_account.friends_want_add.remove(User.objects.get(pk=int(request.GET['id'])))
            return JsonResponse({"data_text":"OK"}, status=200)
        except:
            return JsonResponse({"data_text":"Error"}, status=500)
    return JsonResponse({"data_text":"Error"}, status=500)

def friend_add(request):
    user_account = user_ret(request)
    if request.is_ajax():
        try:
            User.objects.get(pk=int(request.GET['id'])).friends_want_add.add(user_account)
            return JsonResponse({"data_text":"Submit"}, status=200)
        except:
            return JsonResponse({"data_text":"Error"}, status=500)
    else:
        return JsonResponse({"data_text":"No ajax"}, status=500)

def all_users(request):
    user_account = user_ret(request)
    value_find = 'all'
    if request.method == "POST":
        try:
            users=User.objects.filter(username=request.POST['find_name'])
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
        r_copy = request.POST
        if not r_copy['country']:
            r_copy = request.POST.copy()
            r_copy['country'] = user_account.country
        form = ChangeForm(r_copy,request.FILES,instance=user_account)
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
            error = form.errors 
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


from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "users/passwords/password_reset_email.txt"
                    c = {
                        "email":user.email,
                        'domain':'127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'gsambir519@gmail.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("password_reset_done")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="users/passwords/password_reset.html", context={"password_reset_form":password_reset_form})
