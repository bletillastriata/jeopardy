from django.shortcuts import render, get_object_or_404, redirect
from .models import Clue
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ClueSearchForm
from django.db.models import Q
import datetime


def home(request):
	clues_list = Clue.objects.all()
	paginator = Paginator(clues_list, 50)
	page = request.GET.get('page')
	clues = paginator.get_page(page)

	form = ClueSearchForm()

	return render(request, 'home.html',{'clues':clues, 'form':form})

def clue_topics(request, pk):
	clue = get_object_or_404(Clue, pk=pk)
	return render(request, 'clues.html', {'clue':clue})

def search(request):
	if request.method == 'POST':

		form = ClueSearchForm(request.POST)
		print(form.is_valid())

		if form.is_valid():
			keyword = form.cleaned_data['keyword']
			clues_list = Clue.objects.filter(
				Q(question__icontains=keyword) |
				Q(answer__icontains=keyword) |
				Q(category__icontains=keyword)	
				)
			print("data was", form.cleaned_data)

			# filtering by date(s)
			if form.cleaned_data['start_date'] != '' and form.cleaned_data['end_date'] != '':
				start_date = form.cleaned_data['start_date']
				start_date = datetime.datetime.strptime(start_date, '%M-%d-%Y').date()
				end_date = form.cleaned_data['end_date']
				end_date = datetime.datetime.strptime(end_date, '%M-%d-%Y').date()
				clues_list = clues_list.filter(airdate__range=[start_date, end_date])
			if form.cleaned_data['start_date'] != '':
				start_date = form.cleaned_data['start_date']
				start_date = datetime.datetime.strptime(start_date, '%M-%d-%Y').date()
				clues_list = clues_list.filter(airdate__range=[start_date, datetime.date.today()])
			
			# filtering by value (difficulty)
			if form.cleaned_data['value'] != 'any':
				clues_list = clues_list.filter(value__exact=form.cleaned_data['value'])
			
			# filtering by category
			if form.cleaned_data['category'] != '':
				clues_list = clues_list.filter(category__exact=form.cleaned_data['category'])
			
			clues_list = clues_list.order_by('airdate')

			
			return render(request, 'searchresults.html',{'clues':clues_list, 'keyword':keyword})
	else:
		form = ClueSearchForm()
		return render(request, 'search.html', {'form': form})

