from rest_framework import serializers
from banker.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    def get_total(self, obj):
        queryset = Transaction.objects.filter(account=obj.account)
        total = 0
        for x in queryset:
            if x.time > obj.time:
                pass
            else:
                if x.trans_type == "+":
                    total = total + x.amount
                else:
                    total = total - x.amount
        return total


    class Meta:
        model = Transaction
        exclude = ('account',)
