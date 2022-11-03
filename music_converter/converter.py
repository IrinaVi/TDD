def converter(sound_wave):
    adjusted_sound_wave = []
    for frequency in sound_wave:
        if frequency < 40:
            adjusted_sound_wave.append(40)
        elif frequency > 1000:
            adjusted_sound_wave.append(1000)
        else:
            adjusted_sound_wave.append(frequency)
    return adjusted_sound_wave