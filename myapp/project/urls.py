from django.urls import path
from .api import *


urlpatterns = [
    path('ov/submissions/', OrPodanieIssuesListView.as_view(), name='Submissions'),
    path('ov/submissions/<int:id>', OrPodanieDeleteAPIView.as_view(), name='Delete Submission'),
    path('companies/', CompaniesListAPIView.as_view(), name='Companies'),
]