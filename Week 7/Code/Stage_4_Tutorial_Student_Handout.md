# Assignment 2 – Case Study 

# Stage 4 Tutorial Activities 

# Object-Oriented Design Decisions 

Week 7 | 60 minutes 

## **Activity 1 - Encapsulation Review** 

|Class|Protected state / invariant|Public operations|
|---|---|---|
|Patient|Patient ID, name and contact<br>details must not be blank|update_details()|
|Practitioner|Practitioner ID, name and specialty<br>must not be blank|update_availability(), is_available()|
|Appointment|Must have an ID, Patient,<br>Practitioner and valid time. Status<br>changes must be legal|validate(), reschedule(), cancel()|



## **Activity 2 - Composition or Inheritance?** 

Appointment and Patient -> □ Composition/association Reason: An appointment has a patient but is not a type of patient 

Appointment and Practitioner -> □ Composition/association  Reason: An Appointment has a Practitioner, but it is not a type of Practitioner. 

Doctor and Practitioner (hypothetical) -> □ Inheritance  Reason: A Doctor could be a specialised type of Practitioner. 

Clinic and Appointment -> □ Composition/association  Reason: A Clinic could contain Appointments, but an Appointment is not a type of Clinic. 

## **Activity 3 - Responsibility Allocation** 

Who decides whether SCHEDULED can become CANCELLED? The appointment class because it owns and protects its status. 

Who validates a patient name? The Patient class when a Patient is created or updated 

Should Appointment execute SQL? Why? No. Appointment should contain domain rules not database code 

Should the UI decide whether a status transition is legal? No. The Appointment class should enforce the rule so it applies regardless of the interfaceee 

## **Activity 4 - AI Code Critique** 

AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections. 

Ai Critique 

Public status mutation allows invalid changes. Make status protected and provide controlled methods. 

SQL inside cancel() mixes domain and database responsibilities. Remove the SQL. 

NotificationManager is unsupported by the confirmed requirements. Remove the dependency. 

Appointment should not inherit from PatientRecord because an Appointment is not a Patient. 

cancel() must confirm the appointment is scheduled before changing its status. 

## **Exit question** 

Why can code be object-oriented syntactically but still have poor object-oriented design? 

Code can still use classes and still have poor object-oriented design if state is public, responsibility are placed in the wrong classes 

