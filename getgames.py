from gogapi import GogApi, Token
import json

token = Token.from_file("token.json")
if token.expired():
    token.refresh()
    token.save("token.json")

api = GogApi(token)

# api.web_games_gogdata()


# prod = api.product(2134842136)
# prod.update_galaxy(expand=True)

game_ids = api.web_user_games()['owned']

print("Games:", game_ids)

myfile = open("owned.json", 'w')
myfile.write(json.dumps(game_ids))
myfile.close()


def get_gameinfo(id):
    raw_game = api.web_account_gamedetails(id)

    if type(raw_game) is not dict:
        return {
            "id": id,
            "error": "no data"
        }

    languages = []
    downloads = raw_game['downloads']
    for i in range(0, len(downloads)):
        print(i)
        download = downloads[i]
        languages.append(download[0])

    return {
        "id": id,
        "title": raw_game['title'],
        "releaseTimestamp": raw_game['releaseTimestamp'],
        "backgroundImage": raw_game['backgroundImage'],
        "languages": languages
    }

games_with_info = []
for i in range(0, len(game_ids)):
        game_id = game_ids[i]
        print("fetching for id", game_id)
        games_with_info.append(
            get_gameinfo(game_id)
        )



myfile = open("owned.json", 'w')
myfile.write(json.dumps({
 "ids": game_ids,
 "data": games_with_info
}))
myfile.close()
