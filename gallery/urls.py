from django.urls import path, include
from .views import(
  PostListView
)

app_name ='gallery'

urlpatterns =[
    path('', PostListView.as_view(), name='post_list'),
]

