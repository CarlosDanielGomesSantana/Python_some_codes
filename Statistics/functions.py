"""
Facilitar a prova de Estatística e Probabilidade
"""
from beautifultable import BeautifulTable
import numpy as np
from numpy.lib.scimath import sqrt

t_tabelado = {1: [0.158,  0.325, 0.510, 0.727, 1.000, 1.376, 1.963, 3.078, 6.314, 12.706, 31.821, 63.657, 636.619],
              2: [0.142, 0.289, 0.445,  0.617, 0.816,  1.061, 1.386, 1.886,  2.920, 4.303,  6.965, 9.925, 31.598],
              3: [0.137, 0.277, 0.424, 0.584, 0.765, 0.978, 1.25, 1.638, 2.353, 3.182, 4.541, 5.541, 12.924],
              4: [0.134, 0.271, 0.414, 0.569, 0.741, 0.941, 1.19, 1.533, 2.132, 2.776, 3.747, 4.604, 8.61],
              5: [0.132, 0.267, 0.408, 0.559, 0.727, 0.92, 1.156, 1.476, 2.015, 2.571, 3.365, 4.032, 6.869],
              6: [0.131, 0.265, 0.404, 0.553, 0.718, 0.906, 1.134, 1.44, 1.943, 2.447, 3.143, 3.707, 5.959],
              7: [0.13, 0.263, 0.402, 0.549, 0.711, 0.896, 1.119, 1.415, 1.895, 2.365, 2.365, 3.499, 5.408],
              8: [0.13, 0.262, 0.399, 0.546, 0.706, 0.889, 1.108, 1.397, 1.86, 2.306, 2.896, 3.355, 5.041],
              9: [0.129, 0.261, 0.398, 0.543, 0.703, 0.883, 1.1, 1.383, 1.833, 2.262, 2.821, 3.25, 4.781],
              10: [0.129, 0.26, 0.397, 0.542, 0.7, 0.879, 1.093, 1.372, 1.812, 2.228, 2.764, 3.169, 4.587],
              11: [0.129, 0.26, 0.396, 0.54, 0.697, 0.876, 1.088, 1.363, 1.796, 2.201, 2.718, 3.106, 4.437],
              12: [0.128, 0.259, 0.395, 0.539, 0.695, 0.873, 1.083, 1.356, 1.782, 2.179, 2.681, 3.055, 4.318],
              13: [0.128, 0.259, 0.394, 0.538, 0.694, 0.87, 1.079, 1.35, 1.771, 2.16, 2.65, 3.012, 4.221],
              14: [0.128, 0.258, 0.393, 0.537, 0.692, 0.868, 1.076, 1.345, 1.761, 2.145, 2.624, 2.977, 4.14],
              15: [0.128, 0.258, 0.393, 0.536, 0.691, 0.866, 1.074, 1.341, 1.753, 2.131, 2.602, 2.947, 4.073],
              16: [0.128, 0.258, 0.392, 0.535, 0.69, 0.865, 1.071, 1.337, 1.746, 2.12, 2.583, 2.921, 4.015],
              17: [0.128, 0.257, 0.392, 0.534, 0.689, 0.863, 1.069, 1.333, 1.74, 2.11, 2.567, 2.898, 3.965],
              18: [0.127, 0.257, 0.392, 0.534, 0.688, 0.862, 1.067, 1.33, 1.734, 2.101, 2.552, 2.878, 3.922],
              19: [0.127, 0.257, 0.391, 0.533, 0.688, 0.861, 1.066, 1.328, 1.729, 2.093, 2.539, 2.861, 3.883],
              20: [0.127, 0.257, 0.391, 0.533, 0.687, 0.86, 1.064, 1.325, 1.725, 2.086, 2.528, 2.845, 3.85],
              21: [0.127, 0.257, 0.391, 0.532, 0.686, 0.859, 1.063, 1.323, 1.721, 2.08, 2.518, 2.831, 3.819],
              22: [0.127, 0.256, 0.39, 0.532, 0.686, 0.858, 1.061, 1.321, 1.717, 2.074, 2.508, 2.819, 3.792],
              23: [0.127, 0.256, 0.39, 0.532, 0.685, 0.858, 1.06, 1.319, 1.714, 2.069, 2.5, 2.807, 3.767],
              24: [0.127, 0.256, 0.39, 0.531, 0.685, 0.857, 1.059, 1.318, 1.711, 2.064, 2.492, 2.797, 3.745],
              25: [0.127, 0.256, 0.39, 0.531, 0.684, 0.856, 1.058, 1.316, 1.708, 2.06, 2.485, 2.787, 3.726],
              26: [0.127, 0.256, 0.39, 0.531, 0.684, 0.856, 1.058, 1.315, 1.706, 2.056, 2.479, 2.779, 3.707],
              27: [0.127, 0.256, 0.389, 0.531, 0.684, 0.856, 1.057, 1.314, 1.703, 2.052, 2.473, 2.771, 3.69],
              28: [0.127, 0.256, 0.389, 0.53, 0.683, 0.856, 1.056, 1.313, 1.701, 2.048, 2.467, 2.763, 3.674],
              29: [0.127, 0.256, 0.389, 0.53, 0.683, 0.854, 1.055, 1.311, 1.699, 2.045, 2.462, 2.756, 3.659],
              30: [0.127, 0.256, 0.389, 0.53, 0.683, 0.854, 1.055, 1.31, 1.697, 2.042, 2.457, 2.75, 3.646],
              40: [0.126, 0.255, 0.388, 0.529, 0.681, 0.851, 1.05, 1.303, 1.684, 2.021, 2.423, 2.704, 3.551],
              60: [0.126, 0.254, 0.387, 0.527, 0.679, 0.848, 1.046, 1.296, 1.671, 2.0, 2.39, 2.66, 3.46],
              120: [0.126, 0.254, 0.386, 0.526, 0.677, 0.845, 1.041, 1.289, 1.658, 1.98, 2.358, 2.617, 3.373],
              "i": [0.126, 0.253, 0.385, 0.524, 0.674, 0.842, 1.036, 1.282, 1.645, 1.96, 2.326, 2.576, 3.291]
              }


def var(array):
    """
    Calcula o valor da variância
    """
    math = np.lib.scimath
    np_array = np.array(array)
    division = 1/len(np_array)
    bessel = 1/(len(np_array) - 1)
    sum_1 = math.power(np_array, 2).sum()
    sum_2 = math.power(np_array.sum(), 2)
    return bessel*(sum_1 - division*(sum_2))


def cov(x, y):
    """
    Calcula o valor da covariância
    """
    math = np.lib.scimath
    array_x = np.array(x)
    array_y = np.array(y)
    division = 1/len(x)
    bessel = 1/(len(x) - 1)
    sum_1 = (array_x*array_y).sum()
    sum_2 = array_x.sum()*array_y.sum()
    cov = bessel*(sum_1 - division*(sum_2))
    return cov


def r(x, y, nround=2):
    """
    Calcula o coeficiente de correlação linear de Pearson
    """
    r = cov(x, y)/((var(x)*var(y))**(1/2))

    return round(r, nround)


def r_class(r):
    """
    Classificação do coeficiente de correlação linear de Pearson
    """
    if round(abs(r), 2) <= 0.19:
        return "Muito Fraca"
    elif 0.2 < round(abs(r), 2) <= 0.39:
        return "Fraca"
    elif 0.4 < round(abs(r), 2) <= 0.69:
        return "Moderado"
    elif 0.7 < round(abs(r), 2) <= 0.89:
        return "Forte"
    else:
        return "Muito Forte"


def cov_signal(x): return "Sinérgico" if x > 0 else "Antisinérgico"


def tStudent(x, y, nround=4):
    """
    Calcula o t crítico de Student
    """
    pearson = r(x, y)
    return round(abs(pearson)*(sqrt(len(x)-2/(1 - pearson**2))), nround)


def erro_padrao_r(x, y):
    """
    Calcula o erro padrão do coeficiente r
    """
    return sqrt(1 - r(x, y)**2/(len(x)-2))


def t_tab(liberdade, alpha):
    """
    Achar o valor referente à o grau de liberdade e alpha
    """
    def acharAlpha(Liberdade, Alpha):
        if 0.001 == Alpha:
            return t_tabelado[Liberdade][12]
        elif 0.01 == Alpha:
            return t_tabelado[Liberdade][11]
        elif 0.02 == Alpha:
            return t_tabelado[Liberdade][10]
        elif 0.05 == Alpha:
            return t_tabelado[Liberdade][9]
        elif 0.1 == Alpha:
            return t_tabelado[Liberdade][8]
        elif 0.2 == Alpha:
            return t_tabelado[Liberdade][7]
        elif 0.3 == Alpha:
            return t_tabelado[Liberdade][6]
        elif 0.4 == Alpha:
            return t_tabelado[Liberdade][5]
        elif 0.5 == Alpha:
            return t_tabelado[Liberdade][4]
        elif 0.6 == Alpha:
            return t_tabelado[Liberdade][3]
        elif 0.7 == Alpha:
            return t_tabelado[Liberdade][2]
        elif 0.8 == Alpha:
            return t_tabelado[Liberdade][1]
        else:
            return t_tabelado[Liberdade][0]
    if liberdade <= 30:
        return acharAlpha(liberdade, alpha)
    elif 30 < liberdade <= 40:
        return acharAlpha(liberdade, alpha)
    elif 40 < liberdade <= 60:
        return acharAlpha(liberdade, alpha)
    elif 60 < liberdade <= 120:
        return acharAlpha(liberdade, alpha)
    else:
        return acharAlpha("i", alpha)


def hipot(x, y, alpha):
    """
    Faz o teste de Hipótese
    """
    grau_liberdade = len(x) - 2
    erro_sig = alpha
    if tStudent(x, y) > t_tab(grau_liberdade, erro_sig):
        return True
    else:
        return False
    


def determinarR(r): True if 0.9 <= r**2 <= 1 else False


def createTable(x, y):
    """
    Cria tabela de correlação-regressão
    """
    array_x = np.array(x)
    array_y = np.array(y)
    table = BeautifulTable()
    row = table.rows
    column = table.columns
    for i, j in zip(array_x, array_y):
        row.append([i, j, i**2, j**2, i*j])
    row.append([sum(array_x), sum(array_y), sum(array_x**2),
                sum(array_y**2), sum(array_x*array_y)])
    rows_header = [str(i+1) for i in range(len(row)-1)]
    rows_header.append("\u2211")
    row.header = rows_header
    column.header = ["xi", "yi", "x²i", "y²i", "y²i \u00b7 y²i"]
    print(table)


def tTable(): pass
