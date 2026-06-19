
password = input("Enter your password: ")

if len(password) < 8:
    print("❌ Weak: Password must be at least 8 characters long.")
else:
    print("✅ Good: Password length is acceptable.")
