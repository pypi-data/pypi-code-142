from tortoise import fields, models


class ValorantGame(models.Model):
    match_id = fields.CharField(pk=True, max_length=200)
