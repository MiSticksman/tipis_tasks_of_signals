from numpy.fft import fft, ifft, fftfreq, rfftfreq, rfft, irfft
from scipy.signal import butter, filtfilt

from constants import *
from scipy import signal


def unipolar_meander(freq=2, amplitude=1):
    return amplitude * (np.sign(np.sin(2 * np.pi * freq * TIME)) + 1) / 2


def amplitude_modulation(freq=2, amplitude=1):
    # meandr = amplitude * np.sin(2 * np.pi * freq * t)
    # for i in range(len(meandr)):
    #     if meandr[i] > 0:
    #         meandr[i] = amplitude
    #     else:
    #         meandr[i] = 0
    fc = 10
    carrier = 1 * np.cos((2 * np.pi * fc * TIME) + np.pi / 2)  # несущий высокочастотный сигнал
    # product1 = carrier * (1 + meandr)
    modulator = unipolar_meander(freq, amplitude)  # информационный сигнал
    am = carrier * (1 + modulator)
    return am


def amplitude_modulation_spectrum(freq=2):
    y = amplitude_modulation(freq)
    n = len(y)
    # frq = np.arange(n)
    # frq = frq[range(int(n))]
    frq = rfftfreq(n, 1 / FS)
    yf = rfft(y)  # деление на n - нормализация
    # yf = (np.abs(s1) ** 2) / n
    # yf = yf[range(int(n))]
    yf[0] = 0
    return frq, yf


def frequency_modulation(freq=2):
    carrier = 1 * np.cos((2 * np.pi * freq * TIME))  # base signal
    # phi = (CARRIER_FREQ * TIME) + (freq * carrier)
    # fm = np.sin(np.pi * phi)

    # fm = 1 * np.cos(2 * np.pi * fc * TIME + (5 * 1/freq) * np.sin(freq * TIME))

    fc = 10  # carrier frequency
    k = 0.05  # sensitivity
    phi = 2 * np.pi * fc * TIME + k * np.cumsum(carrier)  # phase
    fm = np.cos(phi)  # modulated signal
    return fm


def frequency_modulation_spectrum(freq=2):
    y = frequency_modulation(freq)
    n = len(y)
    frq = rfftfreq(n, 1 / FS)
    yf = rfft(y)
    # yf = (np.abs(s1) ** 2) / n
    # yf = yf[range(int(n))]
    yf[0] = 0
    return frq, yf


def phase_modulation(freq=2):
    fc = 10
    # carrier = 1 * np.cos((2 * np.pi * fc * TIME) + np.pi / 2)
    modulator = unipolar_meander(freq)
    beta = np.pi / 2
    pm = np.cos((fc * 2 * np.pi * TIME) + (beta * modulator))
    return pm


def phase_modulation_spectrum(freq=2):
    y = phase_modulation(freq)
    n = len(y)
    frq = rfftfreq(n, 1 / FS)
    yf = rfft(y)
    # yf = (np.abs(s1) ** 2) / n
    # yf = yf[range(int(n))]
    yf[0] = 0
    return frq, yf


def synthesis_of_amplitude_modulation_signal():
    x, yf = amplitude_modulation_spectrum()
    new_map = dict(sorted(dict(zip(yf, x)).items(), reverse=True))
    # y = list(new_map.keys())
    # for i in range(3, len(y)):
    #     y[i] = 0

    # yf = sorted(yf, reverse=True)
    # for i in range(3, len(yf)):
    #     yf[i] = 0
    # x = list(new_map.values())[:3]
    new_sig = irfft(yf)
    return new_sig

def spectrum_with_fundamental_frequencies():
    _, yf = amplitude_modulation_spectrum()
    yf_abs = np.abs(yf)
    index = yf_abs > 50
    yf_clean = index * yf
    return yf_clean

def s_o_a_m_s():
    yf_clean = spectrum_with_fundamental_frequencies()
    f_clean = irfft(yf_clean)
    return f_clean


def filtering_of_synthesized_am_signal():
    y = synthesis_of_amplitude_modulation_signal()
    new_sig = ifft(y)
    return new_sig

def ex():
    y = s_o_a_m_s()
    b, a = butter(3, 0.9)
    filtered = filtfilt(b, a, y)
    return filtered
