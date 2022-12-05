import pendulum

from redisopy.base.connection import connect
from redisopy.fields import StringField, IntField, BooleanField, DatetimeField
from redisopy.models import Model


class Person(Model):
    name = StringField()
    age = IntField()
    is_active = BooleanField()

    class Meta:
        key_prefix = "UpUp:person:"


class Person2(Model):
    name = StringField()
    age = IntField()

    class Meta:
        key_prefix = "UpUp:person2:"


connect(db=3)


def test_use_model():
    class PersonWithId(Model):
        id = IntField()
        name = StringField()
        age = IntField()

    person = Person(name='John', age=20, is_active=True)
    person.save()
    person2 = Person(name='John', age=20, is_active=False)
    person2.save()
    person3 = PersonWithId(name='John Has id', age=20, id=1)
    person3.save(is_override=True)
    rows = Person.filter()
    for r in rows:
        print(r)


def test_instance_delete():
    person = Person2(name='John', age=20)
    person.save()
    person.delete()


def test_get_instance():
    person = Person2(name='test', age=99)
    person.save()
    person2 = Person2.get_by_id(r_id=person.record_id)
    print(person2)


def test_time():
    class PersonWithTime(Model):
        name = StringField()
        age = IntField()
        time = DatetimeField()

    person = PersonWithTime(name='John', age=20, time=pendulum.now())
    person.save()
