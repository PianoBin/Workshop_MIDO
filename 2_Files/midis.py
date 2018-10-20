from mido import MidiFile

mid = MidiFile('Happier_PB.mid')

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.is_meta:
            print(msg)
        #print(msg)