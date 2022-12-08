from enum import Enum

Events: list[str] = ['ready', '']


class Intents(Enum):  # Discord intents
    Guilds: int = 1 << 0
    GuildMembers: int = 1 << 1
    GuildBans: int = 1 << 2
    GuildEmojiAndStickers: int = 1 << 3
    GuildIntegrations: int = 1 << 4
    GuildWebhooks: int = 1 << 5
    GuildInvites: int = 1 << 6
    GuildVoiceStates: int = 1 << 7
    GuildPresences: int = 1 << 8
    GuildMessages: int = 1 << 9
    GuildMessageReactions: int = 1 << 10
    GuildStartTyping: int = 1 << 11
    DirectMessages: int = 1 << 12
    DirectMessageReactions: int = 1 << 13
    DirectMessageTyping: int = 1 << 14
    MessageContent: int = 1 << 15
    GuildScheduledEvents: int = 1 << 16
    AutoModerationConfiguration: int = 1 << 20
    AutoModerationExecution: int = 1 << 21
    GuildsAll: int = 69631
    DirectMessagesAll: int = 28672
    AutoModerationAll: int = 3145728
    All: int = 3244031


class ChannelType(Enum):
    TextChannel: int = 0
    VoiceChannel: int = 2
