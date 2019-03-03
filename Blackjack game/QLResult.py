import Blackjack
import QLearning

blackjack = Blackjack.Blackjack()
iteration = 50000
alpha = 0.1
gamma = 0.1
epsilon = 0.9
games = 100000
wins = 0
lose = 0
draw = 0
total = 0
ql = QLearning.QLearning(game=blackjack, iterations=iteration, alpha=alpha, gamma=gamma, epsilon=epsilon)
print("learning finished, testing started")
for game_number in range(games):
    total += 1
    blackjack.start_game()
    while True:
        actions = ql.Policy[blackjack.get_player_state()][blackjack.get_dealer_state()]
        best_action = 0
        for i in range(0, len(actions)):
            if actions[i] > actions[best_action]:
                best_action = i
        blackjack.player_plays(best_action)
        while not blackjack.isPlayer and blackjack.isRunning:
            blackjack.dealer_plays()
        if not blackjack.isRunning:
            break
    if blackjack.get_reward() > 0:
        wins += 1
    if blackjack.get_reward() == 0:
        draw += 1
    if blackjack.get_reward() < 0:
        lose += 1

csv_file_path = "result.csv"
csv = open(csv_file_path, "a")
csv.write("iteration: ," + str(iteration) + "\n" +
          "alpha: ," + str(alpha) + "\n" +
          "gamma: ," + str(gamma) + "\n" +
          "epsilon: ," + str(epsilon) + "\n" +
          "games:  ," + str(games) + "\n")
csv.write("\n")
csv.write("Iterations, Win rate, Loss Rate \n")
csv.write(str(iteration)+ ", " + str(wins / total)+ ", " + str(lose / total) + "\n")
csv.write("\n")

actions = ["H", "S", "D"]

csv.write("Hard\n")
csv.write(",2, 3, 4, 5, 6, 7, 8, 9, T, A\n")
for i in range(2, 22):
    csv.write(str(i) + ",\t")
    for j in range(2, 12):
        action, val = max(enumerate(ql.Q_values[i][j]), key=lambda x: x[1])
        csv.write(actions[action] + ", ")
    csv.write("\n")


csv.write("Soft\n")
csv.write(",2, 3, 4, 5, 6, 7, 8, 9, T, A\n")
for i in range(113, 122):
    csv.write(str(i - 100) + ",\t")
    for j in range(2, 12):
        action, val = max(enumerate(ql.Q_values[i][j]), key=lambda x: x[1])
        csv.write(actions[action] + ", ")
    csv.write("\n")
csv.write("\n")
csv.close()


csv_file_path = "rest.csv"
csv = open(csv_file_path, "a")
for i in range(2, 22):
    for j in range(2, 12):
        action, val = max(enumerate(ql.Q_values[i][j]), key=lambda x: x[1])
        csv.write(actions[action] + ", ")
    csv.write("\n")
for i in range(113, 122):
    for j in range(2, 12):
        action, val = max(enumerate(ql.Q_values[i][j]), key=lambda x: x[1])
        csv.write(actions[action] + ", ")
    csv.write("\n")
csv.write("\n")





