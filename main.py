import serial
import tkinter as tk
from tkinter import ttk, messagebox

# Try to connect to Arduino
try:
    arduino = serial.Serial('COM3', 9600)  # Update COM port if needed
except serial.SerialException:
    messagebox.showerror("Connection Error", "Could not connect to Arduino.\nCheck USB and COM port.")
    exit()

# Send commands
def send_command(cmd):
    try:
        command = f"*{cmd}#"
        arduino.write(command.encode())
        print(f"Sent: {command}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send command:\n{e}")

# Setup GUI
root = tk.Tk()
root.title("Smart Relay Control")
root.geometry("360x300")
root.configure(bg="#1e1e2e")

# Button styling
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton",
                font=("Segoe UI", 12),
                padding=10,
                background="#44475a",
                foreground="#f8f8f2")
style.map("TButton",
          background=[("active", "#6272a4")],
          foreground=[("active", "#ffffff")])

# Title
title = tk.Label(root, text="🔌 Smart Relay Control", font=("Segoe UI", 18, "bold"),
                 fg="#f8f8f2", bg="#1e1e2e")
title.pack(pady=20)

# Buttons
ttk.Button(root, text="Turn ON Light",
           command=lambda: send_command("turn on light")).pack(pady=10)

ttk.Button(root, text="Turn OFF Light",
           command=lambda: send_command("turn off light")).pack(pady=10)

ttk.Button(root, text="Exit",
           command=lambda: (arduino.close(), root.destroy())).pack(pady=30)

# Fade-in animation
alpha = 0.0
def fade():
    global alpha
    alpha += 0.01
    if alpha <= 1:
        root.attributes("-alpha", alpha)
        root.after(20, fade)

root.attributes("-alpha", 0.0)
fade()

root.mainloop()
