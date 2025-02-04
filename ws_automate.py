import pyautogui
import time
import sys
import random
from colorama import Fore, Style

from colorama import init
init(autoreset=True)

# Constants
NUMBER_OF_TASKS = int(sys.argv[1])
MIN_OF_RANGE = int(sys.argv[2])
MAX_OF_RANGE = int(sys.argv[3])
TASK_TYPE = sys.argv[4]

# Helper Function: Map task type to binary values
def map_to_binary(data):
    return [0 if item == "POI" else 1 for item in data]

# Generate random wait times
random_secs_UKM = [random.randint(MIN_OF_RANGE, MAX_OF_RANGE) for _ in range(50)]
random_secs_POI = [random.randint(MIN_OF_RANGE, MAX_OF_RANGE) for _ in range(50)]

# Create binary mapping based on the number of tasks
data = [TASK_TYPE] * NUMBER_OF_TASKS
poi_ukm_ = map_to_binary(data)

# Main Function
def main():
    total_amount = len(poi_ukm_)
    print(f"\n{Fore.CYAN}Total Tasks: {total_amount}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Starting in 5 seconds! Please click on the first cell of the loop.{Style.RESET_ALL}")
    time.sleep(5)

    for i, poi_value in enumerate(poi_ukm_):
        pyautogui.typewrite("true")

        # Press 'right' key based on poi_value
        for _ in range(3 if poi_value == 1 else 2):
            pyautogui.press("right")
            time.sleep(0.5)

        # Determine the task type and delay time
        if poi_value == 1:
            task_type = "MAP DATA"
            r_value = random.choice(random_secs_UKM)
        else:
            task_type = "POI"
            r_value = random.choice(random_secs_POI)

        # Enhanced Countdown with Visual Effects
        for j in reversed(range(r_value)):
            print("\n" + "=" * 50)  # Decorative border
            print(
                f"{Fore.LIGHTCYAN_EX}TASK {i + 1}/{total_amount} - {task_type}{Style.RESET_ALL}\n"
                f"{Fore.GREEN}COUNTDOWN: {j + 1} SECONDS REMAINING!{Style.RESET_ALL}\n"
                f"{Fore.YELLOW}TN: {i + 1} | TA: {total_amount}{Style.RESET_ALL}"
            )
            print("=" * 50)  # Decorative border
            time.sleep(1)

        pyautogui.typewrite("true")
        pyautogui.press("down")

        # Press 'left' key based on poi_value
        for _ in range(3 if poi_value == 1 else 2):
            pyautogui.press("left")
            time.sleep(0.5)

        print(f"{Fore.LIGHTGREEN_EX}{i + 1} tasks completed! {total_amount - (i + 1)} remaining...{Style.RESET_ALL}")

    print(f"{Fore.LIGHTMAGENTA_EX}All tasks completed!{Style.RESET_ALL}")

# Entry point
if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}. Please ensure valid input values for tasks and ranges.")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")
