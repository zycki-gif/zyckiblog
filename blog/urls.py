from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
    
]
