
from midiutil.MidiFile import MIDIFile

# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)



# add some notes
channel = 0
volume = 100


instrument = 39   # Violin
mf.addProgramChange(track, channel, time, instrument)


pitch = 60           # C4 (middle C)
time = 0             # start on beat 0
duration = 3         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 64           # E4
time = 0             # start on beat 2
duration = 3        # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 67           # G4
time = 1            # start on beat 4
duration = 3        # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 59           # G4
time = 0            # start on beat 4
duration = 3        # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

# write it to disk
with open("output.wav", 'wb') as outf:
    mf.writeFile(outf)


class Note:
    def __init__(self, pitch, time, duration, volume):
        self.pitch = pitch
        self.time = time
        self.duration = duration
        self.volume = volume

    def addSelfToTrack(self, file: MIDIFile, track: int, channel: int):
        file.addNote(track, channel, self.pitch, self.time, self.duration, self.volume)

class InstrumentPlayer():
    def __init__(self, file: MIDIFile):
        self.notes = {}
        self.rootfile = file

    def addNote(self, track: int, channel: int, pitch, time, duration, volume):
        newNote = Note(pitch, time, duration, volume)
        newNote.addSelfToTrack(self.rootfile, track, channel)

    def PianoWrite(self):
        ...

class MAINNotes:
    ...

class IsaacisnotaPiano():
    ...





