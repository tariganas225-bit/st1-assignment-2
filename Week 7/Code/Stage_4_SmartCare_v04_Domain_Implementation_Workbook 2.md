# SmartCare v0.4 - Domain Implementation Workbook 

Week 7 student resource 

## **1. UML-to-Code Trace** 

|UML element|Python element|Implemented?|Notes|
|---|---|---|---|
|Patient class|class Patient|Yes|Core domain class|
|Patient attributes|_patient_id, _name,<br>_contact_details|Yes|Protected and validated|
|update_details()|Patient.update_details()|Yes|Updates valid patient<br>details|
|Practitioner class|class Practitioner|Yes|Core domain class|
|Practitioner ID and name|_practitioner_id, _name|Yes|Protected and validated|
|Practitioner availability|availability,<br>update_availability(),<br>is_available()|Not Yet|Present in UML but not<br>required by Lab C<br>implementation|
|Practitioner specialty|_specialty|Yes|Added because stage 4<br>Lab C needed it|
|Appointment class and<br>associations|class Appointment,<br>_patient, _practitioner|Yes|Connects one Patient and<br>one Practitioner|
|Appointment attributes<br>and status|_appointment_id,<br>_appointment_time,<br>_status,<br>AppointmentStatus|Yes|Status is protected by an<br>enum|
|Appointment operations|validate(), reschedule(),<br>cancel()|Yes|Includes validation and<br>transition rules|



## **2. Domain Invariants** 

|Class|Invariant / rule|How protected|
|---|---|---|
|Patient|Patient ID cannot be blank|Constructor validation|



|Patient|Name and contact details cannot<br>be blank|Constructor and update_details()<br>validation|
|---|---|---|
|Practitioner|ID, name and specialty cannot be<br>blank|Constructor validation|
|Appointment|Appointment ID cannot be blank|validate()|
|Appointment|Must contain a Patient, Practitioner<br>and date time|Type and missing value validation|
|Appointment|Status must be Scheduled,<br>Completed or Cancelled|AppointmentStatus enum|
|Appointment|Only scheduled appointments can<br>be rescheduled or cancelled|Checks inside reschedule() and<br>cancel()|
|Appointment|Cancellation must not delete the<br>appointment|Status changes to cancelled while<br>the object remains|



## **3. Composition / Inheritance Decisions** 

|Relationship|Decision|Rationale|
|---|---|---|
|Appointment Patient|Association|Appointment has a Patient but is<br>not a Patient|
|Appointment Practitioner|Association|Appointment has a Practitioner but<br>is not a Practitioner|
|Appointment inherits Patient|Rejected|Appointment is not a specialised<br>Patient|
|Appointment inherits Practitioner|Rejected|Appointment is not a specialised<br>Practitioner|
|Clinic Appointment|Association if Clinic is introduced|A Clinic may have Appointments<br>but is not an Appointment|



## **4. AI Pair-Programming Record** 

|AI contribution|Conforms?|Decision|Reason|Verification|
|---|---|---|---|---|
|AppointmentStatus|Yes|Accepted|Restricts status|Checked all three|
|enum|||values|enum values|



|Protected _status|Yes|Accepted|Prevents direct<br>status mutation|Confirmed there is<br>no status setter|
|---|---|---|---|---|
|validate()|Yes|Accepted|Rejects invalid<br>information|Tested an empty<br>appointment ID|
|Transition checks|Yes|Accepted|Prevent illegal<br>cancellation and<br>rescheduling|Tested repeated<br>cancellation|
|Any type hints|Partial|Modified|Did not represent<br>UML associations<br>clearly|Replaced with<br>Patient and<br>Practitioner|
|Public Appointment<br>attributes|Partial|Modified|Allowed<br>uncontrolled<br>changes|Changed attributes<br>to protected state|
|__str__()|Not required|Rejected|Not required by the<br>approved model|Removed during<br>refactoring|
|Database and<br>notification code|Yes|Excluded|Outside the domain<br>layer and<br>requirements|Reviewed generated<br>classes and imports|



## **5. Updated UML** 

Insert updated UML only if implementation revealed a justified design change. Explain every change. 

Photo can be seen in VScode/github 

There were quite a few changes with the UML diagram one of the main ones were from changing the attributes from public (+) to private (-) because the Python classes use encapsulation to prevent their data from being changed directly. The practitioner was updated from a string to a list, patient and practitioner references were added to appointment The Appointment status type was changed from String to AppointmentStatus, and a new AppointmentStatus enumeration was added to restrict the status to SCHEDULED, COMPLETED or CANCELLED. This was the majority of the changes 

