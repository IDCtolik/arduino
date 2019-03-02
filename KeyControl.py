import pyHook
import pythoncom
import serial


#react only to keys 0-9
TRIGGER_KEYS = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
hm = pyHook.HookManager()
ser = serial.Serial('COM3', 9600)

#this defines the behaviour of what to do when recognizing a key pressed
def _on_key_press(event):
	global ser
	global TRIGGER_KEYS
	if event.Ascii in TRIGGER_KEYS:
		ser.write(b'1')
	return True

#keyhook setup
hm.KeyDown = _on_key_press
hm.HookKeyboard()
pythoncom.PumpMessages()
