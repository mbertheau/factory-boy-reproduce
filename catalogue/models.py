# -*- coding: utf-8 -*-

from django.db import models


class Category(models.Model):
    full_name = models.CharField('Full Name', max_length=255,
                                 db_index=True, editable=False)

    def __unicode__(self):
        return self.full_name


class ProductCategory(models.Model):
    product = models.ForeignKey('Product')
    category = models.ForeignKey(Category)


class Product(models.Model):
    categories = models.ManyToManyField(Category, through=ProductCategory)
