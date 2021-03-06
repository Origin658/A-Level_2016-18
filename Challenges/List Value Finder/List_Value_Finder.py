#Joe Young
#v.1


def value_finder(List):
    value = 0    
    for i in List:
        value += i
    return value

def value_finder_r_single(List):
    value = 0
    if List == []:
        return 0
    else:
        return (List[0] + value_finder_r_single(List[1:]))

def value_finder_r_multi(List):
    value = 0    
    for i in List:
        if type(i) == list:
            value += value_finder_multi(i)
        else:
            value += i
    return value


def main():
    lists = [10,10]
    one = value_finder(lists)
    print(one)
    #----------------------------------------
    lists = [10,10]
    two = value_finder_r_single(lists)
    print(two)
    #----------------------------------------
    lists = [10,10,[5,5],5,5,[5,[5,5],5]]
    three = value_finder_multi(lists)
    print(three)
    


if __name__ == "__main__":
    main()