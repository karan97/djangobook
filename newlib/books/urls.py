from django.urls import path

from . import views

urlpatterns = [
    path('books', views.BooksListView.as_view(),name="books.list"),
    path('books/<int:pk>', views.BooksDetailView.as_view(), name="books.detail"),
    path('books/<int:pk>/edit', views.BooksUpdateView.as_view(), name="books.update"),
    path('books/<int:pk>/delete', views.BooksDeleteView.as_view(), name="books.delete"),
    path('books/new',views.BooksCreateView.as_view(), name="books.new"),
]