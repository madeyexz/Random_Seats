import random

row = int(input("座位表排數 = "))
BA_column = int(input("文組列數 = "))
BS_column = int(input("理組列數 = "))

BA = [45, 46, 33, 2, 43, 16, 36, 44, 9, 48, 40, 15, 1] # q = 13
BS = [13, 8, 34, 47, 39, 41, 14, 12, 32, 35, 42, 31, 11, 38, 7, 3, 4, 5, 6] # q = 19

if (BA_column + BS_column)*row < (len(BA) + len(BS)):
    print("錯誤：座位表無法容納所有學生")

elif (BS_column)*row < len(BS):
    print("錯誤：座位表無法容納所有「理組」學生")

elif (BA_column)*row < len(BA):
    print("錯誤：座位表無法容納所有「文組」學生")

else:
    z_str_BA = []
    z_str_BS = []
    random.shuffle(BA)                        # shuffle the order of elements in "BA"
    random.shuffle(BS)                        # shuffle the order of elements in "BS"

    for item in BA:
        item = str(item).zfill(2)
        z_str_BA.append(item)                  # insert "0" before one digit numbers

    for item in BS:
        item = str(item).zfill(2)
        z_str_BS.append(item)                  # insert "0" before one digit numbers

    print()
    print("排列順序為：先文後理")
    print()

    # 生成 文理標題
    for i in range(1, BA_column + 1):
        print("文", end = " ")
    for i in range(1, BS_column + 1):
        print("理", end = " ")
    print()
    
    # 自定義文理組列數
    for row in range(row):
        for column in range(BA_column):
            if len(z_str_BA) == 0:
                print("00", end = " ")
            else:
                print(z_str_BA.pop(), end = " ")
        for column in range(BS_column):
            if len(z_str_BS) == 0:
                print("00", end = " ")
            else:
                print(z_str_BS.pop(), end = " ")
        print()
    print()

    print("注：\"00\"為空位")