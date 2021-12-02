import sys
from mido import MidiFile


def decode_midi(midi_path):
    """
    Turn a midi track into a list of tuples

    :param midi_path: string
    :return: list
    """
    midi = MidiFile(midi_path, clip=True)
    final_array = []
    for note in midi.play():
        if note.time > 0:
            true_time = note.time
            print(note)
            if note.type == 'note_on':
                final_array.append((False, 0, true_time))
            else:
                final_array.append((True, note.note, true_time))
    return final_array


def write_to_file(path, text):
    """
    Write something to a file.

    :param path: string
    :param text: any
    :return: None
    """
    with open(path, "w") as file:
        file.write(str(text))


def main(midi_path, output_path):
    """
    Drives to program

    :param midi_path: string
    :param output_path: string
    :return: None
    """
    midi_array = decode_midi(midi_path)
    write_to_file(output_path, midi_array)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
