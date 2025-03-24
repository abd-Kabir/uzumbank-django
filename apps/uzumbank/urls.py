from django.urls import path
from .views import CheckView, CreateView, ConfirmView, ReverseView, StatusView

app_name = 'uzumbank'
urlpatterns = [
    path('uzumbank/check/', CheckView.as_view(), name='uzumbank_check'),
    path('uzumbank/create/', CreateView.as_view(), name='uzumbank_create'),
    path('uzumbank/confirm/', ConfirmView.as_view(), name='uzumbank_confirm'),
    path('uzumbank/reverse/', ReverseView.as_view(), name='uzumbank_reverse'),
    path('uzumbank/status/', StatusView.as_view(), name='uzumbank_status'),
]
