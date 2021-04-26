from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("OTConverter")
    window.minsize(300, 200)

    ui = UI(window)
    ui.start()

    window.mainloop()

if __name__ == '__main__':
    main()