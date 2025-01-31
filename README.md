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

The interpreter path shows we have selected it ".venv" (name) "venv" (virtual envrionment).

If you prefer the terminal because you're a pro.

```
#Create a new project folder:
   mkdir python_project

#Move into your new folder:
   cd python_project

#Create a virtual environment:
   python -m venv myvenv
   
   ## Then activate it 
   Windows:    myvenv\Scripts\activate
   Mac/Linux:  source myvenv/bin/activate
``` 
I believe mac/linux with VSCode does it automatically, you just need to reload a terminal . While Windows, just uses the venv but not sure always activates it but works regardless? 

If you really want to make sure:
![image](https://github.com/user-attachments/assets/f491e860-c0f8-49e0-8024-93cee4c5d757)


## Explorer

In your explorer you now have a .venv (the .env is something different for API keys).
This is a portable python executable. 

![image](https://github.com/user-attachments/assets/f4063072-1aaf-42d0-8425-c07a2ab80313)

**Try to keep your projects organized. There are some rules for folders and file names:**

DIRECTORIES

my_package
mypackage
company_project

MODULES/FILES

utils.py
database_connector.py
auth_helper.py

No spaces, capitals, or "-","."

## Running files

You can then simply right click a python file:

![image](https://github.com/user-attachments/assets/8fcfb8df-3229-4e02-9c68-682c4d754920)

Some things that are useful here, copying paths or relative paths. Or running the script. 

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
- Search in a file CTRL + F

## Highlighting

You can verify your extensions work also very helpful. 

![image](https://github.com/user-attachments/assets/687b48b3-345e-4577-860c-8704dd1b4b21)

## PIP

**Only install packages after having done the venv, as it will install the packages inside this small python and not system wide.**
```
pip install x y
```
You can see it work directly as the files are being installed in the venv:

![image](https://github.com/user-attachments/assets/71ac0edc-5682-4306-be9f-dbd41eda3dd3)

This is important for two reasons: Security as python can be used for malicious code. 
But also once you will want to work with other projects or re-use code in 5 years. 

Can use ```pip list``` for packages in your venv. 

Then you can simply create a ```requirements.txt``` 
Where you keep track of the packages needed. Or do this automatically:
```
pip freeze > requirements.txt
```

If you're working with someone else's code this will also be useful:

```
pip install -r requirements.txt 
```

VSCode detects it automatically if you're creating a venv like the steps above. 


## Running

``` 
+ (.venv) PS C:\Users\hade\Desktop\new> & c:/Users/hade/Desktop/new/.venv/Scripts/python.exe c:/Users/hade/Desktop/new/hello.py
hello world
## VENV is on ######### CWD ########## VENV Python virtual path ############################ SCRIPT I WANT TO RUN ############
```

Then in your hello.py put the following content:

```
import sys
print (f'{sys.executable}')
```

If you run this and get ``` yourfoldername\.venv\Scripts\python.exe ``` 

Well the set up worked because it's using the new mini-python we created. 

You can achieve the same in terminal: ``` which python ##MacLinux 
where python ##Windows```

## Imports

I like to break down imports into something clear: Internal & external

External is going to be first for example one of the most used packages:

``` import numpy as np ```

Which let's me use numpy in my code (as np):

``` simple_array = np.arange(10) ``` 

This is useful to make code shorter "as" and set what you want here. You could use nup or nump idk 😕

----

Internal is slightly different and trickier for beginners as they often work in single files. But I think it's very important to understand:

Now we create a second file called "world.py" along with our first "hello.py".

```
#hello.py
import sys
import numpy as np

def exec():
    print (f'{sys.executable}')
    simple_array = np.arange(10)
    print(f"Simple array: {simple_array}")

#world.py
from hello import exec
exec()
``` 

This is illustrative of course, but the idea is that you can easily use something in something else? 

**Better exercise is to do a calculator with a main file, operations file and state file**

---

Sub-imports: Create a folder called: 'utils'

Drag the hello.py into it

Now change the imports to:
```
#world.py
from utils.hello import exec
exec()
```
Cool! 

Now create another file 'random_number.py' in the utils folder.
```
#utils/random_number.py
import numpy as np
import random

def get_random_element(array):
    return random.choice(array)
```
Chnage the other file slightly
```
#utils/hello.py
import sys
import numpy as np
from utils.random_array import get_random_element

def exec():
    print(f'{sys.executable}')
    simple_array = np.arange(10)
    print(f"Simple array: {simple_array}")
    print(f"Random element from simple array: {get_random_element(simple_array)}")
```

Run this one.
```
#world.py
from utils.hello import exec
exec()
```

You see how it's important to understand how you can effectively build features in a clean manner, aswell as understanding why its practical to break down certain things to an extreme.
Again a better exercise is the calculator.

## Comments & Debug

Two ways of making comments in python:
Useful for pseudo-code, for clarity:

![Screenshot from 2025-01-31 11-01-30](https://github.com/user-attachments/assets/545b3114-ca6c-42e8-bba7-e3fb71ec8acb)

My favourite is # but you can also use """ for multi-line. It will ignore that block. 

This is useful for debug then temporarily disabling a feature while keeping it in the code. 
```
a = 2 + 5
#b = 7 + 4

c = a #+ b
print (f'{c}) 
```


Shortcut to comment out a block: 
Windows: Shift + Alt + A
Linux: Shift + Ctrl + A
macOS: Shift + Option + A

For debug, I recommend following error lines (more specifically last or before last error in terminal output) then adding print statements to anything that could have caused. 
This will help you reverse engineer your own code. 




