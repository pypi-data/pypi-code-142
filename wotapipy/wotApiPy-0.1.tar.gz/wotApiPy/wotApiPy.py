import requests
import os
import json
import httplib2


def allTankopedia(application_id):
    tankopedia = Tankopedia(application_id)
    tankopedia.technic()
    tankopedia.achievements()
    tankopedia.crewSkills()
    tankopedia.crewSpecialties()
    tankopedia.equipmentAndEquipment()
    tankopedia.gameCards()
    tankopedia.modules()
    tankopedia.personalCombatTasks()
    tankopedia.personalReserves()
    tankopedia.stripes()
    tankopedia.equipmentConfiguration()
    tankopedia.characteristicTechnic()


def allImage():
    image = Image()
    image.iconAchievements()
    image.iconCrewSkills()
    image.iconModules()
    image.iconEquipmentAndEquipment()
    image.iconStripes()
    image.iconTechnic()


class Tankopedia():
    def __init__(self, application_id):
        self.cwd = str(os.getcwd())
        self.application_id = application_id

    def technic(self):
        url = requests.get(
            f'https://api.worldoftanks.eu/wot/encyclopedia/vehicles/?application_id={self.application_id}')

        try:
            os.mkdir(self.cwd + '\\WOT')
        except FileExistsError:
            pass

        r = json.loads(url.text)
        name = 'allTanks.json'
        with open(self.cwd + '\\WOT\\' + name, 'w', encoding="utf-8") as output_file:
            json.dump(r, output_file, indent=4)

    def giveTankId(self):
        tank_id = {}
        with open(self.cwd + "\\WOT\\allTanks.json", "r") as read_file:
            data = json.load(read_file)

            data = data['data']
            for key in data:
                tank_id[key] = data[key]["name"]

        return tank_id

    def characteristicTechnic(self):
        try:
            os.makedirs(self.cwd + '\\WOT\\characteristic')
        except FileExistsError:
            pass

        tanks_id = self.giveTankId()
        for key in tanks_id:
            url = requests.get(
                'https://api.worldoftanks.eu/wot/encyclopedia/vehicleprofile/?application_id=%s&tank_id=%s' %
                (self.application_id, key))

            r = json.loads(url.text)
            name = '%s.json' % key
            with open(name, 'w', encoding="utf-8") as output_file:
                json.dump(r, output_file, indent=4)
            os.replace(
                name, '%s\\%s' %
                (self.cwd + '\\WOT\\characteristic', name))

    def equipmentConfiguration(self):
        try:
            os.makedirs(self.cwd + '\\WOT\\configuration')
        except FileExistsError:
            pass

        tanks_id = self.giveTankId()
        for key in tanks_id:
            url = requests.get(
                'https://api.worldoftanks.eu/wot/encyclopedia/vehicleprofiles/?application_id=%s&tank_id=%s' %
                (self.application_id, key))

            r = json.loads(url.text)
            name = '%s.json' % key
            with open(name, 'w', encoding="utf-8") as output_file:
                json.dump(r, output_file, indent=4)
            os.replace(
                name, '%s\\%s' %
                (self.cwd + '\\WOT\\configuration', name))

    def achievements(self):
        url = requests.get(
            f'https://api.worldoftanks.eu/wot/encyclopedia/achievements/?application_id={self.application_id}')

        try:
            os.mkdir(self.cwd + '\\WOT')
        except FileExistsError:
            pass

        r = json.loads(url.text)
        name = 'achievements.json'
        with open(self.cwd + '\\WOT\\' + name, 'w', encoding="utf-8") as output_file:
            json.dump(r, output_file, indent=4)

    def tankopedia(self):
        url = requests.get(
            f'https://api.worldoftanks.eu/wot/encyclopedia/info/?application_id={self.application_id}')

        try:
            os.makedirs(self.cwd + '\\WOT')
        except FileExistsError:
            pass

        r = json.loads(url.text)
        name = 'tankopedia.json'
        with open(self.cwd + '\\WOT\\' + name, 'w', encoding="utf-8") as output_file:
            json.dump(r, output_file, indent=4)

    def gameCards(self):
        url = requests.get(
            f'https://api.worldoftanks.eu/wot/encyclopedia/arenas/?application_id={self.application_id}')

        try:
            os.makedirs(self.cwd + '\\WOT')
        except FileExistsError:
            pass

        r = json.loads(url.text)
        name = 'gameCards.json'
        with open(self.cwd + '\\WOT\\' + name, 'w', encoding="utf-8") as output_file:
            json.dump(r, output_file, indent=4)

    def equipmentAndEquipment(self):
        url = requests.get(
            f'https://api.worldoftanks.eu/wot/encyclopedia/provisions/?application_id={self.application_id}')

        try:
            os.makedirs(self.cwd + '\\WOT')
        except FileExistsError:
            pass

        r = json.loads(url.text)
        name = 'equipmentAndEquipment.json'
        with open(self.cwd + '\\WOT\\' + name, 'w', encoding="utf-8") as output_file:
            json.dump(r, output_file, indent=4)

    def personalCombatTasks(self):
        url = requests.get(
            f'https://api.worldoftanks.eu/wot/encyclopedia/personalmissions/?application_id={self.application_id}')

        try:
            os.makedirs(self.cwd + '\\WOT')
        except FileExistsError:
            pass

        r = json.loads(url.text)
        name = 'personalCombatTasks.json'
        with open(self.cwd + '\\WOT\\' + name, 'w', encoding="utf-8") as output_file:
            json.dump(r, output_file, indent=4)

    def personalReserves(self):
        url = requests.get(
            f'https://api.worldoftanks.eu/wot/encyclopedia/boosters/?application_id={self.application_id}')

        try:
            os.makedirs(self.cwd + '\\WOT')
        except FileExistsError:
            pass

        r = json.loads(url.text)
        name = 'personalReserves.json'
        with open(self.cwd + '\\WOT\\' + name, 'w', encoding="utf-8") as output_file:
            json.dump(r, output_file, indent=4)

    def modules(self):
        url = requests.get(
            f'https://api.worldoftanks.eu/wot/encyclopedia/modules/?application_id={self.application_id}')

        try:
            os.makedirs(self.cwd + '\\WOT')
        except FileExistsError:
            pass

        r = json.loads(url.text)
        name = 'modules.json'
        with open(self.cwd + '\\WOT\\' + name, 'w', encoding="utf-8") as output_file:
            json.dump(r, output_file, indent=4)

    def stripes(self):
        url = requests.get(
            f'https://api.worldoftanks.eu/wot/encyclopedia/badges/?application_id={self.application_id}')

        try:
            os.makedirs(self.cwd + '\\WOT')
        except FileExistsError:
            pass

        r = json.loads(url.text)
        name = 'stripes.json'
        with open(self.cwd + '\\WOT\\' + name, 'w', encoding="utf-8") as output_file:
            json.dump(r, output_file, indent=4)

    def crewSpecialties(self):
        url = requests.get(
            f'https://api.worldoftanks.eu/wot/encyclopedia/crewroles/?application_id={self.application_id}')

        try:
            os.makedirs(self.cwd + '\\WOT')
        except FileExistsError:
            pass

        r = json.loads(url.text)
        name = 'crewSpecialties.json'
        with open(self.cwd + '\\WOT\\' + name, 'w', encoding="utf-8") as output_file:
            json.dump(r, output_file, indent=4)

    def crewSkills(self):
        url = requests.get(
            f'https://api.worldoftanks.eu/wot/encyclopedia/crewskills/?application_id={self.application_id}')

        try:
            os.makedirs(self.cwd + '\\WOT')
        except FileExistsError:
            pass

        r = json.loads(url.text)
        name = 'crewSkills.json'
        with open(self.cwd + '\\WOT\\' + name, 'w', encoding="utf-8") as output_file:
            json.dump(r, output_file, indent=4)


class Image():
    def __init__(self):
        self.cwd = str(os.getcwd())

    def iconTechnic(self):
        image = {}
        type = ['big', 'small', 'contour']

        for type in type:
            with open(self.cwd + "\\WOT\\allTanks.json", "r") as read_file:
                data = json.load(read_file)

                data = data['data']
                for key in data:
                    image[str(data[str(key)]['tag'])] = str(
                        data[str(key)]['images'][f'{type}_icon'])

            try:
                os.makedirs(self.cwd + f"\\WOT\\images\\tank\\{type}_icon")
            except FileExistsError:
                pass

            for k in image:
                h = httplib2.Http(self.cwd + '\\WOT\\.cache')
                response, content = h.request(image[k])
                out = open(
                    self.cwd +
                    f'\\WOT\\images\\tank\\{type}_icon\\{k}.jpg',
                    'wb')
                out.write(content)
                out.close()

    def iconEquipmentAndEquipment(self):
        image = {}

        with open(self.cwd + "\\WOT\\equipmentAndEquipment.json", "r") as read_file:
            data = json.load(read_file)

            data = data['data']
            for key in data:
                image[str(data[str(key)]['tag'])] = str(
                    data[str(key)]['image'])

        try:
            os.makedirs(self.cwd + f"\\WOT\\images\\equipmentAndEquipment")
        except FileExistsError:
            pass

        for k in image:
            h = httplib2.Http(self.cwd + '\\WOT\\.cache')
            response, content = h.request(image[k])
            out = open(
                self.cwd +
                f'\\WOT\\images\\equipmentAndEquipment\\{k}.jpg',
                'wb')
            out.write(content)
            out.close()

    def iconPersonalReserves(self):
        image = {}
        type = ['large', 'small']

        for type in type:
            with open(self.cwd + "\\WOT\\personalReserves.json", "r") as read_file:
                data = json.load(read_file)

                data = data['data']
                for key in data:
                    image[key] = str(data[str(key)]['images'][f'{type}'])

            try:
                os.makedirs(
                    self.cwd +
                    f"\\WOT\\images\\personalReserves\\{type}")
            except FileExistsError:
                pass

            for k in image:
                h = httplib2.Http(self.cwd + '\\WOT\\.cache')
                response, content = h.request(image[k])
                name = k
                out = open(
                    self.cwd +
                    f'\\WOT\\images\\personalReserves\\{type}\\{name}.jpg',
                    'wb')
                out.write(content)
                out.close()

    def iconModules(self):
        image = {}

        with open(self.cwd + "\\WOT\\modules.json", "r") as read_file:
            data = json.load(read_file)

            data = data['data']
            for key in data:
                image[str(data[str(key)]['type'])] = str(
                    data[str(key)]['image'])

        try:
            os.makedirs(self.cwd + f"\\WOT\\images\\modules")
        except FileExistsError:
            pass

        for k in image:
            h = httplib2.Http(self.cwd + '\\WOT\\.cache')
            response, content = h.request(image[k])
            out = open(self.cwd + f'\\WOT\\images\\modules\\{k}.gif', 'wb')
            out.write(content)
            out.close()

    def iconAchievements(self):
        image = {}
        types = ['big', 'small']

        for type in types:
            with open(self.cwd + "\\WOT\\achievements.json", "r") as read_file:
                data = json.load(read_file)

                data = data['data']
                for key in data:

                    if 'options' in data[key] and data[str(
                            key)]['options'] and key != 'marksOnGun':
                        m = 0
                        for i in data[str(key)]['options']:
                            if type == 'big':
                                image[str(data[key]['name']) + '_' +
                                      str(m)] = str(i[f'image_big'])
                                m += 1
                            else:
                                image[str(data[key]['name']) + '_' +
                                      str(m)] = str(i[f'image'])
                                m += 1

                    elif key != 'marksOnGun':
                        if type == 'big':
                            image[data[key]['name']] = str(
                                data[key][f'image_big'])
                        else:
                            image[data[key]['name']] = str(data[key][f'image'])

                    elif key == 'marksOnGun':
                        typesGun = ['x180', 'x85', 'x71']
                        for o in range(0, 2):
                            for u in data[key]['options'][o]['nation_images'][typesGun[o]]:
                                image[f'marksOnGun_{typesGun[o]}_{u}'] = data[key]['options'][o]['nation_images'][typesGun[o]][u]
            try:
                if type == 'big':
                    os.makedirs(self.cwd + f"\\WOT\\images\\achievements\\big")
                else:
                    os.makedirs(
                        self.cwd + f"\\WOT\\images\\achievements\\small")
            except FileExistsError:
                pass

            for k in image:
                h = httplib2.Http(self.cwd + '\\WOT\\.cache')
                response, content = h.request(image[k])

                name = k.replace('"', '').replace('?', '').replace(':', ' -')
                if type == 'big':
                    out = open(
                        self.cwd +
                        f'\\WOT\\images\\achievements\\big\\{name}.png',
                        'wb')
                else:
                    out = open(
                        self.cwd +
                        f'\\WOT\\images\\achievements\\small\\{name}.png',
                        'wb')
                out.write(content)
                out.close()

    def iconStripes(self):
        image = {}
        type = ['big', 'small', 'medium']

        for type in type:
            with open(self.cwd + "\\WOT\\stripes.json", "r") as read_file:
                data = json.load(read_file)

                data = data['data']
                for key in data:
                    image[str(data[str(key)]['name']).replace(':', '')] = str(
                        data[str(key)]['images'][f'{type}_icon'])

            try:
                os.makedirs(self.cwd + f"\\WOT\\images\\stripes\\{type}_icon")
            except FileExistsError:
                pass

            for k in image:
                h = httplib2.Http(self.cwd + '\\WOT\\.cache')
                response, content = h.request(image[k])
                out = open(
                    self.cwd +
                    f'\\WOT\\images\\stripes\\{type}_icon\\{k}.jpg',
                    'wb')
                out.write(content)
                out.close()

    def iconCrewSkills(self):
        image = {}
        type = ['big', 'small']

        for type in type:
            with open(self.cwd + "\\WOT\\crewSkills.json", "r") as read_file:
                data = json.load(read_file)

                data = data['data']
                for key in data:
                    image[str(data[str(key)]['skill'])] = str(
                        data[str(key)]['image_url'][f'{type}_icon'])

            try:
                os.makedirs(
                    self.cwd +
                    f"\\WOT\\images\\crewSkills\\{type}_icon")
            except FileExistsError:
                pass

            for k in image:
                h = httplib2.Http(self.cwd + '\\WOT\\.cache')
                response, content = h.request(image[k])
                out = open(
                    self.cwd +
                    f'\\WOT\\images\\crewSkills\\{type}_icon\\{k}.png',
                    'wb')
                out.write(content)
                out.close()
