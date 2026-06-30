import time
from mpmath import pi, mp

def calculate_pi_digits(num_digits):
    """
    Calculates and returns the first 'num_digits' digits of Pi.
    The function uses mpmath to do the heavy lifting.
    """
    print("Pi calculation started...")
    print(f"Setting required precision (mp.dps) for {num_digits:,} digits.")

    mp.dps = num_digits + 2 

    start_time = time.time()
    
    # mpmath.pi returns a high-precision Decimal object which can be converted to string
    pi_value = pi
    
    # Convert the result to a string
    pi_string = str(pi_value)
    
    end_time = time.time()
    
    print("\n=========================================")
    print("✅ Calculation Complete!")
    print(f"Time taken: {end_time - start_time:.2f} seconds.")
    print("=========================================\n")

    # The string representation from mpmath usually includes the '3.' prefix.
    # We slice it to get exactly the requested digits after the decimal point (index 1 onwards).
    # Since we set dps = num_digits + 2, the length will be correct.
    result_digits = pi_string[2:2+num_digits]

    print(f"Successfully calculated {len(result_digits):,} digits of Pi.")
    
    # Print only a snippet to avoid overwhelming the output buffer.
    snippet = result_digits[:100] + "..."
    print("--- Displaying first 100 digits (Snippet) ---")
    print(snippet)

    return result_digits # Return the full string for use in other programs

if __name__ == "__main__":
    default_digits = 1000000
    user_input = input("How much digits you want to generate [Be careful, generating too many digits can take a long time!] [ Leave blank for default 1 Million ]: ").strip()
    if user_input == "":
        TARGET_DIGITS = default_digits
    else:
        try:
            TARGET_DIGITS = int(user_input.replace(",", ""))
        except ValueError:
            print("Invalid input. Using default 1 Million digits.")
            TARGET_DIGITS = default_digits

    calculate_pi_digits(TARGET_DIGITS)
