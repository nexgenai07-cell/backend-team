import requests

api_url = "https://jsonplaceholder.typicode.com/users"
try:
    response = requests.get(api_url, timeout=5)
    
    # Check if the HTTP request was successful
    response.raise_for_status()

    users_list = response.json()
    
    print("Output:")
    
    # 4. Loop through each user in the list to extract data
    for user in users_list:
        # Using safe .get() method to prevent crashes if any key is missing
        name = user.get('name')
        email = user.get('email')

        print(f"Name: {name}")
        print(f"Email: {email}")

except requests.exceptions.RequestException as error:
    # Handles network issues, bad URLs, or server downs
    print(f"\nAPI Error: Could not fetch data. Details: {error}")