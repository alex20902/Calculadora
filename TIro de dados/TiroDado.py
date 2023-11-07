
#different numeros
import random



#rango de numeros
min_val = 1
max_val = 6
roll_again = "si"

while roll_again == "si" or roll_again == "y":
    print("tirando los dados...")
    print("los numeros son...")

    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))

    roll_again = input("¿ Quieres tirar los dados otra vez?")




