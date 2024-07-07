from django.db import models
from professionals.models import Professionals

class Schedules(models.Model):
    professional = models.ForeignKey(Professionals, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["appointment_date"]
        unique_together = ["professional", "appointment_date"]

    def __str__(self):
        return f"{self.professional.fullname} - {self.appointment_date}"



