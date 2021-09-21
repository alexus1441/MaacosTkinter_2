import tkinter as tk
window = tk.Tk()

sveiciens = tk.Label(text = "datoriku maacos")

sveiciens.pack()
button = tk.Button(
  text="Nospied!",
  width=25,
  height=5,
  bg="violet",
  fg="dark green",
)
button.pack()
window.mainloop()
