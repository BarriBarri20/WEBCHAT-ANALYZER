from flask import Flask
import flask

from openaiscirpts import call_api_openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

prompt = """
<div class="bg-white min-h-screen relative overflow-hidden"><div class="absolute top-0 left-0 w-full h-full overflow-hidden"><div class="absolute top-0 left-0 w-[50%] h-[50%] bg-blue-500 rounded-full mix-blend-multiply filter blur-[200px]"></div><div class="absolute bottom-0 right-0 w-[60%] h-[60%] bg-red-500 rounded-full mix-blend-multiply filter blur-[200px]"></div><div class="absolute top-0 right-0 w-[40%] h-[40%] bg-green-500 rounded-full mix-blend-multiply filter blur-[200px]"></div><div class="absolute bottom-0 left-0 w-[30%] h-[30%] bg-yellow-500 rounded-full mix-blend-multiply filter blur-[200px]"></div></div><header class="flex justify-between p-6 bg-transparent text-black"><div><h1 class="font-bold text-2xl">Colorful Motifs</h1></div><div class="space-x-4"><a class="text-black hover:underline" href="#">Home</a><a class="text-black hover:underline" href="#">About</a><a class="text-black hover:underline" href="#">Contact</a></div></header><main class="p-6 flex items-center justify-center h-[50vh]"><h2 class="text-6xl font-bold text-center text-black">A Grand Movie Title</h2></main><section class="mt-10 mb-10 px-6"><p class="font-normal text-lg text-black mb-4">Here's a thought to enrich your day:</p><blockquote class="border-l-4 border-black pl-4 italic text-lg text-black">"The only way to do great work is to love what you do." - Steve Jobs</blockquote></section><footer class="p-6 bg-transparent text-black text-center"><p>2023 Colorful Motifs</p></footer></div>
"""

@app.route('/get_choices', methods=['GET'])
def index():

    theme = flask.request.args.get('mood', "funny")
    lang = flask.request.args.get('lang', "english")
    print(theme)

    css_results = call_api_openai(prompt, theme, lang).replace('\n', '').strip()
    return flask.jsonify({"html": css_results})

           

if __name__ == "__main__":
    app.run(debug=True)