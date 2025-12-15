from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''Анджелина Джоли (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
 
Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]

def index(request):
	data = {
		'title': 'The main page', 
		'menu': menu,
		'posts': data_db
		}
	return render(request, 'women/index.html', context=data)


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


def about(request):
	d = {
		'title': 'About website',
		'menu': menu
		}
	return render(request, 'women/about.html', d)


def show_post(request, post_id):
	return HttpResponse(f'Отображение статьи с id = {post_id}')


def addpage(request):
	return HttpResponse('ADD THE page')


def contact(request):
	return HttpResponse('Feedback')


def login(request):
	return HttpResponse('Log IN')


def show_category(request, cat_id):
	return index(request)