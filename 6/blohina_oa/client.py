from random import choice
import requests
s = requests.Session()
server_link = 'http://127.0.0.1:8000'
diseases = ['Agoraphobia','Antisocial personality disorder', 'Any anxiety disorder', 'Any disruptive behaviour disorder', 'Any mood disorder', 'Attention deficit hyperactivity (ADHD)', 'Bipolar disorder', 'Conduct disorder', 'Dysthymia (persistent, mild depression)', 'Generalized anxiety disorder (GAD)', 'Intermittent explosive disorder', 'Major depression', 'Oppositional defiant disorder', 'Panic disorder', 'Post-traumatic stress disorder (PTSD)', 'Separation anxiety','Social phobia', 'Specific phobia']
entity = choice(diseases)
r = s.get(server_link, params = {'entity': entity})
print(r.json())
