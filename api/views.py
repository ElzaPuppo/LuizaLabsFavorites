from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Product, Client, Brand, Favorite, Review
from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
import json
from django.core import serializers
from .forms import RegisterProduct
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg
from django.db import models
from django.db.models import ExpressionWrapper, FloatField


def index(request):
    produtos = Product.objects.all()
    listaProdutos = Product.objects.all()
    search = request.GET.get('search')
    context = {'produtos': produtos, 'listaProdutos': listaProdutos}
    return render(request, 'index.html', context)

@csrf_exempt
def brands(request):
    if request.method == "GET":
        brand = Brand.objects.all()
        brands = []
        for bra in brand:
            brands.append(bra.to_dict())

        return JsonResponse({"brands": brands}, safe=False)

    elif request.method == "POST":
        payload = json.loads(request.body)
        name = payload.get("name")
       
        brands = Brand()
        brands.name = name
        brands.save()

        return JsonResponse({"brand": brands.to_dict()}, json_dumps_params={'ensure_ascii':False})

    else:
        HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def deletebrand(request, idbrand):
    if request.method == "DELETE":
        brand = get_object_or_404(Brand,pk=idbrand)
        name = brand.name

        brand.delete()
        return HttpResponse(f"A marca {name} foi deletada com sucesso!")

    else:
        HttpResponseNotAllowed(["DELETE"])


@csrf_exempt
def client(request, idclient):
    if request.method == "GET":
        client =get_object_or_404(Client, pk=idclient)

        return JsonResponse({"clients": client.to_dict()}, json_dumps_params={'ensure_ascii':False})

    elif request.method == "PUT":
        payload = json.loads(request.body)
        name = payload.get("name")
        email = payload.get("email", 0)    

        clients = Client.objects.get(pk=idclient)
        clients.name = name
        clients.email = email
        clients.id = idclient
        clients.save()
        
        return JsonResponse({"client": clients.to_dict()}, json_dumps_params={'ensure_ascii':False})
    elif request.method == "DELETE":        
        client = get_object_or_404(Client,pk=idclient)
        name = client.name
        client.delete()
        return HttpResponse(f"Cliente {name} deletado com sucesso!")

    else:
        HttpResponseNotAllowed(["GET", "PUT", "DELETE"])


@csrf_exempt
def clients(request):
    if request.method == "GET":
        client = Client.objects.all().order_by("name")
        clients = []
        for cli in client:
            clients.append(cli.to_dict())

        return JsonResponse({"clients": clients}, safe=False)

    elif request.method == "POST":
        payload = json.loads(request.body)
        payload = json.loads(request.body)
        name = payload.get("name")
        email = payload.get("email", 0)       

        clients = Client()
        clients.name = name
        clients.email = email
        try:
             clients.save()
        except IntegrityError as e: 
            print(e.message)
        
        return JsonResponse({"client": clients.to_dict()})

    else:
        HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def product(request, idproduct):
    if request.method == "GET":
        product = get_object_or_404(Product, pk=idproduct)
        review = Review.objects.all()
        review = review.filter(product=idproduct)
        reviews = []
        for rev in review:
            reviews.append(rev.to_dict())
        final = {"products": product.to_dict() }
        reviw = {"reviews": reviews }
        return JsonResponse(f"{final } - {reviw}" , json_dumps_params={'ensure_ascii':False}, safe=False)
    elif request.method == "PUT":
        payload = json.loads(request.body)
        title = payload.get("title")
        price = payload.get("price", 0)
        image = "URL"
        brand = Brand.objects.get(pk= payload.get("brand_id"))

        products = get_object_or_404(Product, pk=idproduct)
        products.title = title
        products.price = price
        products.brand = brand
        products.save()
        
        return JsonResponse({"product": products.to_dict()}, json_dumps_params={'ensure_ascii':False})
    elif request.method == "DELETE":        
        product = get_object_or_404(Product,pk=idproduct)
        name = product.title
        product.delete()
        return HttpResponse(f"Produto {name} deletado com sucesso!")

    else:
        HttpResponseNotAllowed(["GET", "PUT", "DELETE"])


@csrf_exempt
def products(request):
    if request.method == "GET":
        permission_classes = (IsAuthenticated)
        product = Product.objects.all().order_by("title")
        products = []
        for prod in product:
            products.append(prod.to_dict())

        return JsonResponse({"produtos": products}, safe=False)

    elif request.method == "POST":
        payload = json.loads(request.body)
        title = payload.get("title")
        price = payload.get("price", 0)
        brand = Brand.objects.get(pk= payload.get("brand_id"))  

        products = Product()
        products.title = title
        products.price = price
        products.brand = brand
        products.save()
        
        return JsonResponse({"product": products.to_dict()}, json_dumps_params={'ensure_ascii':False})

    else:
        HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def deletefavorite(request, idclient, idproduct):
    if request.method == "DELETE":
        favorite = get_object_or_404(Favorite,client_id=idclient, product_id=idproduct)
        nameC = favorite.client.name
        nameP = favorite.product.title

        favorite.delete()
        return HttpResponse(f"Favorito do produto {nameP} do cliente {nameC} deletado com sucesso!")

    else:
        HttpResponseNotAllowed(["DELETE"])


@csrf_exempt
def favorite(request, idclient):
    if request.method == "GET":
        favorite = get_list_or_404(Favorite, client=idclient)
        favorites = []
        for fav in favorite:
            favorites.append(fav.product.to_dict())

        return JsonResponse({"favorites": favorites}, safe=False)
    else:
        HttpResponseNotAllowed(["GET"])


@csrf_exempt
def favorites(request):
    if request.method == "GET":
        favorite = Favorite.objects.all()
        favorites = []
        for fav in favorite:
            favorites.append(fav.to_dict())

        return JsonResponse({"favorites": favorites}, safe=False)

    elif request.method == "POST":
        payload = json.loads(request.body)
        client = get_object_or_404(Client, pk= payload.get("client_id")) 
        product = get_object_or_404(Product, pk= payload.get("product_id")) 
       
        favorites = Favorite()
        favorites.client = client
        favorites.product = product
        favorites.save()

        return JsonResponse({"favorite": favorites.to_dict()}, json_dumps_params={'ensure_ascii':False})

    else:
        HttpResponseNotAllowed(["GET", "POST"])


@csrf_exempt
def detailreview(request, idclient, idproduct):
    if request.method == "GET":
        review = get_list_or_404(Review, client_id=idclient, product_id=idproduct)
        reviews = []
        for rev in review:
            reviews.append(rev.to_dict())

        return JsonResponse({"review": reviews}, safe=False)

    elif request.method == "DELETE":
        review = get_object_or_404(Review,client_id=idclient, product_id=idproduct)
        nameC = review.client.name
        nameP = review.product.title

        review.delete()
        return HttpResponse(f"Review do produto {nameP} do cliente {nameC} deletado com sucesso!")

    else:
        HttpResponseNotAllowed(["DELETE", "GET"])


@csrf_exempt
def review(request, idproduct):
    if request.method == "GET":
        review = get_list_or_404(Review, product=idproduct)
        reviews = []
        for rev in review:
            reviews.append(rev.to_dict())

        return JsonResponse({"reviews": reviews}, safe=False)
    else:
        HttpResponseNotAllowed(["GET"])


@csrf_exempt
def reviews(request):
    if request.method == "GET":
        review = Review.objects.all()
        reviews = []
        for rev in review:
            reviews.append(rev.to_dict())

        return JsonResponse({"reviews": reviews}, safe=False)

    elif request.method == "POST":
        payload = json.loads(request.body)
        client = get_object_or_404(Client, pk= payload.get("client_id")) 
        product = get_object_or_404(Product, pk= payload.get("product_id"))  
        text = payload.get("text")
        score = payload.get("score")

        reviews = Review()
        reviews.client = client
        reviews.product = product
        reviews.text = text
        reviews.score = score
        reviews.save()
        product = Product.objects.get(pk=payload.get("product_id"))         
        storage = Review.objects.filter(product = payload.get("product_id")).aggregate(Avg('score', output_field=FloatField()))
        product.reviewScore =round(storage['score__avg'],2)
        product.save()
        review = Review.objects.get(pk=reviews.id) 

        return JsonResponse({"review": review.to_dict()}, json_dumps_params={'ensure_ascii':False})

    else:
        HttpResponseNotAllowed(["GET", "POST"])     