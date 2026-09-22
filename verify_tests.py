import csv

from mm1 import calculate_mm1


def verify_test_vectors(filename="mm1_test_vectors.csv"):

    passed = 0
    failed = 0

    with open(filename, "r", newline="") as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            test_id = int(row["test_id"])

            lambda_rate = float(row["lambda_rate"])
            mu_rate = float(row["mu_rate"])
            n = int(row["n"])

            expected = calculate_mm1(
                lambda_rate,
                mu_rate,
                n
            )

            # Verify stability
            csv_stable = row["stable"] == "True"

            if csv_stable != expected["stable"]:
                print(f"FAIL - Test {test_id}: stability mismatch")
                failed += 1
                continue

            # Verify rho
            csv_rho = float(row["rho"])

            if abs(csv_rho - expected["rho"]) > 1e-12:
                print(f"FAIL - Test {test_id}: rho mismatch")
                failed += 1
                continue

            # Stable test cases
            if expected["stable"]:

                metrics = [
                    "P0",
                    "Pn",
                    "L",
                    "Lq",
                    "W",
                    "Wq"
                ]

                test_passed = True

                for metric in metrics:

                    csv_value = float(row[metric])
                    expected_value = expected[metric]

                    if abs(csv_value - expected_value) > 1e-12:
                        print(
                            f"FAIL - Test {test_id}: "
                            f"{metric} mismatch"
                        )
                        test_passed = False

                # Verify queueing identities
                if abs(
                    expected["L"] -
                    lambda_rate * expected["W"]
                ) > 1e-12:
                    print(
                        f"FAIL - Test {test_id}: "
                        "L = λW verification failed"
                    )
                    test_passed = False

                if abs(
                    expected["Lq"] -
                    lambda_rate * expected["Wq"]
                ) > 1e-12:
                    print(
                        f"FAIL - Test {test_id}: "
                        "Lq = λWq verification failed"
                    )
                    test_passed = False

                if test_passed:
                    passed += 1
                else:
                    failed += 1

            else:
                passed += 1

    print("\n========== VERIFICATION ==========")
    print(f"Tests passed : {passed}")
    print(f"Tests failed : {failed}")
    print("==================================")

    if failed == 0:
        print("\nALL TESTS PASSED.")
    else:
        print("\nVERIFICATION FAILED.")


if __name__ == "__main__":
    verify_test_vectors()