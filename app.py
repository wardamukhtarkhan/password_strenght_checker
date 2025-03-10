import string
import random
import re

class PasswordStrengthMeter:
    def check_password_strength(self, password):
        score = 0
        feedback = []
        
        # Check length
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Password should be at least 8 characters long")
            
        # Check for numbers
        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("Add some numbers")
            
        # Check for uppercase and lowercase
        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("Use both uppercase and lowercase letters")
            
        # Check for special characters
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        else:
            feedback.append("Add special characters (!@#$%^&*)")
            
        # Determine strength
        if score <= 1:
            strength = "Very Weak"
        elif score == 2:
            strength = "Weak"
        elif score == 3:
            strength = "Moderate"
        else:
            strength = "Strong"
            
        return score, feedback, strength
    
    def generate_strong_password(self, length=12):
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(characters) for _ in range(length))
        return password 