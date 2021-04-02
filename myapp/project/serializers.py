from rest_framework import serializers
from .models import *


class OrPodanieIssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrPodanieIssues
        # fields = '__all__'
        fields = ["id", "br_court_name", "kind_name", "cin", "registration_date","corporate_body_name", "br_section", "br_insertion", "text","street", "postal_code", "city"]


class CompaniesSerializer(serializers.ModelSerializer):
    or_podanie_issues_count = serializers.SerializerMethodField()
    znizenie_imania_issues_count = serializers.SerializerMethodField()
    likvidator_issues_count = serializers.SerializerMethodField()
    konkurz_vyrovnanie_issues_count = serializers.SerializerMethodField()
    konkurz_restrukturalizacia_actors_count = serializers.SerializerMethodField()

    class Meta:
        model = Companies
        fields = ['cin', 'name', 'br_section', 'address_line', 'last_update', 'or_podanie_issues_count', 'znizenie_imania_issues_count', 'likvidator_issues_count', 'konkurz_vyrovnanie_issues_count', 'konkurz_restrukturalizacia_actors_count']

    def get_or_podanie_issues_count(self, cin):
        return OrPodanieIssues.objects.filter(cin=cin.cin).count()

    def get_znizenie_imania_issues_count(self, cin):
        return ZnizenieImaniaIssues.objects.filter(cin=cin.cin).count()

    def get_likvidator_issues_count(self, cin):
        return LikvidatorIssues.objects.filter(cin=cin.cin).count()

    def get_konkurz_vyrovnanie_issues_count(self, cin):
        return KonkurzVyrovnanieIssues.objects.filter(cin=cin.cin).count()

    def get_konkurz_restrukturalizacia_actors_count(self, cin):
        return KonkurzRestrukturalizaciaActors.objects.filter(cin=cin.cin).count()