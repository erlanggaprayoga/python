import statistics
# 1 Cari Rata Rata
data = [90, 84, 88, 83, 87, 85, 83, 71]
rerata = statistics.mean(data)

# 2 Cari Varian
list_varian = []
for bilangan in data:
    list_varian.append(
        (bilangan - rerata)**2
    )
varian = sum(list_varian) / (len(data) - 1)

# 3 Hitung Standar Deviasi
simpangan_baku = statistics.sqrt(varian)
print(f'data \t \t -> {data}')
print(f'simpangan baku \t \t -> {simpangan_baku}')