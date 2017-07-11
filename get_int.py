def get_int(msg):
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print err


msg = get_int("type a number: ")
print msg