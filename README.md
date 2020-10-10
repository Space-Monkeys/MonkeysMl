## MonkeysML
>  Python development test on the ESP32 microcontroller with micropython and Machine Learning with ScikitLearn

> configuration:
* pip install - r requirements
* cd src/
* flask run

```bash
curl --request POST \
  --url http://127.0.0.1:5000/ml \
  --header 'content-type: application/json' \
  --data '{
	"logicals" : [1,1]
}'
```

