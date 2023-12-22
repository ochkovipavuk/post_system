import itertools

FSP = open("FSP.txt", "r")
ASK = open("FSPask.txt", "w")

Y = FSP.readline().split("{")[1].split("}")[0]
A = FSP.readline().split("{")[1].split("}")[0].split(",")
X = FSP.readline().split("{")[1].split("}")[0].split(",")
A1 = FSP.readline().split("{")[1].split("}")[0].split(",")
R = FSP.read().replace(" ", ""). replace("\n", "").split("{")[1].split("}")[0].split(",")

def check_Y(alf, y):
    for i in range(len(y)):
        if y[i] not in alf:
            print(y[i], "Ошибка! Нет в алфавите. Уравнение")
            return True
    return False

def check_R(alf, vars, rules):
    for i in rules:
        for j in range(len(i)):
            if i[j] not in alf and i[j] != ">" and i[j] not in vars:
                print(i[j], "Ошибка! Нет в алфавите или переменных. Правила")
                return True
    return False

def big_sec(a1, y):
    temp_sec = 0
    max_sec = 0
    for i in range(len(y)):
        if y[i] in a1:
            temp_sec += 1
        else:
            if temp_sec > max_sec:
                max_sec = temp_sec
            temp_sec = 0
    return max_sec

def mod_rule(rule, x, size):
    right_rule = rule.split(">")[0]
    new_rule = ""
    for i in range(len(right_rule)):
        if right_rule[i] == x:
            new_rule += "$" * size
        else:
            new_rule += right_rule[i]
    return new_rule

def mod_rule_fu(rule, x, size):
    right_rule = rule.split(">")[0]
    new_rule = ""
    for i in range(len(right_rule)):
        if right_rule[i] == x:
            new_rule += x * size
        else:
            new_rule += right_rule[i]
    return new_rule

def mod_a1(rule, a1):
    new_rule = ""
    for i in range(len(rule)):
        if rule[i] in a1:
            new_rule += "$"
        else:
            new_rule += rule[i]
    return new_rule

def mod_y(y, a1):
    new_y = ""
    for i in range(len(y)):
        if y[i] in a1:
            new_y += "$"
        else:
            new_y += y[i]
    return new_y

def num_x_in_rule(rule, x):
    num = 0
    new_x = []
    for i in x:
        if i in rule:
            num += 1
            new_x.append(i)
    return num, new_x

def ind_rule(m_y, m_r):
    ind = []
    for i in range(len(m_y)):
        buff = m_y.find(m_r, i)
        if buff != -1:
            ind.append(buff)
    return ind

def accord_y_rule(y, rule, ind, a1):
    for i in range(len(rule)):
        if rule[i] in a1:
            if rule[i] != y[ind + i]:
                return False
    return True


def generate_sequences(num_vars, max_value):
    variables = [i + 1 for i in range(num_vars)]
    all_sequences = list(itertools.product(variables, repeat=max_value))
    all_sequences.reverse()
    return all_sequences

def eq_rule(y, x, rule, a1):
    ask = -1
    ask_s = []
    num_x, new_x = num_x_in_rule(rule, x)
    max_seq = big_sec(a1, y)
    temp_rule = rule.split(">")[0]
    m_y = mod_y(y, a1)
    nux_x_flag = True
    if num_x > 0:
        size_x = generate_sequences(max_seq, num_x)
        for j in range(max_seq ** num_x):
            m_r = temp_rule

            for q in range(num_x):
                m_r = mod_rule(m_r, new_x[q], size_x[j][q])
            rwa = m_r
            m_r = mod_a1(m_r, a1)
            ind = ind_rule(m_y, m_r)
            if len(ind) > 0:
                for q in ind:
                    if accord_y_rule(y, rwa, q, a1):
                        ask = q
                        ask_s = size_x[j]
                        break
            if ask != -1:
                break
    else:
        ask = y.find(temp_rule)
        nux_x_flag = False

    return ask, ask_s, new_x, nux_x_flag

def use_rule(index, size_l, x_l, rule, y, alf):
    new_y = ""
    for i in range(index):
        new_y += y[i]
    new_rule = rule
    for i in range(len(x_l)):
        new_rule = mod_rule_fu(new_rule, x_l[i], size_l[i])
    index_of_x = []
    for i in range(len(x_l)):
        index_of_x.append([])
    new_new_rule = ""
    for i in range(len(new_rule)):
        for j in range(len(x_l)):
            wf = False
            if new_rule[i] == x_l[j]:
                new_new_rule += y[index + i]
                index_of_x[j].append(i)
                wf = True
            elif new_rule[i] not in x_l:
                new_new_rule += new_rule[i]
                wf = True
            if wf:
                break
    new_rule = new_new_rule
    list_of_x_val = []
    for i in range(len(x_l)):
        ask = ""
        for j in range(len(index_of_x[i])):
            if j > 0:
                if index_of_x[i][j] - index_of_x[i][j - 1] != 1:
                    break
            ask += new_rule[index_of_x[i][j]]
        list_of_x_val.append(ask)
    left_rule = rule.split(">")[1]
    for i in range(len(left_rule)):
        for j in range(len(x_l)):
            wf = False
            if left_rule[i] == x_l[j]:
                new_y += list_of_x_val[j]
                wf = True
            elif left_rule[i] not in x_l:
                new_y += left_rule[i]
                wf = True
            if wf:
                break
    for i in range(index + len(new_rule), len(y)):
        new_y += y[i]
    return new_y

def use_rule_x(index, y, rule):
    new_y = ""
    for i in range(index):
        new_y += y[i]
    new_y += rule.split(">")[1]
    for i in range(index + len(rule.split(">")[0]), len(y)):
        new_y += y[i]
    return new_y


# Проверяем начальные данные
if check_Y(A, Y) or check_R(A, X, R):
    exit()

iter = 0
while True:
    flag = False
    for i in R:     # Идем по правилам
        start_point, size_list, x_list, x_flag = eq_rule(Y, X, i, A1)   # проверяем можно ли юзануть правило
        if start_point != -1:   # если да
            iter += 1
            ASK.write(str(iter) + "." + "\n")
            ASK.write(" начальная строка - " + str(Y) + "\n")
            ASK.write(" правило - " + str(i) + "\n")
            if x_flag:
                Y = use_rule(start_point, size_list, x_list, i, Y, A)     # юзаем правило
            else:
                Y = use_rule_x(start_point, Y, i)
            ASK.write(" после правила - " + str(Y) + "\n")
            flag = True     # отмечаем что за этот цикл прохода оп правилам они были юзаны
            break
    # Если правила не юзаются тормозим
    if flag:
        flag = False
    else:
        break
ASK.close()
print("Вычисления закончены")
