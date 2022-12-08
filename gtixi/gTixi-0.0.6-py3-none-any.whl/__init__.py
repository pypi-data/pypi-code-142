
__all__ = ['alib','waText','waFile','wa','wad','SvgScreen',
    'baseMod','loopMod','menu',
    'starMessager','wsServer','httpServer','wsCtrl']
#init alib
from .alib import alib
from .wadapter import Wa,SvgScreen
from . import wadapter as wad
from . import waText
from . import waFile
wa = Wa()

#init baseMod
from .starMod import baseMod,loopMod,menu

#init messager and servers
from .starServer import sm,wsServer,httpServer,wsCtrl
starMessager = sm
