from rest_framework import serializers

class SalesTaxDataSerializer(serializers.Serializer):
    zipCode = serializers.CharField(max_length=7)
    state = serializers.CharField(max_length=20)
    combined_rate = serializers.CharField(max_length=10)
    local_rate = serializers.CharField(max_length=10)
    state_rate = serializers.CharField(max_length=10)
    population = serializers.CharField(max_length=20)