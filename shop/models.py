from django.db import models
from django.dispatch import receiver
from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from installment.models import *
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="categories/", default="")

    class Meta:
        verbose_name_plural = _("categories")
        verbose_name = _("categories")

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="subCategories/", default="")
    parent = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name="Category",
    )

    class Meta:
        verbose_name_plural = _("subCategories")
        verbose_name = _("subCategories")

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name="vendor email address",
        max_length=255,
        unique=True,
    )
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _("Vendor")
        verbose_name = _("Vendor")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Product Name"))
    slug = models.SlugField(unique=True)
    description = models.TextField()
    plans = models.ManyToManyField(InstallMentsPlans)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        verbose_name="Sub Category",
        related_name="products",
    )
    image = models.ImageField(upload_to="products/")
    seller = models.ForeignKey(Vendor, on_delete=models.CASCADE, verbose_name="Vendor")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    favorits = models.ManyToManyField(User)

    class Meta:
        verbose_name_plural = _("products")

    def __str__(self):
        return self.name


class Order(models.Model):
    PENDING_STATE = "p"
    COMPLETED_STATE = "c"


    ORDER_CHOICES = ((PENDING_STATE, "pending"), (COMPLETED_STATE, "completed"))
    status = models.CharField(
        max_length=1, choices=ORDER_CHOICES, default=PENDING_STATE
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        related_name="product_order",
        on_delete=models.CASCADE,
        verbose_name="Product Name",
    )
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order Item #{self.product.name}"

    @property
    def total(self):
        return self.quantity * self.product.price


STATUS_CHOICES = [
    ("a", "Accepted"),
    ("r", "Refused"),
    ("p", "Pending"),
    ("c", "Cancled"),
]


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    plan = models.ForeignKey(
        InstallMentsPlans, on_delete=models.CASCADE, verbose_name=_("Plan")
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("Product")
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="")
    deposit = models.CharField(max_length=55 , default='', blank=True)
    id_image_front = models.ImageField(upload_to="requests/frontId/" , default='')
    id_image_back = models.ImageField(upload_to="requests/backId/", default='')
    another_files = models.ImageField(upload_to="requests/anotherFiles", default='')

    def __str__(self):
        return f"Installment Request from #{self.user.pk}"




class IntrestedCategory(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("User"), default=""
    )
    category = models.ManyToManyField(
        Category,
        verbose_name=_("Category"),
    )

    class Meta:
        verbose_name_plural = _("IntrestedCategory")
        verbose_name = _("IntrestedCategory")

    def __str__(self):
        return self.user.email


class UserFavoriets(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("User")
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("Product")
    )

    class Meta:
        verbose_name_plural = _("UserFavoriets")
        verbose_name = _("UserFavoriets")

    def __str__(self):
        return self.user.email
