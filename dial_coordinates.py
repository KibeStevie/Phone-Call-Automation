import pyautogui
import time
import csv
from datetime import datetime
import os

# Configuration
LOG_FILE = "logs/dial_log.txt"
CSV_FILE = "contacts.csv"

def log(status, number, details=""):
    """Log dialing attempts with timestamp"""
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {status} - {number} {details}\n")

def dial_number(number):
    """
    Dial a phone number using hardcoded coordinates
    Coordinates are calibrated for 1920x1080 resolution
    """
    try:
        # Step 1: Click on the Phone tab in Phone Link (assuming it's not already open)
        pyautogui.click(360, 63)  # Adjust these coordinates for your UI
        time.sleep(2)
        
        # Step 2: Click on the dial pad button
        pyautogui.click(763, 152)  # Coordinates for dial pad button
        time.sleep(1)
        
        # Step 3: Clear any existing number and type the new number
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.5)
        pyautogui.typewrite(str(number), interval=0.05)
        time.sleep(1)

        # Step 4: Confirm the contact selection
        pyautogui.press("enter")  # Press Enter to select the contact
        time.sleep(2)  # Wait for dial screen to load
        
        # Step 5: Click the call button
        pyautogui.click(763, 719)  # Coordinates for call button
        time.sleep(3)
        
        # Step 6: Wait briefly, then hang up 
        pyautogui.click(871, 826)  # Same coordinates for hangup button
        time.sleep(1)
        
        log("SUCCESS", number)
        print(f"Called {number} successfully")
        
    except Exception as e:
        log("FAILED", number, str(e))
        print(f"Failed to call {number}: {e}")

def main():
    """Main function to process CSV file and dial numbers"""
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                number = row[0].strip()
                if not number.isdigit():
                    log("FAILED", number, "(Invalid number)")
                    print(f"Invalid number skipped: {number}")
                    continue
                
                print(f"Preparing to dial: {number}")
                dial_number(number)
                time.sleep(5)  # Wait between calls to avoid UI overload
                
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found. Please create the file with phone numbers.")
        log("ERROR", "N/A", f"CSV file {CSV_FILE} not found")

if __name__ == "__main__":
    print("Phone Link Dial Automation (Coordinate-Based)")
    print("Starting in 5 seconds...")
    time.sleep(5)
    main()