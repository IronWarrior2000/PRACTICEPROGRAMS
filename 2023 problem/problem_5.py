## Problem 5 Mystic: The happening


def mystic():
    data_set_count = int(input("Enter the amount of data sets "))
    highest_circulation = 0

    for i in range(0,data_set_count):
        data_set = list(input("Enter the numbers seperated by a space for the list: ").split())
        
        data_set_dict = {}
        
        for z in data_set:
            data_set_dict[z] = data_set_dict.get(z,0)+1

        temp_ = 0
        for key, value in data_set_dict.items():
            temp = value

            x = int(key) * value
            
            if temp < x:
                temp = x

            highest_circulation = temp
        print(highest_circulation)

    

def main():
    mystic()
main()
        