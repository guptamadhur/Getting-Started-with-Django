from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

class Another(View):
    books = Book.objects.all()
    output = ''
    for book in books:
        output += f"We have {book.title} books with ID {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)

def first(request):
    return HttpResponse('First Message from Views')

def htmlFirst(request):
    books = Book.objects.all()
    return render(request, 'first_temp.html', {'books': books})