# from flask import Flask, request, jsonify
# app = Flask(__name__)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         input_text = request.form['input_text']
#         # Call the Chat GPT API and get the response
#         # You can use a library like requests to send HTTP requests to the API
#         # For example: response = requests.post(api_url, data={'text': input_text})
#         # Parse the response and get the output
#         # For example: output = response.json()['output']
#         output = "Hello, World!"  # Replace this with the actual output from the API
#         return jsonify({'output': output})
#     else:
#         return '''
#             <form method="post">
#                 <input type="text" name="input_text">
#                 <input type="submit" value="Submit">
#             </form>
#         '''
