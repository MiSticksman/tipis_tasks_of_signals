import matplotlib.pyplot as plt
import numpy as np

from modulation import *
import os

if __name__ == '__main__':

    colors = ['r', 'g', 'b']
    modulation_names = ["am", "fm", "pm"]
    spectrum_names = ["am spectrum", "fm spectrum", "pm spectrum"]

    freq = 2
    amplitude = 3

    plt.figure(figsize=(16, 10))

    am = amplitude_modulation(freq=freq, amplitude=amplitude)
    ams_x, ams_y = modulation_spectrum(amplitude_modulation, freq=freq)

    fm = frequency_modulation(freq=freq)
    fms_x, fms_y = modulation_spectrum(frequency_modulation, freq)

    pm = phase_modulation(freq=freq)
    pms_x, pms_y = modulation_spectrum(phase_modulation, freq=freq)

    modulations = [am, fm, pm]

    spectra_x = [ams_x, fms_x, pms_x]
    spectra_y = [ams_y, fms_y, pms_y]

    images = 'images'
    if not os.path.isdir(images):
        os.mkdir(images)

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

    plt.savefig(images + '/modulations.jpg')

    plt.figure(figsize=(16, 10))

    yf_clean = spectrum_with_main_frequencies()
    plt.subplot(2, 2, 1)
    plt.plot(ams_x, np.abs(yf_clean))
    plt.xlim(0, 25)

    f_clean = synthesis_of_am_signal()
    plt.subplot(2, 2, 2)
    plt.plot(TIME, f_clean)

    meander = unipolar_meander(freq, amplitude=1)
    # meander[0] = 0
    plt.subplot(2, 2, 3)
    plt.plot(TIME, meander)

    filtering = execute_filter_signal(synthesis_of_am_signal)
    plt.subplot(2, 2, 4)
    t2 = np.arange(0, 1, 1 / len(filtering))
    plt.plot(TIME, filtering)

    plt.savefig(images + '/synthesisAndFiltration.jpg')

    plt.show()

