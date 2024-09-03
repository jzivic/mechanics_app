


b = {
        "length": [0, 10],
        "z": [0, 10],
        # "M": [10]
}




n = len(b.get("z", [])) + len(b.get("M", []))  # n will be 5


print(n)