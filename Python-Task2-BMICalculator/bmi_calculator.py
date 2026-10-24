
def get_positive_number(prompt):
    """Ask the user for a valid positive number."""
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Error: Value must be greater than zero.")
                continue

            return value

        except ValueError:
            print("Error: Please enter a valid number.")


def calculate_bmi(weight, height):
    """Calculate BMI using kilograms and metres."""
    return weight / (height ** 2)


def classify_bmi(bmi):
    """Return a category based on standard adult BMI cutoffs."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 38)
    print("       BMI CALCULATOR")
    print("=" * 38)
    print("Enter weight in kilograms and height in metres.")

    while True:
        weight = get_positive_number("Enter weight (kg): ")
        height = get_positive_number("Enter height (m): ")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print("\n--- Your Result ---")
        print(f"Weight   : {weight:.2f} kg")
        print(f"Height   : {height:.2f} m")
        print(f"BMI      : {bmi:.2f}")
        print(f"Category : {category}")

        again = input(
            "\nCalculate again? (y/n): "
        ).strip().lower()

        if again != "y":
            print("Thank you for using BMI Calculator!")
            break


if __name__ == "__main__":
    main()

