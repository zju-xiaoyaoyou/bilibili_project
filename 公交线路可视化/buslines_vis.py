from flask import Flask, send_from_directory
from flask import render_template
import json

def get_city_info_by_pinyin(city_name_pinyin):
    json_url = './data/BaiduMap_CityInfo.json'
    with open(json_url, 'r') as f:
        json_data = json.load(f)
    for key, value in json_data.items():
        if(city_name_pinyin == value['city_name_pinyin']):
            return value

app = Flask(__name__)

@app.route('/buslines/data/<path:filename>')
def get_json(filename):
    return send_from_directory('./data', filename)

@app.route('/buslines/<city_name_pinyin>')
def buslines_vis(city_name_pinyin):
    city_info = get_city_info_by_pinyin(city_name_pinyin)
    city_center = city_info['city_center']
    print(city_center)
    city_dict = {
        'json_url': f'./data/lines-bus_{city_info['city_name_pinyin']}.json',
        'center': [city_center['lng'], city_center['lat']],
        'zoom': 11
    }
    html = render_template('lines-bmap-effect.html', city_dict=city_dict)
    return html

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=False, port=8888)