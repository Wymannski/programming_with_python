nb_call = 0
def main():
   print(eval1(4))

   tpl = ('xyz',821,4.45,'max',19.2)
   print(tpl[1:3])

   lst = list(range(0,20))
   print(dicotomic_search(7,lst))
   print(nb_call)

def eval1(n):
    line = [1,1]
    for i in range(n):
        current = [1]
        for j in range(len(line)-1):
            current.append(line[j]+line[j+1])
        current.append(1)
        line = current
    return line

def dicotomic_search(element, sorted_list):
    global nb_call
    nb_call += 1
    if len(sorted_list) == 1:
        return 0

    m = len(sorted_list) // 2
    if sorted_list[m] == element:
        return m
    elif sorted_list[m] > element:
        return dicotomic_search(element,sorted_list[:m])
    else:
        return m + dicotomic_search(element,sorted_list[m:])

if __name__ == '__main__':
    main()