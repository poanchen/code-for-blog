from django.conf.urls import url

urlpatterns = [
  # http://127.0.0.1:8000/search
  # http://127.0.0.1:8000/search/
  url(r'^search/?', views.search, name='search'),
]