# Assignment 2 – Case Study Lab 

# Stage 2 Lab Activities 

# SmartCare Requirements Engineering 

AI OFF -> AI ON -> VERIFY | 1 hour 

## **Learning objectives** 

- Analyse the SmartCare client brief. 

- Identify stakeholders and scope. 

- Write functional and non-functional requirements. 

- Develop user stories and Given-When-Then acceptance criteria. 

- Use AI to critique requirements without allowing it to invent stakeholder needs. 

- Produce SmartCare Requirements Specification v1.0. 

## **Part A - Client Brief: AI OFF** 

SmartCare uses spreadsheets and paper records. Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history. Management wants a small, maintainable patient, practitioner and appointment system. 

## **Part B - Stakeholders and Scope: AI OFF** 

Identify at least four stakeholders. Create In Scope and Out of Scope lists. Label uncertain features as provisional rather than confirmed. 

Stakeholders: Patients Reception staff Practitioners Clinic management Software developer 

Patients: Need accurate records, reliable appointments and privacy Reception Staff: Need to create, find, update and cancel appointments efficiently Practitioners: Need to assess their availability and appointment schedules Clinic management: Needs reliable records and basic operational reports Software developer: Needs clear, testable requirements and manageable scope 

In scope 

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

## **Part C - Functional Requirements: AI OFF** 

Write 8-12 numbered functional requirements using FR-01, FR-02 and so on. Each should describe one observable capability. 

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

## **Part D - Non-Functional Requirements: AI OFF** 

Write 4-6 numbered non-functional requirements covering appropriate qualities such as reliability, maintainability, usability, data integrity or testability. 

NFR-01: Performance - Patient results should return results pretty quickly and should not take too long 

NFR-02: Usability - The system will display clear labels, instructions and error messages. 

NFR-03: Reliability - Saved information will remain available after the application is closed and restarted 

NFR-04: Data integrity - Invalid input should not damage or remove existing records 

NFR-05: Testability - Important functions, such as booking and cancellation, should be testable separately 

NFR-06: Security - Only authorised clinic staff should access patient information 

## **Part E - User Stories and Acceptance Criteria: AI OFF** 

Write 4-6 user stories. For at least three, create Given-When-Then acceptance criteria including one negative or failure scenario. 

US-01: As a receptionist I want to be able to register a patient so that their information can be used for appointments 

US-02: As a receptionist I want to search for a patient by ID so that I can quickly locate the correct record. 

US-03: As a practitioner I want to view my schedule so that I know which patients I will see. 

US-04: As a clinic manager I want to view appointment reports so that I can monitor clinic operations. 

US-05: As a receptionist I want to go back to the canceled appointments history and reschedule an old patient. 

US-06: As a receptionist I want to cancel or reschedule an appointment so that changes are accurately recorded. 

1. Successful booking 

Given: an existing patient, practitioner and available time 

When: the receptionist enters valid appointment information 

Then: the system creates the appointment with a Booked status. 

#### 2. Patient search 

Given: a patient record exists 

When: the receptionist searches using the patient’s ID 

Then: the system displays the matching patient record. 

#### 3. Double booking failure 

Given: a practitioner already has an appointment at a particular time 

When: the receptionist attempts to book another appointment for the same practitioner and time 

Then: the system rejects the booking and displays an explanation. 

## **Part F - AI Requirements Review: AI ON** 

Prompt: Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation. 

The AI review identified the following issues: 

- “Fast,” “secure” and “easy to use” were not measurable. 

- The exact patient, practitioner and appointment fields were not defined. 

- User permissions were unclear. 

- Appointment-status values needed to be defined consistently. 

- The expected number of stored records was unknown. 

- The cancellation requirement needed to explain whether cancelled appointments remain in history. 

- Features such as reminders, payments and treatment recommendations had no supporting evidence. 

## **Part G - VERIFY the AI Review** 

Classify each significant AI suggestion as Accepted, Modified, Rejected, or Unverified. Explain the evidence used. 

|**AI suggestion**|**Classif**<br>**cation**|**Evidence and explanation**|
|---|---|---|
|Validate all appointment<br>felds|Accepte<br>d|Stage 1 testing showed that blank and invalid<br>values could be accepted|
|Prevent practitioner<br>double-booking|Accepte<br>d|Duplicate bookings are an identifed clinic<br>problem|
|Use Booked, Completed<br>and Cancelled statuses|Accepte<br>d|The case identifes inconsistent appointment-<br>status information|
|Guarantee a two-second<br>search time|Modife<br>d|A measurable limit is useful, but the client must<br>confrm the target and expected dataset|
|Add user login and detailed<br>permissions|<br>Unverif<br>ed|Privacy is important, but the required roles and<br>authentication method are not confrmed|
|Add SMS reminders|Rejecte<br>d|The client did not request reminders|
|Add AI treatment<br>recommendations|Rejecte<br>d|Treatment recommendations<br>are outside the system’s scope|



## **Part H - Finalise SmartCare v0.2** 

Submit stakeholder analysis, scope, 8-12 FRs, 4-6 NFRs, 4-6 user stories, acceptance criteria, assumptions/open questions and selected AI review evidence. 

## **Reflection** 

In 150-250 words: What did AI notice that you missed? What did AI invent or overreach on? Which requirement changed after review? Why must requirements have evidence? 

AI helped me notice that several of my requirements were extremely vague too test. The reason this was said was because of the words I chose such as “fast,” “secure” and “easy”, whilst these words sounded reasonable they did not provide a clear result that could be checked. AI also identified missing questions about user permissions, appointment statuses, expected data volumes and record retention. These points helped me make the requirements more specific. 

Even though AI did give some great ideas it does sometimes overdoes it by suggesting features that sound useful but have no evidence from the client. For example SMS reminders, online payments, facial recognition and AI treatment recommendations. I rejected these suggestions because they were not part of the SmartCare problems or the scope of the first version. 

One requirement that was changed was the cancellation requirement. The original requirement said that appointments should normally be easy to cancel. This was very unclear as it did not identify the user, system behaviour or effect on appointment history. I changed it to state that staff can cancel an appointment by changing its status to Cancelled while keeping it in the appointment history. 

And requirements must have evidence because every feature adds development work, testing and maintenance. Evidence is what connects a requirement to a real stakeholder need or business problem and prevents unsupported AI suggestions from expanding the project. 

