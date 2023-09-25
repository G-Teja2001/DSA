n = int(input('Enter a num: '))
numMoves = 3

res = n%(numMoves+1)

if not res:
    print("Player A is guaranteed a loss no matter how many matches he picks at first.")
else:
    print(f'Player A is guaranteed a win if he picks {res} matchsticks first.')