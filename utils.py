class Utils;
    def reveresed(num):
        if (isinstance(num, int)):
            return int(str(num).reveresed())
        else:
            return "Invalid Input"

    def formatter(num):
        if (isinstance(num, int)):
            return (bin(num), oct(num))
        else:
            return "Invalid Input"