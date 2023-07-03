import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['input_text']
        temp = 0.6
        responseTone = "neutral"
        response_text = askGPT(text, temp, responseTone)
        return render_template('index.html', output=response_text)
    return render_template('index.html')

def askGPT(text, temp, responseTone):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        # prompt = "Analyze the following conversation, be sure to identify the tone (and the tones of each person) and provide a short " + responseTone + " follow-up response to the last question/comment proposed by the person in the conversation. Here is the conversation: " + text + " if you arent sure of the names of people talking, replace names with person 1 and person 2 etc. DO NOT MODIFY THE EXISTING CONVERSATION, ONLY ADD TO IT",
        prompt = "Analyze the following conversation, and try to identify the tones of all members of the conversation. Then, given the context of the conversation, come up with a "+responseTone+" response that I (assume I am a member of the conversation) can send to follow up with. Here is the conversation: " + text+ "if you arent sure of the names of the people, just call the people person 1, person 2 etc. after each tone, write ",
        temperature = temp,
        max_tokens = 300,
    )
    return response.choices[0].text

if __name__ == '__main__':
    app.run(debug=True)