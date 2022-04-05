from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import(
  PostListView
)

app_name ='gallery'

urlpatterns =[
    path('', PostListView.as_view(), name='post_list'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
