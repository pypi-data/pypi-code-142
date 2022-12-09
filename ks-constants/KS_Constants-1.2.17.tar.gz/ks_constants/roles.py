from enum import Enum, IntEnum
from ks_constants.devs import Developer
from ks_constants.locale import Language


class Team(IntEnum):
    Survivor = 0
    Kerrigan = 1

    @classmethod
    def from_index(cls, index):
        return Team.Survivor if index == 0 else Team.Kerrigan


class RoleType(Enum):
    Builder = (0, Team.Survivor)
    Support = (1, Team.Survivor)
    Defender = (2, Team.Kerrigan)
    Hunter = (3, Team.Kerrigan)

    def __init__(self, _id: int, team: Team):
        self._id = id
        self._team = team

    def get_team(self) -> Team:
        return self._team

    def to_int(self):
        return self._id

class Role(Enum):
    Kerrigan = (0, RoleType.Hunter, {Language.English: 'Kerrigan', Language.Korean: '케리건'}, Developer.geo, Developer.Luminous, True)
    Scientist = (1, RoleType.Builder, {Language.English: 'Scientist', Language.Korean: '과학자'}, Developer.geo, Developer.Luminous, True)
    Dark_Templar = (2, RoleType.Support, {Language.English: 'Dark Templar', Language.Korean: '암흑기사'}, Developer.geo, Developer.Luminous, True)
    Ascendant = (3, RoleType.Builder, {Language.English: 'Ascendant', Language.Korean: '승천자'}, Developer.Luminous, None, True)
    Spirit = (4, RoleType.Builder, {Language.English: 'Spirit', Language.Korean: '혼령'}, Developer.Luminous, None, True)
    Ares = (5, RoleType.Builder, {Language.English: 'Ares', Language.Korean: '아레스'}, Developer.Luminous, None, True)
    Prophet = (6, RoleType.Support, {Language.English: 'Prophet', Language.Korean: '선지자'}, Developer.Luminous, None, True)
    Stukov = (7, RoleType.Builder, {Language.English: 'Stukov', Language.Korean: '스투코프'}, Developer.Luminous, None, True)
    Artanis = (8, RoleType.Builder, {Language.English: 'Artanis', Language.Korean: '아르타니스'}, Developer.Luminous, None, True)
    Zagara = (9, RoleType.Defender, {Language.English: 'Zagara', Language.Korean: '자가라'}, Developer.Luminous, None, True)
    Engineer = (10, RoleType.Builder, {Language.English: 'Engineer', Language.Korean: '공학자'}, Developer.Luminous, None, True)
    Team_Nova = (11, RoleType.Support, {Language.English: 'Team Nova', Language.Korean: '팀노바'}, Developer.Luminous, None, True)
    Nomad = (12, RoleType.Builder, {Language.English: 'Nomad', Language.Korean: '유랑선'}, Developer.Luminous, None, True)
    Dehaka = (13, RoleType.Hunter, {Language.English: 'Dehaka', Language.Korean: '데하카'}, Developer.Luminous, None, True)
    Helios = (14, RoleType.Builder, {Language.English: 'Helios', Language.Korean: '헬리오스'}, Developer.Luminous, None, True)
    Random = (15, None, {Language.English: 'Random', Language.Korean: '무작위'}, Developer.Luminous, None, True)
    Thakras = (16, RoleType.Hunter, {Language.English: 'Thakras', Language.Korean: '타크라스'}, Developer.Luminous, None, True)
    Swann = (17, RoleType.Support, {Language.English: 'Swann', Language.Korean: '스완'}, Developer.Luminous, None, True)
    Warden = (18, RoleType.Support, {Language.English: 'Warden', Language.Korean: '수호자'}, Developer.Luminous, None, True)
    Selendis = (19, RoleType.Builder, {Language.English: 'Selendis', Language.Korean: '셀렌디스'}, Developer.hex, Developer.Susu, True)
    Niadra = (20, RoleType.Defender, {Language.English: 'Niadra', Language.Korean: '니아드라'}, Developer.Luminous, None, True)
    Mira = (21, RoleType.Builder, {Language.English: 'Mira', Language.Korean: '미라'}, Developer.Luminous, None, True)
    Scion = (22, RoleType.Support, {Language.English: 'Scion', Language.Korean: '후계자'}, Developer.Luminous, None, True)
    Technician = (23, RoleType.Builder, {Language.English: 'Technician', Language.Korean: '기술자'}, Developer.Fatline, Developer.Sox, True)
    Warfield = (24, RoleType.Builder, {Language.English: 'Warfield', Language.Korean: '워필드'}, Developer.Fatline, Developer.Sox, True)
    Champion = (25, RoleType.Builder, {Language.English: 'Champion', Language.Korean: '챔피언'}, Developer.Luminous, None, True)
    Elementalist = (26, RoleType.Support, {Language.English: 'Elementalist', Language.Korean: '원소술사'}, Developer.Fatline, Developer.Sox, True)
    Brakk = (27, RoleType.Hunter, {Language.English: 'Brakk', Language.Korean: '브라크'}, Developer.Fatline, Developer.Sox, True)
    Glevig = (28, RoleType.Defender, {Language.English: 'Glevig', Language.Korean: '글레빅'}, Developer.Fatline, Developer.Sox, True)
    Delta_Squad = (29, RoleType.Support, {Language.English: 'Delta Squad', Language.Korean: '델타 특공대'}, Developer.Luminous, None, True)
    Phaegore = (30, RoleType.Defender, {Language.English: 'Phaegore', Language.Korean: '파에고르'}, Developer.Templar, None, True)
    Alarak = (31, RoleType.Builder, {Language.English: 'Alarak', Language.Korean: '알라라크'}, Developer.Luminous, None, True)
    Izsha = (32, RoleType.Defender, {Language.English: 'Izsha', Language.Korean: '이즈샤'}, Developer.Susu, None, True)
    Malus = (33, RoleType.Hunter, {Language.English: 'Malus', Language.Korean: '말러스'}, Developer.Susu, None, True)
    Kraith = (34, RoleType.Hunter, {Language.English: 'Kraith', Language.Korean: '크레이스'}, Developer.Templar, None, True)
    Energizer = (35, RoleType.Builder, {Language.English: 'Energizer', Language.Korean: '에너자이저'}, Developer.Fatline, Developer.Sox, True)
    Andor = (36, RoleType.Builder, {Language.English: 'Andor', Language.Korean: '안도르'}, Developer.Korneel, None, True)
    DJ = (37, RoleType.Builder, {Language.English: 'DJ', Language.Korean: '디제이'}, Developer.Sox, None, True)
    Rattlesnake = (38, RoleType.Support, {Language.English: 'Rattlesnake', Language.Korean: '방울뱀'}, Developer.Legacy, Developer.Templar, True)
    SgtHammer = (39, RoleType.Builder, {Language.English: 'SgtHammer', Language.Korean: '해머 상사'}, Developer.Archlei, Developer.Sox, True)
    Chew = (40, RoleType.Support, {Language.English: 'Chew', Language.Korean: '추'}, Developer.Sox, None, True)
    Aewyn = (41, RoleType.Builder, {Language.English: 'Aewyn', Language.Korean: '애윈'}, Developer.Luminous, None, True)
    Critter_Lord = (42, RoleType.Builder, {Language.English: 'Critter Lord', Language.Korean: '곤충 왕'}, Developer.Korneel, None, True)

    def __init__(self,
                 _id: int,
                 role_type: RoleType,
                 name: dict,
                 original_author: Developer,
                 current_author: Developer,
                 available: bool
                 ):
        self._index = _id
        self._name = name
        self._role_type = role_type
        self._original_author = original_author
        self._current_author = original_author if current_author is None else current_author
        self._available = available

    @classmethod
    def from_index(cls, index):
        return _roles_list[index]

    def get_index(self):
        return self._index

    def get_team(self) -> Team:
        if self == Role.Random:
            raise TypeError("Random does not have a team")
        return self._role_type.get_team()

    def get_role_type(self) -> RoleType:
        return self._role_type

    def get_name(self, locale: Language = Language.English) -> str:
        return self._name[locale]
    
    def get_english_name(self):
        return self.get_name(Language.English)

    def get_original_author(self) -> Developer:
        return self._original_author

    def get_current_author(self):
        return self._current_author

    def is_available(self):
        return self._available

_roles_list = list(Role)