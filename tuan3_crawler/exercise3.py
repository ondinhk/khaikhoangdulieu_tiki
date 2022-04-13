import pandas as pd

datashet = pd.read_csv('../tailieu/tuan3_crawler/tailieu/winemag-data-130k-v2.csv', index_col=0)
pd.set_option("display.max_rows", 5)

# 1. median of the points (Trung vị - sắp xếp từ nhỏ tới lớn rồi chọn số giữa)
print("--------------------------------------")
median = datashet.points.median()
print(median)

# 2. not include any duplicates (mảng các giá trị không trùng lặp)
print("--------------------------------------")
countries = datashet.country.unique()
print(countries)

# 3. Đếm số lần xuất hiện của 1 giá tr
print("-------------------------------------")
count_per_country = datashet.country.value_counts()
print(count_per_country)

# 4. mean giá trị trung bình (tổng rồi chia)
print("-------------------------------------")
print(datashet.price.mean())
centered_price = datashet.price - datashet.price.mean()
print(centered_price)

# 5. Loại lời nhất
print("-------------------------------------")
bargain_idx = (datashet.points / datashet.price).idxmax()
# Chỉ số trả về của lần xuất hiện đầu tiên của tối đa trên trục được yêu cầu.
print(bargain_idx)
bargain_wine = datashet.loc[bargain_idx, 'title']
print(bargain_wine)

# 6. Đếm số từ xuất hiện
print("-------------------------------------")
n_trop = datashet.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = datashet.description.map(lambda desc: "fruity" in desc).sum()
# In dữ liệu theo nhãn tùy chinh
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
print(descriptor_counts)

# 7. Apply star.
print("-------------------------------------")


def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1


star_rating = datashet.apply(stars, axis="columns")
print(star_rating.head())
