countries = input().split(", ")
capitals = input().split(", ")
dict_of_capitals = {k: v for k, v in (zip(countries, capitals))}
for k, v in dict_of_capitals.items():
    print(f"{k} -> {v}")
