#programa por KEVIN ALEXANDER TRUJILLO BENAVIDES Y CARMERLO MOLINA

# -*- coding: utf-8 -*-
import numpy as np

# Funcion sigmoide para normalizar entradas.
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivados sigmoideos para ajustar los pesos sinapticos.
def sigmoid_derivative(x):
    return x * (1 - x)

# entrada de datos
training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

# salida de datos
training_outputs = np.array([[0,1,1,0]]).T

# Sembrar numeros aleatorios para hacer el calculo. e los peso
np.random.seed(1)

# Inicializar ponderaciones aleatoriamente con media 0 para crear matrices de ponderaci�n, sin�pticas.
synaptic_weights = 2 * np.random.random((3,1)) - 1

print('Pesos sinapticos de arranque aleatorio: ')
print(synaptic_weights)

# Iterar 10,000 veces
for iteration in range(10000):

    # Define capa de entraa
    input_layer = training_inputs
    # Normaliza el producto de la capa de entrada con los pesos sin�pticos.
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    # cuanto nos perdimos
    error = training_outputs - outputs

    # multiplicar cuanto nos perdimos por el pendiente del sigmoide en los valores en las salidas

    adjustments = error * sigmoid_derivative(outputs)

    # actualizar pesos
    synaptic_weights += np.dot(input_layer.T, adjustments)

print('pesos sinapticos espuess del entrenamiento: ')
print(synaptic_weights)

print("salida despues del entrenamiento:")
print(outputs)
