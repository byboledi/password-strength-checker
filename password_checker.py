password = input("Enter your password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1

# Check for uppercase letters
if any(char.isupper() for char in password):
    score += 1

# Check for lowercase letters
if any(char.islower() for char in password):
    score += 1

# Check for numbers
if any(char.isdigit() for char in password):
    score += 1

# Check for special characters
special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"

if any(char in special_characters for char in password):
    score += 1

# Display the result
if score <= 2:
    print("🔴 Weak Password")

elif score <= 4:
    print("🟡 Medium Password")

else:
    print("🟢 Strong Password")
