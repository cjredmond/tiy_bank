from django.conf.urls import url, include
from django.contrib import admin
from banker.views import index_view, UserCreateView, ProfileView, TransactionCreateView, \
                         TransferCreateView
from api_banker.views import TransactionRetrieveAPIView, TransactionListCreateAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view.as_view(), name='index_view'),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/$', ProfileView.as_view(), name="profile_view"),
    url(r'^transaction/create/$', TransactionCreateView.as_view(), name="transaction_create_view"),
    url(r'^transfer/create/$', TransferCreateView.as_view(), name="transfer_create_view"),
    url(r'^api/transactions/$', TransactionListCreateAPIView.as_view(), name="transaction_list_create_api_view"),
    url(r'^api/transactions/(?P<pk>\d+)/$', TransactionRetrieveAPIView.as_view(), name="transaction_retrieve_api_view"),

]
