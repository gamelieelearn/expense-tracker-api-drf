from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ExpenseDetail, ExpenseList

urlpatterns = [
    path('expenses/', ExpenseList.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseDetail.as_view(), name='expense-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
