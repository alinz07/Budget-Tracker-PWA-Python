from django.urls import re_path
from BudgetTracker import views

urlpatterns=[
    re_path(r'^transactions/$', views.transactionAPI),
    re_path(r'^transactions/([0-9]+)$', views.transactionAPI)
]