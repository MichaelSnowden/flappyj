from pydub import AudioSegment


def main():
    intervals = [{
        "start": 0.7,
        "end": 1.1,
    }, {
        "start": 1.1,
        "end": 1.6,
    }, {
        "start": 1.62,
        "end": 2.1,
    }, {
        "start": 2.0,
        "end": 2.3,
    }, {
        "start": 7.45,
        "end": 8.2
    }]

    song = AudioSegment.from_mp3("audio/link.mp3")

    for i, interval in enumerate(intervals):
        start = interval["start"]
        end = interval["end"]
        start_ms = start * 1000
        end_ms = end * 1000
        extract = song[start_ms:end_ms]
        extract.export("audio/link{}.mp3".format(i), format="mp3")

    extract = song[29.8 * 1000:31.5 * 1000]
    extract.export("audio/death.mp3", format="mp3")


if __name__ == '__main__':
    main()
