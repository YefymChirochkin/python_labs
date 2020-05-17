from Jack import Jack

def main():

    lavita = Jack(20, 2000, "Italy", "black", 500, "ST-10450-GH", 440, 110)
    vitol = Jack(35, 2500, "Ukraine", "gray", 350, "JO-113", 500, 150)
    welle = Jack(30, 3500, "France", "black", 899, "SRT-10101", 600, 175)

    jacks = [lavita, vitol, welle]

    for count_of_object in jacks:
        print(count_of_object)

if __name__ == "__main__":
    main()