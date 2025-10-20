import tkinter as tk
from threading import Thread
import time
from dayzbot import start_bot, stop_bot

class OverlayApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DayZ F-Bot")
        self.root.geometry("260x120+20+20")
        self.root.configure(bg="#1e1e1e")
        self.root.attributes("-topmost", True)
        self.root.wm_attributes("-alpha", 1.0)
        
        self.last_interaction = time.time()
        self.bot_thread = None

        self.label = tk.Label(self.root, text="Натисни Start", fg="white", bg="#1e1e1e", font=("Segoe UI", 10))
        self.label.pack(pady=10)

        self.button = tk.Button(
            self.root, text="▶ Start", command=self.toggle_bot,
            bg="#3a9ff5", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", width=10
        )
        self.button.pack(pady=5)

        self.root.bind_all("<Motion>", self.reset_timer)
        self.root.bind_all("<Key>", self.reset_timer)

        self.update_transparency()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_transparency(self):
        idle = time.time() - self.last_interaction
        if idle > 10:
            self.root.wm_attributes("-alpha", 0.25)
        else:
            self.root.wm_attributes("-alpha", 1.0)
        self.root.after(1000, self.update_transparency)

    def reset_timer(self, event=None):
        self.last_interaction = time.time()

    def update_status(self, text):
        self.label.config(text=text)

    def toggle_bot(self):
        self.reset_timer()
        if self.bot_thread is None or not self.bot_thread.is_alive():
            self.button.config(text="■ Stop", bg="#f54242")
            self.bot_thread = Thread(target=start_bot, args=(self.update_status,), daemon=True)
            self.bot_thread.start()
        else:
            stop_bot()
            self.button.config(text="▶ Start", bg="#3a9ff5")
            self.update_status("Бот зупинено.")

    def on_close(self):
        stop_bot()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = OverlayApp()
    app.run()