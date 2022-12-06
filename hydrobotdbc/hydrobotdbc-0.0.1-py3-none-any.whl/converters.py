from .models import User

def ConvertPyodbcToUser(row):
    return models.User(row.DiscordId, row.UserName, row.Discriminator, row.HydroBux, row.Meows)
