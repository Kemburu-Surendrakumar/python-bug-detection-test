from calculator import add, multiply, divide
from user_utils import normalize_username
from file_utils import get_extension


def main():
    print("Addition:", add(10, 5))
    print("Multiplication:", multiply(3, 4))
    print("Division:", divide(10, 2))
    print("Username:", normalize_username(" Surendra "))
    print("Extension:", get_extension("report.pdf"))


if __name__ == "__main__":
    main()
