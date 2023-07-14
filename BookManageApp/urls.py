from django.urls import path
from .views import UserRegisteration,BookCreate,BookList,BookUpdate,BookReterieve,BookDelete
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns=[
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
    path('registerapi/',UserRegisteration.as_view(),name='user_register'),
    path('list/',BookList.as_view(),name='book_list'),
    path('retrieve/<int:pk>/',BookReterieve.as_view(),name='book_retrieve'),
    path('create/',BookCreate.as_view(),name='book_create'),
    path('update/<int:pk>/',BookUpdate.as_view(),name='book_update'),
    path('delete/<int:pk>/',BookDelete.as_view(),name='book_delete'),
    
]