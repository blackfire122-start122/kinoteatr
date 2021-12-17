from django.shortcuts import render, redirect
from .models import *
from django.http import StreamingHttpResponse, JsonResponse
from .services import open_file
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()

str_url_type = 'all'
str_url_genre = 'all'
year = 'all'

years = [i for i in range(2010,2022)]
years.append("all")
years = years[::-1]

def find_films(str_url_type,str_url_genre,str_year):
    if str_year == 'all' and str_url_genre == 'all' and str_url_type == 'all':
        try:
            films = Films.objects.all()[:50]
            return films
        except:
            return {}
    q_filters = {"type":Q(typef__name = str_url_type),
                "genres":Q(genres__name = str_url_genre),
                "years":Q(year = str_year)
                }

    if str_url_type == 'all':
        del q_filters['type']
    if str_url_genre == 'all':
        del q_filters['genres']
    if str_year.isdigit() == False:
        del q_filters['years']

    try:
        if str_url_type == "Serial":
            del q_filters['type']
            serials = Serials.objects.filter(*(i for i in q_filters.values()))
            return serials
        else:
            films = Films.objects.filter(*(i for i in q_filters.values()))
            return films
    except:
        return {}

def user_ret(request):
    try:
        user = User.objects.get(pk=request.session["id"])
        return user
    except:
        return {}

def like_ajax(request):
    try:
        User.objects.get(pk=request.session["id"]).like_films.add(Films.objects.get(pk=int(request.GET['id'])))
        return JsonResponse({"data_text":"OK"}, status=200)
    except:
        return JsonResponse({"data_text":"error"}, status=500)

def comment_ajax(request):
    user = user_ret(request)
    if request.GET['typefors'] == "Serial":
        where_add = Serials
    else:
        where_add = Films
    if 'id_com' in request.GET:
        try:
            parent_com = Comments.objects.get(pk=request.GET['id_com'])  
            comm = Comments(user=user,parent=parent_com, comment=request.GET['comment'])
        except:
            return JsonResponse({"data_text":"error"}, status=500)
    else:
        comm = Comments(user=user,comment=request.GET['comment'])
    try:
        comm.save()
        where_add.objects.get(pk=request.GET['id']).comments.add(comm)
        return JsonResponse({"data_text":"OK"}, status=200)
    except:
        return JsonResponse({"data_text":"error"}, status=500)

def index(request):
    user = user_ret(request)
    try:
        films = Films.objects.order_by('-year')
    except:
        pass
    if request.method == "POST" and request.POST["name_film"]!='all':
        films = films.filter(name=request.POST["name_film"])[:50]
        name_film = request.POST["name_film"]
    return render(request, 
        "films/index.html",
        {"films":films,
        "genre":Genre.objects.all(),
        "type":Type.objects.all(),
        "years": years,
        "str_type":str_url_type,
        "str_genre":str_url_genre,
        "year":year,
        "reg": user,
        }
)

def about(request):
    user = {}
    user = user_ret(request)
    return render(request, "films/about.html",
        {"genre":Genre.objects.all(),
        "type":Type.objects.all(),
        "years": years,
        "str_type":str_url_type,
        "str_genre":str_url_genre,
        "year":year,
        "reg":user
        }
)

def film(request,typef,fn):
    if typef == "Serial":
        film = Serials.objects.get(id=fn)
    else:
        film = Films.objects.get(id=fn)
    user = {}
    user = user_ret(request)
    return render(request,
        "films/film.html",
        {"film":film,
        "genre":Genre.objects.all(),
        "type":Type.objects.all(),
        "years": years,
        "str_type":str_url_type,
        "str_genre":str_url_genre,
        "year":year,
        "reg":user
        }
)

def tg(request,str_url_type,str_url_genre,str_year):
    name_film = 'all'
    desc_genre = ""
    user = user_ret(request)
    str_sort = "Type: "+str_url_type+" Genre: "+str_url_genre+" Year: "+str_year
    
    films = find_films(str_url_type,str_url_genre,str_year)

    if request.method == "POST" and request.POST["name_film"]!='all':
        try:
            films = films.filter(name=request.POST["name_film"])[:50]
        except:
            pass
        str_sort = "Type: "+str_url_type+" Genre: "+str_url_genre+" Year: "+str_year+" Name: "+request.POST['name_film']
        name_film = request.POST["name_film"]

    if str_url_genre != "all":
        try:
            desc_genre = Genre.objects.get(name=str_url_genre).description
        except:
            pass 
    return render(request,
        "films/index.html",
        {"films":films,
        "genre":Genre.objects.all(),
        "type":Type.objects.all(),
        "years": years,
        "str_type":str_url_type,
        "str_genre":str_url_genre,
        "year":str_year,
        "str_sort":str_sort,
        "reg":user,
        "name_film":name_film,
        'description': desc_genre
        }
)

def get_streaming_video(request,typef,pk):
    file, status_code, content_length, content_range = open_file(request,typef, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

def autor(request):
    return render(request,"films/autor.html")
