from mido.frozen import FrozenMessage, freeze_message, thaw_message

msg = FrozenMessage('note_on')
msgDict = {msg: 'interesting'}
print(msgDict)
#msg.note = 2
thawedMsg = thaw_message(msg)
thawedMsg.note = 2
msg2 = freeze_message(thawedMsg)
msgDict[msg2] = 'fun'
print(msgDict)