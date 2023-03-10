"""
    input : ["goat", "cat", "dog", "hen"]


    function setup(input) -> [input]

    function isInArr(word) -> bool



    setup(["goat", "cat", "dog", "hen"])

    isInArr("goat") returns True
    isInArr("snake") returns False
"""


def setup(input: list[str]) -> list[str]:
    return input



def isInArr(value: str, input: list[str])-> bool:

    return value in setup(input)



if __name__ == "__main__":
    try:
        response= isInArr(
            value="dog",
            input=["goat", "cat", "dog", "hen"]
        )
        print()
        print(response)

    except Exception as e:
        raise e


