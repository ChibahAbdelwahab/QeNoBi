from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    sex = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    location = models.CharField(max_length=10)

    def __str__(self):
        return f'User-{self.user_id}'


class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.description


class Group(models.Model):
    group_id = models.IntegerField(primary_key=True)
    users = models.ManyToManyField(User)
    items = models.ManyToManyField(Item)  # [1,2,2,]
    period = models.DateField(max_length=30, )
    depth = models.IntegerField()
    support = models.IntegerField()

    def __str__(self):
        return self.group_id


class Link(models.Model):
    group_source = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='sources')
    group_target = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='targets')
    user = models.CharField(max_length=30, default="test")

    def __str__(self):
        return f'{self.group_source.group_id}-{self.group_target.group_id}'


class Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    date = models.DateTimeField()


class MiningGroupsExperiment(models.Model):
    # TODO  add model constraints min < max
    # TODO Define possible values for demographics
    frequency = models.CharField(max_length=5, default="1D")
    demographics = models.CharField(max_length=100, default="['sex']")
    support = models.IntegerField()
    min_items = models.PositiveIntegerField()
    max_items = models.PositiveIntegerField()


class SankeyExperiment(models.Model):
    dataset = models.CharField(max_length=100)
    date_min = models.DateField(max_length=100)
    date_max = models.DateField(max_length=100)
    demographics = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    time_granularity = models.CharField(max_length=100)
    support = models.IntegerField()
    products_min = models.IntegerField()
    max_products = models.IntegerField()


class TimeGranularity(models.Model):
    value = models.CharField(max_length=10)
    name = models.CharField(max_length=10)


class DataSetDescription(models.Model):
    name = models.CharField(max_length=100)
    customers_properties = models.ManyToManyField("Property", related_name="dataset_customers", blank=True)
    items_properties = models.ManyToManyField("Property", related_name="dataset_items", blank=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}({self.value})"
