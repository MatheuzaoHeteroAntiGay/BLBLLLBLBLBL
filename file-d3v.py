# Import required modules
import time
import subprocess
import json

# Define the application package name
package_name = "com.shopee.international"

# Start the application
subprocess.call(["am", "start", "-n", package_name])

# Wait for the application to start
time.sleep(10)

# Check if the application is running
if subprocess.call(["dumpsys", "activity", "recents"]) != 0:
    print("Application not found")
    exit()

# Check if the user is logged in
if subprocess.call(["input", "text", "123456"]) != 0:
    print("User is not logged in")
    exit()

# Go to the cart page
subprocess.call(["input", "keyevent", "82"]) # Back button
subprocess.call(["input", "keyevent", "22"]) # Menu button
subprocess.call(["input", "text", "Carrinho"])
subprocess.call(["input", "keyevent", 66]) # Enter button

# Wait for 3 minutes
time.sleep(180)

# Click the Continue button
subprocess.call(["input", "keyevent", 21]) # Down button
subprocess.call(["input", "keyevent", 66]) # Enter button

# Wait for 30 seconds
time.sleep(30)

# Click the Payment Method button
subprocess.call(["input", "keyevent", 21]) # Down button
subprocess.call(["input", "keyevent", 66]) # Enter button

# Wait for 30 seconds
time.sleep(30)

# Load credit card information from a JSON file
with open("credit_cards.json") as f:
    cards = json.load(f)

# Loop through each credit card and input the information
for card in cards:
    # Input the card number
    subprocess.call(["input", "text", card["number"]])

    # Input the expiration date
    subprocess.call(["input", "text", card["expiration"]])

    # Input the CVV
    subprocess.call(["input", "text", card["cvv"]])

    # Input the cardholder name
    subprocess.call(["input", "text", card["name"]])

    # Input the data field
    subprocess.call(["input", "text", "1430"])

    # Input the complement field
    subprocess.call(["input", "text", "101"])

    # Click the Next button
    subprocess.call(["input", "keyevent", 66]) # Enter button

    # Wait for 30 seconds
    time.sleep(30)