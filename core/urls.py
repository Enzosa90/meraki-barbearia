from django import urls
from . import views

urlpatterns = [
    urls.path('', views.IndexListView.as_view(), name='index'),
]