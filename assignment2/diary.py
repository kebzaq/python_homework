import traceback
from datetime import datetime
# Task 1: Diary
try:
    with open("diary.txt", "a") as f:
        now = datetime.now()
        f.write(f"Entry Date and Time: {now}\n")
        res = input(" What happened today?")
        f.write(res +"\n")

        while True:
            resp = input("What else?")
            if resp.lower() == "done for now":
                break;
            f.write(resp + "\n")
except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")

# read the file
with open("diary.txt", "r") as f:
    print(f.read())
