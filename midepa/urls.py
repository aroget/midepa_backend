from django.conf.urls import url, include
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^api/v1/', include('midepa.api.urls', namespace='api')),
    url(r'^auth', views.obtain_auth_token),
]
