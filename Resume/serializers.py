from rest_framework import serializers
from .models import ResumeData

class ResumeSerializer(serializers.ModelSerializer):
    # uid = serializers.UUIDField(required=False)
    # experience = serializers.CharField(required=False)
    # projects = serializers.CharField(required=False)

    class Meta:
        model = ResumeData
        fields = '__all__'