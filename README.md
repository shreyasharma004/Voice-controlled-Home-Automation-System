# Arduino Relay Control via Voice Commands (Python + Tkinter)

## Overview

This project enables you to control a relay connected to an Arduino board using simple Python commands via serial communication. The Python app sends voice-command-style strings (`*turn on light#` and `*turn off light#`) to the Arduino, which processes them to toggle the relay state accordingly.

A clean and user-friendly interface is provided using **Tkinter**, making it easy to turn your relay ON or OFF with just a button click.

---

## Features

- Configurable COM Port (default: `COM3`) for serial communication with Arduino.
- Sends custom commands (`*turn on light#` and `*turn off light#`) matching Arduino voice logic.
- Simple Tkinter-based GUI with ON/OFF buttons.
- Graceful cleanup: serial port is properly closed when the app exits.

---

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- `pyserial` package installed (install via `pip install pyserial`).
- Arduino IDE for uploading the sketch.
- Arduino board connected to your PC (ensure you know the correct COM port).

### Hardware Setup

- Connect a relay module to your Arduino (for example, on pin 13).
- Ensure the relay is powered and connected correctly.

---

## Setup & Usage

1. **Upload Arduino Sketch**

   Upload the provided Arduino sketch to your board. This sketch listens for serial commands and toggles the relay accordingly.

2. **Close Arduino Serial Monitor**

   Ensure the Arduino Serial Monitor is closed before running the Python app because only one application can access the COM port at a time.

3. **Configure COM Port**

   If your Arduino is not on `COM3`, update the `COM_PORT` variable in `main.py` accordingly.

4. **Run the Python App**

   ```bash
   python main.py
   
5. **Use the GUI**

   - Click Turn ON to send the command to turn the relay on.
   - Click Turn OFF to send the command to turn the relay off.
   - The relay connected to your Arduino should toggle accordingly.

6. **Exit**

   When closing the application window, the serial port will close cleanly.

---

## Troubleshooting

- **COM Port Not Found**  
  Check your system's Device Manager (Windows) or equivalent to confirm the correct COM port number assigned to your Arduino. Update the `COM_PORT` setting in the Python script accordingly.

- **Relay Not Switching**  
  Verify your wiring connections between the Arduino and the relay module. Also, ensure the Arduino sketch is correctly uploaded and that it is receiving and processing the serial commands as expected.

- **Port Access Error**  
  Ensure that no other application (such as the Arduino Serial Monitor) is currently accessing the COM port. Only one program can use the serial port at a time, so close any other programs before running the Python application.
