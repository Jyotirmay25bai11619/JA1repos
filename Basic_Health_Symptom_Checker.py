def start_checker():
    print("---- Basic Health Symptom Checker ----")
    print("Please answer 'yes' or 'no' to the following questions.")
    print("----------------------------------------")

# Question 1: Emergency Check
    answer = input("Are you having chest pain or difficulty breathing? ")

    if answer == "yes":
        print("\n>>> URGENT: Call emergency services (108/112) immediately.")
        return # Stop the program here

    else:
        # If not an emergency, check for fever
        answer = input("Do you have a fever (temperature over 100°F / 37.8°C)? ").lower().strip()

        if answer == "yes":
            # Branch: User has a fever
            answer = input("Do you have a dry cough? ").lower().strip()

            if answer == "yes":
                print("\n>>> ASSESSMENT: Possible viral infection or Flu. Drink plenty of fluids and rest.")
            else:
                # Fever but no cough
                answer = input("Do you have a severe headache? ").lower().strip()
                if answer == "yes":
                     print("\n>>> ASSESSMENT: Consult a doctor. Fever with severe headache requires attention.")
                else:
                     print("\n>>> ASSESSMENT: General fever. Monitor your temperature.")

        else:
            # Branch: User does NOT have a fever
            answer = input("Do you have stomach or abdominal pain? ").lower().strip()

            if answer == "yes":
                print("\n>>> ASSESSMENT: Possible food poisoning or digestive issue. Avoid solid foods for a few hours.")
            else:
                # No fever, no stomach pain
                answer = input("Do you feel unusually tired/fatigued? ").lower().strip()
                
                if answer == "yes":
                    print("\n>>> ASSESSMENT: You might be dehydrated or sleep deprived.")
                else:
                    print("\n>>> ASSESSMENT: No specific symptoms detected. You seem to be okay!")

    print("\n----------------------------------------")
    print("DISCLAIMER: I am a python script, not a doctor.")
    print("Always seek professional medical advice.")

if __name__ == "__main__":
    start_checker()