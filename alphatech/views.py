from datetime import date
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Mentee, Mentor

# Create your views here.

# Index Page
def index(request):
    return render(request, 'alphatech/index.html', {'message': '1'})

# Blog Page
def blog(request):
    sent = {
        'blogs' : Blog.objects.all()[::-1], #To make the newer post appear upper
        'message' : '2'
    }
    return render(request, 'alphatech/blog.html', sent)

# Mentor Page
def mentor(request):
    sent = {
        'mentors' : Mentor.objects.all(),
        'message' : '3'
    }
    return render(request, 'alphatech/mentor.html', sent)

# Mentee Page
def mentee(request):
    sent = {
        'mentees' : Mentee.objects.all(),
        'message' : '4'
    }
    return render(request, 'alphatech/mentee.html', sent)

# Author Page
def author(request):
    return render(request, 'alphatech/author.html', {'message' : '5'})

# Read More
def read_more(request, blog_id):
    content_blog = Blog.objects.get(pk = blog_id)
    return render(request, 'alphatech/read_more.html', {'blog_id': blog_id, 'content_blog': content_blog})

# Forms Page
def forms(request):
    return render(request, 'alphatech/forms.html', {})

# After Submit
def submit_form(request):
    new_content = Blog(foto = request.POST['foto'], jumlah_komentar = 0, judul_post = request.POST['judul_post'], konten = request.POST['konten'], waktu_publikasi = date.today())
    new_content.save()
    return HttpResponse('Thankyou, your story has been submitted! :D')