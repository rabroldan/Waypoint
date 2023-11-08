def argtest(argv):  # this is the main function
    if len(argv) > 1:
        if ("-c" in argv) or ("-config" in argv):
            return True
        elif argv == "-h" or argv == "-help":
            return True
        elif argv == "-v" or argv == "-version":
            return True
        else:
            return False
