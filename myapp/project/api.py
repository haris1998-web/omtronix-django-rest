from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import django_filters
from rest_framework import filters
from django.db import models


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'per_page'
    # page_size = 10

    def get_paginated_response(self, data):
        if 'page' in self.request.query_params:
            page = self.request.query_params['page']
        else:
            page = 1
        return Response({
            'results': data,
            'metadata': {
                'page': page,
                'per_page': self.get_page_size(self.request),
                'pages': self.page.paginator.num_pages,
                'total': self.page.paginator.count,
            },
        })


class ItemPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'per_page'
    # page_size = 10

    def get_paginated_response(self, data):
        if 'page' in self.request.query_params:
            page = self.request.query_params['page']
        else:
            page = 1
        return Response({
            'items': data,
            'metadata': {
                'page': page,
                'per_page': self.get_page_size(self.request),
                'pages': self.page.paginator.num_pages,
                'total': self.page.paginator.count,
            },
        })


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
        serializer = self.serializer_class(data=self.request.data)
        # data = serializer.data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        order_sign = ''
        queryset = super(OrPodanieIssuesListView, self).get_queryset()
        order_by = self.request.query_params.get('order_by', '')
        order_type = self.request.query_params.get('order_type', '')
        registration_date__lte = self.request.query_params.get('registration_date_lte', '')
        registration_date__gte = self.request.query_params.get('registration_date_gte', '')
        page = self.request.query_params.get('page', '')
        query = self.request.query_params.get('query', '')

        if order_type:
            if order_type=='asc':
                order_sign = ''
            else:
                order_sign = '-'
            queryset = queryset.order_by(order_sign+order_by)
        if registration_date__lte:
            queryset = queryset.filter(registration_date__lte=registration_date__lte, registration_date__gte=registration_date__gte)
        # print(order_sign+order_by)
        if page:
            return queryset
        if query:
            return queryset
        return OrPodanieIssues.objects.all()[:10]


class OrPodanieDeleteAPIView(generics.DestroyAPIView, generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = OrPodanieIssuesSerializer

    def get_queryset(self):
        queryset = OrPodanieIssues.objects.filter(id=self.kwargs['id'])
        return queryset

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.serializer_class()
            self.perform_destroy(instance)
            return Response({'message': 'Záznam zmazaný'}, status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({'message': 'Záznam neexistuje'}, status=status.HTTP_400_BAD_REQUEST)


class CompaniesListAPIView(generics.ListAPIView):
    serializer_class = CompaniesSerializer
    queryset = Companies.objects.all()
    pagination_class = ItemPageNumberPagination

    search_fields = ("name", "address_line")

    filter_backends = [DjangoFilterBackend, CustomSearchFilter]

    filter_fields = {
        'last_update': ['lte', 'gte']
    }

    def get_queryset(self):
        queryset = super(CompaniesListAPIView, self).get_queryset()
        order_by = self.request.query_params.get('order_by', '')
        order_type = self.request.query_params.get('order_type', '')
        last_update_lte = self.request.query_params.get('last_update_lte', '')
        last_update_gte = self.request.query_params.get('last_update_gte', '')
        query = self.request.query_params.get('query', '')
        page = self.request.query_params.get('page', 1)
        # print(page)

        if order_type:
            if order_type=='asc':
                order_sign = ''
            else:
                order_sign = '-'
            queryset = queryset.order_by(order_sign+order_by)
        if last_update_lte:
            queryset = queryset.filter(last_update__lte=last_update_lte, last_update__gte=last_update_gte)
        if query:
            return queryset
        if page:
            return queryset
        return Companies.objects.all()[:10]


