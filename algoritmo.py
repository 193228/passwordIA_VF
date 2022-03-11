import math
import string
import pandas as pd
from EasyGA.crossover import Crossover
from EasyGA.mutation import Mutation
from EasyGA.parent import Parent
from EasyGA.survivor import Survivor
from main import *
import EasyGA
import random
from tablaFrecuencia import *
lista = []

class algoritmo:
    def __init__(self, password=""):
        self.password = password

    # getter method
    def get_password(self):
        return self.password

    # setter method
    def set_password(self, x):
        self.password = x

clase = algoritmo()

def funcionFitness(chromosome):
    suma = sum(1 for gene, letter in zip(chromosome, clase.get_password()) if gene.value == letter)
    return suma

def busqueda(lista,dato):
    caracter = ""
    while lista:
        valor = lista.pop(0)
        prob = float(valor["probabilidad"])/100
        if prob <= dato:
            caracter= valor["caracter"]
            return caracter

def generar_cadena():
    try:
        tabla = inicializacion()
        cadena = ""
        r = random.uniform(0,1)
        c = busqueda(tabla,r)
        cadena = cadena + str(c)
        return cadena
    except:
        print("cadena descifrada")
        pass

def listaCaracteres():
    lista = []
    for i in string.printable: #obtenemos todos los caracteres imprimibles
        lista.append(i)
    return lista

def seleccion(lista):
    reverseCharList = []
    for someChar in lista:
        reverseCharList.append(lista.pop(0))
    return reverseCharList

def inicializoAlgoritmo(password, ventana):
    # inicializadores
    clase.set_password(password)  # agrego un setter del password
    AG = EasyGA.GA()  # inicializo el algoritmo genetico
    # Atributos a utilizar
    AG.chromosome_length = len(password)
    AG.fitness_goal = len(password)
    AG.population_size = int(ventana.ingresoPoblacionInicial.text())
    if ventana.botonDescifrado.isChecked() and len(ventana.ingresoNumeroGeneraciones.text()) == 0:
        AG.generation_goal = math.inf
    if not ventana.botonDescifrado.isChecked() and len(ventana.ingresoNumeroGeneraciones.text()) >0:
        AG.generation_goal = int(ventana.ingresoNumeroGeneraciones.text())  # math.inf #no termina hasta que se encuentre la solucion

    #maximizamos la funcion
    AG.target_fitness_type = 'max' #minimo o maximo en caso de ser necesario

    AG.fitness_function_impl = funcionFitness #funcionFitness
    AG.gene_impl = lambda: generar_cadena() #debe de recibir la lista de acuerdo a las probabilidades mas altas
    # metodos de implementacion
    AG.gene_mutation_rate = 0.05 #default

    #usando las estrategias a utilizar
    AG.parent_selection_impl = Parent.Rank.tournament  # usamos la seleccion de torneo
    AG.survivor_selection_impl = Survivor.fill_in_best  # usamos el metodo por el mejor individuo
    AG.crossover_individual_impl = Crossover.Individual.single_point  # metodo de punto unico
    AG.mutation_individual_impl = Mutation.Individual.individual_genes  # mutacion de genes

    return AG

def get_rand_number(min_value, max_value):
    range = max_value - min_value
    choice = random.uniform(0,1)
    return min_value + range*choice


def monte_carlo(num_samples, suma):
    lower_bound = 0
    upper_bound = suma
    sum_of_samples = 0

    for i in range(num_samples):
        x = get_rand_number(lower_bound, upper_bound)
        sum_of_samples += suma

    return (upper_bound - lower_bound) * float(sum_of_samples / num_samples)

def obtenerAG(ga):
    lista = []
    i = 0
    while ga.active():
        ga.evolve(1)
        i = i+1
        data = {
            "generacion":i,
            "poblacion":ga.population,
            "mejor chromosoma":list(ga.population[0]),
            "peor chromosoma": list(ga.population[-1]),
            "fitness mejor chromosoma":ga.population[0].fitness,
            "fitness peor chromosoma":ga.population[-1].fitness
        }
        lista.append(data)
    df = pd.DataFrame(lista)
    return df

#ruleta