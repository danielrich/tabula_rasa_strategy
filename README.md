# tabula_rasa_strategy
I want high level game agents trainable tabula rasa on home computing hardware.

I enjoy strategy games, and I especially enjoy games that have deep skill levels. Not sure on the correct terminology but what I mean is games that have many different skill levels.

Chess is a game that you can easily find a player that can always beat you and then easily find a player that can always beat them and so on. Very deep "skill tree".

Tic-tac-toe on the other hand is fairly shallow, if a player learns to play well then they can typically draw against anyone and everyone. It is hard to evaluate how deep a game is without a deep community of players, and I want to be able to do it using an alphago zero approach, so I can find these deep games and have the bots provide instruction to kick-start that deep level of knowledge that otherwise takes many people and a long time to accumulate.

Unfortunatly due to the computing power needed for an alphago zero approach it would be really expensive to do for a wide variety of games. Perhaps a large community leela-zero style could happen but I think that is unlikely since it will be split accross many games and interests.

My goal then is to work on a tabula rasa bot that could achieve alphazero like performance for many games but do it using moderate computational resources.

I am going to start with a simple tablut https://en.wikipedia.org/wiki/Tafl_games#Tablut approach. I am not sure how complex it will be but it appears to have kinda low branching so I want to build a traditional alpha-beta chess style engine to give me a reasonable compare. After some play testing I then want to bench mark a whole bunch of different tabula rasa approaches and see how it does.

I then want to add a bunch of games in for evaluation so I can see how well it does at learning them. I hope at the end to be able to provide a resource so that any games can easily have a high level player/s developed.
