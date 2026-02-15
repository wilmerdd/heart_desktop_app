import pandas as pd


def preprocess(data: dict):

    # Mapeos EXACTOS del dataset Kaggle
    sex_map = {"M": 1, "F": 0}
    chest_map = {"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3}
    ecg_map = {"Normal": 0, "ST": 1, "HVI": 2}
    angina_map = {"Y": 1, "N": 0}
    slope_map = {"Up": 0, "Flat": 1, "Down": 2}

    data["Sex"] = sex_map[data["Sex"]]
    data["ChestPainType"] = chest_map[data["ChestPainType"]]
    data["RestingECG"] = ecg_map[data["RestingECG"]]
    data["ExerciseAngina"] = angina_map[data["ExerciseAngina"]]
    data["ST_Slope"] = slope_map[data["ST_Slope"]]

    return pd.DataFrame([data])
