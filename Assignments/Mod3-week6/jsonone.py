import json

data = '''
{
    "name" : "Aruna",
    "phone" : {
    "type" : "intl",
    "number" : "+1 999-999-999"
    },
    "email" : {
    "hide" : "yes"
    }
}'''
   
info = json.loads(data)
print("Name: ", info['name'])
print("Hide: ", info['email']['hide'])   