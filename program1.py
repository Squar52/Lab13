class SEA:
    def __init__(self, name, ocean, area, depth):
        self.name = name
        self.ocean = ocean
        self.area = float(area)
        self.depth = float(depth)
    def set_area(self, area):
        self.area = float(area)
    def set_depth(self, depth):
        self.depth = float(depth)
    def show(self):
        print(f"{self.name} | океан: {self.ocean} | площа: {self.area} тис. км² | глибина: {self.depth} м")
seas = [
    SEA("Чорне", "Атлантичний", 436, 2212),
    SEA("Середземне", "Атлантичний", 2500, 5121),
    SEA("Балтійське", "Атлантичний", 415, 459),
    SEA("Червоне", "Індійський", 450, 3039),
]
print("Список морів:")
for s in seas:
    s.show()
name = input("\nНазва моря для зміни: ").strip().lower()
for s in seas:
    if s.name.lower() == name:
        s.set_area(input("Нова площа (тис. км²): "))
        s.set_depth(input("Нова глибина (м): "))
        break
else:
    print("Такого моря немає.")
print("\nСписок після змін:")
for s in seas:
    s.show()