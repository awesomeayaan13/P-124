from flask import Flask,jsonify,request
app=Flask(__name__)

tasks=[
    {
        'id':1,
        'name':"NPC_36932",
        'contact':"59234",
        'done':False
    },
    {
        'id':2,
        'name':"NPC_420",
        'contact':"00001",
        'done':False
    }
]

@app.route("/")

def no():
    return "yay"

@app.route("/add-data",methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please Provide the data"
        },400)
    contact={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }
    tasks.append(contact)
    return jsonify({
            "status":"Success",
            "message":"Task Added Successfully"
        })

@app.route("/get-data")
def get_contact():
    return jsonify({
            "data":tasks
        })

if __name__ == '__main__':
    app.run()
