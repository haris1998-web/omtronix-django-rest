from rest_framework import serializers
from .models import *


class OrPodanieIssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrPodanieIssues
        # fields = '__all__'
        fields = ["id", "br_court_name", "kind_name", "cin", "registration_date","corporate_body_name", "br_section", "br_insertion", "text","street", "postal_code", "city"]