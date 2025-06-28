from django.urls import reverse

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .models import Image


class SimplestTest(TestCase):
    def test_addition(self):
        self.assertEqual(1+1, 2)

class ModelTest(TestCase):
    def test_post_creation(self):
        image = SimpleUploadedFile(
        name='test_image.jpg',
        content=b'\x47\x49\x46\x38\x89\x61',
        content_type='image/jpeg'
        )
        post = Image.objects.create(text='Hello WOrld', image=image)

        self.assertEqual(post.text, 'Hello WOrld' )

class ViewTest(TestCase):
    def test_the_homepage_status(self):
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

