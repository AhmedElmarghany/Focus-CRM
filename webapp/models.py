from django.db import models

# Category model
class Category(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Client model
class Record(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    phone = models.IntegerField()
    tall = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    address = models.CharField(max_length=500)
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name