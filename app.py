from flask import Flask, request, jsonify
from YouTube_Scrape import scrape_videos

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def api_scrape():
    query = request.args.get('q', 'inteligencia artificial')
    idioma = request.args.get('idioma', 'es')
    resultados = scrape_videos(query, idioma)
    return jsonify(resultados)

if __name__ == '__main__':
    app.run()
