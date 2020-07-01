from django.urls import path
from .views import *
from .jwt_views import views
urlpatterns = [
    path('list1', StatusListSearchAPIView.as_view()),
    path('list2/', StatusListSearchGeneric.as_view()),
    path('create_gen',StatusCreateGeneric.as_view()),
    path('get_gen/<int:id>',StatusRetrieveSerializer.as_view()),
    path('update_gen/<int:id>', StatusUpdateGeneric.as_view()),
    path('del_gen/<int:id>', StatusDeleteGeneric.as_view()),
    path('ret_upd_del/<int:id>',StatusDeleteRetriveUpdateGeneric.as_view()),
    path('create_lis_mix',StatusCreateListMixin.as_view()),
    path('single_crudl',StatusCRUDL.as_view()),
    path('double_crudl2/<int:id>',StatusRetUpdDel.as_view()),
    path('double_crudl2', StatusListCreate.as_view()),
    ###JWT_VIEWS
    path('hello',views.HelloView.as_view()),
    path('login',views.AuthView.as_view()),
    path('register',views.RegisterAuth.as_view())
]