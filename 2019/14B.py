day14 = __import__("14A")


ore_per_fuel = day14.produce("FUEL", 1)[0]["quantity"]
ore_in_stock = 1_000_000_000_000
create_n = round(ore_in_stock / ore_per_fuel)
used_ore = day14.produce("FUEL", create_n)[0]["quantity"]
print(int(create_n * ore_in_stock / used_ore))
