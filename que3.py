from django.dispatch import Signal, receiver
from django.db import transaction
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)


my_signal = Signal()


@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver modifying the database...")
    MyModel.objects.create(name="Test")

with transaction.atomic():
    print("Creating a model instance...")
    MyModel.objects.create(name="Initial")
    print("Sending signal...")
    my_signal.send(sender=None)

print("Model instances after sending signal:")
print(MyModel.objects.all())
