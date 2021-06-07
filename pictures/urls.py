from django.urls import path
from .views import *

urlpatterns = [
    path('', PicturesHome.as_view(), name='home'),
    path('upload/', AddPicture.as_view(), name='add'),
    path('delete/<int:pk>/', DeletePicture.as_view(), name='delete')
]
