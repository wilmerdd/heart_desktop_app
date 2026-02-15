import joblib
from config import MODEL_PATH

class HeartFailureModel:

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, df):
        pred = self.model.predict(df)[0]
        prob = self.model.predict_proba(df)[0][1]
        return pred, prob
