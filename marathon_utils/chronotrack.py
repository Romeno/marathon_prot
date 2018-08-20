import chronotrack

from django.conf import settings

api = chronotrack.Chronotrack(client_id=settings.CT_CLIENT_ID, user_id=settings.CT_LOGIN, user_pass=settings.CT_PASSWORD)
api.set_auth_type(chronotrack.AUTH_SIMPLE)
api.set_debug()
