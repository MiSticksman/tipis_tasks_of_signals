import matplotlib.pyplot as plt
import numpy as np

from modulation import *
import os

if __name__ == '__main__':

    colors = ['r', 'g', 'b']
    modulation_names = ["am", "fm", "pm"]
    spectrum_names = ["am spectrum", "fm spectrum", "pm spectrum"]

    plt.figure(figsize=(16, 10))

    freq = 2
    amplitude = 10

    am = amplitude_modulation(freq=freq, amplitude=amplitude)
    ams_x, ams_y = amplitude_modulation_spectrum(freq=freq)

    fm = frequency_modulation(freq=freq)
    fms_x, fms_y = frequency_modulation_spectrum(freq)

    pm = phase_modulation(freq=freq)
    pms_x, pms_y = phase_modulation_spectrum(freq=freq)

    modulations = [am, fm, pm]

    spectra_x = [ams_x, fms_x, pms_x]
    spectra_y = [ams_y, fms_y, pms_y]

    for i in range(3):
        plt.subplot(2, 3, i + 1)
        plt.plot(TIME, modulations[i], colors[i])
        plt.title(modulation_names[i])
        plt.ylabel('amplitude')
        plt.xlabel('time')

        plt.subplot(2, 3, i + 4)
        plt.title(spectrum_names[i])
        plt.plot(spectra_x[i], np.abs(spectra_y[i]), colors[i])
        plt.ylabel('power')
        plt.xlabel('freq')
        plt.xlim(0, 30)

    modulations = "modulations"
    if not os.path.isdir(modulations):
        os.mkdir(modulations)
    plt.savefig(modulations + '/modulation.jpg')

    plt.figure(figsize=(16, 10))

    synthesis = synthesis_of_amplitude_modulation_signal()
    plt.subplot(4, 1, 1)
    t1 = np.arange(0, 1, 1 / len(synthesis))
    plt.plot(t1, synthesis)

    # yf_clean = spectrum_with_fundamental_frequencies()
    # plt.subplot(4, 1, 2)
    # plt.plot(ams_x, np.abs(yf_clean))
    # plt.xlim(0, 30)

    f_clean = s_o_a_m_s()
    plt.subplot(4, 1, 2)
    plt.plot(TIME, f_clean)

    meander = unipolar_meander(freq, amplitude)
    meander[0] = 0
    plt.subplot(4, 1, 3)
    plt.plot(TIME, meander)

    filtering = filtering_of_synthesized_am_signal()
    filt = ex()
    plt.subplot(4, 1, 4)
    t2 = np.arange(0, 1, 1 / len(filtering))
    plt.plot(TIME, filt)

    plt.show()



# TODO обрезать am спектр (оставить три основные: 8, 10, 12 частоты), провести синтез сигнала (получится отдаленный модулирванный сигнал), затем провести фильтрацию этого сигнала (должен получиться менадр)

    # plt.subplot(2, 3, 1)
    # plt.plot(TIME, am, 'r')
    # plt.title("am")
    # plt.ylabel('amplitude')
    # plt.xlabel('time')
    #
    #
    # plt.subplot(2, 3, 4)
    # plt.plot(ams_x, ams_y, 'r')
    # plt.title("am spectrum")
    # plt.ylabel('power')
    # plt.xlabel('freq')
    # plt.xlim(0, 30)

    # plt.subplot(2, 3, 2)
    # plt.plot(TIME, fm, 'g')
    # plt.title("fm")
    # plt.ylabel('amplitude')
    # plt.xlabel('time')
    #
    #
    # plt.subplot(2, 3, 5)
    # plt.plot(fms_x, fms_y, 'g')
    # plt.title("fm spectrum")
    # plt.ylabel('power')
    # plt.xlabel('freq')
    # plt.xlim(0, 30)
    #
    #
    # plt.subplot(2, 3, 3)
    # plt.plot(TIME, pm, 'b')
    # plt.title("pm")
    # plt.ylabel('amplitude')
    # plt.xlabel('time')
    #
    #
    # plt.subplot(2, 3, 6)
    # plt.plot(pms_x, pms_y, 'b')
    # plt.title("pm spectrum")
    # plt.ylabel('power')
    # plt.xlabel('freq')
    # plt.xlim(0, 30)

