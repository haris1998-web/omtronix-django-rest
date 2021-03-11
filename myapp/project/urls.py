from django.urls import path
from .api import *


urlpatterns = [
    path('submissions/', OrPodanieIssuesListView.as_view(), name='Submissions'),
    path('submissions/<int:id>', OrPodanieDeleteAPIView.as_view(), name='Delete Submission'),
]