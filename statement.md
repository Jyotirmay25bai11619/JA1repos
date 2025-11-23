# Project Statement: Basic Health Symptom Checker

## Problem Statement
In the absence of immediate professional medical advice, individuals often struggle to accurately assess the severity of their physical symptoms. This uncertainty leads to two primary issues in the healthcare ecosystem:

1.Critical Delays: Patients with potentially life-threatening conditions (e.g., chest pain, difficulty breathing) may hesitate to call emergency services due to uncertainty or fear of overreacting.

2.Resource Strain: Conversely, patients with minor, self-treatable ailments (e.g., mild fatigue, common cold) may visit emergency rooms or clinics, unnecessarily overcrowding healthcare facilities and diverting attention from critical cases.

There is a clear need for an accessible, preliminary digital triage tool that can guide users toward the appropriate level of care based on a logical assessment of their symptoms.

## Scope of the Project
The scope of this project is to develop a text-based (CLI) software utility using Python that simulates a basic medical triage process.

In Scope:

* Logic Implementation: Designing a hard-coded decision tree using conditional control structures (if-elif-else) to route users through diagnostic paths.

* Emergency Triage: Implementing immediate "fail-fast" logic to identify and flag high-risk symptoms (chest pain, breathing issues) before proceeding to minor checks.

* Input Handling: Developing robust input validation to handle case sensitivity and whitespace in user responses (e.g., accepting " yes ", "YES", "y").

* Basic Assessment: Covering a limited set of common symptom branches:

    * Emergency Checks

    * Fever/Viral Infections

    * Abdominal/Digestive Issues

    * Fatigue/Dehydration

Out of Scope:

* GUI: Graphical User Interface (slated for future enhancements).

* Database: Persistent storage of patient history (slated for future enhancements).

* Medical Diagnosis: The tool provides assessments and recommendations, not professional medical diagnoses.

## Target Users

* General Public: Individuals seeking quick guidance on whether their symptoms require immediate emergency care, a doctor's visit, or home rest.

* Computer Science Students: Peers and educators looking for a practical demonstration of conditional logic and software design patterns in Python.

* Remote/Rural Populations: Users in areas with limited immediate access to doctors who need a first-line assessment tool.

## High-Level Features

* Priority Triage System: The application automatically prioritizes life-threatening questions at the start of the interaction.

* Interactive Questionnaire: A conversational command-line interface that adapts subsequent questions based on previous answers.

* Input Sanitization Module: Automatic cleaning of user inputs to prevent program crashes due to formatting errors.

* Actionable Assessments: Provides distinct, color-coded (text-based) outcomes such as "Call 911," "Consult a Doctor," or "Rest and Hydrate."

* Lightweight Architecture: Runs natively in any standard Python environment without heavy external dependencies.
