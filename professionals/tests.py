from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Professionals

class ProfessionalsModelTest(TestCase):

    def setUp(self):
        self.professional1 = Professionals.objects.create(
            fullname="John Doe",
            profession="Dentist",
            address="123 Main St",
            contact="123-456-7890",
            socialname="JD"
        )
        self.professional2 = Professionals.objects.create(
            fullname="Jane Smith",
            profession="Therapist",
            address="456 Elm St",
            contact="987-654-3210",
            socialname="JS"
        )
        self.professional_detail_url = reverse('professional-detail', kwargs={'professional_id': self.professional1.id})
        self.professional_list_url = reverse('professional-list')  # Adicione esta linha

    def test_professional_creation(self):
        data = {
            "fullname": "John Updated",
            "profession": "Dentist",
            "address": "123 Main St",
            "contact": "123-456-7890",
            "socialname": "JD"
        }
        response = self.client.post(reverse('professional-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_professional_update(self):
        data = {
            "fullname": "John Updated",
            "profession": "Dentist",
            "address": "123 Main St",
            "contact": "123-456-7890",
            "socialname": "JD"
        }
        response = self.client.put(self.professional_detail_url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.professional1.refresh_from_db()
        self.assertEqual(self.professional1.fullname, "John Updated")

    def test_professional_delete(self):
        response = self.client.delete(self.professional_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Professionals.objects.filter(id=self.professional1.id).exists())

    def test_professional_list(self):
        response = self.client.get(self.professional_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['fullname'], "John Doe" )
        self.assertEqual(response.data[1]['fullname'], "Jane Smith")

     