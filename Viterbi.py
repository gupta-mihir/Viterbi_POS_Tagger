


def prob_word_tag(word, tag):
    print("This is the word: ", {word}, " and this is the tag: ", {tag})
    if word == ':':
        tag = ':'
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
        for j in range(0, len(str)):
            split_str = str[j].split('/')
            if split_str[0] != '\n':
                working_str = word_tag_combo[split_str[0]]
                sp_working = working_str.split(' ')
                tags_instance = {}
                prev_tagger = []
                prob_t = ''
                prob_w = ''
                for i in sp_working:
                    tags_instance[i] = 1
                for key in tags_instance:
                    prob_w = prob_word_tag(split_str[0], key)
                    print('prob w of ', {split_str[0]}, 'and ', {key})
                    print(prob_w)
                    if '<s>' in tags_instance and key != '<s>':
                        prob_t = prob_tag_tag(key, '<s>')
                        print('prob t of ', {key}, 'and <s>')
                        print(prob_t)
                    elif '<s>' not in tags_instance:
                        for iter in prev_tagger:
                            prob_t = prob_tag_tag(key, iter)
                            print('prob t of ', {key}, 'and ', {iter})
                            print(prob_t)
                    else:
                        continue
            else:
                continue



with open('pos.train.txt') as f:
    lines = f.readlines()

print(type(lines))
                                                                    #definition of all dictionaries needed
pos_tag_dict = {}
word_pos_count = {':' : 0, '(' : 0, ')' : 0, 'TO' : 0, 'CD' : 0 }
word_tag_combo = {':' : '', '(' : '', ')' : '', 'TO' : '', 'CD' : '' }
prev_tag_count = {'<s> POS' : 1}
count_word_tag_pair = {}

for i in range(0, len(lines)):                                  #MODIFIED
    str = lines[i].split(' ')
    temp = lines[i]
    sp_temp = temp.split(' ')
    pre_tag = sp_temp[len(sp_temp) - 2]
    pre_tag_new = ''
    counter = 0
    is_slash_pre = False
    for iter in pre_tag:
        if iter == '/':
            is_slash_pre = True
        if iter == ' ':
            break
        if is_slash_pre == True and iter != '/':
            pre_tag_new = pre_tag_new + iter
    
        
        
    val = 0
    temp_new = ''
    while(temp[val] != '/'):
        temp_new = temp_new + temp[val]
        if temp[val] == '/':
            break
        else:
            val = val+1
    temp_tag = ''
    is_slash = False
    for iter in temp:
        if iter == '/':
            is_slash = True
        if iter == ' ':
            break
        if is_slash == True and iter != '/':
            temp_tag = temp_tag + iter
    #print(pre_tag)
    print(pre_tag_new)
    print('tag temp = ')
    print(temp_tag)
    temp_tag = '<s>'

    word_tag_combo[temp_new] = '<s>'
    pair_str = temp_new + ' ' + '<s>'
    pair_tagger = pre_tag_new + ' ' + temp_tag
    if pair_str in count_word_tag_pair:
        pos_tag_dict['<s>'] += 1    
    else:
        pos_tag_dict['<s>'] = 1
    if pair_str in count_word_tag_pair:
        count_word_tag_pair[pair_str] += 1    
    else:
        count_word_tag_pair[pair_str] = 1
    if i == 0:
        pair_tagger = '<s> <s>'
    if pair_tagger in prev_tag_count:
        prev_tag_count[pair_tagger] += 1
    else:
        prev_tag_count[pair_tagger] = 1
    for j in range(0, len(str)):
        sp_str = str[j].split('/')
        if j > 0:
            prev_str = str[j-1].split('/')
        else:
            prev_str = ['<s>','<s>']
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

viterbi(lines)