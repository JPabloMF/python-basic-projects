gravity_planets = {
    "mercury": 3.7,
    "venus": 8.87,
    "earth": 9.8,
    "mars": 3.7,
    "jupiter": 24.79,
    "saturn": 10.44,
    "uranus": 8.87,
    "neptune": 11.15
}


def options():
    print("Choose a planet:")
    print("Mercury")
    print("Venus")
    print("Earth")
    print("Mars")
    print("Jupiter")
    print("Saturn")
    print("Uranus")
    print("Neptune")

def get_person_weight(planet, weight):
    if planet.lower() in gravity_planets:
        final_weight = weight * \
            gravity_planets[planet.lower()] / gravity_planets["earth"]
        print("Your final weight in",
              planet.lower(), "is", final_weight)
    else:
        print("You type an wrong planet")
        init()


def init():
    global options
    options()
    planet = input("Type a planet: ")
    while planet == "":
        planet = input("Type a planet")

    weight = input("Type your weight in KG")
    while weight == "":
        weight = input("Type your weight in KG")

    get_person_weight(planet=planet, weight=float(weight))


init()
