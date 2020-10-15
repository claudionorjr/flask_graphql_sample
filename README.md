payloads:
query posts:
{
  allPosts{
    edges{
      node{
        title
        body
        author{
          username
        }
      }
    }
  }
}


query users:
{
  allUsers{
    edges{
      node{
        username
      }
    }
  }
}


Mutation create user:
mutation {
  createUser(username:"johndoe"){
    user{
      uuid
      username
    }
  }
}


Mutation create post:
mutation {
  createPost(username:"johndoe", title:"Hello 2", body:"Hello body 2"){
    post{
      title
      body
      author{
        username
      }
    }
  }
}