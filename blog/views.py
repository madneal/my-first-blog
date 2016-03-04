#!/usr/bin/python
#  -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from reportlab.pdfgen import canvas
from django.http import StreamingHttpResponse
import os
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(created_date=timezone.now()).order_by('published_date')
    return render(request,'blog/index.html',{'posts':posts})

def cv(request):
    return  render(request,'blog/cv.html',{})

def cv_zh(request):
    return render(request,'blog/cv_zh.html',{})

def index(request):
    return render(request,'blog/index.html',{})

def weatherapp(request):
    return render(request,'blog/weatherapp.html',{})

def download_file(request):
    BASE = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(BASE,"static/media/cv.pdf")
    def file_iterator(filename,chunk_size=512):
        with open(filename) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_filename = "cv.pdf"
    response = StreamingHttpResponse(file_iterator(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format('cv.pdf')

    return response

def download_cv(request):
    BASE = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(BASE,'static/media/中文简历.pdf')
    def file_iterator(filename,chunk_size=512):
        with open(filename) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    response = StreamingHttpResponse(file_iterator(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format('中文简历.pdf')

    return  response

def output_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment;filename="cv.pdf"'

    p = canvas.Canvas(response)

    p.drawString(100,100,"hello world")
    p.showPage()
    p.save()
    return response