import sys

def main(argv):
    assert argv

    _input_string = str(argv[0])
    
    print('Hello ' + str(_input_string) +'!')

if __name__ == '__main__':
    main(sys.argv[1:])
