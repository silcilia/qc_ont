
from automation.device_detector import run_detection


if __name__ == "__main__":

    ip_address = input("Masukkan IP Address ONT: ").strip()

    print("\nMemulai proses Device Detection...\n")

    result = run_detection(ip_address)

    print("========== HASIL DEVICE DETECTION ==========")

    for key, value in result.items():
        print(f"{key}: {value}")

    print("============================================")
