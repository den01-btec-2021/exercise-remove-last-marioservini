def remove_last(strings):
    strings.pop()

def main():
    #write your code below this line
    strings = []
    strings.append('First')
    strings.append('Second')
    strings.append('Third')
    print(strings)
    remove_last(strings)
    remove_last(strings)
    print(strings)
    
if __name__ == '__main__':
    main()
