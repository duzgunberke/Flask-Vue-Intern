# Flask-Vue-Intern

Flask was used for the background in this project. Vue is used for the frontend. It is a basic blogging application.


## Environment Variables

You will need to add the following environment variables to your *.env* file to run this project. Create your *.env* file in backend and frontend folders

#### Backend :
`DATABASE_URI`  = `mongodb+srv://{username}:{password}@{clustername}.g4lwsqz.mongodb.net/{databasename}?retryWrites=true&w=majority`

`SECRET_KEY`  = `It's a secret key for a your application`

#### Frontend
`VUE_API_URL` = `URL where your backend server is running`

`VUE_API_HEADER`  = `Get token from localstorage`

  


## Run project

Follow the steps below to run the project

In backend folder :

```bash
  pip install -r requirements.txt
```
```bash
  python main.py
```
In frontend folder :

```bash
  npm install
```
```bash
  npm install --global yarn
```
```bash
  yarn run serve
```



## API Map

#### Get all blogs

```http
  GET /blogs
```




#### Add blog
```http
  POST /blogs
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | **Required**. Title of the new blog |
| `description` | `string` | **Required**. Description of the new blog |
| `current_user` | `string` | **Required**. Author of the new blog |



#### Get blog by id

```http
  POST /getblogbyid
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. ID of the blog |


#### Update blog

```http
  GET - PUT /blog/{id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. ID of the blog | 
| `title` | `string` | **Required**. Title of the updated blog |
| `description` | `string` | **Required**. Description of the updated blog |


#### Delete blog

```http
 DELETE /blog/{_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `_id`      | `string` | **Required**. ID of the blog | 

#### Signup User

```http
  POST /signup
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string`| **Required**. New user's name |
| `surname`      | `string`| **Required**. New user's surname |
| `email`      | `string`| **Required**. New user's email |
| `username`      | `string`| **Required**. New user's username |
| `password`      | `string`| **Required**. New user's password |

#### Login User

```http
  POST /signup
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string`| **Required**. User's username |
| `password`      | `string`| **Required**. User's password |

#### Get Users

```http
  GET /users
```


#### Current User

```http
  GET /currentuser
```

| How | Its     | Working                       |
| :-------- | :------- | :-------------------------------- |
| `token`      | `header` | The information of the logged in user stored in the token in the http header |
