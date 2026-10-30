import numpy as np
import matplotlib.pyplot as plt

def signal(a, n):
    return a ** n * np.where(n >= 0, 1, 0)

def fourier_signal(a, n, N):
    return (1 - a * np.exp(-1j * 2 * np.pi / N * n)) ** (-1)

if __name__ == "__main__":
    fig, (ax1, ax2) = plt.subplots(2, 1, tight_layout=True)

    N = 16
    a = 0.9
    n = np.arange(0, N)
    w = 2 * np.pi * n / N
    w2 = 2*np.pi * np.arange(6 * N) / (6 * N)


    s = signal(a, n)
    fs = fourier_signal(a, n, N)
    fs_ifft = np.fft.ifft(fs)
    fsn = np.fft.fft(fs_ifft, n=6*N)

    ax1.plot(w, np.abs(fs))
    ax1.plot(w2, np.abs(fsn))
    ax2.plot(n, s)
    ax2.plot(n, fs_ifft)
    ax1.set_xlabel("Frequency [Hz]")
    ax1.set_ylabel("Magnitude")
    ax2.set_xlabel("Time index (n)")
    ax2.set_ylabel("Amplitude")
    ax1.set_title("Magnitude of Spectra")
    ax2.set_title("Signal Amplitudes")
    plt.show()

    fig, (ax1, ax2) = plt.subplots(2, 1, tight_layout=True)

    N = 8
    a = 0.8
    n = np.arange(0, N)
    w = 2 * np.pi * n / N
    w2 = 2*np.pi * np.arange(6 * N) / (6 * N)

    s = signal(a, n)
    fs = fourier_signal(a, n, N)
    fs_ifft = np.fft.ifft(fs)
    fsn = np.fft.fft(fs_ifft, n=6*N)

    ax1.plot(w, np.abs(fs))
    ax1.plot(w2, np.abs(fsn))
    ax2.plot(n, s)
    ax2.plot(n, fs_ifft)
    ax1.set_xlabel("Frequency [Hz]")
    ax1.set_ylabel("Magnitude")
    ax2.set_xlabel("Time index (n)")
    ax2.set_ylabel("Amplitude")
    ax1.set_title("Magnitude of Spectra")
    ax2.set_title("Signal Amplitudes")
    plt.show()

    fig, (ax1, ax2) = plt.subplots(2, 1, tight_layout=True)

    N = 64
    a = 0.8
    n = np.arange(0, N)
    w = 2 * np.pi * n / N
    w2 = 2*np.pi * np.arange(6 * N) / (6 * N)

    s = signal(a, n)
    fs = fourier_signal(a, n, N)
    fs_ifft = np.fft.ifft(fs)
    fsn = np.fft.fft(fs_ifft, n=6*N)

    ax1.plot(w, np.abs(fs))
    ax1.plot(w2, np.abs(fsn))
    ax2.plot(n, s)
    ax2.plot(n, fs_ifft)
    ax1.set_xlabel("Frequency [Hz]")
    ax1.set_ylabel("Magnitude")
    ax2.set_xlabel("Time index (n)")
    ax2.set_ylabel("Amplitude")
    ax1.set_title("Magnitude of Spectra")
    ax2.set_title("Signal Amplitudes")
    plt.show()
