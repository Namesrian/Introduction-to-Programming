def main (): 
    print('counting up from 0 to 50:')
    for i in range (0,51): 
        print(i, end=' ')
    print('\n')
    print('counting down from 50 to 0:')
    for i in range (50, -1, -1): 
        print(i, end=' ')
    print('\n')
    print('counting up from 30 to 50:')
    for i in range (30, 51): 
        print(i, end=' ')   
    print('\n')
    print('counting down from 50 to 10 in steps of 2:')
    for i in range (50, 9, -2): 
        print(i, end=' ')
    print('\n')
    print('counting up from 100 to 200 in steps of 5:')
    for i in range (100, 201, 5): 
        print(i, end=' ')
    print('\n')
if __name__ == "__main__":
    main ()