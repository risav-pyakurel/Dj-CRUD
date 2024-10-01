from django.db import models
from apps.category.models import Category
from apps.tags.models import Tag


class News(models.Model):
    title = models.CharField(max_length= 250)
    description = models.CharField(max_length=300)
    is_active = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete= models.PROTECT)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
