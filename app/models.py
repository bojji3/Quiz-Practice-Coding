from django.db import models 
from django.utils import timezone 
 
class Member(models.Model): 
    name = models.CharField(max_length=255) 
    description = models.TextField() 
    created_at = models.DateTimeField(default=timezone.now) 
 
    def __str__(self): 
        return self.name 
