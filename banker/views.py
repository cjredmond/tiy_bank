from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from banker.models import Transaction, Account


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
                start = start - x.amount
        # for x in y:
        #     start = start + x.amount
        context['balance'] = start
        context['trans'] = trans
        return context

class TransactionCreateView(CreateView):
    model = Transaction
    success_url = "/"
    fields = ('amount', 'trans_type' )
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.account = self.request.user.account
        return super().form_valid(form)

# Create your views here.
