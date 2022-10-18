from django.urls import path, re_path
from .import views
from django.http import request
from django.conf.urls import url


urlpatterns += [
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='мои заказы'),


]




