from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class BookItem(models.Model):
    book = models.OneToOneField("books.Book", on_delete=models.CASCADE, related_name="store_item")
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def in_stock(self):
        return self.quantity > 0

    def __str__(self):
        return self.book.title

    def __repr__(self):
        return f"<BookItem book_id={self.book_id} price={self.price} quantity={self.quantity}>"


class CartStatus(models.TextChoices):
    NEW = "new", "New"
    PENDING = "pending", "Pending"
    COMPLETED = "completed", "Completed"
    FAILED = "failed", "Failed"


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shopping_carts")
    books = models.ManyToManyField("books.Book", related_name="purchases")
    status = models.CharField(max_length=12, choices=CartStatus.choices, default=CartStatus.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "shopping cart"
        verbose_name_plural = "shopping carts"

    def __str__(self):
        return f"Shopping cart for {self.user}"

    def __repr__(self):
        return f"<ShoppingCart id={self.pk} user_id={self.user_id} status={self.status} created_at={self.created_at}>"

    @property
    def total(self):
        return round(self.books.aggregate(total=models.Sum("store_item__price"))["total"], 2)

    @property
    def items_count(self):
        return self.books.count()

    def get_absolute_url(self):
        return reverse("store:detail", kwargs={"pk": self.pk})
