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


## POST

```json

{"description": "Some task"}
```

## PUT

```json
{"todo_id": 12143433233, "status": "True"}
```

## DELETE

```json
{"todo_id": 12143433233}
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