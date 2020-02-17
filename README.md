# Simple TODO List 

## Link

https://todo-andrii.appspot.com/

## RESTful web service

| HTTP Method | Action                            | Examples                 |
|-------------|-----------------------------------|--------------------------|
| GET         | Obtain information about all task | /get                     |
| POST        | Create new task                   | /add                     |
| PUT         | Update status of task             | /mark                    |
| DELETE      | Delete task                       | /remove                  |

## GET
### Success Response

```json

HTTP/1.0 200 OK
Content-Type: application/json

{
    "result": [{
        "description": "Some task", 
        "id": 122342344234, 
        "status":"False"
    }]
}

```


## POST
### Data
```json

{"description": "Some task"}
```

### Success Response

```json

HTTP/1.0 200 OK
Content-Type: application/json

{"description": "Some task", "id": 34343432323, "status": "False"}

```

## PUT

### Data
```json
{"todo_id": 12143433233, "status": "True | False"}
```

### Success Response

```json

HTTP/1.0 200 OK
Content-Type: application/json

{"id": 12143433233, "status": "True | False"}

```

## DELETE

### Data

```json
{"todo_id": 12143433233}
```

### Success Response

```json

HTTP/1.0 200 OK
Content-Type: application/json

{"id": 3432323434431}

```

## How to deploy 

1) Install the [Cloud SDK](https://cloud.google.com/sdk/docs/)
2) Create a new project:

    `gcloud projects create [YOUR_PROJECT_ID]`

    Verify the project was created:

    `gcloud projects describe [YOUR_PROJECT_ID]`

3) Initialize your App Engine app with your project and choose its region:

    `gcloud app create --project=[YOUR_PROJECT_ID]`

4) Clone the Todo List repository to your local machine.

    `git clone https://github.com/andriisem/todo-list.git`

5) Deploy app by running the following command from the todo-list directory:

    ` gcloud app deploy app.yaml --project [YOUR_PROJECT_ID]`