from datetime import datetime


class Practitioner:
    def __init__(
        self,
        practitioner_id: str,
        name: str,
        specialty: str,
        availability: list[datetime]
    ) -> None:
        if not practitioner_id.strip():
            raise ValueError("Practitioner ID is required.")

        if not name.strip():
            raise ValueError("Practitioner name is required.")

        if not specialty.strip():
            raise ValueError("Specialty is required.")

        self._practitioner_id = practitioner_id.strip()
        self._name = name.strip()
        self._specialty = specialty.strip()
        self._availability = list(availability)

    def update_availability(
        self,
        availability: list[datetime]
    ) -> None:
        self._availability = list(availability)

    def is_available(self, appointment_time: datetime) -> bool:
        return appointment_time in self._availability