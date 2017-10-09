# rubiks_solver

An Experiment in Reinforcement Learning using LSTM-weighted reward functions.

I thought it'd be interesting to try to build a minimal Reinforcement Learning environment and train a model to solve a virtual Rubik's cube.

(Came up with this during a boring Linear Algebra class so forgive me if it makes no sense. Just trying it out cause RL seems cool.)

I'm encoding the state of the rubiks cube as a 6-by-9 (faces by cells-per-face) vector where each cell is a one-hot represeneting one of the six possible colors on a cube.

"LSTM-weighted" must sound weird; Let me try to explain. Since a Rubik's cube might need to get a bit less organized to reach the solved goal, I imagine that an appropriate reward function might have to take into account the pattern of previous rewards to determine it's own value. An LSTM Cell could correctly weight how much to consider each previous reward and determine an appropraite reward value for the current state that accounts for the intermittent-delayed-reward nature of the Rubik's cube's solution process.

I'm going to start by trying to put together an appropriate environment for this.

Then I'll come in full force with all the Machine Learning mAgIc and see where this takes me.