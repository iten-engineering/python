
articles = {
    1 : "Bildschrim",
    2 : "Tastatur"
}
print(articles)

articles[3] = "Maus"
print(articles)

for k,v in articles.items():
    print(k, v)

print(articles.values())


game_config = {
    "max_players" : 5,
    "color" : "red",
    "teams" : ["Team A", "Team B"]
}

print(game_config["max_players"])