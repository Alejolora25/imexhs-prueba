# test_cases.py
from main import tower_of_hanoi_with_colors

print("Caso 1 (esperado OK):")
n1 = 3
disks1 = [(3, "red"), (2, "blue"), (1, "red")]
print(tower_of_hanoi_with_colors(n1, disks1))
print()

print("Caso 2 (esperado -1):")
n2 = 3
disks2 = [(3, "red"), (2, "red"), (1, "red")]
print(tower_of_hanoi_with_colors(n2, disks2))

print("\nCaso 3 (esperado -1):")
n3 = 2
disks3 = [(2, "red"), (1, "red")]
print(tower_of_hanoi_with_colors(n3, disks3))

print("\nCaso 4 (esperado OK):")
n4 = 3
disks4 = [(3, "red"), (2, "green"), (1, "blue")]
print(tower_of_hanoi_with_colors(n4, disks4))
