import unittest
from models.lesson import Lesson

class TestLesson(unittest.TestCase):

    def setUp(self):
        self.lesson = Lesson('Sun Salutations', 10, 'Beginner', 'Monday', "08:00", 60)

    def test_lesson_has_name(self):
        self.assertEqual('Sun Salutations', self.lesson.name)

    def test_lesson_has_capacity(self):
        self.assertEqual(10, self.lesson.capacity)

    def test_lesson_has_category(self):
        self.assertEqual('Beginner', self.lesson.category)

    def test_lesson_has_day(self):
        self.assertEqual('Monday', self.lesson.day)

    def test_lesson_has_time(self):
        self.assertEqual("08:00", self.lesson.time)

    def test_lesson_has_duration(self):
        self.assertEqual(60, self.lesson.duration)