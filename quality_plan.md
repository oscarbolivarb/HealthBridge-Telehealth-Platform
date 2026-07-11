# Software Quality Plan 

The HealthBridge Telehealth Platform will focus on three software quality attributes: usability, security and maintainability. These are important because it helps the system to be easy to use, it protects patient's information and it will be easy to update.

## 1. Usability 

## Why It Matters

Patients and healthcare providers should be able to use the system without any confusions and the platform should work on a desktop as well as on a mobile device. 

### Early Planning

To be able to improve the usability the project will have to:

- Use a simple layout.
- Make navigation easy.
- Use clear labels and instructions. 
- Consider accessibility for all the users.

## 2. Security 

## Why It Matters

The platform will store private information from patients and keep this information safe making it HIPAA compliant.

### Early Planning

To be able to improve the security the project will have to:

- Use a secure login method.
- Give users access based on their roles.
- Protect patient's information.
- Follow secure development practices.

## 3. Maintainability

## Why It Matters

Since this project will continue to grow throughout the course, the software should be easy to update, improve and fix any problems that are found. 

### Early Planning

To be able to improve the maintainability the project will have to:

- Keep files organized.
- Write clean and readable code. 
- Update the project's documentation.
- Use GitHub to track any changes.

## Summary

By focusing on usability, security and maintainability from the beginning, this will make the platform easy to use, while protecting patient's information and being able to improve throughout the project. 


# Milestone 5 QA Update

## Scope 

This milestone focuses on testing the main HealthBridge features that has been planned so far, the testing includes a patient intake validation, an appointment scheduling during the clinic hours, role base access, time zone conversion, calendar scheduling and protecting sensitive patient information.

The items that are not included are the real EHR connection, a production database, mobile application testing and a full performance testing. These areas will be tested later as the project continues.

## Test Strategy 

Two testing levels are used for this milestone. 

Unit testing checks individual functions such as validation a phone number, the date of birth, insurance member ID, clinic hours and user roles. 

Integration testing checks that different parts of the system work together, one test verifies that an appointment is added to the calendar service, while another verifies that sensitive patient’s information is removed before it is written to the audit log. 

## Environments and Test Data

The tests run locally using Python, the test data is created inside the test files and it resets before every test starts with a clean environment. 

These are fictional patient information that is uses, there are no real patient records, passwords, API keys or medical information are stored in the repository. 

## Metrics

These are the metrics that will be tracked during this milestone:

-	Test coverage across the functions that are included in the project
-	Test pass rate 
-	Defect count by severity
-	
## How to Run 

Run the complete test:

```bash

python -m unittest discover -s testing_qa/test_suite -p "test_*.py" -v
