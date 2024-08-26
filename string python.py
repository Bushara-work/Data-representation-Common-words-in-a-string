import re
import decimal 
stringa = input("What is your sentence?")

stringa = stringa.lower()


new_string = re.sub('[^a-zA-Z]+', ' ', stringa)
new_string = new_string.strip()

new_string_list = new_string.split(' ')


set_or_list = input('Do you want to use a dictionary or list for calculation?')
set_or_list = set_or_list.lower()
while set_or_list != 'dictionary' and set_or_list != 'list':
    try:
        set_or_list = input('Do you want to use a 1 set to dictionary or a parrallel list for calculation?')
        set_or_list = set_or_list.lower()
    except ValueError:
        print("This is an invalid response")

decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

if set_or_list == 'dictionary':
    set = set(new_string_list)
    res = dict.fromkeys(set, 0)
    total_words = 0
    for word in set:
        count = new_string_list.count(word)
        res[word] = count
        total_words += count
    unique_words_count = len(set)
    print("There are " + str(unique_words_count) + " words")
    
    Keymax = max(res.values())
    Keymin = min(res.values())

    #Prints the first occurance of the word with the lowest and highest respective values

    for age, name in res.items():
        if name == Keymax:
            print('The most common word is ' + age + ' It appears ' + str(name) + ' times')
            break
    for age, name in res.items():
        if name == Keymin:
            print('The least common word is ' + age + ' It appears ' + str(name) + ' times')
            break
    
    sorted_dict = {key: value for key, 
               value in sorted(res.items(), 
                               key=lambda item: item[1],
                               reverse = True)}
    
    print('In the order of most to least common here are the words and how often they show up:')
    for age, name in sorted_dict.items():
        percent = decimal.Decimal(name / total_words)*100  
        print('The word ' + age + ' makes up about ' + str(percent) + '%' + ' of the sentence.')
        

else:
    unique_list = []
    count = []
    total_words = 0
    for item in new_string_list:
        if item not in unique_list:
            unique_list.append(item)
            count.append(new_string_list.count(item))
            total_words += new_string_list.count(item)
    Maxcount = max(count)
    Mincount = min(count)

    #returns the first occuarance of a word that appeared in the stirng the maximum/minimum counted times respectivly
    index_Maxcount = count.index(Maxcount)
    index_Mincount = count.index(Mincount)
    print("The most common word is: " + unique_list[index_Maxcount] + ' it appears: ' + str(Maxcount) + " times")
    print("The least common word is: " + unique_list[index_Mincount] + ' it appears: ' + str(Mincount) + " times")

    combined_list = sorted(zip(unique_list, count), key=lambda x: x[1], reverse=True)
    print(combined_list)

    print('In the order of most to least common here are the words and how often they show up:')
    
    for string, num in combined_list:
        percent = decimal.Decimal(num / total_words)*100 
        print('The word ' + string + ' makes up about ' + str(percent) + '%' + ' of the sentence.')
        