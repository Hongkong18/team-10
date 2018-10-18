from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/codeforgood'

mongo = PyMongo(app)
eventsdb = mongo.db.events
employeesdb = mongo.db.employees
volunteersdb = mongo.db.volunteers
sponsorsdb = mongo.db.sponsors

@app.route('/event', methods=['GET'])
def get_event():
    name = request.args.get('name')
    print(name)
    event = eventsdb.find_one({'name': name})
    return jsonify({'result' : {
        'name': event['name'],
        'date': event['date'],
        'introduction': event['introduction'],
        'volunteers': event['volunteers'],
        'employees': event['employees'],
        'vendors': event['vendors'],
        'sponsors': event['sponsors']}})

@app.route('/events', methods=['GET'])
def get_all_events():
    cursor = eventsdb.find({})
    events = []
    for event in cursor:
        events.append({
        'name': event['name'],
        'date': event['date']})
    return jsonify({'result': events})

@app.route('/employees', methods=['GET'])
def get_available_employees():
    name = request.args.get('name')
    event = eventsdb.find_one({'name': name})
    current_employees = []
    for employee in event['employees']:
        current_employees.append(employee['name'])
    cursor = employeesdb.find({'availableTime': {'$gt': 0}})
    employees = []
    for employee in cursor:
        if employee['name'] not in current_employees:
            employees.append({'name':employee['name'],
            'email':employee['email']})
    return jsonify({'result': employees})

@app.route('/volunteers', methods=['GET'])
def get_available_volunteers():
    name = request.args.get('name')
    event = eventsdb.find_one({'name': name})
    current_volunteers = []
    for volunteer in event['volunteers']:
        current_volunteers.append(volunteer['name'])
    cursor = volunteersdb.find({'availableTime': {'$gt': 0}})
    current_volunteers = event['volunteers']
    volunteers = []
    for volunteer in cursor:
        if volunteer['name'] not in current_volunteers:
            volunteers.append({'name':volunteer['name'],
            'email':volunteer['email']})
    return jsonify({'result': volunteers})

@app.route('/sponsors', methods=['GET'])
def get_available_sponsors():
    name = request.args.get('name')
    event = eventsdb.find_one({'name': name})
    current_sponsors = []
    for sponsor in event['sponsors']:
        current_sponsors.append(sponsor['name'])
    all_sponsors = sponsorsdb.find({})
    sponsors = []
    for sponsor in all_sponsors:
        if sponsor['name'] not in current_sponsors:
            sponsors.append({'name' : sponsor['name'],
            'email':sponsor['email']})
    return jsonify({'result': sponsors})

if __name__ == '__main__':
    app.run(debug=True)