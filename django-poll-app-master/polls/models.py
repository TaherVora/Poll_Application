from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)
    publisher = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"Question { self.question_text }"

    def was_published_recently(self):
        """
        Was published recently?
        :return:
        """
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'was published recently?'

class Choice(models.Model):
    choice_text = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"Choice { self.choice_text }"
