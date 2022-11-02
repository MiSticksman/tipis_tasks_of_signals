from numpy import sign
from numpy.fft import rfftfreq, rfft, irfft
from scipy.signal import butter, filtfilt

from constants import *


def unipolar_meander(freq=2, amplitude=1):
    return amplitude * (np.sign(np.sin(2 * np.pi * freq * TIME)) + 1) / 2


def amplitude_modulation(freq=2, amplitude=1):
    fc = 10
    carrier = 1 * np.cos((2 * np.pi * fc * TIME) + np.pi / 2)  # несущий высокочастотный сигнал
    modulator = unipolar_meander(freq, amplitude)  # информационный сигнал
    am = carrier * (1 + modulator)
    return am


def frequency_modulation(freq=2):
    carrier = 1 * np.cos((2 * np.pi * freq * TIME))  # base signal
    fc = 10  # carrier frequency
    k = 0.05  # sensitivity
    phi = 2 * np.pi * fc * TIME + k * np.cumsum(carrier)  # phase
    fm = np.cos(phi)  # modulated signal
    return fm


def phase_modulation(freq=2):
    fc = 10
    # carrier = 1 * np.cos((2 * np.pi * fc * TIME) + np.pi / 2)
    modulator = unipolar_meander(freq)
    beta = np.pi / 2
    pm = np.cos((fc * 2 * np.pi * TIME) + (beta * modulator))
    return pm


def modulation_spectrum(modulation, freq=2):
    y = modulation(freq)
    n = len(y)
    frq = rfftfreq(n, 1 / FS)
    yf = rfft(y)  # деление на n - нормализация
    yf[0] = 0
    return frq, yf


# def amplitude_modulation_spectrum(freq=2):
#     y = amplitude_modulation(freq)
#     n = len(y)
#     # frq = np.arange(n)
#     # frq = frq[range(int(n))]
#     frq = rfftfreq(n, 1 / FS)
#     yf = rfft(y)  # деление на n - нормализация
#     # yf = (np.abs(s1) ** 2) / n
#     # yf = yf[range(int(n))]
#     yf[0] = 0
#     return frq, yf


# def frequency_modulation_spectrum(freq=2):
#     y = frequency_modulation(freq)
#     n = len(y)
#     frq = rfftfreq(n, 1 / FS)
#     yf = rfft(y)
#     yf[0] = 0
#     return frq, yf


# def phase_modulation_spectrum(freq=2):
#     y = phase_modulation(freq)
#     n = len(y)
#     frq = rfftfreq(n, 1 / FS)
#     yf = rfft(y)
#     yf[0] = 0
#     return frq, yf


def synthesis_of_amplitude_modulation_signal():
    _, yf = modulation_spectrum(amplitude_modulation)
    new_sig = irfft(yf)
    return new_sig


def spectrum_with_main_frequencies():
    _, yf = modulation_spectrum(amplitude_modulation)
    yf_abs = np.abs(yf)
    index = yf_abs > 50
    yf_clean = index * yf
    return yf_clean


def synthesis_of_am_signal():
    yf_clean = spectrum_with_main_frequencies()
    f_clean = irfft(yf_clean)
    return f_clean


def execute_filter_signal(synthesized_signal):
    y = synthesized_signal()
    filtered = []
    b, a = butter(4, 0.008)
    for i in filtfilt(b, a, y):
        filtered.append((sign(i) + 1) / 2)
    return filtered
