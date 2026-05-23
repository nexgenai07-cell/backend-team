# Input list containing user dictionaries
users = [
    {'name': 'Ali', 'active': True},
    {'name': 'Sara', 'active': False},
     {'name': 'Aliza', 'active': True},
    {'name': 'Saram', 'active': False},
]
print("--- Active User Filtering ---")
print("Output:")
# This loops through 'users' and filters only those where user['active'] is True.
active_users = [user for user in users if user['active'] == True]

# Displaying the filtered active users
for user in active_users:
    print(user)