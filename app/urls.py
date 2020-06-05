from django.urls import path
from .views import *
from .puredjangoapi.views import *
urlpatterns = [
    path('sample', json_example_view.as_view()),
    path('sample_mixin',Json_example_using_mixin.as_view()),
    path('serial_update',Serialized_UpdateClass_View.as_view()),
    path('serial_list',SerializedListView.as_view()),
    path('serial_single',Serialize_single_Object.as_view()),
    path('serial_single_manager',SerializeSingleObject_using_update_manager.as_view()),
    path('serial_list_manager',SerializeList_using_update_manager.as_view()),
    path('serial_list_essential',SerializeList_Only_UsefulData_Using_Update_Manager.as_view()),
    #Here we are dealing with Pure django API
    path('pure_single/<int:id>',UpdateModelDetailAPIView.as_view()),
    path('pure_list',UpdateModelListView.as_view())
]