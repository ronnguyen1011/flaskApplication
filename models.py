# Example model class
class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def save(self):
        # Logic to save the user to the database
        pass

    def delete(self):
        # Logic to delete the user from the database
        pass

    @staticmethod
    def get_all():
        # Logic to fetch all users from the database
        pass