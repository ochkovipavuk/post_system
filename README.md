# post_system
### Иммитация работы формальной системы Поста
На вход программе поступает файл FSP.txt, в котором записаны:
```
TAPE={11+111*11111=}
A={1,+,*,/,=}
X={x,y}
A1={1}
R={1*y= > *y=y,
x+*y= > =x}
```
- TAPE - лента
- A - алфавит
- X - перемнные
- A1 - аксиомы
- R - правила

Программа идёт по правилам сверяясь можно ли их применить. Для интерпретации переменных используется перербор. Программа находит величину самого большого числа и на место переменных подставляется числа от самого большого до минимального, пока не найдется подходящая подстрока в ленте, если такого не происходит переходим к следующему правилу. Из этого логично вытекает, что чем больше переменных в правиле (нужно проверить все комбинации) и чем больше максимальное значение в ленте, тем дольше будет работать программа, но на 3 переменных и 2 правилах при достаточно большом максимальном значении программа отрабатывает практически мгновенно. Так что, поскольку нам не требуется проводить много расчетов для больших лент, это не является значительным недостатком.

На выход программа отдает содержимое файла FSPask.txt. В нём записаны номер действия, лента до применения правила, применяемое правило и итоговое состояние ленты.

В дополнении, в файле FSP_example.txt разделённые пустой строкой хранятся варианты входных данных для программы.

---
### Emulation Post systen
A file is received at the program input FSP.txt in which the following are recorded:
```
TAPE={11+111*11111=}
A={1,+,*,/,=}
X={x,y}
A1={1}
R={1*y= > *y=y,
x+*y= > =x}
```
- TAPE - tape
- A - alphabet
- X - variables
- A1 - axioms
- R - rules

The program follows the rules, checking whether they can be applied. To interpret variables, an over-selection is used. The program finds the value of the largest number and the numbers from the largest to the smallest are substituted in place of the variables until a suitable substring is found in the tape, if this does not happen, proceed to the next rule. It logically follows from this that the more variables in the rule (you need to check all combinations) and the higher the maximum value in the tape, the longer the program will work, but on 3 variables and 2 rules, with a sufficiently large maximum value, the program works almost instantly. So, since we don't need to do a lot of calculations for large tapes, this is not a significant disadvantage.

The program outputs the contents of the file FSPask.txt . It records the action number, the tape before the rule was applied, the applied rule, and the final state of the tape.

In addition, in the file FSP_example.txt The input data options for the program are stored separated by an empty string.
