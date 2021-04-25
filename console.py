import pdb

from models.lesson import Lesson
from models.member import Member
from models.booking import Booking

import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
lesson_repository.delete_all()
member_repository.delete_all()

member1 = Member('Ginny', 'Deluxe')
member_repository.save(member1)

member2 = Member('Max', 'Deluxe')
member_repository.save(member2)

member3 = Member('Abby', 'Standard')
member_repository.save(member3)

member4 = Member('Nadine', 'Standard')
member_repository.save(member4)

pdb.set_trace()