from django.db import models

# Create your models here.
class Elder(models.Model):
    """A model representing an elder."""
    # Personal information
    name = models.CharField(max_length=100)
    personal_id = models.CharField(max_length=13)
    apartment = models.CharField(max_length=100)
    head_caretaker = models.CharField(max_length=100, verbose_name='Head Caretaker') #ForeignKey USER

    # Condition
    physical_con = models.TextField(verbose_name='Physical condition')
    mental_con = models.TextField(verbose_name='Mental condition')
    weight = models.FloatField()
    length = models.FloatField()
    
    mood = models.CharField(max_length=200)
    social_activity = models.CharField(max_length=200)

    # Foods
    coffee = models.CharField(max_length=200)
    breakfast = models.CharField(max_length=200)
    eating_needs = models.TextField()

    def __str__(self):
        """Return a string representation of the model"""
        return self.name.title()


class Log(models.Model):
    """Represents a documentation log."""
    elder = models.ForeignKey(Elder, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    author = models.CharField(max_length=100) #ForeignKey USER

    def __str__(self):
        return self.text