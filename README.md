# aiven-hw

## producer.py

This Python script generates event data representing a person at a point-in-time. The event has this structure:

```json
{
    entry_time: "2023-12-03T20:54:27.121758"
    uuid: "ce4bbb9d-4173-4346-a809-cec0d4ec7db7"
    username: "zwright"
    name: "Michael Lin"
    sex: "M"
    address: "88912 Marcia Meadows East Carol, VI 21704"
    mail: "glasschristina@hotmail.com"
    birthdate: "1974-05-08"
}
```

```sh
python3 producer.py --service-uri <service_uri> \
     --ca-path <ca_file> \
     --key-path <servicekey_file> \
     --cert-path <servicecert_file> \
     --num-events <num_events>
```


