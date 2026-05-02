import time

def countdown_timer():
    while True:
        try:
            print("Type 0 if you wish to quit.\n")
            seconds = int(input("Enter seconds: "))
        except ValueError:
            print("\nPlease enter an integer.")
            continue

        if seconds == 0:
            print("\nQuitting...")
            return
        elif seconds < 0:
            print("\nPlease enter a positive integer.")
            continue
        else:
            for i in range(seconds, 0, -1):
                print(f"Time left: {i} seconds", end="\r")
                time.sleep(1)
            print("\nTime's up!")

if __name__ == "__main__":
    print("=== Python Countdown Timer ===")
    countdown_timer()