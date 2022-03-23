import sys
sys.stdin = open('input.txt')   # 수영장

def main():
    T = int(input())
    for tc in range(1, T + 1):
        price = list(map(int, input().split()))
        plan = list(map(int, input().split()))
        solver = Solver(plan, price)

        solver.sol(0, 0)
        print(f'#{tc} {solver.min_price}')

class Solver:
    def __init__(self, plan, price):
        self.plan = plan
        self.day = price[0]
        self.month = price[1]
        self.qmonth = price[2]
        self.min_price = price[3]

        self.monthPerDay = self.month / self.day

    def sol(self, start, money):
        if start < 10:
            if sum(self.plan[start:start+3]) > 0:
                self.sol(start+3, money+self.qmonth)
        if start < 12:
            plan_start = self.plan[start]
            if plan_start == 0:
                self.sol(start+1, money)
            elif plan_start > self.monthPerDay:
                self.sol(start+1, money+self.month)
            else:
                self.sol(start+1, money+(self.day*plan_start))
        else:
            if money < self.min_price:
                self.min_price = money

if __name__ == '__main__':
    main()
