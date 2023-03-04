# logs_parser

### **Logs parser with profiler**

##### *What it is doing?*

There is a call center call log. It records the start and end time of the call.
The number of entries in the log can be very large.
It is a memory-efficient script that can determine the minimum number of call center agents so that no call is waiting for an agent.


##### *How to test?*
1. Run **gen_logs.py**
`python3 gen_logs.py`
You will see your *logfile* in *logs* directory.
Also you can modify amount of minimum and maximum lines of the file.

2. Run **main.py**
`python3 main.py`
It may take some time to finish, depending on amount of the lines of the logfile and your hardware.
As a result you will get a print message *"The call took ..."*.
And you will get a report that you can find in *profile_reports* directory.

The core of the script is **LogParser** that defined in *parse_logs.py*.

