from django.db import models

# Create your models here.
class EmployeePerformance(models.Model):
    employee_name = models.CharField(max_length=100)
    performance_score = models.DecimalField(max_digits=5,decimal_places=2)