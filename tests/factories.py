# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from factory import DjangoModelFactory, RelatedFactory, LazyAttribute
from catalogue.models import Product, ProductCategory, Category


class ProductCategoryFactory(DjangoModelFactory):
    FACTORY_FOR = ProductCategory

    category = LazyAttribute(lambda o: Category.objects.get(pk=1))


class ProductFactory(DjangoModelFactory):
    FACTORY_FOR = Product

    category = RelatedFactory(ProductCategoryFactory, 'product')
