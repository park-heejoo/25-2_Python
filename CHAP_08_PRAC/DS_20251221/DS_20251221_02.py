class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(self.owner,"계좌가 생성되었습니다.")

    def get_balance(self):
        return self.balance

    def set_balance(self, amount):
        if amount<0:
            print("0 이상인 값만 허용합니다")
        else:
            self.balance+=amount

    def deposit(self, amount):
        if amount<0:
            print("0보다 큰 금액만 입금 가능합니다")
        else:
            self.balance += amount
            print(f"{self.owner} 통장에 {self.balance}원이 입금되었습니다")

    def withdraw(self, amount):
        if self.balance < amount:
            print("잔액이 부족합니다.")
        else:
            self.balance -= amount
            print(f"{self.owner} 통장에 {self.balance}원이 출금되었습니다")


a=BankAccount("A")
b=BankAccount("B")

a.deposit(100)
b.deposit(200)
a.withdraw(30)
b.withdraw(50)

print(f"{a.owner} 계좌의 현재 잔액:", a.get_balance())
print(f"{b.owner} 계좌의 현재 잔액:", b.get_balance())

a.set_balance(500)
print(f"{a.owner} 계좌의 수정된 잔액:", a.get_balance())