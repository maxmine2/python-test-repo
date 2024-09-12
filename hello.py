import os

def username():
    dir_path = os.path.dirname(os.path.realpath(__file__)).lower()
    start = dir_path.find("users/")
    if start == -1:
        return None
    start += len("users/")
    end = dir_path.find("/", start)
    if end == -1:
        return None
    return dir_path[start:end]


def main():
    name = username()
    if not name:
        print("Привет! Добро пожаловать на курс по питону!")
    else:
        print(f"Привет, {name}! Добро пожаловать на курс по питону!")


if __name__ == "__main__":
    main()
