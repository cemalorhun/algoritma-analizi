def sort_insertion(my_list):

    for i in range(1,len(my_list)):

        val_current = my_list[i]
        pos = i 
         
        # check backwards through sorted list for proper pos of val_current
        while((pos > 0) and (my_list[pos-1] > val_current)):
            my_list[pos] = my_list[pos-1]
            pos = pos-1
             
        if pos != i:
            my_list[pos] = val_current 
    
    return my_list 
    

if __name__ == "__main__":
    
    my_list = [54,26,93,17,77,31,44,55,20]
    print(my_list)
    print sort_insertion(my_list)
