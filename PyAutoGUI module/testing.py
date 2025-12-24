import tkinter as tk
from tkinter import messagebox
import time
import threading
import pyautogui as p

class PhoneMessengerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Number Messenger")
        
        # Variables
        self.phone_numbers = tk.StringVar()
        self.message = tk.StringVar()
        self.interval = tk.IntVar(value=1)  # Default interval of 1 second
        
        # Create widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Phone numbers label and text area
        tk.Label(self.root, text="Phone Numbers (one per line):").pack(pady=(10, 0))
        self.phone_text = tk.Text(self.root, height=10, width=40)
        self.phone_text.pack(padx=10, pady=5)
        
        # Message label and entry
        tk.Label(self.root, text="Message:").pack()
        self.message_entry = tk.Entry(self.root, textvariable=self.message, width=50)
        self.message_entry.pack(padx=10, pady=5)
        
        # Interval label and spinbox
        tk.Label(self.root, text="Interval (seconds):").pack()
        self.interval_spin = tk.Spinbox(
            self.root, from_=1, to=60, textvariable=self.interval, width=5
        )
        self.interval_spin.pack(pady=5)
        
        # Submit button
        self.submit_btn = tk.Button(
            self.root, text="Submit", command=self.on_submit, bg="#4CAF50", fg="white"
        )
        self.submit_btn.pack(pady=10, ipadx=10, ipady=5)
        
        # Status label
        self.status_label = tk.Label(self.root, text="", fg="blue")
        self.status_label.pack(pady=5)
        
    def on_submit(self):
        # Get the input values
        phone_numbers = self.phone_text.get("1.0", tk.END).strip().split('\n')
        message = self.message.get().strip()
        interval = self.interval.get()
        
        # Validate inputs
        if not phone_numbers or not all(phone_numbers):
            messagebox.showerror("Error", "Please enter at least one phone number")
            return
            
        if not message:
            messagebox.showerror("Error", "Please enter a message")
            return
            
        if interval <= 0:
            messagebox.showerror("Error", "Interval must be at least 1 second")
            return
        
        # Disable submit button during sending
        self.submit_btn.config(state=tk.DISABLED, bg="gray")
        self.status_label.config(text="Preparing to send messages...")
        
        # Start sending in a separate thread to keep UI responsive
        threading.Thread(
            target=self.send_messages,
            args=(phone_numbers, message, interval),
            daemon=True
        ).start()
        
    def send_messages(self, phone_numbers, message, interval):
        """Simulate sending messages with delay"""
        try:
            for i, number in enumerate(phone_numbers, 1):
                if not number.strip():
                    continue

                print(number)
                # Update status in the UI thread
                self.root.after(0, self.update_status, 
                              f"Sending to {number} ({i}/{len(phone_numbers)})")
                
                # Here you would actually send the message
                # For this example, we'll just simulate it
                print(f"Sending to {number}: {message}")

                # pyautogui to send the msg
                whatsapp_windows = p.getWindowsWithTitle("WhatsApp")
                if not whatsapp_windows:
                    print("WhatsApp window not found! Open WhatsApp first.")
                    exit()

                window = whatsapp_windows[0]
                window.restore()  # Un-minimize if needed
                window.activate()
                time.sleep(0.5)  # Wait for window to focus

                left, top, width, height = window.left, window.top, window.width, window.height

                click_x = left + (width // 2)  # Center horizontally
                click_y = top + 30  # 30 pixels below the top (adjust as needed)

                # 4. Move and click
                p.moveTo(click_x, click_y, duration=0.5)  # Smooth movement (optional)
                p.click()
                print(f"Clicked at: ({click_x}, {click_y})")
                
                p.keyDown("ctrl")
                p.keyDown("n")

                time.sleep(1)
                p.keyUp("ctrl")
                p.keyUp("n")

                p.write(number)

                time.sleep(3)
                logo_position = p.locateOnScreen('search.png')

                print("Searching for logo")
                if logo_position:
                    print(f"Logo found at position: {logo_position}")
                    p.moveTo(logo_position.left + 25, logo_position.top + 75)
                    p.click(button="left")
                else:
                    print("Logo not found")

                print("Found it!")
                
                time.sleep(3)
                p.write(message, interval = 0.2)

                print("Done typing")
                time.sleep(2)
                p.press("enter")

                print("Sent")

                # Wait for the specified interval (except after last message)
                if i < len(phone_numbers):
                    time.sleep(interval)
                    
            # When done
            self.root.after(0, self.sending_complete)
            
        except Exception as e:
            self.root.after(0, self.sending_error, str(e))
            
    def update_status(self, text):
        self.status_label.config(text=text)
        
    def sending_complete(self):
        messagebox.showinfo("Success", "All messages sent successfully!")
        self.status_label.config(text="All messages sent successfully!", fg="green")
        self.submit_btn.config(state=tk.NORMAL, bg="#4CAF50")
        
    def sending_error(self, error):
        messagebox.showerror("Error", f"An error occurred: {error}")
        self.status_label.config(text=f"Error: {error}", fg="red")
        self.submit_btn.config(state=tk.NORMAL, bg="#4CAF50")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneMessengerApp(root)
    root.mainloop()
