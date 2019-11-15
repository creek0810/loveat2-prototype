user_data = [
    {
        "id": "admin",
        "role": "admin"
    },
    {
        "id": "customer",
        "role": "customer"
    }
]
def who(id):
    for u in user_data:
        if u["id"] == id:
            return u
    return None