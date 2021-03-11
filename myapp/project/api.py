from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework import status


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'per_page'


class CustomSearchFilter(SearchFilter):
    search_param = 'query'


class CustomOrderingFilter(OrderingFilter):
    ordering_param = 'order_by'


class OrPodanieIssuesListView(generics.ListCreateAPIView):
    queryset = OrPodanieIssues.objects.all()
    serializer_class = OrPodanieIssuesSerializer

    pagination_class = CustomPageNumberPagination

    search_fields = ("corporate_body_name", "cin", "city")

    filter_backends = [DjangoFilterBackend, CustomSearchFilter]
    filter_fields = {
        'registration_date': ['lte', 'gte']
    }

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class()
        data = serializer.data

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        order_sign = ''
        queryset = super(OrPodanieIssuesListView, self).get_queryset()
        order_by = self.request.query_params.get('order_by', '')
        order_type = self.request.query_params.get('order_type', '')

        if order_type:
            if order_type=='asc':
                order_sign = ''
            else:
                order_sign = '-'
            return queryset.order_by(order_sign+order_by)

        # print(order_sign+order_by)
        return OrPodanieIssues.objects.all()


class OrPodanieDeleteAPIView(generics.DestroyAPIView, generics.RetrieveAPIView):
    lookup_field = 'id'

    def get_queryset(self):
        return OrPodanieIssues.objects.filter(id=self.kwargs['id'])

    serializer_class = OrPodanieIssuesSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status.HTTP_204_NO_CONTENT)