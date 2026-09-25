from datetime import datetime

from Part_B_Patient import Patient
from Part_C_Practitioner import Practitioner
from Part_G_Code import Appointment
from Part_G_Code import AppointmentStatusError


patient = Patient(
    "P001",
    "Alex Smith",
    "0400 000 000"
)

practitioner = Practitioner(
    "PR001",
    "Dr Lee",
    "General Practice"
)

appointment = Appointment(
    "A001",
    patient,
    practitioner,
    datetime(2026, 9, 25, 10, 0)
)

print("Starting status:", appointment.get_status().value)

appointment.reschedule(datetime(2026, 9, 25, 11, 0))
print("New appointment time:", appointment.get_appointment_time())

appointment.cancel()
print("Status after cancellation:", appointment.get_status().value)

try:
    appointment.cancel()
except AppointmentStatusError as error:
    print("Error:", error)

try:
    invalid_appointment = Appointment(
        "",
        patient,
        practitioner,
        datetime(2026, 9, 25, 12, 0)
    )
except ValueError as error:
    print("Error:", error)