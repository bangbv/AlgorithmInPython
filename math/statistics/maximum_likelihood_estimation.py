import numpy as np


def normal_mle(X):
    """
    Perform Maximum Likelihood Estimation for a normal distribution.

    Parameters:
    X: array-like, observed data (1D array)

    Returns:
    mu_mle: float, the MLE estimate of the mean
    sigma_mle: float, the MLE estimate of the standard deviation
    """
    # Estimate the mean (MLE for mean is the sample mean)
    mu_mle = np.mean(X)

    # Estimate the variance (MLE for variance is the sample variance)
    # Note: we use np.var with ddof=0 for population variance (MLE variance)
    variance_mle = np.var(X, ddof=0)

    # Standard deviation is the square root of the variance
    sigma_mle = np.sqrt(variance_mle)

    return mu_mle, sigma_mle


if __name__ == "__main__":
    # Example usage
    X = np.array([1.2, 1.8, 2.1, 1.9, 1.5])  # Example observed data

    # Perform MLE
    mu_mle, sigma_mle = normal_mle(X)

    print("MLE for Mean (mu):", mu_mle)
    print("MLE for Standard Deviation (sigma):", sigma_mle)

