import json 



def run():
    agency_json_path = 'lifeweb_gateways/components/news.json'
    with open(agency_json_path, 'r') as j:
        agency = json.loads(j.read())

    instagram_json_path = 'lifeweb_gateways/components/instagram.json'
    with open(instagram_json_path, 'r') as j:
        instagram = json.loads(j.read())

    tel_group_json_path = 'lifeweb_gateways/components/telegram_group.json'
    with open(tel_group_json_path, 'r') as j:
        tel_group = json.loads(j.read())

    tel_chanel_json_path = 'lifeweb_gateways/components/telegram_channel.json'
    with open(tel_chanel_json_path, 'r') as j:
        tel_chanel = json.loads(j.read())

    twitter_json_path = 'lifeweb_gateways/components/twitter.json'
    with open(twitter_json_path, 'r') as j:
        twitter = json.loads(j.read())

    return  instagram['data']  ,tel_group['data'] , \
            tel_chanel['data'] ,twitter['data'] , agency['data']