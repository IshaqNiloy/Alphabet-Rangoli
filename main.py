def print_rangoli(size):
    alphabet_rangoli = ''
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dash_list = ['', '--', '----', '------', '--------', '----------', '------------', '--------------', '----------------', '------------------', '--------------------',
                 '----------------------', '------------------------', '--------------------------', '----------------------------', '------------------------------',
                 '--------------------------------', '----------------------------------', '------------------------------------', '--------------------------------------',
                 '----------------------------------------', '------------------------------------------', '--------------------------------------------',
                 '----------------------------------------------', '------------------------------------------------', '--------------------------------------------------']
    increasing_point = 0
    n = 1 #Initialization for the while loop
    counter = 1 #This variable was used to determine the breaking point of the first for loop.
    start = size - 1 #Used to get the index of the first letter of every line of the string. This index corresponds to a letter in 'alphabet_list'.
    lower_counter = 1 #Used for the lower portion of the shape from where the number of letters starts to decrease.
    dash_list_counter = size - 1 #This counter was used as an index that corresponds to a sequence of dashes in 'dash_list'.

    while n <= size + size - 1: #Used to add a new line to the desired string.
        alphabet_rangoli += dash_list[dash_list_counter] #Used to add dashes at the beginning of the string.
        for i in range(start, -1, -1): #The second parameter is used to go to the beginning of the 'alphabet_list' and the third parameter is used to decrease the value of 'i' everytime the loop runs. This loop was used to add letters to every line of the string in descending order.
            alphabet_rangoli += alphabet_list[i] #A letter is added from the 'alphabet_list' in descending order
            if n == 1 or n == size + size - 1: #This condition is used to escape the first and last line of the string. Otherwise, an extra dash would be added to the first and last line of the string.
                pass
            else:
                alphabet_rangoli += '-' #A dash is added after every letter.
            increasing_point = i #The value of this variable indicates from where the value of 'j' of the next for loop should be increased.
            if counter == n: #Used to break the loop. After this, the next loop will be executed to get the letters of a single line in ascending order.
                break
            else:
                counter += 1
            if n > size and counter > size - lower_counter: #This condition was used for the lower portion of the shape from where the number of letters starts to decrease.
                lower_counter += 1
                break
        for j in range(increasing_point + 1, size): #This loop is used to add letters to every line of the string in ascending order.
            alphabet_rangoli += alphabet_list[j] #A letter is added from the 'alphabet_list' in ascending order.
            if j < size - 1: #This conditiion is used to add a dash after every letter except the last letter of the line.
                alphabet_rangoli += '-'
        alphabet_rangoli += dash_list[dash_list_counter] #Used to add dashes at the end of the string.
        alphabet_rangoli += '\n' #Used to go to the next line.
        n += 1
        counter = 1 #Sets the counter to its initial value so that it can be reused in the first for loop.
        if dash_list_counter > 0 and n <= size: #This condition implicitly determines whether the number of dashes should be increased or decreased.
            dash_list_counter -= 1 #For the upper portion where the number of letters is increasing.
        else:
            dash_list_counter += 1 #For the lower portion where the number of letters is decreasing.

    print(alphabet_rangoli)

if __name__ == '__main__':
    n = int(input())
    print(print_rangoli(n))
