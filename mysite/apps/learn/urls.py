#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-15 15:53:20
# @Author  : Zhangyu

from django.urls import path

from . import views

app_name = 'learn' #polls 命名空间
urlpatterns = [
    path('',  views.IndexView.as_view(),  name='index'),
    path('<int:pk>/',  views.DetailView.as_view(),  name='detail'),
    path('<int:pk>/results/',  views.ResultsView.as_view(),  name='results'),
    path('<int:question_id>/vote/',  views.vote,  name='vote'),
]