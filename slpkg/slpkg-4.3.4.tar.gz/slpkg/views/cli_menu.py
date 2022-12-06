#!/usr/bin/python3
# -*- coding: utf-8 -*-


from slpkg.configs import Configs


class Usage:

    def __init__(self):
        colors = Configs.colour
        color = colors()

        self.BOLD = color['BOLD']
        self.RED = color['RED']
        self.CYAN = color['CYAN']
        self.YELLOW = color['YELLOW']
        self.ENDC = color['ENDC']


    def help_short(self):
        args = (f'Usage: {Configs.prog_name} [{self.YELLOW}OPTIONS{self.ENDC}] [{self.CYAN}COMMAND{self.ENDC}] <packages>\n'
                f'\n  slpkg [{self.YELLOW}OPTIONS{self.ENDC}] [--yes, --jobs, --resolve-off, --reinstall, --skip-installed]\n'
                f'  slpkg [{self.CYAN}COMMAND{self.ENDC}] [update, upgrade, check-updates, clean-logs, clean-tmp]\n'
                f'  slpkg [{self.CYAN}COMMAND{self.ENDC}] [-b, build, -i, install, -d, download] <packages>\n'
                f'  slpkg [{self.CYAN}COMMAND{self.ENDC}] [-r, remove, -f, find, -w, view, -s, search] <packages>\n'
                "  \nIf you need more information please try 'slpkg --help'.")

        print(args)
        raise SystemExit()


    def help(self, status: int):
        args = [f'{self.BOLD}USAGE:{self.ENDC} {Configs.prog_name} [{self.YELLOW}OPTIONS{self.ENDC}] [{self.CYAN}COMMAND{self.ENDC}] <packages>\n',
                f'{self.BOLD}DESCRIPTION:{self.ENDC}',
                '  Packaging tool that interacts with the SBo repository.\n',
                f'{self.BOLD}COMMANDS:{self.ENDC}',
                f'  {self.RED}update{self.ENDC}                        Update the package lists.',
                f'  {self.CYAN}upgrade{self.ENDC}                       Upgrade all the packages.',
                f'  {self.CYAN}check-updates{self.ENDC}                 Check for news on ChangeLog.txt.',
                f'  {self.CYAN}clean-logs{self.ENDC}                    Clean dependencies log tracking.',
                f'  {self.CYAN}clean-tmp{self.ENDC}                     Delete all the downloaded sources.',
                f'  {self.CYAN}-b, build{self.ENDC} <packages>          Build only the packages.',
                f'  {self.CYAN}-i, install{self.ENDC} <packages>        Build and install the packages.',
                f'  {self.CYAN}-d, download{self.ENDC} <packages>       Download only the scripts and sources.',
                f'  {self.CYAN}-r, remove{self.ENDC} <packages>         Remove installed packages.',
                f'  {self.CYAN}-f, find{self.ENDC} <packages>           Find installed packages.',
                f'  {self.CYAN}-w, view{self.ENDC} <packages>           View packages from the repository.',
                f'  {self.CYAN}-s, search{self.ENDC} <packages>         Search packages from the repository.\n',
                f'{self.BOLD}OPTIONS:{self.ENDC}',
                f'  {self.YELLOW}--yes{self.ENDC}                         Answer Yes to all questions.',
                f'  {self.YELLOW}--jobs{self.ENDC}                        Set it for multicore systems.',
                f'  {self.YELLOW}--resolve-off{self.ENDC}                 Turns off dependency resolving.',
                f'  {self.YELLOW}--reinstall{self.ENDC}                   Upgrade packages of the same version.',
                f'  {self.YELLOW}--skip-installed{self.ENDC}              Skip installed packages.\n',
                '  -h, --help                    Show this message and exit.',
                '  -v, --version                 Print version and exit.\n',
                'Edit the configuration file in the /etc/slpkg/slpkg.toml.',
                'If you need more information try to use slpkg manpage.']

        for opt in args:
            print(opt)
        raise SystemExit(status)
