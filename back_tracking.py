import itertools

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
percentages = [10, 20, 30, 40]

len_users = len(users)
len_emoticons = len(emoticons)

# possibleSales = []

# for user in users:
#     if user[0] not in possibleSales:
#         possibleSales.append(user[0])

# possibleSales.sort()

sale_datas = list(itertools.product(percentages, repeat=len_emoticons))

maxJoin = 0
maxAmount = 0
min_sale = [1] * len_emoticons

for sale in sale_datas:
    user_join = [False] * len_users
    totalAmount = 0

    for i in range(len_users):
        [target_percentage, target_amount] = users[i]
        amount = 0
        for j in range(len_emoticons):
            if sale[j] >= target_percentage:
                amount += emoticons[j] * (100 - sale[j]) / 100
        if amount >= target_amount:
            user_join[i] = True
        else:
            totalAmount += amount
        
        join = sum(user_join)

    if (join > maxJoin) or (join >= maxJoin and totalAmount > maxAmount):
        maxJoin = join
        maxAmount = totalAmount
        min_sale = sale


