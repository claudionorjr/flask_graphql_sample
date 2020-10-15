import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from src.models import User, Post
from data.database import db


class PostObject(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (graphene.relay.Node, )


class UserObject(SQLAlchemyObjectType):
   class Meta:
       model = User
       interfaces = (graphene.relay.Node, )


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True) 
        username = graphene.String(required=True)


    post = graphene.Field(lambda: PostObject)

    def mutate(self, info, title, body, username):
        user = User.query.filter_by(username=username).first()
        post = Post(title=title, body=body)

        if user is not None:
            post.author = user

        db.session.add(post)
        db.session.commit()
        return CreatePost(post=post)


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)


    user = graphene.Field(lambda: UserObject)

    def mutate(self, info, username):
        user = User(username=username)
        
        db.session.add(user)
        db.session.commit()
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(PostObject)
    all_users = SQLAlchemyConnectionField(UserObject)
    
    
schema = graphene.Schema(query=Query, mutation=Mutation)
