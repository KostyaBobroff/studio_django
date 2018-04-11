from django.db import models
from django.utils import timezone


class Material(models.Model):
    name_material = models.CharField(max_length=50)
    price_for_1m = models.FloatField()
    footage = models.FloatField()

    def __str__(self):
        return self.name_material


class Model(models.Model):
    name_model = models.CharField(max_length=50)
    sewing_cost = models.FloatField()
    # sewing_time = models.DateTimeField(auto_now_add=True)
    sewing_time = models.TimeField()

    def __str__(self):
        return self.name_model


class Color(models.Model):
    name_color = models.CharField(max_length=50)

    def __str__(self):
        return self.name_color


class Catalog(models.Model):
    model = models.ForeignKey('Model', on_delete=models.CASCADE)
    material = models.ForeignKey('Material', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return '{} {} {}'.format(self.model.name_model,self.color.name_color,self.material.name_material)


class Order(models.Model):
    catalog = models.ForeignKey('Catalog', on_delete=models.CASCADE)
    price = models.FloatField()  # можно ли сделать, чтобы price сразу считался с учетом стоимости материала+стоимости пошития
    # +меркам человека
    # cutter
    order_date = models.DateTimeField(auto_now_add=True)
    date_of_completion = models.DateTimeField()# sewing_time + order_date = date_of_completion

