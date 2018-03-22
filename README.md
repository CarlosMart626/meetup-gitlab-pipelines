# Gitlab pipelines using pytest and flake8

<p align="center">
  <img src="https://s3.amazonaws.com/carlosmart.co/gitlab-python.jpg">
</p>

## Gitlab Pipeline
This example contains the following stages:

* build
* test
* staging
* integration_tests
* deploy

[Gitlab pipeline caption]

## Example Django project

This is an example **Gitlab Pipelines** using a project of a **courses** platform allowing to create users and courses and to enroll into a desired course using graphql.

### Courses Features
- Create students with profile
- Create courses
- Enroll students to courses

### Running the project
**Requires Docker installed**
To run the project execute: 

```
cd djcourses
docker-compose up
```

After run this command open your navigator at `http://localhost:8080/graphiql` to get into the Graphql query environment.

### Firsts Graphql queries

**Query**
``` json
query{
  hello
}
```

**Result**
``` json
{
  "data": {
    "hello": "world"
  }
}
```
