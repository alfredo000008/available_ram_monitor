import os

def main():

    name = os.getenv("USERNAME")

    if name is None:
        print("Name env variable could not be found.")
        return
    print(f"Hello {name}. This is a message from the CI/CD pipeline.")

if __name__ == "__main__":
    main()