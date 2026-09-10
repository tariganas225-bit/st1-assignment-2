# Assignment 2 Case Study 

# Stage 2 Tutorial From Problems to Requirements 

Week 5 | 60 minutes 

## **Learning goals** 

- Analyse stakeholders. 

- Distinguish functional and non-functional requirements. 

- Recognise ambiguity and unsupported requirements. 

- Define scope. 

- Develop user stories and acceptance criteria. 

- Critique AI-generated requirements. 

## **Activity 1 - Stakeholder Map** 

|Stakeholder|Need|Potential confict|
|---|---|---|
|Patients|We need accurate records, and a<br>simple way to book, schedule and<br>cancel appointments.|Some clients may have preferred<br>appointment times, this may cause<br>confict with the practitioner<br>availability.|
|Reception and administration staf|The reception will need to quickly<br>fnd and create patient records<br>when needed, and update or<br>cancel appointments without<br>duplicates|A confict could be when reception<br>and administration staf are trying<br>to complete their job and having to<br>do security checks and validation<br>may slow down the daily work.|
|Practitioners|Accurate schedules, availability<br>information and appointment<br>history|A big confict could be schedule<br>changes made by patients or staf<br>may disrupt their workload.|
|Clinic management|Reliable operational reports,<br>improved eficiency and a<br>manageable system.|Additional reporting features may<br>increase cost and project<br>complexity.|
|Softwaredeveloper and support<br>staf|Clear, testable requirements and<br>maintainable business logic|Stakeholders may request extra<br>features beyond the frst version’s<br>scope and this could increase cost<br>and complexity of the overall<br>project.|



## **Activity 2 - Functional or Non-Functional?** 

□ Functional   The system shall allow staff to cancel an appointment. 

□ Non-functional   The system should remain responsive for the course-scale dataset. 

□ Functional     The system shall retain cancelled appointments. 

□ Non-functional   Core business logic should be independently testable. 

□ Functional  The system shall search for a patient by ID. 

## **Activity 3 - Repair Ambiguous Requirements** 

The system should be easy to use. 

Problem: “Easy to use” is subjective and cannot be tested. Clarification question: What tasks should users be able to complete, and how quickly? 

Patient search should be fast. 

Problem: “Fast” does not specify a specific response time. Clarification question: How many seconds should a patient search take? 

The system should securely manage data. 

Problem: “Securely” does not explain what security is required. Clarification question: Who should be allowed to view or change patient information? 

Appointments should normally be easy to cancel. 

Problem: “Normally” and “easy” are unclear, and it does not say who can cancel appointments. Clarification question: Who can cancel an appointment, and should the cancelled appointment remain in the history? 

## **Activity 4 - AI Requirements Audit** 

Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope. 

|AI suggestion|Classifcation|Evidence / reason|
|---|---|---|
|Patients receive SMS reminders.|Unsupported|SMS reminders were not requested<br>or discussed in Stage 1.|
|Facial recognition login.|Unsupported|Stage 1 found no client evidence<br>and rejected it unless the client<br>later requests it.|



|Receptionists create<br>appointments.|Confrmed|The Stage 1 Lab and case study<br>explicitly says the receptionist<br>records patient appointments.|
|---|---|---|
|Online payment.|Unsupported|It was rejected in the current<br>version in stage one|
|Practitioners view schedules.|Assumption requiring validation|Stage 1 feature table classifed<br>practitioner schedule viewing as<br>provisional and requiring client<br>confrmation.|
|AI recommends treatments.|Out of scope|Stage 1 audit rejected diagnosis<br>and treatment recommendations<br>because the system is for<br>appointment management.|
|Cancelled appointments remain in<br>history.|Assumption requiring validation|Stage 1 engineering brief<br>specifcally listed this as a<br>question that must be answered by<br>the client.|



## **Exit question** 

Why is 'AI suggested it' not sufficient evidence for a requirement? 

“AI suggested it” is not sufficient evidence because AI can invent a feature that the client may never use or it was never requested in the beginning. Requirements must be supported by the client’s problems, stakeholder needs or business rules and then validated with the relevant stakeholders. The software engineer remains responsible for checking scope, privacy, safety and whether each requirement is necessary tested and implemented properly. 

