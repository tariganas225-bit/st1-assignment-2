# Assignment 2-Case Study 

# Stage 4 Lab Activities 

# Implementing the SmartCare Domain Layer 

DESIGN FIRST -> AI PAIR PROGRAMMING -> REVIEW -> VERIFY | 1hour 

## **A - Revisit Approved UML** 

Confirm responsibilities, attributes and relationships before coding. 

The UML diagram that I did last week had three domain classes, patient, practitioner and appointment 

Patient stores the patient ID, name and contact details and provides the update_details() operation. 

Practitioner stores the practitioner ID, name and availability and provides update_availability() and is_available() operations. 

Appointment stores the appointment ID, appointment time and status and provides validate(), reschedule() and cancel() operations. 

## **B - Implement Patient: AI OFF** 

Implement Patient with type hints and basic validation. 

Code is in the weekly folder 

Explanation of what the code does 

The patient class stores a patient ID name and contact details using protected attributes. Type hints show that the values should be strings, while validation prevents blank information from being accepted 

## **C - Implement Practitioner: AI OFF** 

Implement Practitioner with identifier,. 

Code is in the weekly folder 

Explanation of what the code does 

The Practitioner class stores the practitioner’s ID, name and specialty using protected attributes. Type hints show the expected data types, and validation prevents blank values. 

## **D - Implement Appointment: AI ON** 

Give AI the approved Appointment UML, business rules and explicit constraints. Ask it to implement only Appointment and agreed enum/exception. 

AI code Can be seen in the files 

## **E - Review Generated Code** 

Check model consistency, unsupported features, public state mutation, unnecessary inheritance, invented dependencies and error handling. 

The generated code actually mostly followed the approved design. I decided to accept the AppointmentStatus enum, validation, protected status, read-only status property, reschedule() and cancel() methods, and AppointmentStatusError. This code actually correctly prevents illegal repeated transitions and keeps cancelled appointments as objects, it did not add a database and it does not add notifications, and UIs either 

I would most likely modify the patient and practitioner type hints from Any to Patient and Practitioner because the approved UML connects Appointment to those classes. I would also protect appointment_id, patient, practitioner and appointment_time with underscores. 

## **F - Manual Behaviour Checks** 

Create valid objects, test invalid input, cancel a scheduled appointment and attempt an illegal repeated transition. 

## **G - Refactor** 

Remove unnecessary code and make implementation simpler and design-consistent. 

## **H - AI Engineering Log** 

Record prompt, generated contribution, decisions and verification evidence. 

### Prompt used: 

I asked AI to implement only the Appointment class using the approved UML, type hints, an AppointmentStatus enum, protected status transitions and basic validation. I instructed it not to add database, UI, notification, manager, service or inheritance code. 

|AI contribution|Conforms?|Decision|Reason|Verification|
|---|---|---|---|---|
|AppointmentStatus<br>enum|Yes|Accepted|Restricts status<br>values|Checked all three<br>enum values|
|Protected _status|Yes|Accepted|Prevents direct<br>status mutation|Confirmed there is<br>no status setter|
|validate()|Yes|Accepted|Rejects invalid<br>information|Tested an empty<br>appointment ID|
|Transition checks|Yes|Accepted|Prevent illegal<br>cancellation and<br>rescheduling|Tested repeated<br>cancellation|
|Any type hints|Partial|Modified|Did not represent<br>UML associations<br>clearly|Replaced with<br>Patient and<br>Practitioner|
|Public Appointment<br>attributes|Partial|Modified|Allowed<br>uncontrolled<br>changes|Changed attributes<br>to protected state|
|__str__()|Not required|Rejected|Not required by the<br>approved model|Removed during<br>refactoring|
|Database and<br>notification code|Yes|Excluded|Outside the domain<br>layer and<br>requirements|Reviewed generated<br>classes and imports|



## **Suggested AI prompt** 

Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML. 

## **Reflection** 

Which AI-generated part did you modify or reject? Why? How did the approved design constrain the AI? 

I modified the Ai generated code by replacing the any type hints with Patient and Practitioner and changing the Appointment attributes to protected attributes. I removed the str() method because it was not required by the approved model but I did keep the enum validation and protected status transition because they did follow the requirements. 

