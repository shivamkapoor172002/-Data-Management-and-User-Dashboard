from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    field = models.IntegerField(null=True, blank=True)
    is_leave = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, null=True)


class SimplifiedData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    excel_total = models.IntegerField(default=0)
    working_days = models.IntegerField(default=0)
    target = models.IntegerField(default=0)  # Add this line if it's not already there
    period = models.DateField(default=timezone.now)
    month = models.CharField(max_length=20, default='Unknown')

    def __str__(self):
        return f"{self.user.username} - {self.period} - Excel Total: {self.excel_total}, Working Days: {self.working_days}"
    
class UserTarget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    target = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Target: {self.target}"