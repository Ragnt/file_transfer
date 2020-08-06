from views import *


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_post('/upload', store_pcapng_parts)