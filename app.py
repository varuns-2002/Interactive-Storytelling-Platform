from flask import Flask, request, jsonify, render_template
import example_worlds
from models import GeminiModel
from prompts import prompt_narrate_current_scene, prompt_world_update
import re

app = Flask(__name__)

# Instantiate the world and model
world = example_worlds.get_world("1")
model = GeminiModel(r"C:\Users\saxen\Documents\payador-main (2)[1]\payador-main\payador-main\API KEY.txt")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.get_json()
    user_input = data['input']

    # Update the world state and get model responses
    prompt_scene = prompt_narrate_current_scene(world.render_world())
    response_scene = model.prompt_model(prompt_scene)

    prompt_update = prompt_world_update(world.render_world(), user_input)
    response_update = model.prompt_model(prompt_update)

    world.parse_updates(response_update)

    # Format the response
    response_data = {
        'worldState': world.render_world(),
        'narration': response_scene,
        'predictedOutcomes': response_update,
        'predictedNarration': re.findall(r'#([^#]*?)#', response_update)[0]
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
