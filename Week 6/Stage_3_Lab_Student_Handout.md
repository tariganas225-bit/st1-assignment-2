# Assignment 2- Case Study 

# Stage 3 Lab Activities 

# SmartCare Domain Modelling 

AI OFF -> AI ON -> COMPARE -> VERIFY | 1 hour 

## **A - Requirements Review** 

Highlight nouns, verbs and business rules in SmartCare v0.2. 

#### Nouns: 

Patient, practitioner, appointment, patient ID, practitioner ID, availability, schedule, date, time, status, appointment history, report and reception staff. 

#### Verbs: 

Create, search, update, record, display, validate, prevent, reschedule, cancel, retain and produce. 

Business rules: 

1. Each patient must have a unique patient ID. 

2. Each appointment must involve one patient and one practitioner 

3. A practitioner cannot have two appointments at the same time 

4. Appointment statuses include Booked, Completed and Cancelled 

5. A cancelled appointment remains in the appointment history 

6. Reports are produced from recorded appointment information 

## **B - Candidate Classes** 

Record candidate concepts, supporting requirements, state and behaviour. 

The selected domain classes are Patient, Practitioner and Appointment. 

Name and Status are attributes. Cancellation is Appointment behaviour. Database is technical infrastructure. Clinic is not currently required as a domain class 



<!-- Start of picture text -->
Patient precttone<br>aay +String practitioner_id<br>una *String name<br>*String contact_details +String i availability id<br>* update_details(name,\ contact_details) Uesupdate_availability(availability)arahatintapnolerantl aan)<br>has attends<br>S. rae<br>Appointment<br>‘String appointment_id<br>+DateTime appointment_time<br>“String status<br>validate()<br>sreschedule(new_time)<br>+cancel()<br><!-- End of picture text -->

## **E - AI Design Review** 

Ask AI to suggest classes and relationships using only confirmed requirements; require supporting requirement IDs. (Used with co-pilot) 

#### Prompt: 1 

Act as a software domain-model reviewer. Review the proposed Patient, Practitioner and Appointment classes using only the confirmed SmartCare v0.2 requirements. Suggest appropriate attributes, operations, associations and multiplicities. Provide the supporting requirement ID for each suggestion. Do not invent new client features or add technical manager, controller, notification or scheduling classes without evidence. 

#### Response: 

I can perform that review, but the SmartCare v0.2 requirements are not included in your message. 

Because your instruction explicitly says to use only the confirmed SmartCare v0.2 requirements and not invent features, I cannot reliably recommend attributes, operations, associations, multiplicities, or requirement traceability without the actual requirements set. 

Once you provide the SmartCare v0.2 requirements (or the relevant requirement IDs and descriptions), I will produce a review in the following format: 

The output will include: 

Patient class review 

Attributes 

#### Operations 

Associations and multiplicities 

Requirement traceability 

Practitioner class review 

Attributes 

Operations 

Associations and multiplicities 

Requirement traceability 

Appointment class review 

Attributes 

Operations 

Associations and multiplicities 

Requirement traceability 

Gap analysis 

Missing model elements supported by requirements 

Unsupported elements that should be removed 

Ambiguous requirements affecting the domain model 

Provide the SmartCare v0.2 requirements and I will complete the review strictly against them. 

Prompt # 2 

Here are the confirmed SmartCare v0.2 requirements: 

FR-01: Create a patient record with a unique patient ID. 

FR-02: Search for a patient using their ID. 

FR-03: View and update patient information. 

FR-04: Store practitioner details and availability. 

FR-05: Display practitioner availability for appointment booking. 

FR-06: Create, reschedule and cancel appointments. 

FR-07: Reject an appointment if required information is missing. 

FR-08: Prevent double bookings. 

FR-09: Display a practitioner’s appointment schedule. 

FR-10: Record appointment status as Booked, Completed or Cancelled. 

FR-11: Keep cancelled appointments in the appointment history. 

FR-12: Produce basic reports by date, practitioner or appointment status. 

Please review only the Patient, Practitioner and Appointment classes. Suggest suitable attributes, methods, associations and multiplicities. Include the supporting requirement ID for each suggestion. Keep the design basic and do not add unsupported manager, controller, notification or scheduling classes. 

Note: The requirements do not specify individual fields (e.g., name, address, phone number). Therefore, a generic patientInformation attribute is safer than inventing unsupported details. 



<!-- Start of picture text -->
Suggested Operations<br>Operation Purpose<br>createRecord() Create a new patient record<br>findByld() Search for a patient using<br>viewInformation() View patient information<br>updatelnformation() Update patient information<br><!-- End of picture text -->

o Purpose Requirement Create a new patient record FR-01 Search for a patient using ID FR-02 View patient information FR-03 Update patient information FR-03 Ny 



<!-- Start of picture text -->
2. Practitioner Class<br>Suggested Attributes<br>Attribute Reason Requirement<br>practitionerDetails Practitioner information stored by FR-04<br>the system<br>availability Available appointment times FR-04, FR-05<br>Suanested Oneratinns G“9<br>Associations<br>‘equirement<br>Practitioner - Appointment<br>A practitioner can have many appointments. Each appointment is associated with one practitioner. R-05<br>22 R-04<br>R-09<br>ie)<br>Association Multiplicity Requirement<br>Practitioner has Appointments 1 to 0.* FR-05, FR-06, FR-09<br><!-- End of picture text -->

3. Appointment Class Suggested Attributes 

Attribute Reason Requirement appointmentDateTime Needed for booking, FR-06, FR-12 rescheduling and reporting by date status Booked, Completed, FR-10 Cancelled 

cancelledFlag (optional) 

Supports historical retention FR-11 of cancelled appointments 



<!-- Start of picture text -->
If status includes "Cancelled", the separate cancel ledF lag is unnecessary.<br>Using only status is the simpler design.<br>Jin<br>Suggested Operations o<br>Operation Purpose Requirement<br>createAppointment() Create appointment FR-06<br>rescheduleAppointment() Reschedule appointment FR-06 oO<br>cancelAppointment() Cancel appointment FR-06<br>validateRequiredInformation( Reject appointment when FR-07<br>) information is missing<br>checkAvailability0 Prevent double bookings FR-08<br>updateStatus() Maintain FR-10<br>Booked/Completed/Cancelle<br>d status<br><!-- End of picture text -->

#### Suggested Operations 

Associations 

Appointment - Patient 



<!-- Start of picture text -->
Each appointment belongs to exactly one patient.<br>Patient 1 ----- 0..* Appointment<br>Appointment ----- 1 Patient<br>Requirement<br>FR-06, FR-11<br><!-- End of picture text -->



<!-- Start of picture text -->
Appointment - Practitioner<br>Each appointment is booked with exactly one practitioner.<br>2m =<br>Practitioner 1 ----- 0..* Appointment<br>Appointment ----- 1 Practitioner<br>Requirement<br>FR-05, FR-06, FR-09<br>NY<br>Recommended Multiplicity Summary<br>Patient 1 ---------- 0..* Appointment<br>Practitioner 1 ----- 0..* Appointment<br>Appointment -------- 1 Patient<br>Appointment -------- 1 Practitioner<br>Rationale<br><!-- End of picture text -->

e A patient may have no appointments yet or many appointments over time (FR-06, FR-11). e A practitioner may have no appointments yet or many appointments (FR-05, FR-09). e Each appointment must be for one patient and one practitioner to support booking, scheduling, status tracking, and reporting (FR-05, FR-06, FR-09, FR-10). 

### Elements That Should NOT Be Added 

The requirements provide no evidence for: 

- © Notification class 

- e Scheduler/Scheduling class 

- e AppointmentManager class 

- e PatientManager class 

- e PractitionerManager class 

- e Authentication/Login attributes 

- ¢ Billing or Payment classes 

- ¢ Medical records or treatment history 

- ¢ Contact details such as phone, email, address 

- e Room, clinic, or location entities 

These elements would be assumptions beyond the confirmed SmartCare v0.2 requirements and 

should not be included in the domain model at this stage. 

##### Overall Assessment 

The minimal domain model supported by the requirements consists of three core entities: 

- e Patient 

- e Practitioner 

- ¢ Appointment 

with Appointment acting as the association entity connecting one Patient to one Practitioner, while maintaining appointment date/time and status information needed for booking, rescheduling, cancellation, schedule viewing, history retention, and reporting. This design fully supports FR-01 through FR-12 without introducing unsupported etal 



<!-- Start of picture text -->
ass Patient:<br># FR-@1: Create a patient record wit a unique fF ient ID.<br>def __init_(self, 5 ’ ):<br>pass<br># FR-@3: Update patient inf tion.<br>jef update_details(self, ) ):<br>pass<br>class Practitioner:<br>def _init_(self, . A ):<br>pass<br># FR-04: Update practitioner availability.<br>jef update_availability(self, MH<br>pass<br># FR-@5 and FR-@8 heck availability and prevent double bookings.<br>def is_available(self, Ns<br>pass<br>class Appointment:<br># FR-@6 a FR-10: Create an appoint t andrecord it tatus.<br>def __init__(<br>self,<br>,<br>,<br>):<br>pass<br># FR-@7 a FR-@8: Va jate informatio id prevent dout bookings.<br>def validate(self):<br>pass<br># FR-@6 and FR-@8: Reschedule without creating a double booking.<br>def reschedule(self, vis<br>pass<br># FR-@6, FR-10 and FR-11: Cancel and retain the appointment in history.<br>def cancel(self):<br>47 pass|<br><!-- End of picture text -->

## **H - Consistency Check** 

Check model-code consistency; do not implement full behaviour yet. 

## **Reflection** 

What modelling decision was hardest? Where did AI over-design? What evidence supported your final choices? 

The hardest modelling decision was deciding weather stuff like Status and Cancellation should be separate classes. I decided that status should be an attribute of appointment and cancellation should be an Appointment operation because they do not need their own classes. 

The AI slightly went a bit overboard when designing the appointment class by suggesting an optional cancelledFlag I think it’s because I provided a bunch of my requirements from last week. In the end I rejected this because the status attribute already records whether an appointment is booked, completed or  cancelled so this would be quite irrelevant. 

The final decisions I made were supported by the confirmed requirements. Patient is supported by FR-01 to FR-03, Practitioner by FR-04, FR-05 and FR-09, and Appointment by FR-06 to FR-12. 

