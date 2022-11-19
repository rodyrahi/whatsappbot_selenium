def find_no(m):
    try:
        m = m.replace(" ", "")
        int(m)

        print(True , m)
        return True
    except:
        print(False , m)
        return False



