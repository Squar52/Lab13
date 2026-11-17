import random
from pointspace import PointSpace
points = [PointSpace(random.randint(-10, 10),
                     random.randint(-10, 10),
                     random.randint(-10, 10)) for _ in range(8)]
for i, p in enumerate(points, 1):
    print(f"Точка {i}: ", end="")
    p.DisplayCoord()
    octant = p.Octant()
    print("  октанта:", octant if octant else "на межі октант")
    print(f"  відстань до центра: {p.Dist():.2f}")
points[0].SetCoord(1, 2, 3)
print("\nПісля SetCoord першої точки: ", end="")
points[0].DisplayCoord()