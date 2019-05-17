#programa por KEVIN ALEXANDER TRUJILLO BENAVIDES Y CARMERLO MOLINA


# -*- coding: utf-8 -*-
import numpy as np

class NeuralNetwork():

    def __init__(self):
        # Sembrar el generador de n�meros aleatorios.
        np.random.seed(1)

        # Establecer pesos sin�pticos en una matriz de 3x1,
        # con valores de -1 a 1 y media 0
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        """
        Toma la suma ponderada de las entradas y normaliza.
        A trav�s de entre 0 y 1 a trav�s de una funci�n sigmoide
        """
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        """
        La derivada de la funci�n sigmoide utilizada para
        calcular los ajustes de peso necesarios
        """
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        """
        Entrenamos el modelo a trav�s de prueba y error, ajustando el
        Pesos sin�pticos cada vez para obtener un mejor resultado.
        """
        for iteration in range(training_iterations):
            # Pase conjunto de entrenamiento a trav�s de la red neuronal.
            output = self.think(training_inputs)

            # Calcular la tasa de error
            error = training_outputs - output

            # Error multiplicado por entrada y gradiente de la funci�n sigmoide
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            # Ajustar los pesos sin�pticos.
            self.synaptic_weights += adjustments

    def think(self, inputs):
        """
        Pasa entradas a trav�s de la red neuronal para obtener salida
        """

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


if __name__ == "__main__":

    # Inicializar la red neuronal de una sola neurona.
    neural_network = NeuralNetwork()

    print("Pesos sin�pticos de arranque aleatorio: ")
    print(neural_network.synaptic_weights)

    # El conjunto formativo, con 4 ejemplos que consta de 3.
    # valores de entrada y 1 valor de salida
    training_inputs = np.array([[0,0,1],
                                [1,1,1],
                                [1,0,1],
                                [0,1,1]])

    training_outputs = np.array([[0,1,1,0]]).T

    # Entrena la red neuronal
    neural_network.train(training_inputs, training_outputs, 10000)

    print("Synaptic pesos espues del entrenamiento: ")
    print(neural_network.synaptic_weights)

    A = str(input("Input 1: "))
    B = str(input("Input 2: "))
    C = str(input("Input 3: "))

    print("Nueva situaci�n: datos de entrada = ", A, B, C)
    print("datos de salida: ")
    print(neural_network.think(np.array([A, B, C])))
