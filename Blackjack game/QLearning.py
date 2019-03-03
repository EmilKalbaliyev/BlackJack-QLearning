import random


class QLearning:
    def __init__(self, game, alpha=0.1, gamma=1, epsilon=0.15, iterations=2500000):
        self.blackjack = game
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.iteration = iterations
        self.actions = [0, 1, 2]
        self.Q_values = [[[0 for a in range(len(self.actions))] for d in range(12)] for p in range(130)]
        self.Policy = [[[1.0 / len(self.actions) for a in range(len(self.actions))] for d in range(12)] for h in range(130)]
        self.learn()

    def learn(self):
        for i in range(self.iteration):
            # print(i)
            self.blackjack.start_game()
            game = self.play()
            self.change_policy(game)
        return

    def play(self):
        game = []
        while self.blackjack.isRunning:
            state = [self.blackjack.get_player_state(), self.blackjack.get_dealer_state()]
            action = self.eps_action(state)
            self.blackjack.player_plays(action)
            while not self.blackjack.isPlayer and self.blackjack.isRunning:
                self.blackjack.dealer_plays()
            reward = self.blackjack.get_reward()
            state_next = [self.blackjack.get_player_state(), self.blackjack.get_dealer_state()]
            action_next = self.best_action(state_next)
            self.change_q_values(state, action, reward, state_next, action_next)
            game.append([state, action, reward])

        return game


    def eps_action(self, state):
        r = random.random()
        if r < self.epsilon:
            return random.choice(self.actions)

        else:
            return self.best_action(state)


    def best_action (self, state):
        player = state[0]
        dealer = state[1]
        action = -100000
        actions = []

        for a in range(len(self.actions)):
            if action < self.Policy[player][dealer][a]:
                action = self.Policy[player][dealer][a]

        for a in range(len(self.actions)):
            if abs(action - self.Policy[player][dealer][a]) < 0.0001:
                actions.append(a)

        return random.choice(actions)

    def change_q_values(self, state, action, reward, state_next, action_next):
        player = state[0]
        dealer = state[1]
        player_next = state_next[0]
        dealer_next = state_next[1]
        self.Q_values[player][dealer][action] = self.Q_values[player][dealer][action] + self.alpha * (
                reward + self.gamma * self.Q_values[player_next][dealer_next][action_next] -
                self.Q_values[player][dealer][action])
        return

    def change_policy(self, game):
        for i in range(len(game)):
            actions = []
            action = -100000
            player = game[i][0][0]
            dealer = game[i][0][1]

            for a in range(len(self.actions)):
                if action < self.Q_values[player][dealer][a]:
                    action = self.Q_values[player][dealer][a]

            for a in range(len(self.actions)):
                if abs(action - self.Q_values[player][dealer][a]) < 0.0001:
                    actions.append(a)

            self.Policy[player][dealer] = [0, 0, 0]
            for a in actions:
                self.Policy[player][dealer][a] = 1.0/len(actions)
        return