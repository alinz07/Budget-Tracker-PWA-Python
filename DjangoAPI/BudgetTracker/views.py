from django.shortcuts import render
from django.http.response import JsonResponse

#use it to allows other domains to access api methods, other domains like front end project
from django.views.decorators.csrf import csrf_exempt

#to parse incoming data into data model
from rest_framework.parsers import JSONParser

from BudgetTracker.models import Transaction
from BudgetTracker.serializers import TransactionSerializer

# Create your views here.
@csrf_exempt
def transactionAPI(request,id=0):
    if request.method=='GET':
        transactions = Transaction.objects.all()
        transactions_serializer = TransactionSerializer(transactions, many=True)
        return JsonResponse(transactions_serializer.data, safe=False)
    elif request.method=='POST':
        transaction_data=JSONParser().parse(request)
        transaction_serializer = TransactionSerializer(data=transaction_data)
        if transaction_serializer.is_valid():
            transaction_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method=='PUT':
        transaction_data = JSONParser().parse(request)
        transaction=Transaction.objects.get(TransactionId=transaction_data['TransactionId'])
        transaction_serializer=TransactionSerializer(transaction, data=transaction_data)
        if transaction_serializer.is_valid():
            transaction_serializer.save()
            return JsonResponse('Updated successfully', safe=False)
        return JsonResponse("Failed to update.", safe=False)
    elif request.method=='DELETE':
        transaction=Transaction.objects.get(TransactionId=id)
        transaction.delete()
        return JsonResponse("Deleted successfully", safe=False)