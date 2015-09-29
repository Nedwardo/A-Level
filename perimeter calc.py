sides = []
perimeter = 0
Nothing_Important = False
while True:
    try:
        number_of_corners = int(input("How many corners are there? "))
        break
    except:
        print("please input an interger")
print ("Please input vertices starting from the top left and following counterclock-wise inputing their co-ordinate in a graphical format i.e. (1,2)")
for x in range (1,(number_of_corners+1)):
    Nothing_Important = False
    while Nothing_Important != True:
        try:
##            x_dim = int(input("What is the " + str(x) + "th x dimention location "))
##            y_dim = int(input("What is the " + str(x) + "th y dimention location "))
            vertex_coord = list(input("What is the " + str(x) + "th vertex location "))
            sides.append(vertex_coord)
            Nothing_Important = True
        except:
            print("please input an interger")

for x in range (0,(number_of_corners)):
    perimeter += (((sides[x][0]-sides[(x+1)%number_of_corners][0])**2+(sides[x][1]-sides[(x+1)%number_of_corners][1])**2)**0.5)


print(round(perimeter,2))

