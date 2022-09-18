from typing import List
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView,DetailView,ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BooksForm
from .models import Books

class BooksDeleteView(DeleteView):
    model = Books
    success_url = '/smart/books'
    template_name = 'books/books_delete.html'

class BooksUpdateView(UpdateView):
    model = Books
    success_url = '/smart/books'
    form_class = BooksForm

class BooksCreateView(CreateView):
    model = Books
    success_url = '/smart/books'
    form_class = BooksForm
    

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class BooksListView(LoginRequiredMixin,ListView):
    model = Books
    context_object_name = "books"
    template_name = "books/books_list.html"
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.books.all()

class BooksDetailView(DetailView):
    model = Books
    context_object_name = "book"

def detail(request,pk):
    try:
        book = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        raise Http404("book doesn't exist")
    return render(request,'books/books_detail.html',{'book': book})