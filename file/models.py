from tortoise import models, fields


class File(models.Model):
    id = fields.IntField(pk=True)
    file_path = fields.CharField(max_length=512)
    file_hash = fields.CharField(max_length=512, null=True, unique=True)
    uploaded_at = fields.DatetimeField(auto_now_add=True)
