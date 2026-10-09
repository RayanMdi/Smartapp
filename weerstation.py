def fahrenheit(temp_celcius):
    return 32.0 + 1.8 * float(temp_celcius)


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return float(temp_celcius) - (float(luchtvochtigheid) / 100.0) * float(windsnelheid)


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)
    wind = float(windsnelheid)

    if gevoel < 0 and wind > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and wind <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gevoel < 10 and wind > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gevoel < 10 and wind <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"


def weerstation():
    totaal_temp = 0.0
    aantal_dagen = 0

    for dag in range(1, 8):
        invoer_temp = input(f"Wat is op dag {dag} de temperatuur[C]: ").strip()
        if invoer_temp == "":
            print("bye")
            break

        invoer_wind = input(f"Wat is op dag {dag} de windsnelheid[m/s]: ").strip()
        if invoer_wind == "":
            print("bye")
            break

        invoer_vocht = input(f"Wat is op dag {dag} de vochtigheid[%]: ").strip()
        if invoer_vocht == "":
            print("bye")
            break

        try:
            temp_c = float(invoer_temp)
            wind = float(invoer_wind)
            vocht = float(invoer_vocht)
        except ValueError:
            print("Ongeldige invoerwaarde(n). Invoer gestopt.")
            break

        aantal_dagen += 1
        totaal_temp += temp_c
        gemiddelde = totaal_temp / aantal_dagen

        temp_f = fahrenheit(temp_c)
        rapport = weerrapport(temp_c, wind, vocht)

        print(f"Het is {temp_c:.1f}C ({temp_f:.1f}F)")
        print(rapport)
        print(f"Gem. temp tot nu toe is {gemiddelde:.1f}")
        print("==============================")