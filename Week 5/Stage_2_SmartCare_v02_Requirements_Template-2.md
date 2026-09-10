# SmartCare v0.2 - Requirements Specification Template 

## **1. Problem and Scope** 

SmartCare currently uses spreadsheets and paper records to manage patients and appointments. This causes duplicate bookings, difficulty finding patient information, inconsistent appointment statuses, limited visibility of practitioner availability and unreliable appointment history. SmartCare V.02 will provide a small, maintainable system for managing patients, practitioners and appointments. 

### In scope 

- Creating, searching and updating patient records 

- Creating and viewing practitioner records 

- Recording practitioner availability 

- Creating, rescheduling and cancelling appointments 

- Preventing practitioner double-bookings 

- Using consistent appointment statuses 

- Retaining appointment history 

### Out of scope 

- Billing and online payments 

- Health insurance claims 

- AI treatment recommendations 

- Facial recognition 

- Complex hospital functions 

- Integration with external healthcare systems 

### Provisional 

- SMS or email reminders 

- Patient online self-booking 

- Web interface 

- Multiple simultaneous users 

- User login and detailed access permissions 

## **2. Stakeholders** 

|Stakeholder|Need|Evidence|
|---|---|---|
|Patients|Accurate records, reliable|Patients were identifed as|
||appointments and privacy<br>protection|stakeholders in Stage 1, and the case<br>describes problems with patient<br>records and appointments.|



|Reception staf|to create, fnd, update and<br>cancel appointments<br>eficiently|The Stage 1 prototype states that a<br>receptionist records patient<br>appointments|
|---|---|---|
|Practitioners|to assess their availability and<br>appointment schedules|Practitioner management and limited<br>availability visibility are identifed in<br>the case study.|
|Clinic management|reliable records and basic<br>operational reports|Management requested the system,<br>and the case identifes dificulty<br>producing reports.|
|Software developer|clear, testable requirements<br>and manageable scope|The case study requires a junior<br>software engineer to develop the<br>system iteratively.|



## **3. Functional Requirements** 

FR-01: The system will allow staff to create a patient record with a unique patient ID for each patient 

FR-02: The system will allow staff to search for a patient by patient ID 

FR-03: The system will allow staff to view and update patient information 

FR-04: The system will store practitioner details and availability 

FR-05: The system will display practitioner availability and and appointment scheduling 

FR-06: The system will allow reception staff to create, reschedule and cancel appointments 

FR-07: The system will reject information like appointments if required information is missing 

FR-08: The system will prevent a practitioner from being double booked twice 

FR-09: The system will display each practitioner’s appointment schedule. 

FR-10: The system will record when an appointment has been completed, booked or cancelled 

FR-11: If an appointment gets cancelled the appointment will still remain in the systems database history 

FR-12: The system will create basic reports showing appointments by date, practitioner and status 

## **4. Non-Functional Requirements** 

NFR-01: Security - Only authorised clinic staff should access patient information 

NFR-02: Performance - Patient results should return results pretty quickly and should not take too long 

NFR-03: Usability - The system will display clear labels, instructions and error messages. 

NFR-04: Reliability - Saved information will remain available after the application is closed and restarted 

NFR-05: Data integrity - Invalid input should not damage or remove existing records 

NFR-06: Testability - Important functions, such as booking and cancellation, should be testable separately 

## **5. User Stories** 

US-01: As a receptionist I want to be able to register a patient so that their information can be used for appointments. 

US-02: As a receptionist I want to search for a patient by ID so that I can quickly locate the correct record. 

US-03:As a practitioner I want to view my schedule so that I know which patients I will see. 

US-04: As a clinic manager I want to view appointment reports so that I can monitor clinic operations. 

US-05: As a receptionist I want to view appointments so that I can go back to the canceled appointments history and reschedule an old patient. 

US-06: As a receptionist I want to cancel or reschedule an appointment so that changes are accurately recorded. 6. Acceptance Criteria 

GIVEN an existing patient, practitioner and available time 

WHEN the receptionist enters valid appointment information 

THEN the system creates the appointment with a Booked status. 

GIVEN a patient record exists 

WHEN the receptionist searches using the patient’s ID 

THEN the system displays the matching patient record. 

GIVEN a practitioner already has an appointment at a particular time 

WHEN the receptionist attempts to book another appointment for the same practitioner and time THEN the system rejects the booking and displays an explanation. 

## **7. Assumptions and Open Questions** 

### Assumptions 

- Reception staff will be the main users responsible for entering and updating information. 

- Each patient and practitioner will have a unique ID. 

- Appointment statuses will include Booked, Completed and Cancelled. 

- The first version will support one small community clinic. 

### Open questions 

- What information must be stored for each patient and practitioner? 

- Who may create, update, reschedule and cancel appointments? 

- What appointment duration and date-and-time format should be used? 

- How long must completed and cancelled appointments remain in the history? 

- What specific reports does clinic management require? 

- What security, authentication and backup controls are required? 

- How many patients, practitioners and appointments must the system support? 

- Are reminders, online self-booking or multiple simultaneous users required? 

## **8. AI Requirements Review Record** 

|AI suggestion|Evidence?|Decision|Reason|Verifcation|
|---|---|---|---|---|
|Validate all required<br>appointment<br>information|Yes|Accepted|Stage 1 testing<br>showed that missing<br>or invalid information<br>could be accepted|Test blank patient<br>names, missing<br>practitioner names<br>and invalid<br>appointment times.|
|Prevent practitioner<br>double booking|Yes|Accepted|Duplicate<br>appointment<br>bookings are an<br>identifed clinic<br>problem|Attempt to create two<br>appointments for the<br>same practitioner<br>and time|
|Defne consistent<br>appointment<br>statuses|Yes|Accepted|The case study<br>identifes<br>inconsistent<br>appointment status<br>information|Confrm that only the<br>defned statuses<br>Booked, Completed<br>and Cancelled can be<br>recorded.|
|Add user login and<br>detailed access<br>permissions|Partial|Unverifed|Privacy is important,<br>but the required<br>users, permissions<br>and authentication<br>method have not<br>been confrmed.|Ask the client who<br>requires access and<br>what each user<br>should be allowed to<br>do.|
|Add AI treatment<br>recommendations|No|Rejected|Treatment<br>recommendations<br>are outside the scope<br>of the appointment<br>management system|Compare the<br>suggestion with the<br>client brief and<br>confrmed project<br>scope.|



