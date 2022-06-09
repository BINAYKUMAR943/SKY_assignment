from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import load_data_to_database,ReportViewSet


urlpatterns = [
    path("load_data_to_database/", load_data_to_database),
    # path("report/",ReportViewSet.as_view({'get':'list'})) 
    path("report/",ReportViewSet) 
    
]