def find_largest(args):
    largest=args[0]
    for item in args:
     if item>largest:
       largest=item
    return largest

print(find_largest([3, 7, 2, 9, 5]))