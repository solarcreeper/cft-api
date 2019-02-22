import mongoengine


class serverModel(mongoengine.EmbeddedDocument):
    ip = mongoengine.StringField()
    type = mongoengine.StringField()
    username = mongoengine.StringField()
    password = mongoengine.StringField()


class versionModel(mongoengine.EmbeddedDocument):
    ver = mongoengine.StringField
    sub = mongoengine.StringField


class diskModel(mongoengine.EmbeddedDocument):
    type = mongoengine.StringField
    capacity = mongoengine.StringField
    manufacturer = mongoengine.StringField
    model = mongoengine.StringField
    manufacturer_capacity = mongoengine.StringField


class interfaceModel(mongoengine.EmbeddedDocument):
    type = mongoengine.StringField


class cpuModel(mongoengine.EmbeddedDocument):
    num = mongoengine.StringField
    type = mongoengine.StringField
    detail = mongoengine.StringField


class memModel(mongoengine.EmbeddedDocument):
    size = mongoengine.StringField
    num = mongoengine.StringField
    type = mongoengine.StringField


class storageModel(mongoengine.EmbeddedDocument):
    model = mongoengine.StringField
    sn = mongoengine.StringField
    controllers = mongoengine.StringField
    ip = mongoengine.ListField
    version = mongoengine.EmbeddedDocumentField(versionModel)
    disk = mongoengine.EmbeddedDocumentListField(diskModel)
    interface = mongoengine.EmbeddedDocumentListField(interfaceModel)
    cpu = mongoengine.EmbeddedDocumentField(cpuModel)
    mem = mongoengine.EmbeddedDocumentField(memModel)


class InfoModel(mongoengine.Document):
    env_name = mongoengine.StringField()
    date = mongoengine.StringField()
    server = mongoengine.EmbeddedDocumentListField(serverModel)
    storage = mongoengine.EmbeddedDocumentListField(storageModel)
