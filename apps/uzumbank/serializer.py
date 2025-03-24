from rest_framework import serializers
from .models import UzumbankTransaction


# Check Request and Response
class CheckRequestSerializer(serializers.Serializer):
    serviceId = serializers.IntegerField()
    timestamp = serializers.IntegerField()
    params = serializers.JSONField()


class CheckResponseSerializer(serializers.Serializer):
    serviceId = serializers.IntegerField()
    timestamp = serializers.IntegerField()
    status = serializers.CharField()
    data = serializers.JSONField()


# Create Request and Response
class CreateRequestSerializer(serializers.Serializer):
    serviceId = serializers.IntegerField()
    timestamp = serializers.IntegerField()
    transId = serializers.UUIDField()
    params = serializers.JSONField()
    amount = serializers.IntegerField()


class CreateResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UzumbankTransaction
        fields = ['service_id', 'trans_id', 'status', 'trans_time', 'data', 'amount']


# Confirm Request and Response
class ConfirmRequestSerializer(serializers.Serializer):
    serviceId = serializers.IntegerField()
    timestamp = serializers.IntegerField()
    transId = serializers.UUIDField()
    paymentSource = serializers.CharField()
    tariff = serializers.CharField(allow_null=True)
    processingReferenceNumber = serializers.CharField(allow_null=True)
    phone = serializers.CharField()


class ConfirmResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UzumbankTransaction
        fields = ['service_id', 'trans_id', 'status', 'confirm_time', 'data', 'amount']


# Reverse Request and Response
class ReverseRequestSerializer(serializers.Serializer):
    serviceId = serializers.IntegerField()
    timestamp = serializers.IntegerField()
    transId = serializers.UUIDField()


class ReverseResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UzumbankTransaction
        fields = ['service_id', 'trans_id', 'status', 'reverse_time', 'data', 'amount']


# Status Request and Response
class StatusRequestSerializer(serializers.Serializer):
    serviceId = serializers.IntegerField()
    timestamp = serializers.IntegerField()
    transId = serializers.UUIDField()


class StatusResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UzumbankTransaction
        fields = ['service_id', 'trans_id', 'status', 'trans_time', 'confirm_time', 'reverse_time', 'data', 'amount']
