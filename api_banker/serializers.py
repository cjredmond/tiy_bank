from rest_framework import serializers
from banker.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    def get_total():
        return 1

    class Meta:
        model = Transaction
        exclude = ('account',)
