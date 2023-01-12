from django.db import models
from django.contrib.auth import get_user, get_user_model
from django.urls import reverse_lazy

# class Category(models.Model):
#     name = models.CharField(
#         max_length=255,
#         blank=False,
#         null=False,
#         unique=True)
    
#     def __str__(self):
#         return self.name
    
# class Tag(models.Model):
#     name = models.CharField(
#         max_length=255,
#         blank=False,
#         null=False,
#         unique=True)
    
#     def __str__(self):
#         return self.name

User = get_user_model()

class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False)
    
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False)
        
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False)
        
    body = models.TextField(
        blank=True,
        null=False)
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE)

    # author = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    # )
    # category = models.ForeignKey(
    #     Category,
    #     on_delete=models.CASCADE)

    # tags = models.ManyToManyField(
    #     Tag,
    #     blank=True)
    
    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])

    def __str__(self):
        return self.title