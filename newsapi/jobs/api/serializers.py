from datetime import datetime
from django.utils.timesince import timesince

from rest_framework import serializers
from jobs.models import JobOffer


class JobOfferSerializer(serializers.ModelSerializer):
    
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = JobOffer
        fields = "__all__"

        # exclude = ""
        # fields = ("Title","description","body")

