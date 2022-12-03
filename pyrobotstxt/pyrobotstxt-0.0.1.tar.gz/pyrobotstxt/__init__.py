import os
import json
from math import ceil
from datetime import datetime
from PIL import Image

__version__ = (0, 0, 1)

ROBOTS = {
    "Applebot": "Apple",
    "AhrefsBot": "Ahrefs",
    "Baiduspider": "Baidu",
    "Bingbot": "Microsoft Bing",
    "Discordbot": "Discord",
    "DuckDuckBot": "DuckDuckGo",
    "Googlebot": "Google Search Bot",
    "Googlebot-Image": "Google Image Bot",
    "LinkedInBot": "LinkedIn Bot",
    "MJ12bot": "MJ12bot",
    "Pinterestbot": "Pinterest",
    "SemrushBot": "Semrsh",
    "Slurp": "Slurp",
    "TelegramBot": "Telegram",
    "Twitterbot": "Twitter Bot",
    "Yandex": "Yandex",
    "YandexBot": "YandexBot",
    "facebot": "Facebook",
    "msnbot": "MSN Bot",
    "rogerbot": "MOZ Bot",
    "xenu": "xenu",
}


class ImageAsASCII:
    def __init__(self, desired_width=90, image_path=None):

        self.ascii_map = [" ", *("*$+?.%;:,@")]

        self.ascii_img = ""

        self.image = Image.open(image_path).convert("L")

        desired_height = desired_width * self.image.height / self.image.width

        self.image = self.image.resize((ceil(desired_width), ceil(desired_height)))

    def map_to_ascii(self):

        ascii_str = ""

        for pixel in self.image.getdata():

            ascii_str += self.ascii_map[pixel // 25]

        self.ascii_img = "#\t"

        for i in range(0, len(ascii_str), self.image.width):

            self.ascii_img += " ".join(ascii_str[i : i + self.image.width]) + "\n#\t"


class UserAgent:
    def __init__(self, name="*", crawl_delay=0):

        self.uage_aget_name = name

        self.crawl_delay = crawl_delay

        self.sitemaps = []

        self.allowed = []

        self.disallowed = []

        self.content = ""

    def add_allow(self, allow_items, unique=True, comments=""):

        if isinstance(allow_items, str):

            allow_items = [allow_items]

        if not isinstance(allow_items, list):

            print("not supported", type(allow_items))  # raise exception

        else:

            self.allowed += allow_items

            if unique:
                self.allowed = list(set(self.allowed))

    def remove_allow(self, allow_item):

        if allow_item in self.allowed:

            self.allowed -= [allow_item]

    def add_disallow(self, disallow_items, unique=True, comments=""):

        if isinstance(disallow_items, str):

            disallow_items = [disallow_items]

        if not isinstance(disallow_items, list):

            print("not supported", type(disallow_items))  # raise exception

        else:

            self.disallowed += disallow_items

            if unique:
                self.disallowed = list(set(self.disallowed))

    def remove_disallow(self, disallow_item):

        if disallow_item in self.disallowed:

            self.disallowed -= [disallow_item]

    def add_sitemap(self, site_map_path=None, comments=""):

        self.sitemaps.append(site_map_path)

    def remove_sitemap(self, site_map_path=None):

        if site_map_path in self.sitemaps:
            self.sitemaps -= [site_map_path]

    def disallow_pagination(self, prefix="/page/*", comments=""):

        self.add_disallow(disallow_item=prefix, comments=comments)

    def consolidate(self):

        self.content = f"\n\nUser-agent: {self.uage_aget_name}\n"

        if self.allowed:

            self.content += "\n# Allowed Patterns\n"

            self.content += "\n".join([f"Allow: {item}" for item in self.allowed])

        if self.disallowed:

            self.content += "\n\n# Disallowed Patterns\n"

            self.content += "\n".join([f"Disallow: {item}" for item in self.disallowed])

        if self.sitemaps:

            self.content += "\n\n# Site Maps\n"

            self.content += "\n".join([f"Sitemap: {item}" for item in self.sitemaps])


class RobotsTxt:
    def __init__(self, version=""):

        self.user_agents = []

        self.create_time = datetime.now()

        self.version = version

        self.image_branding = None

        self.header = ""

        self.goodbye = ""

    def read(self):

        self.create_time = datetime.now()

    def write(self, file_path="robots.txt"):

        with open(file_path, "w") as f:

            if self.header:

                f.write(f"# {self.header}")

            for ua in mrt.user_agents:

                ua.consolidate()

                f.write(ua.content)

            f.write("\n\n")

            if self.image_branding:

                f.write(self.image_branding)

            if self.goodbye:

                f.write(f"\n\n# {self.goodbye}")

    def include_header(self, message="", append_date=True):

        self.header = f"{message}"

        if append_date:

            self.header += f"\n# Created on {self.create_time} using pyrobotstxt"

    def include_footer(self, message=""):

        self.goodbye = message

    def include_image(self, image_file=None, desired_width=90):

        img = ImageAsASCII(image_path=image_file, desired_width=desired_width)

        img.map_to_ascii()

        self.image_branding = img.ascii_img

    def add_user_agent(self, ua):

        self.user_agents.append(ua)

    def remove_user_agent(self, ua_name=""):

        self.user_agents -= [usa for ua in self.user_agents if usa.name == ua_name]

    @staticmethod
    def robots_name(robot_details):

        return {
            robot: ROBOTS[robot]
            for robot in ROBOTS
            if robot_details.capitalize() in ROBOTS[robot]
        }

    @staticmethod
    def robots_details(roboto_name):

        return {
            robot: ROBOTS[robot]
            for robot in ROBOTS
            if roboto_name.lower() == robot.lower()
        }