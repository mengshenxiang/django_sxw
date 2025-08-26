# -*- coding: utf-8 -*-
# @Time : 2025/8/26 13:07
# @Author : 宋先旺
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]