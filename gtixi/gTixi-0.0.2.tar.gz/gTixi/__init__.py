
__all__ = ['alib','waText','waFile','wa','wad','SvgScreen',
    'baseMod','loopMod','menu',
    'starMessager','wsServer','httpServer','wsCtrl']
#init alib
from gTixi.alib import alib
from gTixi.wadapter import Wa,SvgScreen
import gTixi.wadapter as wad
from gTixi import waText
from gTixi import waFile
wa = Wa()

#init baseMod
from gTixi.starMod import baseMod,loopMod,menu

#init messager and servers
from gTixi.starServer import sm,wsServer,httpServer,wsCtrl
starMessager = sm
