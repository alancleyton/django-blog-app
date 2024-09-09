from django.urls import path

from blog.views import index_view

urlpatterns = [
    path('', index_view, name='index'),
]

