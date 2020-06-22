from django.urls import path
from .views import *
urlpatterns = [
    path('list1', StatusListSearchAPIView.as_view()),
    path('list2/', StatusListSearchGeneric.as_view()),
    path('create_gen',StatusCreateGeneric.as_view()),
    path('get_gen/<int:id>',StatusRetrieveSerializer.as_view()),
    path('update_gen/<int:id>', StatusUpdateGeneric.as_view()),
    path('del_gen/<int:id>', StatusDeleteGeneric.as_view())

]