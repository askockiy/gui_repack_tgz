import tempfile
import shutil
import tkinter as tk
from tkinter import filedialog


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Repack .tar.gz to .tar.gz')
        self.geometry('500x75')

        self.label = tk.Label(self, text='Chose .tar.gz archive')
        self.label.pack()

        self.open_button = tk.Button(self, text='Open', command=self.convert)
        self.exit_button = tk.Button(self, text='Exit', command=self.exit)
        self.open_button.pack(padx=15)
        self.exit_button.pack(padx=15)

    def convert(self):
        fin = filedialog.askopenfilename(title='Select *.tar.gz archive', filetypes=[('name', '*.tar.gz')])
        if fin:
            with tempfile.TemporaryDirectory() as tempdir:
                shutil.unpack_archive(fin, extract_dir=tempdir)
                self.label.config(text=f'File unpacked to {tempdir}')
                fout = filedialog.asksaveasfilename(title='Save as new_name archive', defaultextension="", filetypes=[('new_name', '*.tar.gz')])
                if fout:
                    shutil.make_archive(fout, 'gztar', tempdir)
                    self.label.config(text=f'File saved as {fout}.tar.gz')

    def exit(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
