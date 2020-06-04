from django.urls import path
from .views import *
urlpatterns = [
    path('sample', json_example_view.as_view()),
    path('sample_mixin',Json_example_using_mixin.as_view())
]