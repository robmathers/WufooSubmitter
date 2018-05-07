from os import getenv
from chalice import Chalice, BadRequestError, Response
import requests

app = Chalice(app_name='wufoo-submitter')

@app.route('/')
def index():
    return ''

@app.route('/submit/{form_id}', methods=['POST'], content_types=['application/x-www-form-urlencoded'])
def submit(form_id):
    url = 'https://{subdomain}.wufoo.com/api/v3/forms/{form_id}/entries.json'
    subdomain = getenv('WUFOO_SUBDOMAIN')

    if not subdomain:
        raise BadRequestError('Wufoo subdomain has not been configured.')

    api_key = getenv('WUFOO_API_KEY')

    if not api_key:
        raise BadRequestError('Wufoo API key has not been configured.')

    url = url.format(subdomain=subdomain, form_id=form_id)

    response = requests.post(url,
                             data=app.current_request.raw_body,
                             headers={'content-type': 'application/x-www-form-urlencoded'},
                             auth=(api_key,''))

    return Response(body=response.content,
                    status_code=response.status_code,
                    headers={'x-wufoo-submitter': 'yes'})

