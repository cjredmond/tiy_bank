from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api_banker.serializers import TransactionSerializer
from banker.models import Account, Transaction
from api_banker.permissions import BelongsTo
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication



class TransactionListCreateAPIView(ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(account = user.account.id)
    serializer_class = TransactionSerializer
    def perform_create(self, serializer):
        serializer.save(account=self.request.user.account)
        return super().perform_create(serializer)

class TransactionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (BelongsTo,)
