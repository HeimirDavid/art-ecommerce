import random
import string

from .models import Order

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    the_id = "".join(random.choice(chars) for x in range(size))

    try:
        order = Order.objects.get(order_id=the_id)
        id_generator()
    except Order.DoesNotExist:
        return the_id
