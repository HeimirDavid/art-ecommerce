# Creating the random generated ID as an order reference.
# Source from this tutorial: https://www.youtube.com/watch?v=eU75ovbi8FE&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=38
import random
import string

from .models import Order

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    the_id = "".join(random.choice(chars) for x in range(size))

    # Try if the generated ID already exist, if so, generate one again
    try:
        order = Order.objects.get(order_id=the_id)
        id_generator()
    except Order.DoesNotExist:
        return the_id
