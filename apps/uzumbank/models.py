from django.db import models

from config.models import BaseModel


class TransactionEnum(models.TextChoices):
    CREATED = 'CREATED', 'Created'
    CONFIRMED = 'CONFIRMED', 'Confirmed'
    REVERSED = 'REVERSED', 'Reversed'
    FAILED = 'FAILED', 'Failed'


class UzumbankTransaction(BaseModel):
    service_id = models.BigIntegerField()
    trans_id = models.UUIDField(unique=True)
    timestamp = models.BigIntegerField()
    amount = models.BigIntegerField()
    status = models.CharField(max_length=20, choices=TransactionEnum.choices)  # noqa: cuz noqa
    trans_time = models.BigIntegerField(null=True, blank=True)
    confirm_time = models.BigIntegerField(null=True, blank=True)
    reverse_time = models.BigIntegerField(null=True, blank=True)
    data = models.JSONField(default=dict)

    def __str__(self):
        return f"Transaction {self.trans_id} ({self.status})"

    class Meta:
        db_table = 'uzumbank_transaction'
