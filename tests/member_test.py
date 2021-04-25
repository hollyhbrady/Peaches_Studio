import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member('Ginny', 'Deluxe')