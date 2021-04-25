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

lesson1 = Lesson('Sun Salutations', 10, 'Beginner', 'Monday', "08:00", 60)
lesson_repository.save(lesson1)

lesson2 = Lesson('Yoga for Flexibility', 5, 'Beginner', 'Wednesday', "17:00", 45)
lesson_repository.save(lesson2)

booking1 = Booking(member1, lesson1)
booking_repository.save(booking1)

booking2 = Booking(member2, lesson2)
booking_repository.save(booking2)

booking3 = Booking(member3, lesson2)
booking_repository.save(booking3)

booking4 = Booking(member4, lesson1)
booking_repository.save(booking4)


pdb.set_trace()