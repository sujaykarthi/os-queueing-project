import random


def generate_inputs():
    """
    Generate a stable M/M/1 test case.

    Returns:
        lambda_rate: arrival rate
        mu_rate:     service rate
        n:            number of customers
    """

    lambda_rate = round(random.uniform(1.0, 10.0), 2)

    # Ensure λ < μ so that the M/M/1 system is stable.
    mu_rate = round(random.uniform(lambda_rate + 0.1, 20.0), 2)

    n = random.randint(0, 20)

    return lambda_rate, mu_rate, n