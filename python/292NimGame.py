class NimGame(object):
    def __init__(self, num):
        self.n = num;
    def canWinNim(self, n):
        return bool(n % 4)

def main():
    print('Please input the nim number:')
    a = input()
    print('The result is: ')
    s = NimGame(a)
    print(s.canWinNim(s.n))

main()
