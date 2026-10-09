import json
import urllib.request
import weerstation
import smart_app_controller


def haal_live_weer_utrecht():
    """Haalt actuele weergegevens op via een GET request naar de Open-Meteo REST API."""
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.0908&longitude=5.1222&current=temperature_2m,wind_speed_10m"
    print("\nLive weergegevens ophalen voor Utrecht via API...")

    try:
        request = urllib.request.Request(url, headers={"User-Agent": "SmartApp/1.0"})
        with urllib.request.urlopen(request, timeout=5) as response:
            data_bytes = response.read()
            data_tekst = data_bytes.decode("utf-8")

            # JSON parsen naar een Python dictionary (PROG7 / Spronck H13)
            weer_dict = json.loads(data_tekst)

            huidig = weer_dict.get("current", {})
            temperatuur = huidig.get("temperature_2m")
            windsnelheid = huidig.get("wind_speed_10m")
            tijdstip = huidig.get("time")

            print("====================================")
            print("      LIVE WEER UTRECHT (API)       ")
            print("====================================")
            print(f"Tijdmeting   : {tijdstip}")
            print(f"Temperatuur  : {temperatuur} °C")
            print(f"Windsnelheid : {windsnelheid} km/u")
            print("====================================")
    except urllib.error.URLError as err:
        print(f"Netwerkfout bij verbinden met API: {err}")
    except Exception as fout:
        print(f"Er ging iets mis bij de API-aanroep: {fout}")


def hoofdmenu():
    """Platform controller met keuzemenu (while-loop en condities)."""
    while True:
        print("\n==================================")
        print("    SMART APP PLATFORM HOOFDMENU  ")
        print("==================================")
        print("1. Start Weerstation (Sprint 1)")
        print("2. Start Smart App Controller (Sprint 2)")
        print("3. Bekijk live weer in Utrecht via API (Sprint 3)")
        print("4. Afsluiten")

        keuze = input("Maak een keuze (1-4): ").strip()

        if keuze == "1":
            weerstation.weerstation()
        elif keuze == "2":
            smart_app_controller.smart_app_controller()
        elif keuze == "3":
            haal_live_weer_utrecht()
        elif keuze == "4":
            print("Applicatie beëindigd. Tot ziens!")
            break
        else:
            print("Ongeldige keuze. Kies 1, 2, 3 of 4.")


if __name__ == "__main__":
    hoofdmenu()