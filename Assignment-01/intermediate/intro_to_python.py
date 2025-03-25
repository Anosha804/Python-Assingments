PLANET_GRAVITY = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def calculate_weight(earth_weight, planet):
    """Calculates weight on a given planet based on Earth's weight."""
    gravity = PLANET_GRAVITY.get(planet)
    if gravity:
        return round(earth_weight * gravity, 2)
    return None 

def main():
    print("Planetary Weight Calculator")
    
    while True:
        try:
            earth_weight = float(input("Enter your weight on Earth (kg): "))
            if earth_weight > 0:
                break
            print(" Please enter a positive number.")
        except ValueError:
            print(" Invalid input! Please enter a number.")

    print("\n Available planets:", ", ".join(PLANET_GRAVITY.keys()))
    while True:
        planet = input("Enter a planet name: ").strip()
        if planet in PLANET_GRAVITY:
            break
        print(" Invalid planet! Please choose from the list.")

    weight_on_planet = calculate_weight(earth_weight, planet)
    print(f"\nYour weight on {planet} would be: {weight_on_planet} kg")

if __name__ == "__main__":
    main()
