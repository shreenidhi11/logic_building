# This program checks if two arrays are rotated version of each other

def check_arr_rotations(a1,a2):


    if len(a1) != len(a2):
        return False

    index_0 = a2.index(a1[0])
    if index_0 == -1:
        return False

    current_position = index_0 + 1
    for i in range(1,len(a1)):
        if a1[i] == a2[current_position % len(a2)]:
            pass
        else:
            return False
        current_position+=1
    return True

a1 = [3,1,2]
a2 = [2,3,1]
print(check_arr_rotations(a1,a2))

#---------------------------------------------- output -----------------------------------------------------------------
shreenidhi@MacBookPro new_venv % /usr/local/bin/python3 /Users/shreenidhi/Desktop/Learning/python_auth/new_venv/rotate.py
True
shreenidhi@MacBookPro new_venv 

