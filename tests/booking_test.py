import unittest
from models.booking import Booking
from models.member import Member
from models.lesson import Lesson

class TestBooking(unittest.TestCase):

    def setUp(self):
        self.member = Member('Ginny', 'Deluxe')
        self.lesson = Lesson('Sun Salutations', 10, 'Beginner', 'Monday', 800, 60)
        self.booking = Booking(self.member, self.lesson)

    def test_booking_has_member(self):
        self.assertEqual('Ginny', self.member.name)

    def test_booking_has_lesson(self):
        self.assertEqual('Sun Salutations', self.lesson.name)

    