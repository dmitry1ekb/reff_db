from peewee import *

db = SqliteDatabase('users.db')


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    user_id = IntegerField(unique=True)
    ref = IntegerField(default=0)
    ref_ids = IntegerField(default='')

    @classmethod
    def get_user(cls, user_id):
        return cls.get(user_id == user_id)

    @classmethod
    def get_ref_count(cls, user_id):
        return cls.get_user(user_id).ref

    @classmethod
    def get_ref_ids(cls, user_id):
        return cls.get_user(user_id).ref_ids

    @classmethod
    def increase_ref_count(cls, user_id):
        user = cls.get_user(user_id)
        user.ref += 1
        user.save()

    @classmethod
    def increase_ref_ids(cls, user_id, ref_id):
        user = cls.get_user(user_id)
        user.ref_ids += str(ref_id)
        user.save()

    @classmethod
    def user_exists(cls, user_id):
        query = cls().select().where(cls.user_id == user_id)
        return query.exists()

    @classmethod
    def create_user(cls, user_id):
        user, created = cls.get_or_create(user_id=user_id)