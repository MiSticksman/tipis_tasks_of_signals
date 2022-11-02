from numpy import sign
from numpy.fft import rfftfreq, rfft, irfft
from scipy.signal import butter, filtfilt

from constants import *


def unipolar_meander(freq=2, amplitude=1):
    return amplitude * (np.sign(np.sin(2 * np.pi * freq * TIME)) + 1) / 2


def amplitude_modulation(modulator, freq=2, amplitude=1):
    fc = 10
    carrier = 1 * np.cos((2 * np.pi * fc * TIME) + np.pi / 2)  # несущий высокочастотный сигнал
    modulator = modulator(freq, amplitude)  # информационный сигнал
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
    modulator = unipolar_meander(freq)
    beta = np.pi / 2
    pm = np.cos((fc * 2 * np.pi * TIME) + (beta * modulator))
    return pm


def modulation_spectrum(modulation):
    n = len(modulation)
    frq = rfftfreq(n, 1 / FS)
    yf = rfft(modulation)
    yf[0] = 0
    return frq, yf


# def amplitude_modulation_spectrum(am):
#     n = len(am)
#     # frq = np.arange(n)
#     # frq = frq[range(int(n))]
#     frq = rfftfreq(n, 1 / FS)
#     yf = rfft(am)
#     # yf = (np.abs(s1) ** 2) / n
#     # yf = yf[range(int(n))]
#     yf[0] = 0
#     return frq, yf
#
#
# def frequency_modulation_spectrum(fm):
#     n = len(fm)
#     frq = rfftfreq(n, 1 / FS)
#     yf = rfft(fm)
#     yf[0] = 0
#     return frq, yf
#
#
# def phase_modulation_spectrum(pm):
#     n = len(pm)
#     frq = rfftfreq(n, 1 / FS)
#     yf = rfft(pm)
#     yf[0] = 0
#     return frq, yf


def spectrum_with_main_frequencies(am_spectrum):
    # yf = am_spectrum[1]
    yf_abs = np.abs(am_spectrum)
    average = max(yf_abs) / 2
    index = yf_abs > average
    yf_clean = index * am_spectrum
    return yf_clean


def synthesis_of_am_signal(spectrum_with_main_frequencies):
    f_clean = irfft(spectrum_with_main_frequencies)
    return f_clean


def filtering_of_signal(synthesized_signal):
    filtered = []
    b, a = butter(4, 0.008)
    for i in filtfilt(b, a, synthesized_signal):
        filtered.append((sign(i) + 1) / 2)
    return filtered
