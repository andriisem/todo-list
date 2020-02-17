# Simple TODO List 

## Link

https://todolist-andriisem.appspot.com/

## RESTful web service

| HTTP Method | Action                            | Examples                 |
|-------------|-----------------------------------|--------------------------|
| GET         | Obtain information about all task | /get                     |
| POST        | Create new task                   | /add                     |
| PUT         | Update status of task             | /mark                    |
| DELETE      | Delete task                       | /remove                  |


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