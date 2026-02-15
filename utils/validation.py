FIELDS = [
    "Age","Sex","ChestPainType","RestingBP","Cholesterol",
    "FastingBS","RestingECG","MaxHR",
    "ExerciseAngina","Oldpeak","ST_Slope"
]

def validate(data):

    for f in FIELDS:
        if f not in data or data[f] == "":
            return False, f"Campo vacío: {f}"

    return True, ""

