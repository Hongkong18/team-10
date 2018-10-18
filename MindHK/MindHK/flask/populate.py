import pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient

mongo = MongoClient('localhost', 27017)
db = mongo['codeforgood']
eventsdb = db.events
employeesdb = db.employees
volunteersdb = db.volunteers
sponsorsdb = db.sponsors

eventsdb.delete_many({})
employeesdb.delete_many({})
volunteersdb.delete_many({})
sponsorsdb.delete_many({})

employees = [{
	'name': 'roger',
	'email': 'roger@example.com',
	'availableTime': 3
},
{
	'name': 'shally',
	'email': 'shally@example.com',
	'availableTime': 5
},
{
	'name': 'david',
	'email': 'david@example.com',
	'availableTime': 1
},
{
	'name': 'ed', 
	'email': 'ed@example.com',
	'availableTime': 7
},
{
	'name': 'james', 
	'email': 'james@example.com',
	'availableTime': 1
},
{
	'name': 'tomas', 
	'email': 'tomas@example.com',
	'availableTime': 3
}
]

volunteers = [{
	'name': 'roger_vol',
	'email': 'roger@example.com',
	'availableTime': 3
},
{
	'name': 'shally_vol',
	'email': 'shally@example.com',
	'availableTime': 4
},
{
	'name': 'david_vol',
	'email': 'david@example.com',
	'availableTime': 5
},
{
	'name': 'ed_vol',
	'email': 'ed@example.com',
	'availableTime': 4
},
{
	'name': 'james_vol', 
	'email': 'james@example.com',
	'availableTime': 1
},
{
	'name': 'tomas_vol', 
	'email': 'tomas@example.com',
	'availableTime': 10
}
]

sponsors = [{
	'name': 'roger_spo',
	'email': 'roger@example.com'
},
{
	'name': 'shally_spo',
	'email': 'shally@example.com'
},
{
	'name': 'david_spo',
	'email': 'david@example.com'
},
{
	'name': 'ed_spo',
	'email': 'ed@example.com'
},
{
	'name': 'james_spo',
	'email': 'james@example.com'
},
{
	'name': 'tomas_spo',
	'email': 'tomas@example.com'
}]

events = [{
            'name': 'CodeForGood',
            'introduction': 'Cooperation with JPM HK',
            'date': '11-11-18',
            'employees': [{
                                'name': 'roger',
                                'email': 'roger@example.com',
                                'availableTime': 3
                            },
                            {
                                'name': 'ed',
                                'email': 'ed@example.com',
                                'availableTime': 3
                            },],
            'volunteers': [{
                                'name': 'roger_vol', 
                                'email': 'roger@example.com',
                                'availableTime': 3
                            },
                            {
                                'name': 'ed_vol', 
                                'email': 'ed@example.com',
                                'availableTime': 3
                            },],
            'vendors':  [{
                                'name': 'roger_ven', 
                                'email': 'roger@example.com',
                                'availableTime': 3
                            },
                            {
                                'name': 'ed_ven',
                                'email': 'ed@example.com',
                                'availableTime': 3
                            },],
            'sponsors': [{
                                'name': 'roger_spo',
                                'email': 'roger@example.com',
                                'availableTime': 3
                            },
                            {
                                'name': 'ed_spo',
                                'email': 'ed@example.com',
                                'availableTime': 3
                            },]
        },

            {
                'name': 'CodeForGreat',
                'introduction': 'Cooperation with JPM HK',
                'date': '11-12-18',
                'employees': [{
                                    'name': 'roger', 
                                    'email': 'roger@example.com',
                                    'availableTime': 3
                                },
                                {
                                    'name': 'ed',
                                    'email': 'ed@example.com',
                                    'availableTime': 3
                                },],
                'volunteers': [{
                                    'name': 'roger_vol',
                                    'email': 'roger@example.com',
                                    'availableTime': 3
                                },
                                {
                                    'name': 'ed_vol',
                                    'email': 'ed@example.com',
                                    'availableTime': 3
                                },],
                'vendors':  [{
                                    'name': 'roger_ven',
                                    'email': 'roger@example.com',
                                    'availableTime': 3
                                },
                                {
                                    'name': 'ed_ven', 
                                    'email': 'ed@example.com',
                                    'availableTime': 3
                                },],
                'sponsors': [{
                                    'name': 'roger_spo', 
                                    'email': 'roger@example.com',
                                    'availableTime': 3
                                },
                                {
                                    'name': 'ed_spo',
                                    'email': 'ed@example.com',
                                    'availableTime': 3
                                },]
            },
            {
                'name': 'CodeForSupreme',
                'introduction': 'Cooperation with JPM HK',
                'date': '10-10-18',
                'employees': [{
                                    'name': 'roger', 
                                    'email': 'roger@example.com',
                                    'availableTime': 3
                                },
                                {
                                    'name': 'ed',
                                    'email': 'ed@example.com',
                                    'availableTime': 3
                                },],
                'volunteers': [{
                                    'name': 'roger_vol', 
                                    'email': 'roger@example.com',
                                    'availableTime': 3
                                },
                                {
                                    'name': 'ed_vol',
                                    'email': 'ed@example.com',
                                    'availableTime': 3
                                },],
                'vendors':  [{
                                    'name': 'roger_ven', 
                                    'email': 'roger@example.com',
                                    'availableTime': 3
                                },
                                {
                                    'name': 'ed_ven',
                                    'email': 'ed@example.com',
                                    'availableTime': 3
                                },],
                'sponsors': [{
                                    'name': 'roger_spo', 
                                    'email': 'roger@example.com',
                                    'availableTime': 3
                                },
                                {
                                    'name': 'ed_spo',
                                    'email': 'ed@example.com',
                                    'availableTime': 3
                                },]
            }
]

for event in events:
    eventsdb.insert_one(event)

for employee in employees:
    employeesdb.insert_one(employee)

for volunteer in volunteers:
    volunteersdb.insert_one(volunteer)

for sponsor in sponsors:
    sponsorsdb.insert_one(sponsor)    

