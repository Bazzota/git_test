from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def index(request):
	return HttpResponse('The page of Women app')


def categories(request, cat_id):
	print(request.GET)
	return HttpResponse(f'<h1>The articles by cat</h1><p>Cat: {cat_id}</p>')


def cat_by_slug(request, cat_slug):
	return HttpResponse(f'The article by slug. Slug: {cat_slug}')


def get_request(request):
	print(request.GET)
	return HttpResponse(f'Информация в консоле.')


def archive(request, year):
	if year > 2023 and year < 2050:
		raise Http404()
	elif year > 2050:
		return redirect('home', permanent=True)
	elif year == 100:
		url = reverse('cats', args=('music_sto',)) 
		return redirect(url)
	return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")


def page_not_found(request, exception):
	return HttpResponseNotFound('Страница не найдена')