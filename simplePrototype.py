


import tkinter as tk
from midiutil.MidiFile import MIDIFile





class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.allNotes = []


        self.instruments = {}
        self.getAllInstruments()
        self.populate()

        self.root.mainloop()

    def getAllInstruments(self):
        with open("INSTRUMENTS.txt", "r") as file:
            for line in file.readlines():
                splitline = line.split("\t")
                self.instruments[splitline[0].strip()] = int(splitline[1].strip())

    def addNote(self):
        notesValues = [inputbox.get() for inputbox in self.inputs.values()]

        instrument = self.instruments[self.selectedintrument.get()]

        newNote = Note(*notesValues, instrument)

        self.allNotes.append(newNote)
        newNoteDisplay = tk.Label(self.root, text = str(list(zip(self.inputs.keys(), notesValues))) + str(instrument))
        newNoteDisplay.grid(column = 3, row = len(self.allNotes))
        print(list(zip(self.inputs.keys(), notesValues)), instrument)

        self.root.update()

    def populate(self):

        self.controlframe = tk.Frame(self.root)
        self.controlframe.grid(column = 0, row = 0)
        #controls

        # self.volume_label = tk.Label(self.root, text="Volume:")
        # self.channel_label = tk.Label(self.root, text="Channel:")
        # self.time_label = tk.Label(self.root, text="Time:")
        # self.pitch_label = tk.Label(self.root, text="Pitch:")
        # self.duration_label = tk.Label(self.root, text="Duration:")
        # self.instrument_label = tk.Label(self.root, text="Instrument:")
        #
        # self.volume_input = tk.Entry(self.root)
        # self.channel_input = tk.Entry(self.root)
        # self.time_input = tk.Entry(self.root)
        # self.pitch_input = tk.Entry(self.root)
        # self.duration_input = tk.Entry(self.root)
        # self.instrument_input = tk.Entry(self.root)
        #
        # self.volume_label.grid(column = 0, row = 0)
        # self.channel_label.grid(column = 0, row = 1)
        # self.time_label.grid(column = 0, row = 2)
        # self.pitch_label.grid(column = 0, row = 3)
        # self.duration_label.grid(column = 0, row = 4)
        # self.instrument_label.grid(column = 0, row = 5)
        #
        # self.volume_input.grid(column = 1, row = 0)
        # self.channel_input.grid(column = 1, row = 1)
        # self.time_input.grid(column = 1, row = 2)
        # self.pitch_input.grid(column = 1, row = 3)
        # self.duration_input.grid(column = 1, row = 4)
        # self.instrument_input.grid(column = 1, row = 5)

        ######### SMARTER WAY OF DOING IT ############

        labels = ["Volume:", "Channel:", "Time:", "Pitch:", "Duration:"]
        self.inputs = {}

        for i, label_text in enumerate(labels):
            label = tk.Label(self.controlframe, text=label_text)
            entry = tk.Entry(self.controlframe)

            label.grid(column=0, row=i)
            entry.grid(column=1, row=i)

            # Store references to entries in a dictionary if needed
            self.inputs[label_text[:-1].lower()] = entry


        self.instlabel =  tk.Label(self.controlframe, text="Instrument: ")
        self.instlabel.grid(column=0, row=5)

        self.selectedintrument = tk.StringVar()
        self.selectedintrument.set("Acoustic Grand Piano")
        self.instrumentinput = tk.OptionMenu(self.controlframe, self.selectedintrument, *self.instruments.keys())
        self.instrumentinput.grid(column = 1, row = 5)

        self.notesdisplayframe = tk.Frame(self.controlframe, borderwidth=3)
        self.notesdisplayframe.grid(column=2, row=0)

        self.addnoteButton = tk.Button(self.controlframe, text="Add Note", command= lambda: self.addNote())
        self.exportbutton = tk.Button(self.controlframe, text="Export to file")

        self.addnoteButton.grid(column = 0, row = 6)
        self.exportbutton.grid(column = 0, row = 7)

    def exportall(self):
        newFile = MIDIFile(1)  # only 1 track
        track = 0

        for notes in self.allNotes:
            ...



class Note:
    def __init__(self, volume, channel, time, pitch, duration, instrument):
        self.pitch = pitch
        self.time = time
        self.duration = duration
        self.volume = volume
        self.channel = channel
        self.instrument = instrument

    def addSelfToTrack(self, file: MIDIFile, track: int):
        file.addNote(track, self.channel, self.pitch, self.time, self.duration, self.volume)


main = Main()