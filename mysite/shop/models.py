from django.db import models


class Product(models.Model):
    name = models.CharField("название", max_length=50)
    price = models.IntegerField("цена")
    description = models.TextField("описание")
    photo = models.ImageField("фотография", upload_to="shop/photos", default="", blank=True)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товара"

    def __str__(self):
        return self.name
