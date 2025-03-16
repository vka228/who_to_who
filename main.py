names = ['Person1', 'Person2', 'Person3', 'Person4', 'Person5', 'Person6', 'Person7', 'Person8', 'Person9', 'Person10']
spendings = [2700, 1600, 1900, 700, 0, 0, 0, 0, 0, 0]

def calculate_transactions(spendings):
    n = len(spendings)
    total = sum(spendings)
    average = total / n
    differences = [spending - average for spending in spendings]
    transactions = []
    for i in range(n):
        for j in range(i + 1, n):
            if differences[i] > 0 and differences[j] < 0:
                amount = min(differences[i], -differences[j])
                transactions.append((names[j], names[i], amount))
                differences[i] -= amount
                differences[j] += amount
            elif differences[i] < 0 and differences[j] > 0:
                amount = min(-differences[i], differences[j])
                transactions.append((names[i], names[j], amount))
                differences[i] += amount
                differences[j] -= amount
    return transactions

transactions = calculate_transactions(spendings)

for transaction in transactions:
    print(f"{transaction[0]} ----- {transaction[2].__round__()}p -----> {transaction[1]}")
