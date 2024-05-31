

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
        midle = (data_last + low) // 2
        count = 0
        while True:
            count += 1
            if dat[midle] > search:
                data_last = midle
            elif dat[midle] < search:
                low = midle + 1
            elif dat[midle] == search:
                print(dat[midle], count)
                break
            else:
                print("Bunday element mavjud emas!")
                return binary_search(dat)
    except:
        print("Son kiriting! ")
        return binary_search(dat)

if __name__ == "__main__":
    check_list()
