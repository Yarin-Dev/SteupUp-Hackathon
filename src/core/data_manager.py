import json

DATA_PATH = "src/data/data.json"
WORKOUTS_PATH = "src/data/workouts.json"


with open(DATA_PATH, "r") as file:
    data = json.load(file)

tasks = data.get("tasks", {})
users = data.get("users", {})


def save_data():
    """Save current data to the JSON file."""
    with open(DATA_PATH, "w") as file:
        json.dump(data, file, indent=4)


def get_task(task_name):
    """
    Return a task by name.

    Returns:
        tuple:
            (True, task_data) if task exists
            (False, error_message) otherwise
    """
    if task_name in tasks:
        return True, tasks[task_name]

    return False, "Task does not exist"


def get_all_tasks():
    """Return all workout data from workouts.json."""
    with open(WORKOUTS_PATH, "r") as file:
        return json.load(file)


def sign_in(username, password):
    """
    Check if the username and password are correct.

    :param username: str
        The username entered by the user.

    :param password: str
        The password entered by the user.

    :return: tuple
        Returns (True, user_data) if login succeeded,
        otherwise returns (False, error_message).
    """
    if username not in users:
        return False, "User does not exist"

    if users[username]["password"] != password:
        return False, "Wrong password"

    return True, users[username]


def sign_up(username, password):
    """
    Create a new user account.

    Returns:
        tuple:
            (True, user_data) if registration succeeds
            (False, error_message) otherwise
    """
    if username in users:
        return False, "User already exists"

    users[username] = {
        "username": username,
        "password": password,
        "current_lvl": 0,
        "coins": 0
    }

    data["users"] = users
    save_data()

    return True, users[username]


def add_coins(username, amount):
    """
    Add coins to a specific user.

    :param username: str
        The username of the user.

    :param amount: int
        Amount of coins to add.
    """
    data["users"][username]["coins"] += amount
    save_data()


def level_up(username):
    """Increase a user's level by 1."""
    data["users"][username]["current_lvl"] += 1
    save_data()


def get_coins(username):
    """Return the amount of coins a user has."""
    if "users" not in data or username not in data["users"]:
        return 0

    return data["users"][username]["coins"]