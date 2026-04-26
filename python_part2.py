# ============================================================
# 🐍 Python Part 2 — By Omar Ahmed | iSchool
# ============================================================


# ============================================================
# ✅ 1. FUNCTIONS & PARAMETERS
# ============================================================

def greet(name, age):
    """Function that takes name and age and returns a greeting."""
    return f"Hello {name}! You are {age} years old."

def add(a, b=10):
    """Function with a default parameter."""
    return a + b

print(greet("Omar", 15))   # Hello Omar! You are 15 years old.
print(add(5))              # 15 (uses default b=10)
print(add(5, 20))          # 25


# ============================================================
# ✅ 2. DICTIONARIES & TUPLES
# ============================================================

# Dictionary = key-value pairs (like a real dictionary)
student = {
    "name": "Omar",
    "age": 15,
    "skills": ["Python", "HTML", "CSS"]
}

print(student["name"])         # Omar
print(student["skills"][0])    # Python

# Add new key
student["city"] = "Cairo"

# Loop through dictionary
for key, value in student.items():
    print(f"{key}: {value}")

# Tuple = like a list but IMMUTABLE (can't be changed)
coordinates = (30.0444, 31.2357)  # Cairo coordinates
print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")


# ============================================================
# ✅ 3. FILE HANDLING (Read & Write)
# ============================================================

# Write to a file
with open("data.txt", "w") as file:
    file.write("Name: Omar Ahmed\n")
    file.write("Age: 15\n")
    file.write("City: Cairo\n")

print("File written successfully!")

# Read from the file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Append to the file (add without deleting)
with open("data.txt", "a") as file:
    file.write("Skills: Python, Web Dev\n")


# ============================================================
# ✅ 4. ERROR HANDLING (try / except)
# ============================================================

def divide(a, b):
    """Safe division with error handling."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "❌ Error: Cannot divide by zero!"
    except TypeError:
        return "❌ Error: Please enter numbers only!"
    finally:
        print("Division operation attempted.")  # Always runs

print(divide(10, 2))    # 5.0
print(divide(10, 0))    # Error: Cannot divide by zero!
print(divide(10, "x"))  # Error: Please enter numbers only!


# ============================================================
# ✅ 5. OOP BASICS — Classes & Objects
# ============================================================

class Developer:
    """A class to represent a Developer."""

    # Constructor — runs when object is created
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language
        self.projects = []

    # Method — function inside a class
    def introduce(self):
        return f"I'm {self.name}, {self.age} years old. I code in {self.language}."

    def add_project(self, project):
        self.projects.append(project)
        print(f"✅ Project '{project}' added!")

    def show_projects(self):
        if self.projects:
            print(f"\n{self.name}'s Projects:")
            for i, project in enumerate(self.projects, 1):
                print(f"  {i}. {project}")
        else:
            print("No projects yet.")


# Create an object (instance) of Developer
omar = Developer("Omar", 15, "Python")
print(omar.introduce())

omar.add_project("OmarBot")
omar.add_project("LinguaStory")
omar.add_project("Wave Streetwear")
omar.show_projects()


# ============================================================
# ✅ 6. PYTHON CHATBOT — Built from scratch 🤖
# ============================================================

class OmarBot:
    """A simple chatbot built with OOP."""

    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.score = 0
        self.responses = {
            "hello": "Hey! 👋 I'm OmarBot. How can I help?",
            "hi": "Hi there! 😊 What's up?",
            "how are you": "I'm just code, but I'm running great! 🚀",
            "what is python": "Python is a powerful programming language! 🐍",
            "who made you": "I was built by Omar Ahmed — a 15-year-old developer from Cairo! 🇪🇬",
            "bye": "Goodbye! Keep coding! 💪",
        }

    def get_response(self, user_input):
        """Get bot response based on user input."""
        user_input = user_input.lower().strip()

        if user_input in self.responses:
            self.score += 10  # Add points for known questions
            return self.responses[user_input]
        else:
            return f"🤔 I don't understand '{user_input}' yet. Try: hello, bye, how are you"

    def show_score(self):
        return f"🏆 Your chat score: {self.score} points"

    def run(self):
        """Run the chatbot in a loop."""
        print(f"\n{'='*40}")
        print(f"  Welcome to {self.bot_name}! 🤖")
        print(f"  Type 'bye' to exit")
        print(f"{'='*40}\n")

        while True:
            try:
                user_input = input("You: ").strip()

                if not user_input:
                    print(f"{self.bot_name}: Please say something! 😅\n")
                    continue

                response = self.get_response(user_input)
                print(f"{self.bot_name}: {response}\n")

                if user_input.lower() == "bye":
                    print(self.show_score())
                    break

            except KeyboardInterrupt:
                print(f"\n{self.bot_name}: Bye! 👋")
                break


# ============================================================
# 🚀 RUN THE CHATBOT
# ============================================================

bot = OmarBot("OmarBot 2.0")
bot.run()


# ============================================================
# 🎯 KEY TAKEAWAYS:
# - Functions make code reusable
# - Dictionaries store key-value data
# - Tuples are immutable lists
# - File handling saves data permanently
# - Try/Except prevents crashes
# - OOP organizes code into objects
# ============================================================
