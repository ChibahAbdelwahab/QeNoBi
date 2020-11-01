from django.db import models


# Create your models here.


class Group(models.Model):
    user = models.CharField(max_length=30, default="test")  # [1,2,3,4]
    item = models.CharField(max_length=40, default="test")  # [1,2,2,]
    period = models.DateField(max_length=30, default="test")
    depth = models.CharField(max_length=30, default="test")
    support = models.CharField(max_length=30, default="test")


class Link(models.Model):
    group_source = models.CharField(max_length=30, default="test")  # == 1
    group_target = models.CharField(max_length=30, default="test")
    user = models.CharField(max_length=30, default="test")


class MiningGroupsExperiment(models.Model):
    # TODO  add model constraints min < max
    # TODO Define possible values for demographics
    frequency = models.CharField(max_length=5, default="1D")
    demographics = models.CharField(max_length=100, default="['sex']")
    support = models.IntegerField()
    min_items = models.PositiveIntegerField()
    max_items = models.PositiveIntegerField()

    #
    # class Meta:
    #     db_constraints = {
    #         'items_size_check': 'check (min_items > max_items)',
    #     }
