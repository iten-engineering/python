
articles = {
    11: {
        "name"  : "Bildschirm Belinea X3",
        "price" : 499.50
    },
    12: {
        "name"  : "PC Tastatur Swiss German",
        "price" : 35.00
    },
    13: {
        "name"  : "Logitec Maus",
        "price" : 17.25
    },
    14: {
        "name"  : "USB Hub",
        "price" : 25.70
    },
    15: {
        "name"  : "Lautsprecher X66-12",
        "price" : 87.90
    }
}

print("List all articles:")
for nr in articles:
    print(articles[nr])


print("\nShow article with lowest price:")
article = None
for nr in articles:
    if article == None:
        article = articles[nr]
        continue
    if articles[nr]["price"] < article["price"]:
        article = articles[nr]
print(article)


print("\nGive a 20% discount of all prices and list articles:")
for nr in articles:
    articles[nr]["price"] = articles[nr]["price"] * 0.8
    print(articles[nr])





