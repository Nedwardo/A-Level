a = 'l'
b = '5'
c = 'o'

x = input("Enter your message: ")
values = [globals().get(var, '') for var in list(x)]

print (values)
