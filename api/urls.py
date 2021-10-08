from django.urls import path
from .api_views import ZayavkaApiList

app_name='api'

urlpatterns=[
    path('xd',ZayavkaApiList.as_view(),name='zayavka-api')
]