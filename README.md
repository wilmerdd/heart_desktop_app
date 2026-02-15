# 🫀 Heart Disease Desktop Predictor

Aplicación de escritorio desarrollada en **Python + Tkinter** que integra un modelo de **Machine Learning (Random Forest)** para predecir riesgo de enfermedad cardíaca a partir de datos clínicos del paciente.

El sistema funciona completamente **offline**, permitiendo ingresar información médica básica y obtener una predicción inmediata junto con su probabilidad.

---

## 👨‍💻 Autor

**Wilmer Duque Díaz**

Proyecto académico enfocado en:

- Machine Learning
- Desarrollo de aplicaciones de escritorio
- Ingeniería de software
- Ciencia de datos aplicada

---

## 📌 Descripción General

Esta aplicación permite:

✅ Ingresar datos clínicos del paciente  
✅ Preprocesar variables automáticamente  
✅ Ejecutar un modelo Random Forest entrenado previamente  
✅ Mostrar resultado + probabilidad  
✅ Funcionar sin conexión a internet  

---

## 📦 Características

- Aplicación 100% local
- Interfaz gráfica con Tkinter
- Predicción inmediata
- Arquitectura modular
- Separación ML / UI / Validación
- Escalable y mantenible
- Preparada para empaquetar como ejecutable (.exe)

---

## 🧱 Arquitectura del proyecto

```
heart_desktop_app/
│
├── main.py
├── config.py
├── run.bat
├── requirements.txt
│
├── models/
│     └── best_random_forest_model.pkl
│
├── ml_service/
│     ├── model.py
│     └── preprocessor.py
│
├── utils/
│     └── validation.py
│
├── ui/
│     └── app_ui.py
│
└── screenshots/
      ├── app.png
      └── result.png
```

---

## 🧠 Modelo

Random Forest Classifier entrenado con scikit‑learn.

Salida:
0 → Normal  
1 → Enfermedad cardíaca  

---

## 📚 Dataset

Heart Failure Prediction Dataset – Kaggle (2021)  
Autor: fedesoriano  
https://www.kaggle.com/fedesoriano/heart-failure-prediction

Combinado desde 5 datasets UCI. Dataset final: 918 registros.

---

## ⚙️ Instalación

python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  

---

## ▶ Ejecutar

Doble clic en:

run.bat

o:

python main.py

---

## 🛠 Crear ejecutable

pip install pyinstaller  
pyinstaller --onefile --windowed main.py  

Resultado:

dist/main.exe

---

## 🔒 Aviso

Proyecto educativo. No reemplaza diagnóstico médico.

---

🫀 La tecnología también puede salvar vidas.
