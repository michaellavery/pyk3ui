"""Main TUI implementation for pyk3ui

Author: Michael Lavery  
Created: 
"""


import py_cui

__version__ = 'v0.0.1'

class Pyk3uiApp:

    def __init__(self, master):

        self.master = master
        self.master.add_label('Hello py_cui!!!', 1, 1)


def main():
    root = py_cui.PyCUI(3, 3)
    wrapper =  Pyk3uiApp(root)
    root.start()
