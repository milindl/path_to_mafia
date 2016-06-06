from server import WebServerSocket
import threading

client_scores = {}
wssock = WebServerSocket()
threading.Thread(target = wssock.start).start()
while len(wssock.client_list)<3:                              # Waiting for three clients to join
    pass
print("Enough clients!!!")
for cl in wssock.client_list:
    client_scores[cl] = 0

wssock.send(wssock.client_list, "Round1")
print("initiated round 1")
while len(wssock.forward_q)<3:           # Wait for end of Round 1
    pass
print("Round1 over, printing all messages")

for msg in wssock.forward_q:
    print(msg[1] + " from " + msg[0].name)

for i in range(len(wssock.forward_q)):
    msg = wssock.forward_q.pop()
    client_scores[msg[0]] += int(msg[1])
    print(wssock.forward_q)


wssock.send(wssock.client_list, "Round2")
print("R2 init")
while len(wssock.forward_q)<3:           # Wait for end of Round 1
    pass
print("R2 finish")

for i in range(len(wssock.forward_q)):
    msg = wssock.forward_q.pop()
    client_scores[msg[0]] += int(msg[1])
    print(wssock.forward_q)

winner = wssock.client_list[0]
for cl in wssock.client_list:
    if client_scores[cl]>client_scores[winner]:
        winner = cl

wssock.send(wssock.client_list, winner.name)
