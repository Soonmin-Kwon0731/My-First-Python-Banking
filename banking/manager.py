from .accounts import Account, PremiumAccount

class BankManager:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, acc_num, owner, acc_type):
        if acc_num in self.accounts:
            raise ValueError('이미 있는 계좌번호입니다.')
        
        if acc_type == 'normal':
            new_acc = Account(owner)
        elif acc_type == 'premium':
            new_acc = PremiumAccount(owner)
        else:
            raise ValueError('타입이 잘못되었습니다.')
        
        self.accounts[acc_num] = new_acc
        print(f'계좌 개설 완료: {acc_num} ({owner})')

    
    def get_account(self, acc_num):
        if acc_num not in self.accounts:
            raise KeyError('해당 계좌번호를 찾을 수 없습니다.')
        else:
            return(self.accounts[acc_num])
