#!/usr/bin/python
#  -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
#from reportlab.pdfgen import canvas
from django.http import StreamingHttpResponse
from django.core.exceptions import PermissionDenied
import hashlib
import os
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(created_date=timezone.now()).order_by('published_date')
    return render(request,'blog/index.html',{'posts':posts})

def cv(request):
    return  render(request,'blog/cv-en.html',{})

def cv_zh(request):
    return render(request,'blog/cv-ch.html',{})

def index(request):
    return render(request,'blog/index.html',{})

def project(request):
    return render(request,'blog/project.html',{})

def project_zh(request):
    return render(request,'blog/project_zh.html',{})

def myself(request):
    return render(request,'blog/myself.html',{})

def paper(request):
    return render(request,'blog/paper.html',{})

def paper1(request):
    return render(request,'blog/paper1.html',{})

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



def weixin(request):
    token = 'neal1991'
    signature = request.REQUEST.get('signature', '')
    timestamp = request.REQUEST.get('timestamp', '')
    nonce = request.REQUEST.get('nonce',  '')

    tmp_str = hashlib.sha1(''.join(sorted([token, timestamp, nonce]))).hexdigest()
    if tmp_str == signature:
        return HttpResponse(request.REQUEST.get('echostr', '123'))

    raise PermissionDenied