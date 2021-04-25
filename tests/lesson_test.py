import unittest
from models.lesson import Lesson

class TestLesson(unittest.TestCase):

    def setUp(self):
        self.lesson = Lesson('Sun Salutations', 10, 'Beginner', 'Monday', 800, 60)