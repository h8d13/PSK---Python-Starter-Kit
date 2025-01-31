# PSK---Python-Starter-Kit 🐍 

## Extensions & Venvs

Ctrl Shift X 

![image](https://github.com/user-attachments/assets/9b7e2959-27b6-4e06-af42-48e89c99bef6)

Create a file called hello.py
Press this button at the bottom right:

![image](https://github.com/user-attachments/assets/54ef0904-c9a5-4f91-af33-c1637e867490)

Then '+'

![image](https://github.com/user-attachments/assets/012cee1c-a28c-47e1-809a-c6d1045d9f55)

If this worked you will now see:

![Screenshot from 2025-01-31 09-46-00](https://github.com/user-attachments/assets/38a7d23c-51a2-4c1d-ae23-4531d7bde35a)

The venv shows we have selected it. 


## Explorer

In your explorer you now have a .venv (the .env is something different for API keys).
This is a portable python executable. 

![image](https://github.com/user-attachments/assets/f4063072-1aaf-42d0-8425-c07a2ab80313)

**Try to keep your projects organized. There are some rules for folders and file names:**

DIRECTORIES

my_package
mypackage
company_project

MODULES

utils.py
database_connector.py
auth_helper.py

No spaces, capitals, or "-","."

## Running files

You can then simply right click a python file:

![image](https://github.com/user-attachments/assets/8fcfb8df-3229-4e02-9c68-682c4d754920)

Some things that are useful here, copying paths or relative paths. Or running the script. 

Then in your hello.py put the following content:

```
import sys
print (f'{sys.executable}')
```

If you run this and get "yourfoldername\.venv\Scripts\python.exe "

Well the set up worked because it's using the new mini-python we created. 



## Using the terminal 
```
Cd .. > Goes back one
Cd <directory> goes forward one
Ls > List files
Mkdir <directory> Creates a folder
Pwd > Prints where you are now (Working directory)
``` 
Also useful:
``` 
clear  > Clear terminal
rm <file> Delete
echo > hello.py (Creates file)
code .   (Open vscode in said location)
``` 
Understand relative paths from where you are:
``` 
cp ./folder1/file.txt ./folder2/ (Copy for current directory) 
cp myfile.txt ../ (Copy a file up one) 
```

## Useful shortcuts

- New window: CTRL SHIFT N
- Go to file explorer: CTRL ALT R
- Go to vscode command palette: CTRL SHIFT P
- Search in drectory: CTRL SHIFT F
- Go back to explorer: CTRL SHIFT E

- Need more space CTRL + B

## Highlighting

You can verify your extensions work also very helpful. 

![image](https://github.com/user-attachments/assets/687b48b3-345e-4577-860c-8704dd1b4b21)

