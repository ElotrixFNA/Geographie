import tkinter as tk
from tkinter import filedialog, Text, ttk

class SQLFileEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("SQL File Editor")
        self.root.geometry("500x500")
        self.uploadimg = tk.PhotoImage(file="upload.png")
        self.downloadimg = tk.PhotoImage(file="download.png")  

        root.configure(background='#eeeeee')   

        self.label = tk.Label(root, text="Würth Phoenix", width=5000, height=2, background="#df4851",font=("Wuerth Global", 25))   
        self.label.pack()
        
        self.label = tk.Label(root, text="SQL File Editor", font=("Helvetica", 16), width=5000, background="#df4851")
        self.label.pack()
        
        self.upload_button = tk.Button(root, image= self.uploadimg , width= 75, height= 75, command=self.upload, cursor="hand2")
        self.upload_button["bg"] = "#eeeeee"
        self.upload_button["border"] = "0"
        self.upload_button.pack(side="top", pady=15)
        self.label = tk.Label(root, text="Upload SQL-File", font=("Helvetica", 12))
        self.label.pack(pady=5)
        
        self.text = Text(root, height=23, width=90, state=tk.DISABLED, border="0")
        self.text.pack(pady=10)
        
        self.upload_button = tk.Button(root, image= self.downloadimg , width= 75, height= 75, command=self.save, state=tk.DISABLED, cursor="hand2")
        self.upload_button["bg"] = "#eeeeee"
        self.upload_button.pack(pady=15)
        self.upload_button["border"] = "0"
        self.upload_button.pack(side="top")
        self.label = tk.Label(root, text="Save edited SQL-File", font=("Helvetica", 12))
        self.label.pack(pady=5)
        
    def upload(self):
        file_path = filedialog.askopenfilename(filetypes=[("SQL Files", "*.sql")])
        with open(file_path, "r") as file:
            self.sql_file = file.read()
        self.text.config(state=tk.NORMAL)
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", self.sql_file)
        self.save_button.config(state=tk.NORMAL)
        
    def save(self):
        file_path = filedialog.asksaveasfilename(filetypes=[("SQL Files", "*.sql")])
        self.sql_file = self.text.get("1.0", tk.END)
        with open(file_path, "w") as file:
            file.write(self.sql_file)

if __name__ == "__main__":
    root = tk.Tk()
    app = SQLFileEditor(root)
    root.mainloop()
