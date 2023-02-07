from django.test import TestCase
from .models import Post


class TestModel(TestCase):
    def setUp(self):
        self.blog = Post.objects.create(title='django',
                                        author='ali', slug='test')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), d.title)

    def test_new(self):
        assert 1 == 1