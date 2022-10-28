def prob_word_tag(word, tag):
    print("This is the word: ", {word}, " and this is the tag: ", {tag})
    pair_str = word + ' ' + tag
    count_word = count_word_tag_pair[pair_str]
    count_tag = pos_tag_dict[tag]
    prob = count_word / count_tag
    print('Count word = ', {count_word}, ' count tag = ', {count_tag})
    return prob



def prob_tag_tag(tag, prev_tag):
    print("This is the first tag: ", {tag}, " and this is the prev tag: ", {prev_tag})
    count_tag_pair = prev_tag_count[prev_tag + ' ' + tag]
    count_prev_tag = pos_tag_dict[prev_tag]
    prob = count_tag_pair / count_prev_tag
    return prob

def viterbi(input):
   for i in range(0, len(input)):
    str = input[i].split(' ')
    for iter in range(0, len(str)):
        tags = {}
        str_val = word_tag_combo[str[iter]]
        chunks = str_val.split(' ')
        prev_tag = []
        for j in chunks:

            if j not in tags:
                tags[j] = 1
        if iter == 0:
            print('Will work on this later')
            for key in tags:
                prev_tag.append[key]
        else:
            curr_tag = ''
            for a in prev_tag:
                p_tag = a
                for key in tags:
                    curr_tag = key
                    t_prob = prob_tag_tag(curr_tag, p_tag)
                    w_prob = prob_word_tag()



    



with open('pos.train.txt') as f:
    lines = f.readlines()

print(type(lines))
pos_tag_dict = {}
word_pos_count = {':' : 0, '(' : 0, ')' : 0, 'TO' : 0, 'CD' : 0 }
word_tag_combo = {':' : '', '(' : '', ')' : '', 'TO' : '', 'CD' : '' }
prev_tag_count = {}
count_word_tag_pair = {}

for i in range(0, len(lines)):
    str = lines[i].split(' ')
    print(len(str))
    print(str)
    temp = lines[i]
    val = 0
    temp_new = ''
    while(temp[val] != '/'):
        temp_new = temp_new + temp[val]
        val = val+1
        if val == '/':
            break
    #print(temp_new)
    word_tag_combo[temp_new] = '<s>'
    for j in range(0, len(str)):
        sp_str = str[j].split('/')
        
        if j > 0:
            prev_str = str[j-1].split('/')
        else:
            prev_str = ['<s>','<s>']
        #print(prev_str)
        if len(sp_str) > 1 and len(sp_str) < 3:
            word = sp_str[0]
            pos_word = sp_str[1]
            prev_pos = prev_str[1]
            prev_pair = prev_pos + ' ' + pos_word
            word_pair = word + ' ' + pos_word
            if (word in word_tag_combo):
                word_tag_combo[word] += ' ' + pos_word
            else:
                word_tag_combo[word] = pos_word

            if (word_pair in count_word_tag_pair):
                count_word_tag_pair[word_pair] += 1
            else:
                count_word_tag_pair[word_pair] = 1

            if (prev_pair in prev_tag_count):
                prev_tag_count[prev_pair] += 1
            else:
                prev_tag_count[prev_pair] = 1

            if (word in pos_tag_dict):
                word_pos_count[word] += 1                
            else:
                word_pos_count[word] = 1

            if (pos_word in pos_tag_dict):
                pos_tag_dict[pos_word] += 1
            else:
                pos_tag_dict[pos_word] = 1
#for key in word_tag_combo:    
 #   print(key, '->', word_tag_combo[key])
#print(pos_tag_dict)
#print(prev_tag_count)
#print(count_word_tag_pair)
#print(word_pos_count)
#print(word_tag_combo)
#sen_lines = lines.split('\n')
#print(lines)
print(prob_tag_tag('NN', 'VBZ'))
print(prob_word_tag('Pierre', 'NP'))

