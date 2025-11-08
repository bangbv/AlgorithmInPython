import numpy as np

def softmax(z):
    z = np.asarray(z) # convert input to numpy array
    z = z - z.max()           # stability
    print(f"numpy array z after stability: {z}")
    exp_z = np.exp(z) # exponentiation
    print(f"exp_z: {exp_z}")
    # sum of exponentials
    print(f"sum of exp_z: {exp_z.sum()}")
    result = exp_z / exp_z.sum() # softmax
    return result

if __name__ == "__main__":
    # Example usage
    input_mx = np.array([1, 2, 3])
    print(f"input_mx: {input_mx}")
    print(softmax(input_mx)) # → [0.8438 0.1131 0.0431]
