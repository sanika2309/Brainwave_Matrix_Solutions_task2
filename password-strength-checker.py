import re

def check_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[\W_]', password):  # \W matches any non-alphanumeric character (special character)
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Assess the password strength
    if score == 5:
        return "Strong Password!", feedback
    elif score >= 3:
        return "Moderate Password.", feedback
    else:
        return "Weak Password!", feedback

# Example usage
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions:")
    for suggestion in feedback:
        print(f"- {suggestion}")
