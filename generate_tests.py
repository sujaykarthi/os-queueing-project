import csv
import random

from mm1 import calculate_mm1


def create_test_cases():

    test_cases = []

    # --------------------------------------------------
    # STABLE CASES: λ < μ
    # --------------------------------------------------

    stable_cases = [
        (0.1, 20.0, 0),
        (0.1, 20.0, 20),
        (1.0, 2.0, 0),
        (1.0, 2.0, 10),
        (5.0, 10.0, 5),
        (9.0, 10.0, 10),
        (9.9, 10.0, 20),
        (9.99, 10.0, 20),
        (0.01, 0.02, 1),
        (5.55, 5.56, 15),
    ]

    test_cases.extend(stable_cases)

    # Add random stable cases until we have 80
    while len(test_cases) < 80:

        lambda_rate = round(
            random.uniform(0.01, 10.0),
            2
        )

        mu_rate = round(
            random.uniform(lambda_rate + 0.01, 20.0),
            2
        )

        n = random.randint(0, 20)

        test_cases.append(
            (lambda_rate, mu_rate, n)
        )

    # --------------------------------------------------
    # UNSTABLE CASES: λ >= μ
    # --------------------------------------------------

    unstable_cases = [
        (5.0, 5.0, 0),       # λ = μ
        (5.0, 5.0, 10),
        (10.0, 5.0, 5),
        (15.0, 10.0, 10),
        (20.0, 1.0, 20),
    ]

    test_cases.extend(unstable_cases)

    # Add random unstable cases until we have 100
    while len(test_cases) < 100:

        mu_rate = round(
            random.uniform(0.01, 10.0),
            2
        )

        lambda_rate = round(
            random.uniform(mu_rate, 20.0),
            2
        )

        n = random.randint(0, 20)

        test_cases.append(
            (lambda_rate, mu_rate, n)
        )

    return test_cases


def generate_test_vectors():

    filename = "mm1_test_vectors.csv"

    fieldnames = [
        "test_id",
        "lambda_rate",
        "mu_rate",
        "n",
        "stable",
        "rho",
        "P0",
        "Pn",
        "L",
        "Lq",
        "W",
        "Wq"
    ]

    test_cases = create_test_cases()

    with open(filename, "w", newline="") as csvfile:

        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for test_id, (lambda_rate, mu_rate, n) in enumerate(
            test_cases,
            start=1
        ):

            results = calculate_mm1(
                lambda_rate,
                mu_rate,
                n
            )

            writer.writerow({
                "test_id": test_id,
                "lambda_rate": lambda_rate,
                "mu_rate": mu_rate,
                "n": n,
                "stable": results["stable"],
                "rho": results["rho"],
                "P0": results.get("P0", ""),
                "Pn": results.get("Pn", ""),
                "L": results.get("L", ""),
                "Lq": results.get("Lq", ""),
                "W": results.get("W", ""),
                "Wq": results.get("Wq", "")
            })

    print("\nSuccessfully generated 100 test vectors.")
    print("80 stable + 20 unstable")
    print(f"Saved to: {filename}")


if __name__ == "__main__":
    generate_test_vectors()