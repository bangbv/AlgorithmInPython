import numpy as np

def gaussian_log_likelihood(X, mu, sigma):
    """
    Compute the log likelihood of the data X given a Gaussian distribution
    with mean mu and standard deviation sigma.

    Parameters:
    X: array-like, observed data
    mu: float, mean of the Gaussian
    sigma: float, standard deviation of the Gaussian

    Returns:
    log_likelihood: float, the log likelihood of the data X
    """
    n = len(X)  # number of data points
    log_likelihood = - n * np.log(2 * np.pi * (sigma**2)) - np.sum((X - mu) ** 2) / (2* sigma ** 2)
    return log_likelihood

if __name__ == "__main__":
    # Example data
    X = np.array([1.2, 1.8, 2.1, 1.9, 1.5])  # Observed data
    mu = X.mean()  # Estimated mean
    print(f"Estimated mean: {mu}")
    sigma = X.std()  # Estimated standard deviation
    print(f"Estimated standard deviation: {sigma}")

    # Calculate the log likelihood
    log_likelihood = gaussian_log_likelihood(X, mu, sigma)
    print("Gaussian Log Likelihood: ", log_likelihood)
