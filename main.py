import json

with open("states.json") as f:
  data=json.load(f)

#remove all state names with M, and dump it back to a new json file

for state in data['states']:
  namestate= state['name']
  if namestate[0].lower()=="m":
    del state

with open('newstates2.json', 'w') as f:
   json.dump(data,f,indent=2)

  
  