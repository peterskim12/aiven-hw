import argparse
import os
import sys
import json
from kafka import KafkaProducer
from faker_test import Faker

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--service-uri', help="Service URI in the form host:port",
                        required=True)
    parser.add_argument('--ca-path', help="Path to project CA certificate",
                        required=True)
    parser.add_argument('--key-path', help="Path to the Kafka Access Key (obtained from Aiven Console)",
                        required=True)
    parser.add_argument('--cert-path', help="Path to the Kafka Certificate Key (obtained from Aiven Console)",
                        required=True)
    parser.add_argument('--num-events', help="Number of events to generate", type=int, 
                        required=True)
    args = parser.parse_args()
    validate_args(args)

    producer = KafkaProducer(
        bootstrap_servers=args.service_uri,
        security_protocol="SSL",
        ssl_cafile=args.ca_path,
        ssl_certfile=args.cert_path,
        ssl_keyfile=args.key_path,
    )

    fake = Faker()
    generate_data(producer, fake, args.num_events)


def validate_args(args):
    for path_option in ("ca_path", "key_path", "cert_path"):
        path = getattr(args, path_option)
        if not os.path.isfile(path):
            fail(f"Failed to open --{path_option.replace('_', '-')} at path: {path}.\n"
                 f"You can retrieve these details from Overview tab in the Aiven Console")
    
def generate_data(producer, fake, num_events):
    for _ in range(num_events):
        event = {'entry_time': fake.past_datetime().isoformat(), 'uuid': fake.uuid4()}
        event.update(fake.simple_profile())
        producer.send("pkim_hw_topic", json.dumps(event, default=str).encode("utf-8"))
    
    # Wait for all messages to be sent
    producer.flush()

def fail(message):
    print(message, file=sys.stderr)
    exit(1)

if __name__ == '__main__':
    main()