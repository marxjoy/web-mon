""" Functions and event_loop object 
supports asynchronic requests.  
"""
import aiohttp
import asyncio
import time

async def fetch(session, url):
    """ Input: single url. 
    Make async request. 
    Output: dict(url, content, error (if exist), response time(if exist).
    """
    resp ={}
    resp['url'] = url
    try:
        async with session.get(url) as response:
            start_time = time.time()
            content = await response.text()
            resp_time = time.time() - start_time
            resp['resp_time'] = resp_time
            resp['content'] = content
    except aiohttp.client_exceptions.ClientConnectionError as error:
        error = "".join(["Connection Error: ", str(error)])
        resp['error'] = error
    except aiohttp.client_exceptions.InvalidURL as error:
        error = "".join(["URL Error: ", str(error)])
        resp['error'] = error
    except aiohttp.client_exceptions.ClientResponseError as error:
        error = "".join(["Response Error: ", str(error)])
        resp['error'] = error
    except aiohttp.client_exceptions.ClientError as error:
        error = "".join(["Error: ", str(error)])
        resp['error'] = error
    return resp


async def make_requests(urls):
    """ Input: list of urls. 
    Make asynsc request for urls.
    Output: list of dicts (url, content, error, response time).  
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
    return responses


loop = asyncio.get_event_loop()