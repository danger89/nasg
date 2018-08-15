import os
import re
import argparse
import logging

base = os.path.abspath(os.path.expanduser('~/Projects/petermolnar.net'))
syncserver = 'liveserver:/web/petermolnar.net/web'

site = {
    'title': 'Peter Molnar',
    'url': 'https://petermolnar.net',
    'domain': 'petermolnar.net',
    'pagination': 12,
    'on_front': [
        'article',
        'photo',
        'journal'
    ],
    'licence': 'by-nc-nd',
}

categorydisplay = {
    'article': 'flat',
    'journal': 'flat',
    'photo': 'gallery',
}

licence = {
    'article': 'by',
    'journal': 'by-nc',
}

meta = {
    'webmention': 'https://webmention.io/petermolnar.net/webmention',
    'pingback': 'https://webmention.io/petermolnar.net/xmlrpc',
    'hub': 'https://petermolnar.superfeedr.com/',
    'authorization_endpoint': 'https://indieauth.com/auth',
    'token_endpoint': 'https://tokens.indieauth.com/token',
}

author = {
    'name': 'Peter Molnar',
    'email': 'mail@petermolnar.net',
    'url': 'https://petermolnar.net/',
    'avatar': 'https://petermolnar.net/molnar_peter_avatar.jpg',
    'gpg': 'https://petermolnar.net/pgp.asc',
    'cv': 'https://petermolnar.net/about.html',
    'contact': {
        'xmpp': 'xmpp:mail@petermolnar.net',
        'tumblr': 'https://petermolnarnet.tumblr.com/',
        'wordpress': 'https://petermolnareu.wordpress.com/',
        'flickr': 'https://flickr.com/people/petermolnareu',
        'github': 'https://github.com/petermolnar',
    }
}

paths = {
    'content': os.path.join(base, 'content'),
    'webmentions': os.path.join(base, 'content', 'webmentions'),
    'tmpl': os.path.join(base, 'nasg', 'templates'),
    'watermark': os.path.join(base, 'nasg', 'templates', 'watermark.png'),
    'build': os.path.join(base, 'www'),
}

photo = {
    're_author': re.compile(r'(?:P[eé]ter Moln[aá]r)|(?:Moln[aá]r P[eé]ter)|(?:petermolnar\.(?:eu|net))'),
    'default': 720,
    'sizes': {
        #90 = s
        #360 = m
        720: '',
        1280: '_b',
    },
}

tips = {
    'paypal': 'https://paypal.me/petermolnar/3GBP',
    'monzo': 'https://monzo.me/petermolnar/3',
}

dateformat = {
    'iso': 'YYYY-MM-DDTHH:mm:ssZZ',
    'display': 'YYYY-MM-DD HH:mm',
}

loglevels = {
    'critical': 50,
    'error': 40,
    'warning': 30,
    'info': 20,
    'debug': 10
}

_parser = argparse.ArgumentParser(description='Parameters for NASG')
_booleanparams = {
    'regenerate': 'force downsizing images',
    'force': 'force rendering HTML',
}

for k, v in _booleanparams.items():
    _parser.add_argument(
        '--%s' % (k),
        action='store_true',
        default=False,
        help=v
    )

_parser.add_argument(
    '--loglevel',
    default='info',
    help='change loglevel'
)

args = vars(_parser.parse_args())

loglevel = loglevels.get(args.get('loglevel'))

logger = logging.getLogger("nasg")
logger.setLevel(loglevel)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
logging.getLogger('asyncio').setLevel(loglevel)