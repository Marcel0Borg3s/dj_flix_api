from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import GenreCreateListView, genre_detail_view

from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),

    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', genre_detail_view, name='genre-detail-view'),
]
