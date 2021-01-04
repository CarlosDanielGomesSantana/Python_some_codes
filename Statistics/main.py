from functions import *
x = [15, 18, 29, 45, 51, 55, 63, 70]
y = [16, 38, 24, 31, 49, 54, 32, 55]

createTable(x, y)

print(f"VAR(x) : {round(var(x), 4)}\n")
print(f"VAR(y) : {round(var(y), 4)}\n")
print(f"COV(x;y) : {round(cov(x, y), 4)} -> {cov_signal(cov(x,y))}\n")
print(f"r(x;y) = {r(x,y)} -> {r_class(r(x,y))}\n")
print(f"t crítico é {tStudent(x, y)}\n")

if hipot(x, y, 0.05):
    print(f"{tStudent(x, y)} > {t_tab(len(x) - 2, 0.05)}")
    print(f"Existe uma correlação entre X e Y. Boa qualidade no dados.\n")
else:
    print(f"{tStudent(x, y)} < {t_tab(len(x) - 2, 0.05)}")
    print(f"O r que foi calculado deve-se ao acaso. Mal qualidade nos dados.\n")

print(f"O erro padrão de r é {erro_padrao_r(x, y)}\n")

if determinarR(r(x, y)):
    print(f"{round((r(x,y)**2)*100, 3)}% é explicado pelo modelo linear. Pode ter validade científica.\n")
else:
    print(f"{round((r(x,y)**2)*100, 3)}% é explicado pelo modelo linear\n")
