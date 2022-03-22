from django.urls import path
from .views import *

urlpatterns = [
    path('<int:npm>/', MahasiswaAPIViewWithID.as_view()),
    path('', MahasiswaAPIView.as_view()),
]
