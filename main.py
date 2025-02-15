import sys
from command_executor import execute_command
from nlp_processor import interpret_command

def main():
    print("Welcome to AI Terminal Assistant.")

    while True:
        user_input = input(">> ")
        if user_input.lower() in ["exit, quit"]:
            print("Thanks for Using the Assistant")
            sys.exit(0)

        # Use NLP to interpret the command
        command = interpret_command(user_input)

        # Check if NLP returned an error
        if "Error in NLP processing" in command or not command.strip():
            print("Could not process command. Try rephrasing.")
            continue
        print(f"Executing: {command}")

        output = execute_command(command)
        print(output)

if __name__ == "__main__":
    main()

