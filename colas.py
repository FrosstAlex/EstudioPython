# Colas, las colas son el contrario que las pilas, el primero en entrar es el primero en salir
cola = ["maria", "jose", "alejandro"]
# agregamos elementos al final de la cola
cola.append("carla")
cola.append("flora")
print(cola)
# sacando elementos por el principio de la cola (segun orden indice 0,1,2,3,4,5,6)
n = cola.pop(0)
print(f"atendiendo a {n} ")
n = cola.pop(1)
print(f"atendiendo a {n} ")