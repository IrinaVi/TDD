def converter(sound_wave, lower_limit=40):
    adjusted_sound_wave = []
    for frequency in sound_wave:
        if frequency < lower_limit:
            adjusted_sound_wave.append(lower_limit)
        elif frequency > 1000:
            adjusted_sound_wave.append(1000)
        else:
            adjusted_sound_wave.append(frequency)
    return adjusted_sound_wave