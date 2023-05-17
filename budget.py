class Category:  
    def __init__(self,name:str):
        self.name = name
        self.ledger = []
    def deposit(self,amount:int,description=''):
        self.ledger.append({'amount':amount,'description':description})

    def withdraw(self,amount:int,description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount,'description':description})
            return True
        return False
    def get_balance(self):
        amount_sum = []
        for dictionary in self.ledger:
            if dictionary['amount']:
                amount_sum.append(dictionary['amount']) 
        return sum(amount_sum)
    
    def transfer(self,transfer_amount:int,category:object): 
        if transfer_amount > 0 and self.check_funds(transfer_amount):
            self.withdraw(transfer_amount,'Transfer to ' + category.name)
            category.deposit(transfer_amount,'Transfer from ' + self.name)
            return True
        return False
    
    def check_funds(self, amount:int):
        total_balance = self.get_balance()
        if amount > total_balance:
            return False
        return True
            
    def __repr__(self) -> str:
        lines = []
        lines.append(self.name.center(30, '*'))

        for transaction in self.ledger:
            description = transaction['description']
            amount = transaction['amount']
            amount_str = '{:.2f}'.format(amount)
            formatted_line = f"{description[:23]:23}{amount_str:>7}"
            lines.append(formatted_line)

        total_balance = '{:.2f}'.format(self.get_balance())
        lines.append(f"Total: {total_balance}")

        return '\n'.join(lines)
#
#
#
def create_spend_chart(categories:list):
    category_withdrawals = {}
    total_withdrawals = 0
    for category in categories:
        withdrawals = 0
        for item in category.ledger:
            if item["amount"] < 0:
                withdrawals += abs(item["amount"])
        category_withdrawals[category.name] = withdrawals
        total_withdrawals += withdrawals

    # Calculate the percentage spent for each category
    percentages = {}
    for category in categories:
        percentage = category_withdrawals[category.name] / total_withdrawals * 100
        percentages[category.name] = percentage

    # Create the spend chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for category in categories:
            if percentages[category.name] >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Add the horizontal line and category names
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i != max_name_length - 1:
            chart += "\n"

    return chart



    
    


    

    