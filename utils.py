import telebot
def top_prepod():
    gh = []
    with open('text.txt', 'r', encoding='utf-8') as f:
        gh = list(f)
    for i in range(len(gh)):
        gh[i] = gh[i][:-1]

    d = []
    s =[]
    for i in gh:
        d.append(int(i.split()[1]))
    d.sort(key=int) 
    for j in gh:
        for i in d:
            if int(j.split()[1]) == i:
                d[d.index(i)] = j.split()[0]
                break
    return d
