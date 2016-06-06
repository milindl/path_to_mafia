#Path to MAFIA
Here I will post proofs-of-concept while testing ideas for the ultimate aim, a MAFIA game based on websockets.
The server implementation is taken from my learning-websockets repository and used without modification.

###Rounds_Maths_Game

This was used to test whether the we can have several rounds, maybe time those rounds of a simple activity which may be scored. Useful lessons:
* removeEventListener can be called from within the function that the addEventListener adds!
* Client side will bear a brunt of the game (ie conducting the rounds), but I still require push capability on the server side, and no, I don't want to use something like long-polling, which is but a temporary fix.  
