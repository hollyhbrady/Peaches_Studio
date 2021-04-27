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

lesson1 = Lesson('Sun Salutations', 10, 'Intermediate', 'Monday', "08:00", 60)
lesson_repository.save(lesson1)
lesson2 = Lesson('Sun Salutations', 10, 'Intermediate', 'Wednesday', "08:00", 60)
lesson_repository.save(lesson2)
lesson3 = Lesson('Sun Salutations', 10, 'Intermediate', 'Friday', "08:00", 60)
lesson_repository.save(lesson3)

lesson4 = Lesson('Yoga for Flexibility', 20, 'Beginner', 'Tuesday', "17:00", 45)
lesson_repository.save(lesson4)
lesson5 = Lesson('Yoga for Flexibility', 20, 'Beginner', 'Thursday', "17:00", 45)
lesson_repository.save(lesson5)

lesson6 = Lesson('Yoga for Geriatrics', 5, 'Beginner', 'Wednesday', "11:00", 90)
lesson_repository.save(lesson6)
lesson7 = Lesson('Yoga for Geriatrics', 5, 'Beginner', 'Saturday', "11:00", 90)
lesson_repository.save(lesson7)

lesson8 = Lesson('Prenatal Yoga', 5, 'Beginner', 'Tuesday', "10:00", 60)
lesson_repository.save(lesson8)
lesson9 = Lesson('Prenatal Yoga', 5, 'Beginner', 'Friday', "10:00", 60)
lesson_repository.save(lesson9)

lesson10 = Lesson('Airbending', 10, 'Advanced', 'Monday', "18:00", 120)
lesson_repository.save(lesson10)
lesson11 = Lesson('Ninja Skills', 10, 'Advanced', 'Thursday', "18:00", 120)
lesson_repository.save(lesson11)
lesson12 = Lesson('How to kill your Spouse', 10, 'Advanced', 'Saturday', "14:00", 60)
lesson_repository.save(lesson12)

member1 = Member('Ginny Miller', 'Deluxe')
member_repository.save(member1)

member2 = Member('Maxine Baker', 'Deluxe')
member_repository.save(member2)

member3 = Member('Abby Mang', 'Standard')
member_repository.save(member3)

member4 = Member('Nadine Mang', 'Standard')
member_repository.save(member4)

member5 = Member('Georgia Miller', 'Deluxe')
member_repository.save(member5)

member6 = Member('Hunter Chen', 'Standard')
member_repository.save(member6)

member7 = Member('Marcus Baker', 'Deluxe')
member_repository.save(member7)

member8 = Member('Ellen Baker', 'Deluxe')
member_repository.save(member8)

member9 = Member('Paul Randolph', 'Standard')
member_repository.save(member9)

member10 = Member('Zion Miller', 'Deluxe')
member_repository.save(member10)

member11 = Member('Sophie Sanchez', 'Standard')
member_repository.save(member11)

member12 = Member('Cynthia Fuller', 'Deluxe')
member_repository.save(member12)

member13 = Member('Ellen Baker', 'Deluxe')
member_repository.save(member13)

member14 = Member('Joe Danes', 'Standard')
member_repository.save(member14)

member15 = Member('Nick Bierne', 'Standard')
member_repository.save(member15)


booking1 = Booking(member1, lesson1)
booking_repository.save(booking1)

booking2 = Booking(member2, lesson2)
booking_repository.save(booking2)

booking3 = Booking(member3, lesson2)
booking_repository.save(booking3)

booking4 = Booking(member4, lesson1)
booking_repository.save(booking4)

