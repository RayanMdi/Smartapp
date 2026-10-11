def aantal_dagen(inputfile):
    try:
        bestand = open(inputfile, "r")
        regels = bestand.readlines()
        bestand.close()

        teller = 0
        for regel in regels[1:]:
            if regel.strip() != "":
                teller += 1
        return teller
    except FileNotFoundError:
        print(f"Fout: Bestand '{inputfile}' niet gevonden.")
        return 0


def auto_bereken(inputfile, outputfile):
    try:
        in_file = open(inputfile, "r")
        regels = in_file.readlines()
        in_file.close()

        if len(regels) <= 1:
            print("Geen data om te berekenen.")
            return

        uit_file = open(outputfile, "w")

        for regel in regels[1:]:
            schone_regel = regel.strip()
            if schone_regel == "":
                continue

            delen = schone_regel.split()
            datum = delen[0]
            num_people = int(delen[1])
            temp_setpoint = float(delen[2])
            temp_outside = float(delen[3])
            precip = float(delen[4])

            
            verschil = temp_setpoint - temp_outside
            if verschil >= 20:
                cv = 100
            elif 10 <= verschil < 20:
                cv = 50
            else:
                cv = 0

            
            ventilatie = num_people + 1
            if ventilatie > 4:
                ventilatie = 4

            
            bewatering = precip < 3.0

            uit_file.write(f"{datum};{cv};{ventilatie};{bewatering}\n")

        uit_file.close()
        print(f"Actuatoren berekend en geschreven naar '{outputfile}'.")
    except FileNotFoundError:
        print(f"Fout: Bestand '{inputfile}' bestaat niet.")


def overwrite_settings(outputfile):
    datum = input("Voer de datum in (bijv. 08-10-2024): ").strip()
    systeem = input("Kies systeem (1: CV ketel, 2: ventilatie, 3: bewatering): ").strip()

    if systeem not in ["1", "2", "3"]:
        return -3

    nieuwe_waarde_str = input("Voer de nieuwe waarde in: ").strip()

    if systeem == "1":
        try:
            val = int(nieuwe_waarde_str)
            if val < 0 or val > 100:
                return -3
            nieuwe_waarde = str(val)
        except ValueError:
            return -3
    elif systeem == "2":
        try:
            val = int(nieuwe_waarde_str)
            if val < 0 or val > 4:
                return -3
            nieuwe_waarde = str(val)
        except ValueError:
            return -3
    elif systeem == "3":
        if nieuwe_waarde_str in ["1", "True", "true"]:
            nieuwe_waarde = "True"
        elif nieuwe_waarde_str in ["0", "False", "false"]:
            nieuwe_waarde = "False"
        else:
            return -3

    try:
        in_file = open(outputfile, "r")
        regels = in_file.readlines()
        in_file.close()
    except FileNotFoundError:
        return -1

    gevonden = False
    aangepaste_regels = []

    for regel in regels:
        delen = regel.strip().split(";")
        if len(delen) == 4 and delen[0] == datum:
            gevonden = True
            if systeem == "1":
                delen[1] = nieuwe_waarde
            elif systeem == "2":
                delen[2] = nieuwe_waarde
            elif systeem == "3":
                delen[3] = nieuwe_waarde
            aangepaste_regels.append(f"{delen[0]};{delen[1]};{delen[2]};{delen[3]}\n")
        else:
            aangepaste_regels.append(regel)

    if not gevonden:
        return -1

    uit_file = open(outputfile, "w")
    uit_file.writelines(aangepaste_regels)
    uit_file.close()

    return 0


def smart_app_controller():
    inputfile = "input.txt"
    outputfile = "output.txt"

    while True:
        print("\n--- SMART APP CONTROLLER MENU ---")
        print("1. Hoeveel dagen zijn er aanwezig?")
        print("2. Autobereken alle actuatoren en schrijf naar output.txt")
        print("3. Overschrijf een berekende waarde")
        print("4. Stoppen")

        keuze = input("Maak een keuze (1-4): ").strip()

        if keuze == "1":
            dagen = aantal_dagen(inputfile)
            print(f"Er zijn {dagen} dagen met data aanwezig.")
        elif keuze == "2":
            auto_bereken(inputfile, outputfile)
        elif keuze == "3":
            res = overwrite_settings(outputfile)
            if res == 0:
                print("Succes: Waarde succesvol aangepast.")
            elif res == -1:
                print("Fout (-1): Datum niet gevonden.")
            elif res == -3:
                print("Fout (-3): Ongeldig systeem of ongeldige waarde.")
        elif keuze == "4":
            print("Terug naar het hoofdmenu...")
            break
        else:
            print("Ongeldige keuze. Kies 1, 2, 3 of 4.")
