import time
import json
from timeloop import Timeloop
from datetime import timedelta
from program.models import Page
from program.async_request import loop, make_requests
from program.log import write_log, log_to_html

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
checking_period = int(data['checking_period']['sec']) #checking period

time_loop = Timeloop()

@time_loop.job(interval=timedelta(seconds=checking_period))
def main():
    logs = []
    urls = [data['pages'][page]['url'] for page in data['pages']]
    raw_responses = loop.run_until_complete(make_requests(urls))
    responses = {response['url'] : response for response in raw_responses}
    for page in data['pages']:
        url = data['pages'][page]['url']
        content_requirement = data['pages'][page]['content_requirement']
      # response dict('url':, 'content':, content, 'error':, 'response time':)
        response = responses[url]
        p = Page(url=url, content=content_requirement, response=response)
        if p.is_valid():
            p.is_content_valid()
            p.load_resp_time()
        completed_response = {'log_time': p.log_time, 'url': p.url, 
                       'status': p.status, 'resp_time': p.resp_time}
        logs.append(completed_response)
        p.kill()
    write_log(logs)
    log_to_html(logs)

