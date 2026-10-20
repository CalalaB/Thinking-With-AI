"""Convert a temperature in Celsius to Fahrenheit and Kelvin."""

import math

# Absolute zero is the lowest possible temperature, so no valid
# Celsius reading can go below it.
ABSOLUTE_ZERO_C = -273.15
KELVIN_OFFSET = 273.15


def convert_temp(celsius):
    """Return the given Celsius temperature as (fahrenheit, kelvin)."""
    fahrenheit = celsius * 9 / 5 + 32
    kelvin = celsius + KELVIN_OFFSET
    return fahrenheit, kelvin


def parse_celsius(text):
    """Turn user input into a valid Celsius value.

    Raise ValueError with a helpful message if the input is empty,
    not a number, not finite, or below absolute zero.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError('You did not enter anything.')
    if ',' in cleaned:
        # A comma could be a decimal point (36,6) or a thousands
        # separator (1,000), so ask the user to be clear instead of
        # guessing.
        raise ValueError('Use a full stop for decimals, for example 36.6.')

    try:
        celsius = float(cleaned)
    except ValueError:
        raise ValueError(
            f"'{cleaned}' is not a number. Enter digits only, for example 25."
        ) from None

    # float() accepts 'nan' and 'inf', which are not real temperatures.
    if not math.isfinite(celsius):
        raise ValueError('Please enter an actual temperature.')
    if celsius < ABSOLUTE_ZERO_C:
        raise ValueError(
            f'{celsius} °C is below absolute zero ({ABSOLUTE_ZERO_C} °C).'
        )
    return celsius


def main():
    """Ask for a temperature until the input is valid, then show results."""
    while True:
        text = input('Enter a temperature in Celsius: ')
        try:
            celsius = parse_celsius(text)
            break
        except ValueError as error:
            print(f'Invalid input: {error} Please try again.\n')

    fahrenheit, kelvin = convert_temp(celsius)

    # Two decimal places hides floating-point noise such as
    # 97.88000000000001 and keeps the three lines aligned.
    print(f'Celsius:    {celsius:.2f} °C')
    print(f'Fahrenheit: {fahrenheit:.2f} °F')
    print(f'Kelvin:     {kelvin:.2f} K')


# Run main() only when this file is run directly, not when it is imported.
if __name__ == '__main__':
    main()
