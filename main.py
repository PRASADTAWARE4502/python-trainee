import django
from django.dispatch import Signal, receiver
from django.db import models
import time

django.setup()

my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver started")
    time.sleep(2)  
    print("Receiver finished")


print("Sending signal...")
my_signal.send(sender=None)
print("Signal sent!")


class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

rect = Rectangle(5, 10)
for dimension in rect:
    print(dimension)
