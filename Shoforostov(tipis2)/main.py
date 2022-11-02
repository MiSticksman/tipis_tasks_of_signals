import matplotlib.pyplot as plt
import os

from modulation import *


if __name__ == '__main__':

    colors = ['r', 'g', 'b']
    modulation_names = ["am", "fm", "pm"]
    spectrum_names = ["am spectrum", "fm spectrum", "pm spectrum"]

    freq = 2
    amplitude = 5

    plt.figure(figsize=(16, 10))

    am = amplitude_modulation(unipolar_meander, freq=freq, amplitude=amplitude)
    ams_x, ams_y = modulation_spectrum(modulation=am)

    fm = frequency_modulation(freq=freq)
    fms_x, fms_y = modulation_spectrum(modulation=fm)

    pm = phase_modulation(freq=freq)
    pms_x, pms_y = modulation_spectrum(modulation=pm)

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

    ams_y_clean = spectrum_with_main_frequencies(am_spectrum=ams_y)
    plt.subplot(2, 2, 1)
    plt.plot(ams_x, np.abs(ams_y_clean))
    plt.title('am spectrum with main frequencies')
    plt.ylabel('amplitude')
    plt.xlabel('freq')
    plt.xlim(0, 25)

    ams_synthesis = synthesis_of_am_signal(ams_y_clean)
    plt.subplot(2, 2, 2)
    plt.plot(TIME, ams_synthesis)
    plt.title('synthesis of am signal')
    plt.ylabel('amplitude')
    plt.xlabel('time')

    meander = unipolar_meander(freq, amplitude=1)
    meander[0] = 0
    plt.subplot(2, 2, 3)
    plt.plot(TIME, meander)
    plt.title('modulating signal')
    plt.ylabel('amplitude')
    plt.xlabel('time')

    filtering = filtering_of_signal(ams_synthesis)
    filtering[0] = 0
    plt.subplot(2, 2, 4)
    plt.plot(TIME, filtering)
    plt.title('filtered signal')
    plt.ylabel('amplitude')
    plt.xlabel('time')

    plt.savefig(images + '/synthesisAndFiltration.jpg')

    plt.show()

