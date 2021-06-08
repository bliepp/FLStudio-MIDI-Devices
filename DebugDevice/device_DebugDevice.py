# name=DebugDevice

def OnMidiMsg(event): # debug
    print()
    print("Channel:", event.midiChan, "Port:", event.port)
    print("MIDI Data:", event.midiId, event.data1, event.data2)