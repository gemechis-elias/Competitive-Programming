class Bank:
    def __init__(self, balance: List[int]):
        self.myBank = balance
        self.totalAcc = len(self.myBank)
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <= self.totalAcc  and account2 <= self.totalAcc:
            if self.myBank[account1-1] >= money:
                self.myBank[account1-1] -= money
                self.myBank[account2-1] += money
                return True
        return False
    def deposit(self, account: int, money: int) -> bool:
        if account <= self.totalAcc:
            self.myBank[account-1] += money
            return True
        return False
    def withdraw(self, account: int, money: int) -> bool:
        if account <= self.totalAcc:
            if self.myBank[account-1] >= money:
                self.myBank[account-1] -= money
                return True
        return False  
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
