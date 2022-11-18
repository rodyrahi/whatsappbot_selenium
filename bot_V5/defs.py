def find_no(m):
    try:
        int(m)
        print(True , m)
        return True
    except:
        print(False , m)
        return False
