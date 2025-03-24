from django.urls import path
from . import views



urlpatterns= [
path("mdrrmolandingpage/", views.mdrrmolandingpage, name="mdrrmolandingpage"),
path("mdrrmocms/", views.cms, name="cms"),
path("mdrrmoreport/", views.report, name="report"),
 path('report_detail/<int:id>/', views.report_detail, name='report_detail'),
 
]