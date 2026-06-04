from django.db import models

# Create your models here.
from accounts.models import CustomUser

from products.models import Product


class Cart(models.Model):

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    added_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user.username} - {self.product.name}"