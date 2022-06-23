import base64

from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

ctx.instance.runtime_properties['decoded_secret'] = base64.b64decode(inputs['secret']).decode('utf-8')
