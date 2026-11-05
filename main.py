import time
import random
import os
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Green terminal theme
GREEN = Fore.GREEN
BRIGHT_GREEN = Fore.LIGHTGREEN_EX

# Developer Information
NAME = "RAGA SANDHIYA R"
ROLE = "Aspiring AI Engineer"
EDUCATION = "B.E. Computer Science & Engineering"
INTERESTS = "AI | ML | GenAI | Web Development"
LANGUAGES = "Python | Java | JavaScript"

# Random developer quotes
QUOTES = [
    "Keep learning. Keep building.",
    "Great things are built one line at a time.",
    "Code. Learn. Improve. Repeat.",
    "Stay curious. Stay creative.",
    "Your next idea could change everything."
]

# Random welcome messages
GREETINGS = [
    "Welcome back, developer!",
    "Ready to build something amazing?",
    "Another day, another opportunity to learn!",
    "Keep experimenting. Keep growing!"
]


# Typing animation
def type_text(text, delay=0.025, color=BRIGHT_GREEN):
    print(color, end="", flush=True)

    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)

    print(Style.RESET_ALL)


# Welcome banner
def display_banner():
    print(BRIGHT_GREEN + Style.BRIGHT)
    print("=" * 52)

    type_text(
        "          WELCOME TO DEVPERSONA",
        color=BRIGHT_GREEN + Style.BRIGHT
    )

    print("=" * 52)


# Developer profile
def display_profile():
    print(GREEN + Style.BRIGHT + "\n  DEVELOPER PROFILE")
    print(GREEN + "  " + "-" * 42)

    details = {
        "Name": NAME,
        "Role": ROLE,
        "Education": EDUCATION,
        "Interests": INTERESTS,
        "Languages": LANGUAGES
    }

    for key, value in details.items():
        print(
            BRIGHT_GREEN +
            f"  {key:<12}: {value}"
        )


# Footer with random messages and quotes
def display_footer():
    print(GREEN + "\n" + "=" * 52)

    print(
        BRIGHT_GREEN + Style.BRIGHT +
        "  " + random.choice(GREETINGS)
    )

    print(GREEN + "\n  Today's thought:")

    print(
        BRIGHT_GREEN +
        "  \"" + random.choice(QUOTES) + "\""
    )

    print(GREEN + "=" * 52)


# Main execution
def main():

    # Clear terminal screen
    os.system("cls" if os.name == "nt" else "clear")

    # Display welcome banner
    display_banner()

    # Initialization animation
    type_text(
        "\n  Initializing developer profile...",
        delay=0.04,
        color=BRIGHT_GREEN
    )

    time.sleep(0.5)

    # Display developer information
    display_profile()

    # Display random greeting and quote
    display_footer()

    # Closing message
    type_text(
        "\n  Thanks for visiting DevPersona!",
        color=BRIGHT_GREEN
    )


if __name__ == "__main__":
    main()
