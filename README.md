Companion repository for RSGB 2025 Annual Convention presentation Making Connections with DIY Amateur Radio Software
--

To install the requirements/libraries in a new virtual environment execute the following commands:
```
python3 -m venv rsgb
source rsgb/bin/activate
pip3 install -r requirements.txt
```

When you are finished with your virtual environment, you can deactivate it using the following command: `deactivate` if you want to come back and use it again, you can reenable the virtual environment using `source rsgb/bin/activate`

### Slide 4: Let's Get Started
- helloworld.py
- helloflask.py
- browser.py
- withRequests.py

### Slide 7: Lets do something useful
- rotateflask.py

### Slide 11: Utilising supplied binaries
- flirc.py

### Slide 12: Controlling IC-9700 via serial port
- https://github.com/stevendodd/pycom

### Slide 13: HID Compliant USB Devices
- https://github.com/stevendodd/RC28Server

### Slide 14: Programming with GPIO
- rtty.py
- https://github.com/stevendodd/naki

### Slide 18: Hamlib rigctl python client
- rigctl.py

### Slide 20: Hamlib rotctld server in Python
- https://github.com/stevendodd/rotctlpy/blob/main/rotator.py#L92

### Slide 22: Json based website APIs
- <a href="./hamsat.py">hamsat.py</a>  (requires you to add your hamsat token in a seperate file hamsat.token)

### Slide 23: Callsign look up
- hamqth.py  (requires you to add your hamqth password in a seperate file hamsat.password)

### Extra
- qrz.py  download your QRZ log file using API (requires you to add your QRZ token in a separate file qrz.token)
