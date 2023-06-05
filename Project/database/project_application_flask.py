from flask import Flask, jsonify, abort, request
from vote_characters import votesCharacters

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


# Votting on a character and getting the ip address from where the vote came from
# https://stackoverflow.com/questions/3759981/get-ip-address-of-visitors-using-flask-for-python
@app.route('/vote/<charactername>', methods=['POST'])
def voteCharnames(charactername):
    
    ip_address = request.remote_addr
    data = (charactername, ip_address)
    vote_id = votesCharacters.createVote(data)

    return jsonify({'id':vote_id})




#################################################################
# Counting the votes for each Character
@app.route('/vote/<charactername>', methods=['GET'])
def getVotesChar(charactername):
    count = votesCharacters.countCharactersVotes(charactername)
    return jsonify({charactername:count})



##############################################
@app.route('/vote', methods=['GET'])
def geAllChar(charactername):
    return jsonify({'name':'charactername'}, {'count': 999})



@app.route('/vote/all', methods=['delete'])
def deleteALLVotes():
    return jsonify({'done':True})



# Running the server
if __name__ == "__main__":
    app.run(debug=True)
