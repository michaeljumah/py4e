'''For Statement
python's for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.
'''
words = ['cat', 'window', 'defenestrate', 'demonstrate']
for w in words:
    print(w, len(w))
    
users = {'Hans': 'Active', 'Eleonere': 'inactive', 'jumah': 'active'}
print("All users are:",users)

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        
print ("Active users are:",users)
active_users = {}
for user in users.items():
    if status == 'active':
        active_users[user] = status