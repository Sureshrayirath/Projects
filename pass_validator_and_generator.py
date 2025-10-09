import random
import string

def password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    return score

def strength_label(score):
    return {
        1: "😬 Very Weak",
        2: "😕 Weak",
        3: "😐 Medium",
        4: "🙂 Strong",
        5: "💪 Very Strong"
    }.get(score, "❌ Invalid")

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

def main():
    print("🔐 Password Strength Checker & Generator")
    while True:
        choice = input("\nType a password to check or type 'gen' to generate one (q to quit): ")

        if choice.lower() == "q":
            print("👋 Goodbye!")
            break
        elif choice.lower() == "gen":
            pwd = generate_password()
            print(f"Generated: {pwd}")
            print(f"Strength: {strength_label(password_strength(pwd))}")
        else:
            score = password_strength(choice)
            print(f"Strength: {strength_label(score)}")

if __name__ == "__main__":
    main()
