# Assignment 2-Case Study 

# Stage 3 Tutorial Activities 

# From Requirements to Domain Models 

Week 6 | 60 minutes 

## **Candidate Concepts** 

|Candidate|Class?|Reason|
|---|---|---|
|Patient|Yes|Has its own identity, information<br>and responsibilities|
|Practitioner|Yes|Has a unique identity, availability,<br>details and appointments|
|Appointment|Yes|Has its own identity, date, time,<br>status and relationships|
|Name|No|A name is not a class its the name<br>of a patient or practitioner|
|Clinic|Not currently|Only one clinic is required and no<br>separate Clinic behaviour is<br>confrmed|
|Database|No|A database is a technical<br>infrastructure|
|Cancellation|No|Cancellation is an action<br>performed on an Appointment|
|Status|No|The status is an appointment<br>attribute ie, booked or cancelled or<br>completed|



## **CRC Cards** 

### **Patient** 

Responsibilities Collaborators 

|Store patient ID, name and contact information|Appointment|
|---|---|
|Update patient information and be connected to<br>appointment history|Appointment|



### **Practitioner** 

|Responsibilities|Collaborators|
|---|---|
|Store practitioner details and availability|Appointment|
|Check availability and provide an appointment<br>schedule|Appointment|



### **Appointment** 

|Responsibilities|Collaborators|
|---|---|
|Store appointment time, status, patient and|Patient and Practitioner|
|practitioner||
|Validate, reschedule and cancel an appointment|Patient and Practitioner|



## **Relationship Reasoning** 

Patient to Appointment: which relationship and why? 

This is an association. One patient can have zero or many Appointments, while every Appointment must be connected to exactly one Patient. This means every unique appointment must go with its unique patient 

Practitioner to Appointment: what multiplicity? 

One Practitioner can have zero or many Appointments, while every Appointment must be connected to exactly one Practitioner. 

Should Appointment inherit from Patient? 

No an Appointment is not a type of patient, It is connected to a Patient through an association. 

Does Clinic need to own every object? 

No a clinic does not need to own every object would make the the model unnecessarily complicated. Patient, Practitioner and Appointment can represent the confirmed domain requirements. 

## **AI Model Critique** 

Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine. 

PatientManager: Reject as a domain class. Patient management is required, but a separate manager class is not supported by the requirements. 

PractitionerManager: Reject as a domain class. Practitioner information can be represented by Practitioner 

AppointmentManager: Modify, appointment coordination may eventually require a service, but it should not replace the Appointment domain class. 

ClinicController: Reject from the domain model. It is a technical controller rather than a confirmed business concept. 

NotificationManager: Reject, notifications remain provisional and are not part of the confirmed scope. 

ScheduleEngine: Modify, availability and double-booking checks are required, but a separate scheduling engine is too complex for the current version. This behaviour can initially be allocated to Practitioner 

