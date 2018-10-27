from mongoengine import connect,StringField,DateTimeField,Document

DB_HOST='127.0.0.1'
DB_PORT=27017
DB_NAME='test'

connect(DB_NAME,host=DB_HOST,port=DB_PORT)

class BaseModel(Document):
    create_at=DateTimeField()
    meta={
        'allow_inheritance':True,
        'abstract':True
    }
class Proxy(BaseModel):
    address=StringField(unique=True)
    meta = {'collection':'proxy'}

    @classmethod
    def get_random(cls):
        proxy=cls.objects.aggregate({'$sample':{'size':1}}).next()
        return proxy

