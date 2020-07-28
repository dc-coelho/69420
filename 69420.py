import random as random

def programa():
    count = 1
    def generator():
        temp=""
        for i in range(5):
            temp = (temp + str(random.randint(0,9)))
        print(temp)
        return temp

    num = generator()
    while num != str("69420"):
        num = generator()
        count += 1
    print(f"Foram precisas {count} tentativas para 69420")

if input("\nComeçar? [Y/N]: ").lower() == "y":
    programa()
    while input("\nOutra Vez? [Y/N]: ").lower() == 'y':
        programa()
