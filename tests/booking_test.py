import unittest
from models.booking import Booking

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.member = Member('Ginny', 'Deluxe')
        self.lesson = Lesson('Sun Salutations', 10, 'Beginner', 'Monday', 800, 60)
        self.booking = Booking(member, lesson)

    