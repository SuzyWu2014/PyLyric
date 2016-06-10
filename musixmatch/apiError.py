def status_code(value):
    """
    Get a value, i.e. error code as a int.
    Returns an appropriate message.
    """
    if value == 200:
        q = "The request was successful."
        return q
    if value == 400:
        q = "The request had bad syntax or was inherently impossible"
        q += " to be satisfied."
        return q
    if value == 401:
        q = "Authentication failed, probably because of a bad API key."
        return q
    if value == 402:
        q = "A limit was reached, either you exceeded per hour requests"
        q += " limits or your balance is insufficient."
        return q
    if value == 403:
        q = "You are not authorized to perform this operation / the api"
        q += " version you're trying to use has been shut down."
        return q
    if value == 404:
        q = "Requested resource was not found."
        return q
    if value == 405:
        q = "Requested method was not found."
        return q
    # wrong code?
    return "Unknown error code: " + str(value)


def check_status(response):
    """
    Checks the response in JSON format
    Raise an error, or returns the body of the message
    RETURN:
       body of the message in JSON
       except if error was raised
    """

    if (not 'message') in response.keys():
        raise MusixMatchAPIError(-1)
    msg = response['message']
    if (not 'header') in msg.keys():
        raise MusixMatchAPIError(-1)
    header = msg['header']
    if (not 'status_code') in header.keys():
        raise MusixMatchAPIError(-1)
    code = header['status_code']
    if code != 200:
        raise MusixMatchAPIError(code)
    # all good, return body
    body = msg['body']
    return body


class MusixMatchAPIError(Exception):
        """
        Error raised when the status code returned by the musixMatch API is not 200
        """

        def __init__(self, code, message=None):
            self.mxm_code = code
            if message is None:
                message = status_code(code)
            self.args = ('MusixMatch API Error %d: %s' % (code, message),)
