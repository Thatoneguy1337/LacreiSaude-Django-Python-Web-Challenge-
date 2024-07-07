from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from professionals.models import Professionals
from .models import Schedules

class SchedulesModelTest(APITestCase):

    def setUp(self):
        self.professional = Professionals.objects.create(
            fullname="John Doe",
            profession="Dentist",
            address="123 Main St",
            contact="123-456-7890",
            socialname="JD"
        )
        self.schedule = Schedules.objects.create(
            professional=self.professional,
            appointment_date="2024-07-10T10:00:00Z"
        )
        self.schedule_detail_url = reverse('schedule-detail', kwargs={'schedule_id': self.schedule.id})
        self.schedule_list_url = reverse('schedule-list')

    def test_schedule_creation(self):
        data = {
            "professional": self.professional.id,
            "appointment_date": "2024-07-15T10:00:00Z"
        }
        response = self.client.post(reverse('schedule-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_schedule_delete(self):
        response = self.client.delete(self.schedule_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Schedules.objects.filter(id=self.schedule.id).exists())

    def test_schedule_list(self):
        response = self.client.get(self.schedule_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['appointment_date'], "2024-07-10T10:00:00Z")
