def check_list():
    datas = input("Listga ma'lumotlar kiriting(son): ").split()
    dat = []
    for data in datas:
        try:       
            if data.isdigit():
                for i in datas:
                    dat.append(float(i))
                return binary_search(dat)
            else:
                print("Faqat son kiriting! ")
                return check_list()
        except:
            print("Faqat son kiriting! ")
            return check_list()


def binary_search(dat):
    dat.sort()
    try:
        search = int(input("Qidirayotgan sonni kiriting: "))
        low = 0
        data_last = len(dat)
        count = 0
        while True:
            count += 1
            middle = (data_last + low) // 2
            if dat[middle] < search:
                low = middle + 1
            elif dat[middle] == search:
                print(search)
                print(f"Urunishalr soni {count}")
                break
            elif dat[middle] > search:
                data_last = middle
            else:
                print("Bunday element mavjud emas!")
                return False
    except:
        print("Son kiriting! ")
        return binary_search(dat)

if __name__ == "__main__":
    check_list()
