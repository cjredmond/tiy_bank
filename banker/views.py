from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from banker.models import Transaction, Account
from django.core.urlresolvers import reverse, reverse_lazy

def balance(user):
    trans = Transaction.objects.filter(account = user.account.id)
    start = 0
    for x in trans:
        if x.trans_type == "+":
            start = start + x.amount
        else:
            start = start - x.amount
    return start



class index_view(TemplateView):
    model = Transaction
    template_name = "index.html"

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class ProfileView(ListView):
    model = Transaction
    template_name = "profile.html"
    def get_context_data(self):
        context = super().get_context_data()
        trans = Transaction.objects.filter(account = self.request.user.account.id)
        start = 0
        for x in trans:
            if x.trans_type == "+":
                start = start + x.amount
            else:
                if start - x.amount < 0:
                    pass
                else:
                    start = start - x.amount
        x = balance(self.request.user)
        context['balance'] = start
        context['trans'] = trans
        return context

class TransactionCreateView(CreateView):
    model = Transaction
    def get_success_url(self):
        return reverse('profile_view')
    fields = ('amount', 'trans_type')
    def form_valid(self, form):
        bal = balance(self.request.user)
        instance = form.save(commit=False)
        instance.account = self.request.user.account
        if instance.trans_type == "-":
            if bal - instance.amount < 0:
                return super().form_invalid(form)
        return super().form_valid(form)

class TransferCreateView(CreateView):
    model = Transaction
    fields = ('amount',)
    
    def get_success_url(self):
        return reverse('profile_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.trans_type = "+"
        x = target
        instance.account = Accounts.objects.get(id=x)
        Transaction.objects.create(trans_type='-', amount=instance.amount, account=self.request.user.account)
        return super().form_valid(form)
