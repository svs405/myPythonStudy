def get_int(msg):
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print err

Zero = [" *** ", "** **", "*   *", "*   *", "*   *", "** **", " *** "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" ** ", "*  *", "   *", "  * ", " *  ", "*   ", "****"]
Three = [" ** ", "*  *", "   *", " ** ", "   *", "*  *", " ** "]
Four = []
Five = []
Six = []
Seven = []
Eight = []
Nine = []

digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

num = get_int("type a number: ")
sNum = str(num)

for line in digits[num]:
    str = ""
    for symbol in line:
        if symbol == "*":
            str += sNum
            continue 
        str += symbol
    print str 

#try:
#    sDigits = sys.argv[1]
#except:
#    sDigits = str(get_int("type a number"))

#for digit