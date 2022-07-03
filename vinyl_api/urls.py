from django.urls import path
from . import views

urlpatterns = [
    path('api/records', views.RecordList.as_view(), name='record_list'),
    path('api/records/<int:pk>', views.RecordDetail.as_view(), name='record_detail'), 
]
