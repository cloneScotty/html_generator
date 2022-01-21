import shutil
import os
from tkinter import *

html_shell = """

<!Doctype html>
<html>
<head>
    <body>
        <div class=<class here>
            <h1>Hello</h1><h2>World</h2>
            
            
        
        
        </div>
    </body>
</head>
</html>

"""

root = Tk()

def create_html_template(src_open, src_dest) -> str:
    """---------------- Source_open can be a file already on drive or you can create a new file.  -------------"""
    with open(src_open, 'w+') as f:
        f.writelines(html_shell)
        print(f.readline())
    f.close()

    shutil.copyfile(src_open, src_dest)

    
    os.startfile(src_dest)
    
    
create_html_template("c:/users/scott/desktop/old.txt","c:/users/scott/desktop/new.html" )