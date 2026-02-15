import tkinter as tk
from tkinter import ttk, messagebox
from ml_service.model import HeartFailureModel
from ml_service.preprocessor import preprocess
from utils.validation import validate


class HeartApp:

    def __init__(self):

        self.model = HeartFailureModel()

        self.root = tk.Tk()
        self.root.title("Heart Disease Predictor")
        self.root.geometry("420x650")

        self.entries = {}

        fields = [
            ("Age", tk.Entry),
            ("Sex", ["M","F"]),
            ("ChestPainType", ["TA","ATA","NAP","ASY"]),
            ("RestingBP", tk.Entry),
            ("Cholesterol", tk.Entry),
            ("FastingBS", ["0","1"]),
            ("RestingECG", ["Normal","ST","HVI"]),
            ("MaxHR", tk.Entry),
            ("ExerciseAngina", ["Y","N"]),
            ("Oldpeak", tk.Entry),
            ("ST_Slope", ["Up","Flat","Down"])
        ]

        for label, widget in fields:

            tk.Label(self.root, text=label).pack()

            if widget == tk.Entry:
                e = tk.Entry(self.root)
                e.pack()
            else:
                e = ttk.Combobox(self.root, values=widget, state="readonly")
                e.pack()

            self.entries[label] = e

        tk.Button(self.root, text="PREDECIR", command=self.predict).pack(pady=15)

        self.result = tk.Label(self.root, text="", font=("Arial", 12))
        self.result.pack()

        self.root.mainloop()

    def predict(self):

        data = {k:v.get() for k,v in self.entries.items()}

        valid, error = validate(data)
        if not valid:
            messagebox.showerror("Error", error)
            return

        # convertir numéricos
        numeric = ["Age","RestingBP","Cholesterol","MaxHR","Oldpeak","FastingBS"]

        for n in numeric:
            data[n] = float(data[n])

        df = preprocess(data)

        pred, prob = self.model.predict(df)

        txt = "ENFERMEDAD CARDIACA" if pred == 1 else "CORAZÓN NORMAL"

        self.result.config(
            text=f"{txt}\nProbabilidad: {round(prob*100,2)}%"
        )
