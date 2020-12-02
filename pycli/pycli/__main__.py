import sys
import requests
from .url import url
from datetime import datetime

def get_tasks():
    r = requests.get(url)
    print(r.json())
    
def get_task(task_id):
    r = requests.get(url + task_id)
    print(r.json())

def post_task(args):
    print(args)
    r = requests.post(url, json=args)
    print(r)

def delete_task(task_id):
    r = requests.delete(url + task_id)
    print(r)

commands = {
    "get_tasks": {"func":get_tasks, "args":[]}, 
    "get_task": {"func":get_task, "args":["id"]}, 
    "post_task": {"func":post_task, "args":["title", "pub_date", "description"]}, 
    "delete_task": {"func":delete_task, "args":["id"]}
}

def main():

    args = sys.argv[1:]

    n_args = len(args)

    pub_date = str(datetime.now())

    if n_args > 0:

        command = args[0]

        if command in commands:
            if command == "post_task":

                func_args = {
                    "title":"No title",
                    "pub_date":str(datetime.now()),
                    "description": "No description"
                }

                for arg in args[1:]:
                    split = arg.split("=")
                    if split[0] in commands[command]["args"]:
                        func_args[split[0]] = split[1]

                commands[command]["func"](func_args)

            
            elif command == "get_task":

                task_id = None
                for arg in args[1:]:
                    split = arg.split("=")
                    if split[0] in commands[command]["args"]:
                        task_id = split[1]


                if task_id:
                    commands[command]["func"](task_id)
                else:
                    print("An id is needed for this command")



            elif command == "delete_task":

                task_id = None
                for arg in args[1:]:
                    split = arg.split("=")
                    if split[0] in commands[command]["args"]:
                        task_id = split[1]


                if task_id:
                    commands[command]["func"](task_id)
                else:
                    print("An id is needed for this command")

            else:
                commands[command]["func"]()


        else:
            print("Command '{}' not found. Try: {}".format(command, ', '.join(commands)))


    else:
        print("No command foud")

if __name__ == '__main__':
    main()

