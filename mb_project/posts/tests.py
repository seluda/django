from django.test import TestCase
from .models import Post
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='solo un texto')
    
    def test_text_content(self): 
        post = Post.objects.get(id=1)
        expected_object:name = f'{post.text}'
        self.assertEqual(expected_object_name, 'solo un texto')