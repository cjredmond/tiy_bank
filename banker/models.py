from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Account(models.Model):
    user = models.OneToOneField('auth.User')

    def __str__(self):
        return str(self.user.username)

@receiver(post_save, sender=User)
def create(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        Account.objects.create(user=instance)


TRANSACTION_TYPE = [('+', 'deposit'), ('-', 'withdrawal')]
class Transaction(models.Model):
    trans_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE, null=True)
    account = models.ForeignKey(Account)
    amount = models.FloatField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account.user.username) + str(self.trans_type) + str(self.amount)
