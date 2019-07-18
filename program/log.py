""" Functions writes logs file.  """
import json

def write_log(logs):
    """ Input: list of dict objects.
    Update file log.txt with input data.
    """
    log_lines = []
    for log in logs:
        log_line = " ".join([log['log_time'], log['url'], 
                             log['status'], str(log['resp_time'])])
        log_lines.append(log_line)
    
    log_file = open('Log.txt', 'a+')
    log_file.write("\n")
    log_file.write("\n".join(log_lines))
    log_file.close()


def log_to_html(logfile):
    """ Input: logfile json.
    Save input data to content.html 
    """
    log_lines = []
    for log in logfile:
        log_line = " ".join(['<tr><td>',log['log_time'],'</td><td>', 
                             log['url'],'</td><td>', log['status'],
                             '</td><td>', str(log['resp_time']),'</td></tr>'])
        log_lines.append(log_line)
    log_file = open('templates/content.html', 'w')
    log_file.write("\n")
    log_file.write("\n".join(log_lines))
    log_file.close()
    

#def write_last_log(log):
#    """ Input: list of page objects.
#    Update file log.txt with input data.
#    """ 
#    with open('last_log.json', 'w') as json_data_file:
#        json.dump(log, json_data_file, indent=2)
