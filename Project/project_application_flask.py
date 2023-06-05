from flask import Flask, jsonify, abort

# A simple votting app to see who is the most popular 58 character from the new Game Honkai Star Rail

app = Flask(__name__, static_url_path='', static_folder='html')

chars = [{'name':'Bailu'},
         {'name':'Bronya'},
         {'name':'Clara'},
         {'name':'Gepard'},
         {'name':'Himeko'},
         {'name':'Seele'},
         {'name':'Welt'},
         {'name':'Yanqing'},
         ]

# Request to get all characters names
@app.route('/characters', methods=['GET'])
def getAllCharnames():
    return jsonify(chars)


# Votting on a character
@app.route('/vote/<charactername>', methods=['POST'])
def voteCharnames(charactername):
    return jsonify({'name':charactername})


@app.route('/vote/<charactername>', methods=['GET'])
def getVotesChar(charactername):
    return '999'  # Placeholder 

@app.route('/vote', methods=['GET'])
def geAllChar(charactername):
    return jsonify({'name':'charactername'}, {'count': 999})

@app.route('/vote/all', methods=['delete'])
def deleteALLVotes():
    return jsonify({'done':True})



# Running the server
if __name__ == "__main__":
    app.run(debug=True)
