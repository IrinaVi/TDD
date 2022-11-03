def converter(sound_wave, lower_limit=40, upper_limit=1000):
    adjusted_sound_wave = []
    if len(sound_wave) == 0:
        raise ValueError("Wrong input!")
    for frequency in sound_wave:
        if frequency < lower_limit:
            adjusted_sound_wave.append(lower_limit)
        elif frequency > upper_limit:
            adjusted_sound_wave.append(upper_limit)
        else:
            adjusted_sound_wave.append(frequency)
    return adjusted_sound_wave