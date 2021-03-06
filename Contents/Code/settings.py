PLUGIN_ID   = "com.plexapp.plugins.spotify2"
VERSION     = '0.5.8'
PREFIX      = "/music/spotify"
ROUTEBASE   = PREFIX + '/'

LOGGERS     = [
    'spotify2',

    'cherrypy',
    'plugin',
    'pyemitter',
    'requests',
    'spotify'
]

PREF_SS_RANGES = {
    'Automatic': None,
    'Disabled': False,
    'Enabled': True
}
