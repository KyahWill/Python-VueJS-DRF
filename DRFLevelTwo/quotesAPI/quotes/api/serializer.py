from rest_framework import serializers
from quotes.models import quotes


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = quotes
        fields = "__all__"
