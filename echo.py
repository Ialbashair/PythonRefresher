def echo(text: str, repeitions: int = 3) -> str:
    """Imitate a real-world echo"""
    while(repeitions > 0):
        print(text[-repeitions:])
        repeitions -= 1

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))