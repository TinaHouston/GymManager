import pdb
from models.session import Session
from models.member import Member
from models.booking import Booking

import repositories.session_repository as session_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

member_repository.delete_all()
session_repository.delete_all()
booking_repository.delete_all()

member_1 = Member("Tina Houston", 26)
member_repository.save(member_1)

member_2 = Member("Sara Meil", 27)
member_repository.save(member_2)

member_3 = Member("Stuart Coull", 27)
member_repository.save(member_3)

member_4 = Member("Amanda Burns", 31)
member_repository.save(member_4)

session_1 = Session("Body Pump", True, "12:00pm", "31/01/21")
session_repository.save(session_1)

session_2 = Session("Yoga", False, "1:00pm", "31/01/21")
session_repository.save(session_2)

session_3 = Session("Pilates", True, "4:00pm", "05/02/21")
session_repository.save(session_3)

session_4 = Session("Spin", False, "3:00pm", "10/02/21")
session_repository.save(session_4)

booking_1 = Booking(member_1, session_2)
booking_repository.save(booking_1)

booking_2 = Booking(member_2, session_1)
booking_repository.save(booking_2)

booking_3 = Booking(member_4, session_3)
booking_repository.save(booking_3)

booking_4 = Booking(member_3, session_3)
booking_repository.save(booking_4)

pdb.set_trace()