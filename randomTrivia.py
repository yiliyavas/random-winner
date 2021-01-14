def repetition(n):
    flag = True
    total = n
    List = []
    while total > 0:
        if (total%2) != 0: #the remaining of total dividing by 2  should equal zero
            total= total - 1 
        else:
            List.append(total)
            total = total // 2

            
    return(List)

"""------------------------------------------------"""
def drew_repetiton(n):
    flag = True
    total = n

    if (total%2) != 0: #the remaining of total dividing by 2  should equal zero
        total= total - 1 
    else:
        total = total // 2
    #print('=================================================================', total)
            
    return(total)

"""------------------------------------------------"""
def find_players(r):
    filename = open('names_for_trivia.txt', 'r')
    List_names = []
    for name in filename:
        List_names += name.split()

    who_play = List_names[:(r)]
    
    return who_play
    filename.close()

"""------------------------------------------------"""
def acc_round(list_rounds, r):
    dic = {}
    acc = 0
    for c in (list_rounds):
        acc += 1
        dic[acc] = c
    #print('.........', dic)  
    return dic

"""------------------------------------------------"""
def score_for(p, average_score):
    dic_score = {}
    for i in p:
        r = random.randint(0, 1000)
        dic_score[i] = r
        
    #sorted_dic = sorted(dic_score.items(), key=lambda kv:kv[1])
    sorted_dic = {k: v for k, v in sorted(dic_score.items(), key = lambda v:v[1], reverse=True)}

    filename = open('names_for_trivia.txt', 'w')

    
    main_list = []
    keys_of_dic = sorted_dic.keys()
    for i in keys_of_dic:
        main_list.append(i) 
    #print(main_list, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    for k in main_list:
        filename.write(k + "\n")
    filename.close()

    return (sorted_dic)


def print_txt_file(r):
    file_name = open('names_for_trivia.txt', 'w')
    for i in range(r):
        name = input('Name: ')
        file_name.write(name + "\n")
    file_name.close()

        
""">>>>>>>>>>>>>>>>>>>>>>Driver Code<<<<<<<<<<<<<<<<<<<<<<<<"""

import random
r = int(input('enter the number of players: '))

#r = random.randint(2, 120)
list_rounds = repetition((r)) #repetotion(_)
print(list_rounds)

print_txt_file(r)


accumulator = acc_round(list_rounds, r) #accumulator(_, _)
player_in_first_round = r


print('>>>>>game starts>>>>>')
#print('<<<', player_in_first_round, '>>>')

for i in range (1, len(accumulator) + 1):
    while r != 1:
        average_score = 1
        print()
        player_list = find_players(r) #find_player(_)
        main_dic = score_for(player_list, average_score) #score_for(_)

        print(main_dic)
        
        sum_score = 0
        l_score = []
        for i in main_dic.values():
            sum_score += i
            l_score.append(i)

        sum_name = 0
        l_name = []
        for j in main_dic.keys():
            l_name.append(j)
            sum_name += 1

        average_score = (sum_score//sum_name)
        #print('AVE <<<<<<<<<', average_score)
        
        highest_score = max(l_score)
        index_highest = l_score.index(highest_score)
        winner_name = l_name[index_highest]
        #print(highest_score, '->', winner_name)
        r = drew_repetiton(r)

print('ABSOLUTE WINNER >>>>>>>>>>>', winner_name.upper())
        



        
