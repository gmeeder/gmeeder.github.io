import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# Datos de ejemplo con valores faltantes
X = np.array([[1, 2], [2, 4], [3, np.nan], [4, 8]])
y = np.array([2, 4, 6, 8])

# Imputar valores faltantes
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_imputed, y)

# Imprimir los coeficientes del modelo
print("Coeficientes del modelo:", model.coef_)

# Predecir valores para los datos de entrada originales
predictions = model.predict(X_imputed)

# Imprimir las predicciones
print("Predicciones:", predictions)
