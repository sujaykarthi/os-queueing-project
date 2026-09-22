def calculate_mm1(lambda_rate, mu_rate, n):
    """
    Calculate standard M/M/1 queueing metrics.
    """

    if lambda_rate <= 0 or mu_rate <= 0:
        raise ValueError("λ and μ must be greater than zero.")

    if lambda_rate >= mu_rate:
        return {
            "stable": False,
            "rho": lambda_rate / mu_rate
        }

    rho = lambda_rate / mu_rate

    p0 = 1 - rho

    pn = (1 - rho) * (rho ** n)

    L = lambda_rate / (mu_rate - lambda_rate)

    Lq = (lambda_rate ** 2) / (
        mu_rate * (mu_rate - lambda_rate)
    )

    W = 1 / (mu_rate - lambda_rate)

    Wq = lambda_rate / (
        mu_rate * (mu_rate - lambda_rate)
    )

    return {
        "stable": True,
        "rho": rho,
        "P0": p0,
        "Pn": pn,
        "L": L,
        "Lq": Lq,
        "W": W,
        "Wq": Wq
    }