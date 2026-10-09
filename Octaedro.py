import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ============================
# 1. DEFINIR LOS VÉRTICES
# ============================
A = (0, 2, 0)
B = (2, 0, 0)
C = (4, 2, 0)
D = (2, 4, 0)
E = (2, 2, 3)  # Punta superior
F = (2, 2, -3) # Punta inferior

vertices = [A, B, C, D, E, F]
nombres = ["A", "B", "C", "D", "E", "F"]

# ============================
# 2. CREAR LA FIGURA 3D
# ============================
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# ============================
# 3. DIBUJAR LAS CARAS
# ============================
caras = [
    [A, B, E], [B, C, E], [C, D, E], [D, A, E], # 4 caras de arriba
    [A, B, F], [B, C, F], [C, D, F], [D, A, F]  # 4 caras de abajo
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
    (A, B), (B, C), (C, D), (D, A), # Plano central
    (A, E), (B, E), (C, E), (D, E), # Aristas hacia arriba
    (A, F), (B, F), (C, F), (D, F)  # Aristas hacia abajo
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
ax.set_zlim(-4, 4)

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")
ax.set_title("Octaedro 3D")

plt.show()