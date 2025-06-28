import numpy as np
from scipy.fft import fft, ifft


def fourier_transform(arr_signals):
    # Compute the FFT (Fast Fourier Transform)
    fft_values = fft(arr_signals)
    return fft_values


def inverse_fourier_transform_arr(arr_fft_values):
    # Compute the inverse FFT
    print(f"fourier_transforms:inverse_fourier_transform:fft_values: {arr_fft_values}")
    reconstructed_signal = ifft(arr_fft_values)
    print(f"fourier_transforms:inverse_fourier_transform:reconstructed_signal: {reconstructed_signal}")
    # Since the inverse FFT may introduce small imaginary parts due to numerical errors, take the real part
    reconstructed_signal = np.abs(reconstructed_signal.real)
    return reconstructed_signal


def inverse_fourier_transform(fft_values):
    # Compute the inverse FFT
    print(f"fourier_transforms:inverse_fourier_transform:fft_values: {fft_values}")
    print(f"fourier_transforms:inverse_fourier_transform:type_fft_values: {type(fft_values)}")
    reconstructed_signal = ifft(fft_values)
    print(f"fourier_transforms:inverse_fourier_transform:reconstructed_signal: {reconstructed_signal}")
    # Since the inverse FFT may introduce small imaginary parts due to numerical errors, take the real part
    reconstructed_signal = np.abs(reconstructed_signal.real)
    return reconstructed_signal


if __name__ == "__main__":
    # Test with a single signal
    single_signal = [1, 2, 3, 4, 5]
    print(f"single_signal: {single_signal}")
    single_fft_value = fourier_transform(single_signal)
    print(f"single_fft_value: {single_fft_value}")
    reconstructed_signal = inverse_fourier_transform(single_fft_value)
    print(f"Reconstructed Single Signal: {reconstructed_signal}")