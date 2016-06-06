from server import WebServerSocket
import threading
# This is basically Raja, Mantri, Chor Sipahi with three mantris.
wssock = WebServerSocket()
threading.Thread(target = wssock.start, daemon=True).start()

while len(wssock.client_list)!=5:        # Need to have 4 users in this voting scheme
    pass

mantris = wssock.client_list[0:3]
chor = wssock.client_list[3:4]
sipahi = wssock.client_list[4:]

print("Initiate type-making")
wssock.send(mantris, "#TYPE:Mantri")
wssock.send(mantris, "#NAMES:"+",".join([str(m) for m in mantris]))
wssock.send(chor, "#TYPE:Chor")
wssock.send(sipahi, "#TYPE:Sipahi")

print("End type, initiate voting round")
wssock.send(mantris, "#VOTE:" + chor[0].name + "," + sipahi[0].name)

voting_for = {}
voting_over = 0
while True:
    if voting_over==3:
        break
    with wssock.forward_q_lock:
        for i in range(len(wssock.forward_q)):
            message = wssock.forward_q.pop()
            if message[1][:len("#VOTING_FOR:")] == "#VOTING_FOR:":
                voting_for[message[0]] = message[1][len("#VOTING_FOR:"):]
                wssock.send(mantris, "#VOTING_FOR:"+message[0].name + " for " + message[1][len("#VOTING_FOR:"):])
            for mantri in mantris:
                voting_over += 1 if ((mantri, "#DONE_VOTING")==message) else 0
print("voting round over, results round starts")
# were these guys correct?
ch = 0
sp = 0
for key in voting_for:
    if voting_for[key]==chor[0].name:
        ch+=1
    else:
        sp+=1
if ch>sp:
    wssock.send(wssock.client_list, "#RESULT:WIN")
else:
    wssock.send(wssock.client_list, "#RESULT:LOSE")
