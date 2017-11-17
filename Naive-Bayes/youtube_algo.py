from collections import Counter
global list_word
global word_count
word_count = []
list_word = []

def word_counter():
    word_list = open('input.txt', 'r')
    wordcount = Counter(word_list.read().split())
    for item in wordcount.items():
        list_word.append((item[0], item[1]))
    word_count.append(list_word)

def unique_word():
    input_file = open('input.txt', 'r')
    words = input_file.read()
    word_list = words.split()
    input_file_list_size = len(word_list)
    word_count.append(input_file_list_size)

    output_file = open('output.txt', 'w')
    word_list = set(word_list)
    for word in word_list:
        output_file.write(str(word)+' ')
    output_file.close()
    input_file.close()

def count_repeat_word():
    output_file = open('output.txt', 'r')
    words = output_file.read()
    word_list = words.split(' ')
    output_file_list_size = len(word_list)
    word_count.append(output_file_list_size)

def find_probability_of_words():
    divident = word_count[0] + word_count[1]
    prob = []
    for i in range(len(list_word)):
        calculation = list_word[i][1]/divident
        prob.append((list_word[i][0], calculation))

    return prob

if __name__ == '__main__':
    unique_word()
    count_repeat_word()
    word_counter()
    prob = find_probability_of_words()
    print(prob)

