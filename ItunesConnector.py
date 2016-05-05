"""-------------------------------------------------------------------------
# Name:		Itunes Connector
# Author:	Shujin Wu
# Description: Connect to Itunes to operate or retrive data
# Pre:		Install Pyobjc
-------------------------------------------------------------------------"""

from Foundation import *
from ScriptingBridge import *

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")

print iTunes.currentTrack().name()
print iTunes.currentTrack().artist()
