from django.urls import path
from .views import CheckView, CreateView, ConfirmView, ReverseView, StatusView

app_name = 'uzumbank'
urlpatterns = [
    path('check/', CheckView.as_view(), name='uzumbank_check'),
    path('create/', CreateView.as_view(), name='uzumbank_create'),
    path('confirm/', ConfirmView.as_view(), name='uzumbank_confirm'),
    path('reverse/', ReverseView.as_view(), name='uzumbank_reverse'),
    path('status/', StatusView.as_view(), name='uzumbank_status'),
]
