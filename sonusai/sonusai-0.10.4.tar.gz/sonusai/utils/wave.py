from sonusai.mixture.types import AudioT


def write_wav(name: str, audio: AudioT) -> None:
    import wave

    from sonusai.mixture import CHANNEL_COUNT
    from sonusai.mixture import SAMPLE_BYTES
    from sonusai.mixture import SAMPLE_RATE

    with wave.open(name, mode='w') as f:
        f.setnchannels(CHANNEL_COUNT)
        f.setsampwidth(SAMPLE_BYTES)
        f.setframerate(SAMPLE_RATE)
        f.writeframesraw(audio)
