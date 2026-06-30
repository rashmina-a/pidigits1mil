import time
from mpmath import mp

try:
    import cupy as cp
except ImportError:
    cp = None

def display_banner():
    print("""
▗▄▄▖▗▄▄▄▖    ▗▄▄▄ ▗▄▄▄▖ ▗▄▄▖▗▄▄▄▖▗▄▄▄▖     ▗▄▄▖▗▄▄▄▖▗▖  ▗▖
▐▌ ▐▌ █      ▐▌  █  █  ▐▌     █    █      ▐▌   ▐▌   ▐▛▚▖▐▌
▐▛▀▘  █      ▐▌  █  █  ▐▌▝▜▌  █    █      ▐▌▝▜▌▐▛▀▀▘▐▌ ▝▜▌
▐▌  ▗▄█▄▖    ▐▙▄▄▀▗▄█▄▖▝▚▄▞▘▗▄█▄▖  █      ▝▚▄▞▘▐▙▄▄▖▐▌  ▐▌
    """)

def calculate_pi_digits_gpu(num_digits):
    if cp is None:
        raise RuntimeError("GPU support requested, but CuPy is not installed.")

    arctan_1_5 = cp.arctan(1.0 / 5.0)
    arctan_1_239 = cp.arctan(1.0 / 239.0)
    pi_estimate = 16.0 * arctan_1_5 - 4.0 * arctan_1_239
    return float(pi_estimate)


def calculate_pi_digits(num_digits, use_gpu=False):
    print("Pi calculation started...")
    print(f"Setting required precision (mp.dps) for {num_digits:,} digits.")
    print(f"Using GPU: {use_gpu}")

    mp.dps = num_digits + 2

    start_time = time.time()
    
    if use_gpu and cp is not None:
        pi_value = calculate_pi_digits_gpu(num_digits)
    elif use_gpu and cp is None:
        print("GPU mode requested but CuPy is not available. Falling back to CPU.")
        from mpmath import pi
        pi_value = pi
    else:
        from mpmath import pi
        pi_value = pi

    pi_string = str(pi_value)
    
    end_time = time.time()
    
    print("\n=========================================")
    print("✅ Calculation Complete!")
    print(f"Time taken: {end_time - start_time:.2f} seconds.")
    print("=========================================\n")

    result_digits = pi_string[2:2+num_digits]

    print(f"Successfully calculated {len(result_digits):,} digits of Pi.")
    
    snippet = result_digits[:100] + "..."
    print("--- Displaying first 100 digits (Snippet) ---")
    print(snippet)

    return result_digits

if __name__ == "__main__":
    display_banner()
    
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

    mode_input = input("Calculate normally (1) or use GPU (2)? [Default: 1]: ").strip()
    if mode_input == "2":
        use_gpu = True
    else:
        use_gpu = False

    calculate_pi_digits(TARGET_DIGITS, use_gpu=use_gpu)
