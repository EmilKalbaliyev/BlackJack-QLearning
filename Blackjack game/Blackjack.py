import Hand


class Blackjack:

    def __init__(self):
        self.isRunning = True
        self.isPlayer = True
        self.dealer = Hand.Hand()
        self.player = Hand.Hand()
        self.dealer.add(1)
        self.player.add(2)

    def start_game(self):
        self.isRunning = True
        self.isPlayer = True
        self.dealer = Hand.Hand()
        self.player = Hand.Hand()
        self.dealer.add(1)
        self.player.add(2)

    def player_plays(self, action):
        if self.isRunning==False:
            return
        if self.player.is_bust():
            return
        if self.isPlayer== False:
            return
        if action == 0:
            self.player.add(1)
        elif action == 1:
            self.player.terminate()
        elif action == 2:
            self.player.add(1)
            self.player.set_double_down()
            self.player.terminate()
        if self.player.is_bust():
            self.player.terminate()
            self.isRunning = False
        if self.player.is_terminated():
            self.isPlayer = False

    def dealer_plays(self):
        if self.isRunning==False:
            return
        if self.dealer.is_bust():
            return
        if self.isPlayer:
            return
        if len(self.dealer.hand) == 1:
            self.dealer.add(1)
        elif self.dealer.get_total() < 17 or (self.dealer.aces > 0 and self.dealer.get_total == 17):
            self.dealer.add(1)
            if self.dealer.is_bust():
                self.dealer.terminate()
                self.isRunning = False
        else:
            self.dealer.terminate()
            self.isRunning = False

    def get_reward(self):
        if self.isRunning:
            return 0
        if self.player.is_twenty_one() and self.dealer.is_twenty_one():
            return 0
        score=0
        if self.player.is_double_down():
            score=2
        else :
            score=1
        if self.player.is_twenty_one():
            return 1.5 * score
        if self.dealer.is_twenty_one():
            return -1 * score
        if self.dealer.is_bust():
            return 1 * score
        if self.player.is_bust():
            return -1 * score
        if self.dealer.get_total() > self.player.get_total():
            return -1 * score
        if self.player.get_total()>self.dealer.get_total() :
            return 1 * score
        return 0

    def get_player_state(self):
        ace_score=0
        if self.player.aces > 0:
            ace_score = 100
        else:
            ace_score = 0
        return self.player.get_total() + ace_score

    def get_dealer_state(self):
        return self.dealer.first
