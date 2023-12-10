import mido

# Get filename
print("Enter filename (without extension): ", end="")
filename = input()
input_file = mido.MidiFile(filename + ".mid")

# Get root note which will be the inversion axis
print("Enter root note: ", end="")
root_note = int(input())

# Copy contents to new file
output = input_file

for track in output.tracks:
    for message in track:
        if message.type == "note_on" or message.type == "note_off":
            new_note = root_note + (root_note - message.note)
            message.note = new_note

# Save new file
output.save(filename + "-inverted.mid")