# Basic Health Symptom Checker

> Health symptom checker using conditional logic in Python

## Basic Idea
This is a simple command-line Python program designed to demonstrate how conditional logic works in software. It acts as a digital flowchart: it asks the user "Yes" or "No" questions about their physical condition and uses if/else statements to narrow down possibilities. Based on the answers provided, it outputs a basic assessment or advises the user to seek emergency care.

## How it Works

1. Input Handling
   The program uses the input() function to collect answers from the user. It automatically cleans the input using .lower().strip() so that typing "YES", "yes ", or "Yes" all work correctly.

2. Decision Logic (Branching)
The core of the program relies on nested conditional statements:
Root Check: It first checks for critical emergencies (chest pain/breathing issues). If this is "yes", the program warns the user and stops immediately using return.
Primary Branches: If it is not an emergency, it branches into two main paths:
Fever Path: Asks about coughs or headaches.
No-Fever Path: Asks about stomach pain or fatigue.

3. Output
Based on the specific combination of "Yes/No" answers, the program prints a specific assessment string to the console.

# Disclaimer
This code is for educational purposes only. It is not a medical device and should not be used for actual diagnosis. Always consult a medical professional for health concerns.
