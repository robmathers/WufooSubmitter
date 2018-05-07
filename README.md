# Wufoo Submitter

This is built to allow use of [Wufoo's API][api-docs] to submit form entries without exposing your API key in a client side app.

By using the Wufoo API, you can build forms that submit via Javascript without any Wufoo branding, for a seamless user experience, while still taking advantage of Wufoo's form building, and entry tracking and notification tools.

## Installation
This uses [AWS Chalice](https://github.com/aws/chalice) for a lightweight Lambda SDK.

1. Download the code, you'll likely want to create a virtualenv for it to live in.
1. Install Chalice with `pip install chalice`.
2. `pip install -r wufoo-submitter/requirements.txt` to install the requirements (just [requests](http://docs.python-requests.org/) at the moment).
3. Make sure your [AWS credentials are set up](http://chalice.readthedocs.io/en/stable/quickstart.html#credentials).
4. `chalice deploy`
5. In the AWS Lambda console, set the `WUFOO_SUBDOMAIN` and `WUFOO_API_KEY` environment variables as appropriate. Keep in mind that every deploy will delete these, unless you specify them in the [Chalice config file](http://chalice.readthedocs.io/en/stable/topics/configfile.html). This is done so that they stay out of the git repo.
6. Configure your form to submit following [Wufoo's API docs][api-docs]. The url to use will be your Lambda API URL `/submit/FORM_ID`. The form ID is also called the hash in Wufoo's API.

## Inner Workings
The code is pretty simple. It takes input as given, adds the appropriate API authorization on, and forwards it to Wufoo, returning the response. It checks and returns a 500 error with a message if the API key or Wufoo subdomain aren't configured properly (communicated via the `Message` key of the JSON returned via an error).


[api-docs]: https://wufoo.github.io/docs/#submit-entry
