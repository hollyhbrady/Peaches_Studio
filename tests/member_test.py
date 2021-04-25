import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member('Ginny', 'Deluxe')

    def test_member_has_name(self):
        self.assertEqual('Ginny', self.member.name)

    def test_member_has_membership(self):
        self.assertEqual('Deluxe', self.member.membership)