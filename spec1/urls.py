from django.urls import path
from spec1.views import *

app_name='suma'

urlpatterns=[

    path('nand/',nand,name='nand')
]