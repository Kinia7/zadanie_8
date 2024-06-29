from mongoengine import Document, StringField, ReferenceField, ListField, connect

connect(host="mongodb://localhost:27017")

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)
