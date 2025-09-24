i = 42
f = 3.14
s = "hello"
b = True
lst = [1,2,3]
tup = (1,2)
d = {"a": 1, "b":2}
st = {1,2,3}

# control
for x in lst:
    print(x)
if "a" in d:
    print("has a")


# Functions, arfs, kwargs, annotations
def greet(name: str, / , *, excited: bool = False) -> str:
    msg = F"Hi, {name}"
    return msg + "!" if excited else msg
print(greet("Tatiana", excited=True))

# List/dict comprenhensions & generator
squares = [x*x for x in range(10) if x % 2 == 0]
d = {i: i*i for i in range(5)}
gen = (x*x for x in range(5)) # generator
print(next(gen))

# file I/O and context managers
with open("notes.txt", "w", encoding="utf8") as f:
    f.write("hello\n")

# Exceptions
try:
    1/0
except ZeroDivisionError:
    print("can't divide by zero")