from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'prototype'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='prototype/index.html'), name='index'),

    # Student
    url(r'^student/$', views.StudentListView.as_view(), name='student_list'),
    url(r'^student/(?P<pk>[0-9]+)/$', views.StudentDetailView.as_view(), name='student_detail'),

    # Je
    url(r'^je/$', views.JeListView.as_view(), name='je_list'),
    url(r'^je/(?P<pk>[0-9]+)/$', views.JeDetailView.as_view(), name='je_detail'),
]
