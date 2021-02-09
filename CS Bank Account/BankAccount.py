class Bankaccount:
      pass
  
account_1 = Bankaccount()
account_2 = Bankaccount()
account_3 = Bankaccount()

account_1.full_name = "JConr B. Riddell"
account_1.account_number = 123456789
account_1.routing_number = 987654321
account_1.balance = 100

account_2.full_name = "Julian B. Riddell"
account_2.account_number = 123456799011
account_2.routing_number = 9876545432
account_2.balance = 200

account_3.full_name = "Julian II Riddell"
account_3.account_number = 123456789777
account_3.routing_number = 98765432133
account_3.balance = 300

Bankaccounts = [account_1, account_2, account_3]

for Bankaccount in Bankaccounts:
  print(Bankaccount.full_name)

for Bankaccount in Bankaccounts:
  print(Bankaccount.account_number)

for Bankaccount in Bankaccounts:
  print(Bankaccount.routing_number)

for Bankaccount in Bankaccounts:
  print(Bankaccount.balance)

for Bankaccount in Bankaccounts:
  print(Bankaccount.__dict__)
  