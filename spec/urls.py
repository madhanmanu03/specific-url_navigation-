from django.urls import path
from spec.views import *

app_name='sum'

urlpatterns=[

    path('madhan/',madhan,name='madhan')
]