input_number=input("how many items they want to add: \n ")
number=int(input_number)
items= ()
for i in range(number):
    item=input(f"enter product and price number {i+1} : (like banana,3000) \n")
    name=item.split(",")[0]
    price=item.split(",")[1]
    items+=({"name":name,"price":int(price)},)

def sum(items):
    sum=0
    for item in items:
        sum+=item["price"]
    return sum


def find_largest(args):
    largest=args[0]["price"]
    for item in args:
     if item['price']>largest:
       largest=item["price"]
    return largest


print(f"items: {items}")
print(f"sum: {sum(items)}")
print(f"largest: {find_largest(items)}")
