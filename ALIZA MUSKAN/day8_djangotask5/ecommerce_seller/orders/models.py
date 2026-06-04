from django.db import models

from accounts.models import CustomUser

from products.models import Product


class Order(models.Model):
#  to see which user is odering
    user = models.ForeignKey(
        CustomUser,  on_delete=models.CASCADE
    )
# to see whuch product is odered
    product = models.ForeignKey( Product,  on_delete=models.CASCADE  )

    quantity = models.PositiveIntegerField(default=1)

    total_price = models.DecimalField(  max_digits=10,decimal_places=2 )

    ordered_at = models.DateTimeField(  auto_now_add=True  )

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"