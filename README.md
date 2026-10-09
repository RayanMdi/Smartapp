ClimatePulse — SmartHome Connect Platform

Een Python-platform voor binnenklimaatbeheer, actuatorsturing en weermonitoring.


Onderdelen en Structuur
Het project is modulair gebouwd om de rubric eisen:

weerstation.py: Verwerkt handmatige weersmetingen van maximaal 7 dagen, berekent gevoelstemperatuur en Fahrenheit, geeft klimaatadviezen en houdt een doorlopend gemiddelde bij.
smart_app_controller.py: Leest dagdata in uit input.txt, berekent actuatorstanden voor de CV-ketel, ventilatie en bewatering, schrijft naar output.txt en bevat een overwrite functie met retourcodes.
main.py: Centraal platform met een interactief keuzemenu, foutafhandeling met try/except tegen crashes en data-ophaling via de Open-Meteo REST API (JSON).
input.txt: Databestand met dagelijkse metingen (datum, bezetting, doeltemperatuur, buitentemperatuur, neerslag).


Uitvoering van de applicatie
Zorg dat Python 3 geïnstalleerd is en start het centrale platform vanuit de hoofdmap:

```bash
python main.py
