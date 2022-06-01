#serializers help us convert complex model types to native
#python data types that can be rendered into json/xml.
#also helps converting back to complex types

from rest_framework import serializers
from BudgetTracker.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('TransactionId',
                  'TransactionName',
                  'TransactionValue',
                  'TransactionDate')