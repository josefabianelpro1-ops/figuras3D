import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ============================
# 1. DEFINIR LOS VÉRTICES
# ============================
A = (0, 0, 0)
B = (3, 0, 0)
C = (1.5, 2.6, 0)
D = (0, 0, 4)
E = (3, 0, 4)
F = (1.5, 2.6, 4)

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
    [A, B, C],       # Base inferior
    [D, E, F],       # Base superior
    [A, B, E, D],    # Pared frontal
    [B, C, F, E],    # Pared lateral derecha
    [C, A, D, F]     # Pared lateral izquierda
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
    (A, B), (B, C), (C, A), # Triángulo inferior
    (D, E), (E, F), (F, D), # Triángulo superior
    (A, D), (B, E), (C, F)  # Pilares
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
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 4)
ax.set_zlim(-1, 5)

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")
ax.set_title("Prisma Triangular 3D")

plt.show()