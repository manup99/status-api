from django.urls import path
from .views import *
urlpatterns = [
    path('sample', update_model_detail_view.as_view())
]