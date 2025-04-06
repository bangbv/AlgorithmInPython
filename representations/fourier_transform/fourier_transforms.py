import numpy as np
from scipy.fft import fft, fftfreq


def fourier_transform(arr_signals):
    # Compute the FFT (Fast Fourier Transform)
    arr_fft_values = []
    for signal in arr_signals:
        fft_values = fft(signal)
        arr_fft_values.append(fft_values)
    return arr_fft_values


def inverse_fourier_transform_arr(arr_fft_values):
    arr_reconstructed_signals = []
    for fft_values in arr_fft_values:
        # Compute the inverse FFT
        print(f"fourier_transforms:inverse_fourier_transform:fft_values: {fft_values}")
        print(f"fourier_transforms:inverse_fourier_transform:type_fft_values: {type(fft_values)}")
        reconstructed_signal = np.fft.ifft(fft_values)
        print(f"fourier_transforms:inverse_fourier_transform:reconstructed_signal: {reconstructed_signal}")
        # Since the inverse FFT may introduce small imaginary parts due to numerical errors, take the real part
        reconstructed_signal = np.abs(reconstructed_signal.real)
        arr_reconstructed_signals.append(reconstructed_signal)
    return arr_reconstructed_signals


def inverse_fourier_transform(fft_values):
    # Compute the inverse FFT
    print(f"fourier_transforms:inverse_fourier_transform:fft_values: {fft_values}")
    print(f"fourier_transforms:inverse_fourier_transform:type_fft_values: {type(fft_values)}")
    reconstructed_signal = np.fft.ifft(fft_values)
    print(f"fourier_transforms:inverse_fourier_transform:reconstructed_signal: {reconstructed_signal}")
    # Since the inverse FFT may introduce small imaginary parts due to numerical errors, take the real part
    reconstructed_signal = np.abs(reconstructed_signal.real)
    return reconstructed_signal
