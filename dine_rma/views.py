from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import List
from .forms import ListForm
# Create your views here.

def home(request):
	all_items = List.objects.all()
	if request.method == "POST":
		form = ListForm(request.POST)
		if form.is_valid():
			form.save()
			all_items = List.objects.all()
			messages.success(request, "New restaurent has been added!!!")
			return render(request, "card.html", {"all_items": all_items})
	return render(request, "card.html", {"all_items": all_items})

def delete(request, list_id):
	item = List.objects.get(pk = list_id)
	item.delete()
	messages.success(request, "Restaurent has been deleted!!!")
	return redirect("home")

def about(request):
	message = "This is about page"
	return render(request, "about.html", {"message": message})