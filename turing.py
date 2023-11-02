from sys import argv

def alphaberParser(path: str) -> set:
    with open(path) as alph:
        alph_str = alph.readline()
        result = []
        for i in range(1, len(alph_str)):
            if(alph_str[i-1] == "\\"):
                #print(alph_str[i-1])
                symb = alph_str[i-1] + alph_str[i]
                if not (symb == '\\l' or symb == '\\d'):
                    raise RuntimeError("В Вашем алфавите есть прочие спецсимволы помиио \\d  и \\l") 
                if symb not in result:
                    result.append(symb)
            else:
                if alph_str[i] != '\\':
                    if alph_str[i] not in result:
                        result.append(alph_str[i])
        if alph_str[-1] == '\\':
            raise RuntimeError("В Вашем алфавите есть прочие спецсимволы помиио \\d  и \\l") 
        else:
            if symb not in result:
                result.append(alph_str[-1])
        print("Введенный алфавит:")
        for i in result:
            print(i, end = " ")
        print()
        print()
    return set(result)

def commandsParser(path: str)->dict:
    global alphabet
    state = dict()
    i = 0
    with open(path) as instructions:
        for line in instructions.readlines():
            cmds = line.split()
            if len(cmds) != 6:
                raise RuntimeError("Некорректная комманда")
            if cmds[1] not in alphabet or cmds[3] not in alphabet:
                raise RuntimeError("В алфавите введены не все символы")
            key = (i, cmds[0], cmds[1])
            if cmds[4] not in ["L", "R", "H"]:
                raise RuntimeError("Вместо символа L H R стоит что-то другое")

            if state.get(key, -1) != -1:
                raise RuntimeError("Встретилась одна и та же комманда")
            state[key] = (cmds[3], cmds[4], cmds[5])
            i += 1
    return state

def wordParser(path:str)->list:
    global alphabet
    ans = []
    with open(path) as f:
        l = f.readline()
        for i in range(1, len(l)):
            if(l[i-1] == "\\"):
                symb = l[i-1] + l[i]
                if symb != "\\d":
                    raise RuntimeError("В Вашем слове есть символы не из алфавита") 
                ans.append(symb)
            else:
                if l[i] != '\\':
                    if l[i] not in alphabet:
                        raise RuntimeError("В Вашем слове есть символы не из алфавита") 
                    ans.append(l[i])
        if l[-1] == '\\':
            raise RuntimeError("В Вашем флфавите есть прочие спецсимволы помиио \\d  и \\l") 
        if l[-1] not in alphabet:
            raise RuntimeError("В Вашем слове есть символы не из алфавита") 
        print("Введенное слово:")
        for i in ans:
            print(i, end = " ")
        print()
        print()
        return ans


def diapasonPrint(pos:int, current_pos,  delta: int = 10) -> None:
    global tape
    for i in range(pos-delta+delta//2, pos+delta+delta//2 + 1):
        if i == current_pos:
            print(f"<{tape[i]}>", end = " ")
        else:
            print(tape[i], end = " ")
    print()
    print()
def step():
    global commands, tape
    global current_pos, current_state
    for a, b in commands.items():
        tmp, st, symv = a
        new_symv, step, new_state = b
        if (st, symv) == (current_state, tape[current_pos]):
            break
    else:
        diapasonPrint(start_pos, current_pos)
        raise RuntimeError("Принудительная остановка, нет нужной комманды")
    tape[current_pos] = new_symv
    current_state = new_state
    if current_state == "\o":
        print("---------------------------------")
        print("Oстановка алгоритма")
        return True
        
    if step == "L":
        current_pos -= 1
    elif step == "H":
        pass
    elif step == "R":
        current_pos += 1

if __name__ == "__main__":
    if(len(argv) != 1 and (argv[1] == "-c")):
        print("Введите путь до файла с алфавитом:")
        alphabet_file = input()
        print("Введите путь до файла с командами")
        instructions_file = input()
        print("Введитте путь до файла с входным словом")
        input_file = input()
    else:
        alphabet_file = "alphabet.txt"
        instructions_file = "instructions.txt"
        input_file = "input.txt"
    
    
    alphabet = alphaberParser(alphabet_file)
    commands = commandsParser(instructions_file)
    word = wordParser(input_file)
    tape = [r'\l' for i in range(10_000)]
    start_pos = 5_000
    current_pos = 5_000
    #tape[current_pos] = r'\d'
    for i in range(0, len(word)):
        tape[start_pos + i] = word[i]
    current_state = "S0"
    print("Текущая лента")
    diapasonPrint(start_pos, current_pos)
    f = False
    while True:
        try:
            if f:
                break
            print("Введите комманду:", end = " ")
            cmd = input()
            if cmd == "step" or cmd == "s" or cmd == "":
                x = step()
                if x:
                    f = True
                diapasonPrint(start_pos, current_pos)
            elif cmd == "move" or cmd == "m":
                print("На сколько сдвинуть ленту влево?: ")
                x = int(input())
                start_pos += x
            elif cmd == "c" or cmd == "continue":
                iters = 0
                while iters < 1000:
                    try:
                        x = step()
                        iters += 1
                        if x:
                            f = True
                            break
                    except:
                        print("Алгоритм завершился НЕкорректно")
                        break
                print("Экстренная остановка! Превышен лимит операций.")
            else:
                print("Введите что-то из списка s, m, c")
        except:
            print("Принудительная остановка, нет нужной комманды!")
            break
    print("Результат:")
    diapasonPrint(start_pos, current_pos)
    
