#Path to MAFIA
Here I will post proofs-of-concept while testing ideas for the ultimate aim, a MAFIA game based on websockets.
The server implementation is taken from my learning-websockets repository and used without modification.

###Rounds_Maths_Game

This was used to test whether the we can have several rounds, maybe time those rounds of a simple activity which may be scored. Useful lessons:
* removeEventListener can be called from within the function that the addEventListener adds!
* Client side will bear a brunt of the game (ie conducting the rounds), but I still require push capability on the server side, and no, I don't want to use something like long-polling, which is but a temporary fix.  
####Vote_With_Priv

This was used as a test for the following items:
* Voting in "realtime", as in voters should see other users' votes too. WebSockets really shine here.
* timer is working solidly
* Isolation of various user-groups eg chor-group, mantris group etc. Some ugly on the client side, as group is decided AFTER the client joins, so it is not possible to load only the required parts(or maybe I could use JS to load ONLY the relavant scripts -- good idea, check it out.)
