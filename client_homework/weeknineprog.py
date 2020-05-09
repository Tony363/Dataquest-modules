import string 
# import pandas as pd

def process_line(line, word_count_dict):
    line = line.rstrip()
    word_list = line.rsplit()
    for word in word_list:
        if word != -99: 
            word = word.lower()
            word = word.strip()
            add_word(word, word_count_dict)

def add_word(word, word_count_dict):
    if word in word_count_dict:
        word_count_dict[word] += 1
    else: 
        word_count_dict[word] = 1

def process_file(word_count_dict):
    value_key_list = []
    ## remember to use [] instead () if you want to use pandas
    for key, val, in word_count_dict.items():
        value_key_list.append((val, key))
    value_key_list.sort(reverse=True)
    value_key_list.insert(0,('word','count'))
    value_key_list.insert(1,(len(word_count_dict),'Length of the dictionary'))

    # df = pd.DataFrame(value_key_list)
    # df.columns = ['count','word']
    # df = df[['word','count']]
    # print(df)
    # df.to_csv('word_count.csv')
    with open('random_formated.txt',"w") as f: 
        for val, key in value_key_list:
            f.write("{} {}\n".format(key,val))  

def main():
    word_count_dict = {}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, word_count_dict)
    print('Length of the dictionary: ', len(word_count_dict))
    process_file(word_count_dict)

if __name__ == "__main__": 
    main()

    