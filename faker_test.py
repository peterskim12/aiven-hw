from faker import Faker
import json

fake = Faker()

for _ in range(10):
  event = {'entry_time': fake.past_datetime().isoformat(), 'uuid': fake.uuid4()}
  event.update(fake.simple_profile())
  print(json.dumps(event, default=str))
  
  

