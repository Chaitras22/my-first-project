"""
Shopping List - a tiny program for practising Git.

Run it with:   python shopping_list.py
You will change this file during the exercises in README.md.
"""

items = [
    "Milk",
    "Bread",
    "Eggs",
]


def show_list():
    print("My shopping list")
    print("----------------")
    for number, item in enumerate(items, start=1):
        print(f"{number}. {item}")
    print(f"\nTotal items: {len(items)}")


if __name__ == "__main__":
    show_list()
