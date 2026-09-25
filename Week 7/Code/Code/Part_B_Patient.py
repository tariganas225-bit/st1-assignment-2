class Patient:
    def __init__(
        self,
        patient_id: str,
        name: str,
        contact_details: str
    ) -> None:
        if not patient_id.strip():
            raise ValueError("Patient ID is required.")

        if not name.strip():
            raise ValueError("Patient name is required.")

        if not contact_details.strip():
            raise ValueError("Contact details are required.")

        self._patient_id = patient_id.strip()
        self._name = name.strip()
        self._contact_details = contact_details.strip()

    def update_details(
        self,
        name: str,
        contact_details: str
    ) -> None:
        if not name.strip():
            raise ValueError("Patient name is required.")

        if not contact_details.strip():
            raise ValueError("Contact details are required.")

        self._name = name.strip()
        self._contact_details = contact_details.strip()