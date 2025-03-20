from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializer import (
    CheckRequestSerializer, CheckResponseSerializer,
    CreateRequestSerializer, CreateResponseSerializer,
    ConfirmRequestSerializer, ConfirmResponseSerializer,
    ReverseRequestSerializer, ReverseResponseSerializer,
    StatusRequestSerializer, StatusResponseSerializer,
)


# Check View
class CheckView(APIView):
    def post(self, request):
        serializer = CheckRequestSerializer(data=request.data)
        if serializer.is_valid():
            # Process the request (e.g., validate payment)
            response_data = {
                'serviceId': serializer.validated_data['serviceId'],
                'timestamp': serializer.validated_data['timestamp'],
                'status': 'OK',
                'data': {},
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create View
class CreateView(APIView):
    def post(self, request):
        serializer = CreateRequestSerializer(data=request.data)
        if serializer.is_valid():
            # Create a transaction
            transaction = Transaction.objects.create(
                service_id=serializer.validated_data['serviceId'],
                trans_id=serializer.validated_data['transId'],
                timestamp=serializer.validated_data['timestamp'],
                amount=serializer.validated_data['amount'],
                status='CREATED',
                data=serializer.validated_data['params'],
            )
            response_serializer = CreateResponseSerializer(transaction)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Confirm View
class ConfirmView(APIView):
    def post(self, request):
        serializer = ConfirmRequestSerializer(data=request.data)
        if serializer.is_valid():
            # Confirm the transaction
            try:
                transaction = Transaction.objects.get(trans_id=serializer.validated_data['transId'])
                transaction.status = 'CONFIRMED'
                transaction.confirm_time = serializer.validated_data['timestamp']
                transaction.save()
                response_serializer = ConfirmResponseSerializer(transaction)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            except Transaction.DoesNotExist:
                return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Reverse View
class ReverseView(APIView):
    def post(self, request):
        serializer = ReverseRequestSerializer(data=request.data)
        if serializer.is_valid():
            # Reverse the transaction
            try:
                transaction = Transaction.objects.get(trans_id=serializer.validated_data['transId'])
                transaction.status = 'REVERSED'
                transaction.reverse_time = serializer.validated_data['timestamp']
                transaction.save()
                response_serializer = ReverseResponseSerializer(transaction)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            except Transaction.DoesNotExist:
                return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Status View
class StatusView(APIView):
    def post(self, request):
        serializer = StatusRequestSerializer(data=request.data)
        if serializer.is_valid():
            # Get the transaction status
            try:
                transaction = Transaction.objects.get(trans_id=serializer.validated_data['transId'])
                response_serializer = StatusResponseSerializer(transaction)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            except Transaction.DoesNotExist:
                return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
