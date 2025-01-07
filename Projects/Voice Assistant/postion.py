import pyautogui

# Get the current position of the cursor
while True:        
    x, y = pyautogui.position()

    print(f"Cursor Position: X = {x}, Y = {y}")
356,304