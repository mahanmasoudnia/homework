while True:
    try:
        first_input=input("Enter first number: \n")
        sec_input=input("Enter second number: \n")
        first_number=int(first_input)
        sec_number=int(sec_input)
        break
    except:
        print('Something went wrong, try again')
        
sum=first_number+sec_number
diff=first_number-sec_number
# i know we can use abs() function
if diff<0:
  dist=-diff
else: dist=diff
prod=first_number*sec_number
div=first_number/sec_number
print(f"sum:{sum}, \n diff:{diff}, \n dist:{dist}, \n prod:{prod}, \n div:{div}")