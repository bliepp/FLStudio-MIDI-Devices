# name=Alesis V Series

import transport
import device


current_mode = None

# factory layout
PAD = [ # factory drum pad layout
    49, 41, 42, 46,
    36, 37, 38, 39,
]


class Mode():
    def __init__(self):
        print("Entering ", self.__class__.__name__)
        self.padsChan = 9
        self.lights_off()
        self.set_lights()
    
    def lights_off(self):
        if device.isAssigned():
            for i in range(7):
                device.midiOutMsg(128, 9, PAD[i], 0)

    def set_lights(self):
        pass
        
    def OnNoteOn(self, event):
        # adjusting velocity curve to make response more aggressive
        event.velocity = int((event.velocity*127)**0.5)
    
    def OnNoteOff(self, event):
        pass


class TransportMode(Mode):
    def __init__(self):
        super().__init__()
        self.map = {
            # default values of first pad row
            PAD[0]: transport.setLoopMode,  # pattern/song mode
            PAD[1]: transport.start,        # play/pause
            PAD[2]: transport.stop,         # stop
            PAD[3]: transport.record,       # recording
        }
    
    def set_lights(self):
        if device.isAssigned():
            if transport.getLoopMode():
                device.midiOutMsg(144, 9, PAD[0], 127)
            else:
                device.midiOutMsg(128, 9, PAD[0], 0)
            
            if transport.isPlaying():
                device.midiOutMsg(144, 9, PAD[1], 127)
            else:
                device.midiOutMsg(128, 9, PAD[1], 0)
            
            if transport.isRecording():
                device.midiOutMsg(144, 9, PAD[3], 127)
            else:
                device.midiOutMsg(128, 9, PAD[3], 0)

    def OnNoteOn(self, event):
        if event.midiChan == self.padsChan:
            trigger = self.map.get(event.data1, lambda:None)
            if event.data2 > 0:
                trigger()
            event.handled = True
        else: super().OnNoteOn(event)
    
    def OnNoteOff(self, event):
        if event.midiChan == self.padsChan:
            self.set_lights() # needed, because note off may trigger leds to turn off
            event.handled = True
        else: super().OnNoteOff(event)


class FPCMode(Mode):
    def __init__(self):
        super().__init__()
        self.map = {
            PAD[0]: 49, PAD[1]: 42, PAD[2]: 44, PAD[3]: 46,
            PAD[4]: 36, PAD[5]: 38, PAD[6]: 40, PAD[7]: 37, 
        }

    def OnNoteOn(self, event):
        if event.midiChan == self.padsChan:
            event.data1 = self.map[event.data1]
        else: super().OnNoteOn(event)
    
    def OnNoteOff(self, event):
        if event.midiChan == self.padsChan:
            event.data1 = self.map[event.data1]
        else: super().OnNoteOff(event)


class DeactivatedMode(Mode):
    def __init__(self):
        super().__init__()

    def OnNoteOn(self, event):
        if event.midiChan == self.padsChan:
            event.handled = True # ignore pads
        else: super().OnNoteOn(event)
    
    def OnNoteOn(self, event):
        if event.midiChan == self.padsChan:
            event.handled = True # ignore pads
        else: super().OnNoteOff(event)


modes = { # map buttons to modes
    48: TransportMode,
    49: FPCMode,
    50: DeactivatedMode,
}


# built-in functions
def OnInit():
    global current_mode
    device_assigned = device.isAssigned()
    print("Output device assigned. Everything should work fine."*device_assigned
        + "Not output device assigned. LEDs might not work. "
            "Set input and output device to same port."*(not device_assigned))
    current_mode = TransportMode()

def OnRefresh(flags):
    current_mode.set_lights()

def OnNoteOn(event):
    current_mode.OnNoteOn(event)
def OnNoteOff(event):
    current_mode.OnNoteOff(event)


def OnControlChange(event):
    # setting button led unfortunately does not work.
    global current_mode

    event.handled = False
    next_mode = modes.get(event.data1, False)
    if next_mode and event.data2 == 127:
        current_mode = next_mode()
    event.handled = bool(next_mode) # maybe "or event.handled" needed