import datetime

# Define the file to store the logs
log_file = "input_log.txt"

def log_input(user_input):
    """Appends user input to the log file with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {user_input}\n")

def main():
    print("Input Logger Started. Type 'exit' to stop.")
    while True:
        user_input = input(">> ")
        if user_input.lower() == 'exit':
            print("Exiting logger.")
            break
        log_input(user_input)

if __name__ == "__main__":
    main()
