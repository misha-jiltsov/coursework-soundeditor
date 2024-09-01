
#
# # the gui manager for the main program
# # will need to include all of the sections of the GUI
# import tkinter as tk
#
# class GUI_Manager:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Music Notes Editor")
#         self.root.geometry("800x600")
#
#         # Call the populate method to set up the GUI
#         self.populate()
#
#         self.root.mainloop()
#
#     def populate(self):
#         self.main_paned_window = tk.PanedWindow(self.root, orient=tk.HORIZONTAL, sashrelief="raised")
#         self.main_paned_window.pack(fill="both", expand=True)
#         self.left_paned_window = tk.PanedWindow(self.main_paned_window, orient=tk.VERTICAL, sashrelief="raised")
#         self.main_paned_window.add(self.left_paned_window, minsize=200)  # Default width for library
#         self.right_paned_window = tk.PanedWindow(self.main_paned_window, orient=tk.VERTICAL, sashrelief="raised")
#         self.main_paned_window.add(self.right_paned_window, minsize=600)  # Default width for right side
#
#
#         self.library_frame = tk.Frame(self.left_paned_window, bg="gray", bd=2, relief="solid")
#         self.note_options_frame = tk.Frame(self.right_paned_window, bg="darkgray", bd=2, relief="solid")
#         self.editor_frame = tk.Frame(self.right_paned_window, bg="gray", bd=2, relief="solid")
#         self.control_panel_frame = tk.Frame(self.right_paned_window, bg="darkgray", bd=2, relief="solid")
#
#         # Add the frames to the respective PanedWindows with minsize set for default sizes
#         self.left_paned_window.add(self.library_frame, minsize=400)  # Default height for library
#         self.right_paned_window.add(self.note_options_frame, minsize=100)  # Default height for note options
#         self.right_paned_window.add(self.editor_frame, minsize=350)  # Default height for editor
#         self.right_paned_window.add(self.control_panel_frame, minsize=100)  # Default height for control panel
#
#         self.library_label = tk.Label(self.library_frame, text="Notes and sounds library", bg="gray")
#         self.library_label.place(relx=0.5, rely=0.5, anchor="center")
#         self.note_options_label = tk.Label(self.note_options_frame, text="Note options - reverb, volume", bg="darkgray")
#         self.note_options_label.place(relx=0.5, rely=0.5, anchor="center")
#         self.editor_label = tk.Label(self.editor_frame, text="Music Notes Editor", bg="gray", font=("Arial", 18))
#         self.editor_label.place(relx=0.5, rely=0.5, anchor="center")
#         self.control_panel_label = tk.Label(self.control_panel_frame, text="Control Panel - Play, Pause etc.", bg="darkgray")
#         self.control_panel_label.place(relx=0.5, rely=0.5, anchor="center")
#
#
# # Create the main application window
# class MusicGrid:
#     def __init__(self):
#         self.tracks = []
#
#
#
#
#
# thing = GUI_Manager()
#

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSplitter, QLabel, QTreeView, QFileSystemModel
from PyQt5.QtCore import Qt

class MusicNotesEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Music Notes Editor')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.horizontal_splitter = QSplitter(Qt.Horizontal)



        self.file_system_view = QTreeView()
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath('')


        self.vertical_splitter_left = QSplitter(Qt.Vertical)

        self.sounds_folder = './sounds'
        self.file_system_view.setModel(self.file_system_model)
        self.file_system_view.setRootIndex(self.file_system_model.index(self.sounds_folder))
        self.file_system_view.setStyleSheet("background-color: lightgray; border: 1px solid black;")
        self.file_system_view.setColumnWidth(0, 250)


        self.notes_selector = QLabel('Notes', self)
        self.notes_selector.setStyleSheet("background-color: gray; border: 1px solid black;")
        self.notes_selector.setAlignment(Qt.AlignCenter)



        self.vertical_splitter_right = QSplitter(Qt.Vertical)



        self.music_notes_editor = QLabel('Track Editor', self)
        self.music_notes_editor.setStyleSheet("background-color: gray; border: 1px solid black;")
        self.music_notes_editor.setAlignment(Qt.AlignCenter)

        self.note_options = QLabel('Note options - reverb, volume + Other Controls (Play, Pause, Record)', self)
        self.note_options.setStyleSheet("background-color: lightgray; border: 1px solid black;")
        self.note_options.setAlignment(Qt.AlignCenter)

        self.tracks_panel = QLabel('Tracks View', self)
        self.tracks_panel.setStyleSheet("background-color: lightgray; border: 1px solid black;")
        self.tracks_panel.setAlignment(Qt.AlignCenter)




        self.vertical_splitter_right.addWidget(self.note_options)
        self.vertical_splitter_right.addWidget(self.music_notes_editor)
        self.vertical_splitter_right.addWidget(self.tracks_panel)



        self.vertical_splitter_left.addWidget(self.file_system_view)
        self.vertical_splitter_left.addWidget(self.notes_selector)


        self.horizontal_splitter.addWidget(self.vertical_splitter_left)
        self.horizontal_splitter.addWidget(self.vertical_splitter_right)


        self.main_layout.addWidget(self.horizontal_splitter)


        self.file_system_view.setMinimumWidth(150)
        self.note_options.setMinimumHeight(50)
        self.tracks_panel.setMinimumHeight(50)
        self.music_notes_editor.setMinimumHeight(150)


        self.horizontal_splitter.setSizes([250, 550])
        self.vertical_splitter_right.setSizes([100, 400, 100])

        self.setGeometry(100, 100, 800, 600)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MusicNotesEditor()
    ex.show()
    sys.exit(app.exec_())

