import RPi.GPIO as GPIO
import time

RADIOPIN = 3  # GPIO pin for RTTY transmission

# RTTY data and control variables
ASCII = 7  # Number of ASCII bits for each char
STOPBITS = 2  # Number of stop bits to send
TXDELAY = 2  # Number of seconds to delay between string transmissions
RTTY_BAUD = 300  # Baud rate to transmit at


def rtty_txbit(bit_value):
    GPIO.output(RADIOPIN, bit_value)
    time.sleep(1.0 / RTTY_BAUD)


def rtty_transmit_char(c):
    rtty_txbit(0)  # Start bit
    cc = ord(c)
    for _ in range(ASCII):
        if cc & 1:
            rtty_txbit(1)
        else:
            rtty_txbit(0)
        cc >>= 1
    rtty_txbit(1)  # Stop bit 1
    if STOPBITS == 2:
        rtty_txbit(1)  # Stop bit 2


def rtty_send_string(tx_str):
    for char in tx_str:
        rtty_transmit_char(char)
    time.sleep(TXDELAY)  # Delay after transmission


if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RADIOPIN, GPIO.OUT)
    GPIO.output(RADIOPIN, GPIO.LOW)  # Initial low

    while True:
        rtty_send_string("Hello World")
        time.sleep(0.5)
