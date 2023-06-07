from rest_framework import serializers
from .models import Test, IQTestResult, EQTestResult

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('login',)

class IQTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = IQTestResult
        fields = ('score', 'timestamp', 'test')

class EQTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = EQTestResult
        fields = ('test', 'letters', 'timestamp')