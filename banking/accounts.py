class Account: # 기본 계좌 클래스
    def __init__(self, owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        if amount <=0:
            raise ValueError("입금액은 0보다 커야합니다.")            
        self.balance += amount
        print(f'✅ {amount}원 입금 완료! (현재 잔액: {self.balance}원)')

        if amount >= 50000000:
            raise ValueError("자금 세탁 의심 거래! 국세청에 신고됩니다.")

    def withdraw(self,amount):
        if amount <=0:
            raise ValueError("출금액은 0보다 커야합니다.")
        if self.balance < amount:
            raise ValueError("잔액이 부족합니다.")
        if (self.balance- amount) < 1000:
            raise ValueError(" 이럼 너무 슬픈데요....")
        self.balance -= amount
        print(f'잔액은 {self.balance}원입니다.')

    
    def __str__(self):
        return f"[{self.owner}] 잔액: {self.balance}원"
    
class PremiumAccount(Account):
    def __init__(self,owner, balance = 0, limit=10000):
        super().__init__(owner,balance)
        self.limit = limit
        
    def withdraw(self,amount):
        if amount < 0:
            raise ValueError('출금액은 0보다 커야합니다.')
        
        if (self.balance+self.limit)< amount:
            raise ValueError(f'한도 초과! (최대 출금 가능액: {self.balance + self.limit}원)')
        self.balance-=amount
        print(f'현재 잔액: {self.balance}원')
