# SmartCare v0.3 - Domain Model Workbook 

#### Week 6 student resource 

## **Requirement-to-Concept Trace** 

|Requirement|Concept|State/behaviour|Decision|
|---|---|---|---|
|FR-01|Patient|patient_id, name and<br>contact information|Create Patient class|
|FR-02|Patient|Identify a patient through<br>patient_id|Use patient_id for<br>searching|
|FR-03|Patient|update_details()|Allocate updating to<br>Patient|
|FR-04|Practitioner|name details and<br>availability|Create Practitioner class|
|FR-05|Practitioner|availability and<br>update_availability()|Store availability with<br>Practitioner|
|FR-06|Appointment|patient practitioner time<br>and status|Create Appointment<br>class|
|FR-07|Appointment|validate()|Allocate validation to<br>Appointment|
|FR-08|Practitioner and<br>Appointment|is_available() and confict<br>checking|Check availability before<br>creating an appointment|
|FR-09 and FR-12|Practitioner and<br>Appointment|Schedule and report<br>information|Derive views from stored<br>appointments|
|FR-10 and FR-11|Appointment|status, reschedule() and<br>cancel()|Allocate appointment<br>changes to Appointment|



## **CRC Cards** 

### **Patient** 

|Responsibilities|Collaborators|
|---|---|
|Store patient ID, name and contact information|Appointment|
|Update patient information and be connected to<br>appointment history|Appointment|





<!-- Start of picture text -->
flee Practitioner<br>orig iene *String practitioner_id<br>eae *String name<br>+String copa n tact_detailse) String8 availabitity<br>supdate_details(name, contact_details) ppnaprert+is_available(appointment_time) oracle dt<br>al All<br>has \mt attends<br>‘ KI,<br>Appointment<br>+String appointment_id<br>+DateTime appointment_time<br>+String status<br>validate()<br>+reschedule(new_time)<br>+cancel()<br><!-- End of picture text -->

Appointment is the central class because it connects patients with practitioners and without it the system would fail the patient can have zero or a ton of appointments and a practitioner can have zero or a ton of appointments nothing needs to be inherited because the classes represent different concepts. Schedule and report information can be calculated from appointment records so separate schedule and report classes are unnecessary. 

Patient ID is confirmed by FR-01. Practitioner ID and Appointment ID are provisional design assumptions that should be confirmed before full implementation. 

## **AI Design Review Record** 

|AI suggestion|Evidence|Decision|Reason|Model change|
|---|---|---|---|---|
|Use Patient, Practitioner<br>and Appointment classes|FR-01 to FR-12|Accepted|They are confrmed<br>concepts with state<br>and behaviour|Added the three<br>core classes|
|ScheduleEngine|FR-05, FR-08 and<br>FR-09 provide partial<br>evidence|Modifed|Scheduling is<br>needed, but a<br>separate engine is<br>excessive|Added availability<br>behaviour to<br>Practitioner|
|AppointmentManager|FR-06 to FR-12 provide<br>partial evidence|Modifed|Coordination may<br>later need a service,<br>but it is not a<br>domain entity|Kept appointment<br>behaviour in<br>Appointment|
|ClinicController|No requirements|Rejected|It is a technical<br>controller and could<br>become an<br>unnecessary central<br>class|No change|
|NotifcationManager|No requirements|Rejected|Notifcations remain<br>provisional|No change|



