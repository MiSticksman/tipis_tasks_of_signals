from scipy.fft import fft, rfft
import matplotlib.pyplot as plt
import numpy as np

def harmonic_oscillation(frequency, amplitude=1, t=1, sample_rate=15000):
    x = np.linspace(0, t, num=t * sample_rate)
    y = amplitude * np.sin(2 * np.pi * frequency * x)
    return x, y


def unipolar_meander(frequency, amplitude=1, t=1, sample_rate=1000):
    x, y = harmonic_oscillation(frequency, amplitude, t, sample_rate)
    for i in range(len(y)):
        if y[i] > 0:
            y[i] = 1
        else:
            y[i] = 0
    return x, y


def spectr_of_harmonic(frequency, sample_rate):
    # n = len(y)
    # x = arange(sample_rate)
    # x = np.linspace(0, 1, num=sample_rate)
    _, s = harmonic_oscillation(frequency, sample_rate=sample_rate)
    n = len(s)

    # frq = x # * (sample_rate / n)
    frq = np.arange(n)
    frq = frq[range(int(n / 2))]
    s1 = fft(s)  # деление на n - нормализация
    yf = (np.abs(s1) ** 2) / n
    yf = yf[range(int(n / 2))]
    return frq, yf


def spectr_of_unipolar_meander(frequency, sample_rate):
    _, s = unipolar_meander(frequency, sample_rate=sample_rate)
    n = len(s)
    frq = np.arange(n)
    frq = frq[range(int(n / 2))]
    s1 = fft(s)  # деление на n - нормализация
    yf = (np.abs(s1) ** 2) / n
    yf = yf[range(int(n / 2))]
    yf[0] = 0
    return frq, yf


# решение полностью через scipy
# def spectr(y):
#     s = rfft(y)
#     yf = np.abs(s) / len(y)
#     yf[0] = 0
#     xf = rfftfreq(SAMPLE_RATE, 1 / SAMPLE_RATE)
#     return xf, yf


if __name__ == '__main__':
    plt.figure(figsize=(15, 10))

    x1_harmonic, y1_harmonic = harmonic_oscillation(1)
    x2_harmonic, y2_harmonic = harmonic_oscillation(2)
    x3_harmonic, y3_harmonic = harmonic_oscillation(4)
    x4_harmonic, y4_harmonic = harmonic_oscillation(8)

    ax_1 = plt.subplot(4, 4, 1)
    plt.plot(x1_harmonic, y1_harmonic)
    ax_2 = plt.subplot(4, 4, 2)
    plt.plot(x2_harmonic, y2_harmonic)
    ax_3 = plt.subplot(4, 4, 3)
    plt.plot(x3_harmonic, y3_harmonic)
    ax_4 = plt.subplot(4, 4, 4)
    plt.plot(x4_harmonic, y4_harmonic)

    ax_1.set(title='1')
    ax_2.set(title='2')
    ax_3.set(title='4')
    ax_4.set(title='8')

    x1_meander, y1_meander = unipolar_meander(1)
    x2_meander, y2_meander = unipolar_meander(2)
    x3_meander, y3_meander = unipolar_meander(4)
    x4_meander, y4_meander = unipolar_meander(8)

    ax_5 = plt.subplot(4, 4, 9)
    plt.plot(x1_meander, y1_meander)
    ax_6 = plt.subplot(4, 4, 10)
    plt.plot(x2_meander, y2_meander)
    ax_7 = plt.subplot(4, 4, 11)
    plt.plot(x3_meander, y3_meander)
    ax_8 = plt.subplot(4, 4, 12)
    plt.plot(x4_meander, y4_meander)

    plt.savefig('signals.png')

    SAMPLE_RATE = 15000

    plt.figure(figsize=(15, 10))
    x1_harmonic_spectr, y1_harmonic_spectr = spectr_of_harmonic(1, SAMPLE_RATE)
    x2_harmonic_spectr, y2_harmonic_spectr = spectr_of_harmonic(2, SAMPLE_RATE)
    x3_harmonic_spectr, y3_harmonic_spectr = spectr_of_harmonic(4, SAMPLE_RATE)
    x4_harmonic_spectr, y4_harmonic_spectr = spectr_of_harmonic(8, SAMPLE_RATE)

    ax_1 = plt.subplot(4, 4, 1)
    plt.plot(x1_harmonic_spectr, y1_harmonic_spectr)
    plt.xlim(-1, 10)
    ax_2 = plt.subplot(4, 4, 2)
    plt.plot(x2_harmonic_spectr, y2_harmonic_spectr)
    plt.xlim(0, 10)
    ax_3 = plt.subplot(4, 4, 3)
    plt.plot(x3_harmonic_spectr, y3_harmonic_spectr)
    plt.xlim(0, 10)
    ax_4 = plt.subplot(4, 4, 4)
    plt.plot(x4_harmonic_spectr, y4_harmonic_spectr)
    plt.xlim(0, 20)

    ax_1.set(title='1')
    ax_2.set(title='2')
    ax_3.set(title='4')
    ax_4.set(title='8')

    x1_meander_spectr, y1_meander_spectr = spectr_of_unipolar_meander(1, SAMPLE_RATE)
    x2_meander_spectr, y2_meander_spectr = spectr_of_unipolar_meander(2, SAMPLE_RATE)
    x3_meander_spectr, y3_meander_spectr = spectr_of_unipolar_meander(4, SAMPLE_RATE)
    x4_meander_spectr, y4_meander_spectr = spectr_of_unipolar_meander(8, SAMPLE_RATE)

    ax_5 = plt.subplot(4, 4, 9)
    plt.plot(x1_meander_spectr, y1_meander_spectr)
    plt.xlim(-1, 10)
    ax_6 = plt.subplot(4, 4, 10)
    plt.plot(x2_meander_spectr, y2_meander_spectr)
    plt.xlim(0, 10)
    ax_7 = plt.subplot(4, 4, 11)
    plt.plot(x3_meander_spectr, y3_meander_spectr)
    plt.xlim(0, 16)
    ax_8 = plt.subplot(4, 4, 12)
    plt.plot(x4_meander_spectr, y4_meander_spectr)
    plt.xlim(0, 26)

    plt.savefig('spectrs.png')

    plt.show()

    # другое решение - полностью через scipy
    # _, yf = harmonic_oscillation(frequency, sample_rate=SAMPLE_RATE)
    # spect_of_signals(frequency, yf, SAMPLE_RATE)
    # show()
    #
    #
    # _, y1 = harmonic_oscillation(frequency, sample_rate=SAMPLE_RATE)
    # _, y2 = unipolar_meander(frequency, sample_rate=SAMPLE_RATE)
    #
    #
    # xf, yf = spectr(y2)
    # plt.plot(xf, np.abs(yf))
    # plt.xlim(0, 10)
