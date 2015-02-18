import xbmcaddon
import xbmcgui
 
__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
 
line1 = "This feature is currently under development"
 
xbmcgui.Dialog().ok(__addonname__, line1)
