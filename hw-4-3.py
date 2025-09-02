numbers = (1, 2, 3, 2, 4, 2, 5)

target = int(input("enter the number: "))

count = 0
for n in numbers:
    if n == target:
        count += 1

print(f"number {target} repeated for {count}")