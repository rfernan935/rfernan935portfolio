# IR-Controlled 7-Segment Display
This project lights up the correct digit based on the number button pressed, using an Arduino Uno and an IR remote to control a 7-segment display.

## Highlights
- Displays digits 0–9 on a 7-segment display using an IR remote
- Accurate decoding of remote signals via hex code mapping
- Room to expand for additional functions or multi-digit displays

## Key Features and How They Work
When a number key (0–9) is pressed on the IR remote, the receiver module detects the signal and passes it to the Arduino. The code matches the received IR signal to a predefined hexadecimal code, and then updates the 7-segment display to show the corresponding number.
- The *IRremote* library was utilized to read input from the remote.
- The *SevSeg* library was utilized to control the 7-segment display.
- Each IR signal was mapped to a digit using a switch statement in the code.

### Example Behavior
- Press **1** on the remote, then the display shows **1**
- Press **5** on the remote, then the display shows **5**
- And so on for all digits 0–9

## Learning Phase
Before writing the final code, I wrote a different code to read the raw hexadecimal values sent by each button on the IR remote. I used the values I determined this way to allow me to map each button to the correct hex code in the switch block of the final program.

## Circuit Setup

### Components

- Arduino Uno
- IR receiver (connected to digital pin 12)
- Common cathode 7-segment display
- 8 jumper wires (one for each segment: A–G + decimal point)
- 8 current-limiting resistors (220Ω recommended)
- Breadboard and jumper wires
- USB cable for programming
- 9V battery with on/off toggle case

### Wiring

- Segment pins on the 7-segment display were connected to digital pins 2 through 9 on the Arduino.
- The common cathode pin was connected to GND.
- Each segment had a current-limiting resistor.
- The IR receiver was connected to 5V, GND, and digital pin 12 (for data).
- Built-in LED blinking feedback was enabled to visually confirm IR signal reception.

## Libraries Used

- [IRremote](https://github.com/Arduino-IRremote/Arduino-IRremote): For receiving and decoding IR signals.
- [SevSeg](https://github.com/DeanIsMe/SevSeg): For driving the 7-segment display.

## Future Improvements
- Add more remote button mappings for additional features
- Expand to multiple digits using display multiplexing

***Click [here](https://github.com/rfernan935/rfernan935portfolio/blob/main/Coding%20Projects/Arduino%20IDE/IRremote-7SegDisplay/IRremote-7SegDisplay-InAction.gif) to view it in action.***
