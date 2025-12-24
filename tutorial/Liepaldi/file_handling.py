import pandas as pd

data = [
    ["Lievaldy", 100, "Champion"],
    ["BCR", 110, "Becek"],
    ["Sans", 40, "Sanpek"]
]


df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)
print()
