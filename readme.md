#Эмулятор машины тьюринга на Python3
Простой эмулятор машины тьюринга на python3
##Входные данные:
Файлы по умолчанию:
* input.txt     -       входное слово
* alphabet.txt -     алфавит
* instructions.txt - список команд
Команды должны быть в формате: 

State Symbol ; Symbol {L;H;R} State
То есть 6 слов через пробел

Чтобы выбрать свои файлы при запуске скрипта укажите флаг -c
##Синтаксис:
* Символ lambda = \l
* Символ delta(начало алгоритма) = \d
* Символ omega(конец алгоритма) = \o


##Команды:
* continue или c - запустить алгоритм до конца
* step или s - сделать шаг алгоритма
* m или move - изменить диапазон печати на каждом шаге
