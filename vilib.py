import serial
import paramiko
import requests
from time import sleep
import re

def regex_prompt(prompt_text):
    if '#' in prompt_text:
        pattern = pattern = re.compile(r"^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+:.*[#]", re.IGNORECASE)
    elif '$' in prompt_text:
        pattern = re.compile(r"^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+:.*[$]", re.IGNORECASE)
    return pattern.match(prompt_text)

def execute_client_cmd(url,method,param : list) -> list:
    # Send Json request to given client and returns output
    payload = {
        "method": method,
        "params": param,
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(url, json=payload).json()
    return (response['result'])

def createSSHClient(server, user,password,port):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password,timeout=10)
    return client
    
def vssh(IP,user,password,command):
    if IP != None:
        ssh =''
        #Executes given command in device via ssh
        try:
            ssh = createSSHClient(IP,user,password,port="22")
        except:
            print("SSH connection failed")
        stdin,stdout,stderr = ssh.exec_command(command)
        ssh.close()
        return stdout.readlines()#[-1].strip('\n')
    
def execute_serial_command(port,command):
    if port != None:
        output = ''
        ser = serial.Serial(port, 115200, timeout=1.5)
        #Executing command in DUT
        ser.write(command.encode('utf-8'))
        #ser.reset_output_buffer()
        ser.write(b'\r')
        ext = ser.readlines()#.decode('iso-8859-1').strip()
        for _ in ext:
            output += _.decode()
        ser.close()
        return output
    
def get_and_verify(method,port,command,value):
    response = execute_serial_command(port,command)
    response= response.strip(command)
    if method == "contains" and value in response:
        return "Pass"
    elif method == "equals" and value == response:
        return "Pass"
    else:
        return "Fail"

def execute_multiple_command(port,command : list) -> list:
    for cmd in command:
        execute_serial_command(port,cmd)
        sleep(2)

def exesleep(time):
    #Holds execution for given time
    sleep(time)
    return 'OK'