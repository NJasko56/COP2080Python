# unpacking_operator.py
#a_tuple = (1,2,3,4,5,6,7)
#a_list = [22,33,44,55]
#def some_dict():
    #a_dict = {'abe': 123, 'doe': 345, 'ken': 789}
    #return a_dict
#print(*a_tuple)
#print(*a_list)
#print(*some_dict())

#hp_damage = lambda x: x - damage
#damage = 20
#hp = 100
#print(f'Your character took {damage} points of damge')
#print(f'Your character has droped from {hp} hit points to \
#{hp_damage(hp)} hit points available')

def scoreToNumber(score):
    score = str.upper(score)
    result = 0
    first = score[0]
    if first == "G" :
        result = 10
    elif first == "O" :
        result = 5
    elif first == "P" :
        result = 3
    return result

def main():
    score1 = input('Enter score 1 as Great, Ok or Poor: ')
    score2 = input('Enter score 2 as Great, Ok or Poor: ')
    score3 = input('Enter score 3 as Great, Ok or Poor: ')
    x1 = scoreToNumber(score1)
    x2 = scoreToNumber(score2)
    x3 = scoreToNumber(score3)
    xmax = max(x1, x2, x3)
    some_avg = (x1 + x2 + x3) / 3
    print(f'The maximum score was {xmax}')
    print(f'The avg score on 1-10 scale would have been {round(some_avg, 2)}')

main()