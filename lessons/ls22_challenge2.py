"""LS22 Challenge Question 2."""

a: dict[str, int] = {"k": 1}
b: dict[str, int] = a
c: dict[str, int] = b
a["k"] = 2
b = {"k": 3}
print(a["k"])
print(b["k"])
print(c["k"])