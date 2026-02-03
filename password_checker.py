import re
import getpass
from strength_meter import show_meter

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include numbers.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        suggestions.append("Add special symbols (!@#$...).")

    # Strength decision
    if score <= 3:
        strength = "WEAK"
    elif 4 <= score <= 6:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return score, strength, suggestions


print("🔐 Password Strength Checker\n")
password = getpass.getpass("Enter your password: ")

score, strength, suggestions = check_password_strength(password)

print(f"\nStrength: {strength}  (Score: {score}/7)")

show_meter(score)

if suggestions:
    print("\nSuggestions to improve:")
    for s in suggestions:
        print("-", s)
