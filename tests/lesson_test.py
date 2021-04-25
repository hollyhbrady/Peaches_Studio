import unittest
from models.lesson import Lesson

class TestLesson(unittest.TestCase):

    def setUp(self):
        self.lesson = Lesson('Sun Salutations', 10, 'Beginner', 'Monday', 800, 60)

    def test_lesson_has_name(self):
        self.assertEqual('Sun Salutations', self.lesson.name)

    def test_lesson_has_capacity(self):
        self.assertEqual(10, self.lesson.capacity)