import pyautogui
import time
import csv
from datetime import datetime
import os

# Configuration
LOG_FILE = "logs/dial_log.txt"
CSV_FILE = "contacts.csv"
SCREENSHOTS_DIR = "screenshots"

def log(status, number, details=""):
    """Log dialing attempts with timestamp"""
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {status} - {number} {details}\n")

def find_and_click_element(element_name, confidence=0.8, timeout=10):
    """
    Find and click UI element using screenshot
    Requires OpenCV for confidence parameter (install with: pip install opencv-python)
    """
    screenshot_path = os.path.join(SCREENSHOTS_DIR, f"{element_name}.png")
    
    if not os.path.exists(screenshot_path):
        raise FileNotFoundError(f"Screenshot not found: {screenshot_path}")
    
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            location = pyautogui.locateOnScreen(screenshot_path, confidence=confidence)
            if location:
                center_x, center_y = pyautogui.center(location)
                pyautogui.click(center_x, center_y)
                return True
        except pyautogui.ImageNotFoundException:
            pass
        except Exception as e:
            print(f"Error finding {element_name}: {str(e)}")
        
        time.sleep(1)
    
    raise Exception(f"Could not find {element_name} after {timeout} seconds")

def dial_number(number):
    """
    Dial a phone number using screenshot-based automation
    More robust across different screen resolutions
    """
    try:
        # Step 1: Click on Phone tab (if needed)
        find_and_click_element("phone_tab")
        time.sleep(2)
        
        # Step 2: Click on dial pad button
        find_and_click_element("dial_button")
        time.sleep(1)
        
        # Step 3: Clear existing number and type new number
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.5)
        pyautogui.typewrite(str(number), interval=0.05)
        time.sleep(1)

        # Step 4: Confirm the contact selection
        pyautogui.press("enter")  # Press Enter to select the contact
        time.sleep(2)  # Wait for dial screen to load
        
        # Step 5: Click call button
        find_and_click_element("call_button")
        time.sleep(3)
        
        # Auto hangup after 3 seconds
        find_and_click_element("hangup_button")
        time.sleep(3)
        
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
                time.sleep(5)  # Wait between calls
                
    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found. Please create the file with phone numbers.")
        log("ERROR", "N/A", f"CSV file {CSV_FILE} not found")

if __name__ == "__main__":
    print("Phone Link Dial Automation (Screenshot-Based)")
    print("Starting in 5 seconds...")
    time.sleep(5)
    main()