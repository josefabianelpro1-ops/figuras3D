import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ============================
# 1. DEFINIR LOS VÉRTICES
# ============================
A = (0, 0, 0)
B = (4, 0, 0)
C = (4, 4, 0)
D = (0, 4, 0)
E = (2, 2, 5) # Cúspide (punta)

vertices = [A, B, C, D, E]
nombres = ["A", "B", "C", "D", "E"]

# ============================
# 2. CREAR LA FIGURA 3D
# ============================
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ============================
# 3. DIBUJAR LAS CARAS
# ============================
caras = [
    [A, B, C, D], # Base cuadrada
    [A, B, E],    # Frente
    [B, C, E],    # Derecha
    [C, D, E],    # Fondo
    [D, A, E]     # Izquierda
]

figura_3d = Poly3DCollection(caras, alpha=0.4, edgecolor="black", facecolor="blue")
ax.add_collection3d(figura_3d)

# ============================
# 4. DIBUJAR LOS VÉRTICES
# ============================
for nombre, vertice in zip(nombres, vertices):
    x, y, z = vertice
    ax.scatter(x, y, z, s=80, color="red")
    ax.text(x, y, z + 0.1, nombre, fontsize=12)

# ============================
# 5. DIBUJAR LAS ARISTAS
# ============================
aristas = [
    (A, B), (B, C), (C, D), (D, A), # Base
    (A, E), (B, E), (C, E), (D, E)  # Aristas a la punta
]

for inicio, fin in aristas:
    ax.plot(
        [inicio[0], fin[0]], 
        [inicio[1], fin[1]], 
        [inicio[2], fin[2]], 
        linewidth=2, color="black"
    )

# ============================
# 6. CONFIGURAR LA ESCENA
# ============================
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 5)
ax.set_zlim(-1, 6)

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")
ax.set_title("Pirámide Cuadrangular 3D")

plt.show()