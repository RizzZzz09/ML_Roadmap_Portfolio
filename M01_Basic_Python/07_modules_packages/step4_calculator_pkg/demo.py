import calculator as calc
from calculator import *  # noqa: F403
from calculator import add, sub

result = calc.add.add(10, 2)
print(result)
print("Есть add у пакета? ", hasattr(calc, "add"))
print("Есть add_list у пакета? ", hasattr(calc, "add_list"))

result = add.add(1, 1)
print(result)
result = sub.sub(2, 1)
print(result)

result = plus(11, 11)  # noqa: F405
print(result)
print("Есть add в globals()? ", "add" in globals())
print("Есть plus в globals()? ", "plus" in globals())
