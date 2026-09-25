from datetime import datetime
from enum import Enum

from Part_B_Patient import Patient
from Part_C_Practitioner import Practitioner


class AppointmentStatus(Enum):
    SCHEDULED = "SCHEDULED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class AppointmentStatusError(Exception):
    pass


class Appointment:
    def __init__(
        self,
        appointment_id,
        patient,
        practitioner,
        appointment_time
    ):
        self.__appointment_id = appointment_id
        self.__patient = patient
        self.__practitioner = practitioner
        self.__appointment_time = appointment_time
        self.__status = AppointmentStatus.SCHEDULED

        self.validate()

    def validate(self):
        if self.__appointment_id == "":
            raise ValueError("Appointment ID cannot be empty.")

        if not isinstance(self.__patient, Patient):
            raise ValueError("A valid patient is required.")

        if not isinstance(self.__practitioner, Practitioner):
            raise ValueError("A valid practitioner is required.")

        if not isinstance(self.__appointment_time, datetime):
            raise ValueError("Appointment time must be a datetime.")

    def get_status(self):
        return self.__status

    def get_appointment_time(self):
        return self.__appointment_time

    def reschedule(self, new_time):
        if self.__status != AppointmentStatus.SCHEDULED:
            raise AppointmentStatusError(
                "A cancelled appointment cannot be rescheduled."
            )

        if not isinstance(new_time, datetime):
            raise ValueError("The new time must be a datetime.")

        self.__appointment_time = new_time

    def cancel(self):
        if self.__status != AppointmentStatus.SCHEDULED:
            raise AppointmentStatusError(
                "The appointment has already been cancelled."
            )

        self.__status = AppointmentStatus.CANCELLED