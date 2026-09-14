class Patient:
    # FR-01: Create a patient record with a unique patient ID.
    def __init__(self, patient_id, name, contact_details):
        pass

    # FR-03: Update patient information.
    def update_details(self, name, contact_details):
        pass


class Practitioner:
    # FR-04: Store practitioner details and availability.
    def __init__(self, practitioner_id, name, availability):
        pass

    # FR-04: Update practitioner availability.
    def update_availability(self, availability):
        pass

    # FR-05 and FR-08: Check availability and prevent double bookings.
    def is_available(self, appointment_time):
        pass


class Appointment:
    # FR-06 and FR-10: Create an appointment and record its status.
    def __init__(
        self,
        appointment_id,
        patient,
        practitioner,
        appointment_time,
        status
    ):
        pass

    # FR-07 and FR-08: Validate information and prevent double bookings.
    def validate(self):
        pass

    # FR-06 and FR-08: Reschedule without creating a double booking.
    def reschedule(self, new_time):
        pass

    # FR-06, FR-10 and FR-11: Cancel and retain the appointment in history.
    def cancel(self):
        pass