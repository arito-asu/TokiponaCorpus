
file_path = './corpus.txt'

#--------------------------------

def dupl():
    
    with open(file_path) as file:
        corpus_raw = file.readlines()

    corpus = [s.strip() for s in corpus_raw]
    length = len(corpus)

    checking = 1

    for line in corpus:
        detected = False
        i = 1
        
        print(f'checking line {checking}...',end='')
        
        while i < length:
            
            if checking - 1 == i:
                pass
            
            elif line == corpus[i]:
                detected = True
                print('')
                print(f'**duplication detected:line {i+1}')
                input('  push any key to continue...')
                
            i += 1
        
        if not detected:
            print('done')
        checking += 1

    print('finished!')

#--------------------------------

def words():
    
    with open(file_path) as file:
        corpus_raw = file.readlines()

    corpus = [s.strip() for s in corpus_raw]
    length = len(corpus)

    words = []

    for line in corpus:
        spl_line = line.split()
        line_len = len(spl_line)
        words.append(line_len)
    
    avr = sum(words) / length
    mx = max(words)
    mx_line = words.index(mx)
    mn = min(words)

    for i in range(mn,mx + 1):
        i_col = " " + str(i) if i < 10 else str(i)
        w = words.count(i)
        if w < 10:
            w_col = "   " + str(w)
        elif w < 100:
            w_col =  "  " + str(w)
        else:
            w_col = " " + str(w)
        
        print(i_col + ':' + w_col, end='')
    
        if w > 0:
            bar = ''
            n_bar = round(w / 3)
            for x in range(n_bar):
                bar = bar + '|'
            print('  ' + bar)
        else:
            print('')
        
    print('')
    print(f'average is {avr}')
    print(f'max is {mx}(line:{mx_line + 1})')
    print(f'min is {mn}')

#--------------------------------

def freq():
    
    with open(file_path) as file:
        corpus_raw = file.readlines()

    corpus = [s.strip() for s in corpus_raw]
    simplified = []
    for line in corpus:
        for char in ['.',',',':','?','!']:
            line = line.replace(char,'')
        simplified.append(line)
        
    lines = [l.split() for l in simplified]
    
    dic = {}
    
    for line in lines:
        for i in range(len(line)):
            get = line[i]
            if get not in dic:
                dic.setdefault(get,1)
            else:
                dic[get] = dic[get] + 1
                
    dic_s = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    
    len_max = 9
    
    print(f'{len(dic_s)} words found')
    print('')
    
    for eq in dic_s:
        word = eq[0]
        if len(list(eq[0])) < len_max:
            for i in range(len_max - len(list(eq[0]))):
                word = ' ' + word
        else:
            word = word[:len_max -1]
            word = word + '…'
            
        if eq[1] < 10:
            num = '  ' + str(eq[1])
        elif eq[1] < 100:
            num = ' ' + str(eq[1])
        else:
            num = str(eq[1])
         
        print(f'{word} : {num}', end='')
        bar = ''
        for i in range(round(eq[1] / 20)):
            bar = bar + '|'
        print('  ' + bar)

#--------------------------------

def freqi():
    
    with open(file_path) as file:
        corpus_raw = file.readlines()

    corpus = [s.strip() for s in corpus_raw]
    lines = [l.split() for l in corpus]
    
    dic = {}
    
    for line in lines:
        iw = line[0]
        if iw not in dic:
            dic.setdefault(iw,1)
        else:
            dic[iw] = dic[iw] + 1
                
    dic_s = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    
    len_max = 9
    
    for eq in dic_s:
        word = eq[0]
        if len(list(eq[0])) < len_max:
            for i in range(len_max - len(list(eq[0]))):
                word = ' ' + word
        else:
            word = word[:len_max -1]
            word = word + '…'
            
        if eq[1] < 10:
            num = '  ' + str(eq[1])
        elif eq[1] < 100:
            num = ' ' + str(eq[1])
        else:
            num = str(eq[1])
         
        print(f'{word} : {num}', end='')
        bar = ''
        for i in range(round(eq[1] / 5)):
            bar = bar + '|'
        print('  ' + bar)
    
#--------------------------------
        
def freqtr():
    
    with open(file_path) as file:
        corpus_raw = file.readlines()

    corpus = [s.strip() for s in corpus_raw]
    simplified = []
    for line in corpus:
        for char in ['.',',','?','!']:
            line = line.replace(char,'')
        simplified.append(line)
        
    lines = [l.split() for l in simplified]
    
    dic = {}
    
    for line in lines:
        for i in range(2,len(line)):
            get = (line[i-2],line[i-1],line[i])
            if get not in dic:
                dic.setdefault(get,1)
            else:
                dic[get] = dic[get] + 1
                
    dic_s = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    
    len_max = 15
    count = 0
    bar = ''
    
    print(f'{len(dic_s)} triplets found')
    print('')
    
    for trp in dic_s:
        
        if count == 100:
            count = 0
            input('-- push key to continue--')
            
        phrase = f'{trp[0][0]} {trp[0][1]} {trp[0][2]}'
        p_len = len(list(phrase))
        
        if p_len < len_max:
            for i in range(len_max - p_len):
                phrase = ' ' + phrase
        else:
            phrase = phrase[:len_max -1]
            phrase = phrase + '…'
            
        if trp[1] < 10:
            num = '  ' + str(trp[1])
        elif trp[1] < 100:
            num = ' ' + str(trp[1])
        else:
            num = str(trp[1])
        
        print(f'{phrase} : {num}', end='')
        bar = ''
        for i in range(round(trp[1] / 2)):
            bar = bar + '|'
        print('  ' + bar)
        
        count += 1
        

#--------------------------------
        
def freqd():
    
    with open(file_path) as file:
        corpus_raw = file.readlines()

    corpus = [s.strip() for s in corpus_raw]
    simplified = []
    for line in corpus:
        for char in ['.',',','?','!']:
            line = line.replace(char,'')
        simplified.append(line)
        
    lines = [l.split() for l in simplified]
    
    dic = {}
    
    for line in lines:
        for i in range(1,len(line)):
            get = (line[i-1],line[i])
            if get not in dic:
                dic.setdefault(get,1)
            else:
                dic[get] = dic[get] + 1
                
    dic_s = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    
    len_max = 15
    count = 0
    bar = ''
    
    print(f'{len(dic_s)} doublets found')
    print('')
    
    for trp in dic_s:
        
        if count == 100:
            count = 0
            input('-- push key to continue--')
            
        phrase = f'{trp[0][0]} {trp[0][1]}'
        p_len = len(list(phrase))
        
        if p_len < len_max:
            for i in range(len_max - p_len):
                phrase = ' ' + phrase
        else:
            phrase = phrase[:len_max -1]
            phrase = phrase + '…'
            
        if trp[1] < 10:
            num = '  ' + str(trp[1])
        elif trp[1] < 100:
            num = ' ' + str(trp[1])
        else:
            num = str(trp[1])
        
        print(f'{phrase} : {num}', end='')
        bar = ''
        for i in range(round(trp[1] / 3)):
            bar = bar + '|'
        print('  ' + bar)
        
        count += 1
        
#--------------------------------
        
def freqp():
    
    with open(file_path) as file:
        corpus_raw = file.readlines()

    corpus = [s.strip() for s in corpus_raw]
    simplified = []
    for line in corpus:
        for char in ['.',',',':','?','!',' ']:
            line = line.replace(char,'')
            line = line.lower()
        simplified.append(line)
        
    lines = simplified
    
    dic = {}
    
    for line in lines:
        for i in range(len(line)):
            get = line[i]
            if get not in dic:
                dic.setdefault(get,1)
            else:
                dic[get] = dic[get] + 1
                
    dic_s = sorted(dic.items(),key=lambda x:x[1],reverse=True)
    
    len_max = 9
    
    for eq in dic_s:
        word = eq[0]
        if len(list(eq[0])) < len_max:
            for i in range(len_max - len(list(eq[0]))):
                word = ' ' + word
        else:
            word = word[:len_max -1]
            word = word + '…'
            
        if eq[1] < 10:
            num = '   ' + str(eq[1])
        elif eq[1] < 100:
            num = '  ' + str(eq[1])
        elif eq[1] < 1000:
            num = ' ' + str(eq[1])
        else:
            num = str(eq[1])
         
        print(f'{word} : {num}', end='')
        bar = ''
        for i in range(round(eq[1] / 100)):
            bar = bar + '|'
        print('  ' + bar)
    

#--------------------------------
        
name = ''
while name != 'exit':
    name = input('run:')
    if name != 'exit':
        print('-' * 64)
        print('')
        exec(f'{name}()')
        print('-' * 64)
