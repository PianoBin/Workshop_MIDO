from mido import Message
msg = Message('note_on', note=60)
print(msg)
msg = msg.copy(note=100, velocity=127)
print(msg)
msg2 = Message('note_on', note=100, velocity=3, time=6.2)
print(msg2)
print(msg2.bytes())
print(msg2.hex())
msg3 = Message.from_bytes([0x90, 0x42, 0x60])
print(msg3)
print(msg3.dict())
print(msg3.is_meta)