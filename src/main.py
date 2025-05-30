from textnode import TextNode
import os, shutil
def clean_public(path): 
        if os.path.exists(path):
            shutil.rmtree(path)
        return path
        
def copy_file(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    if not os.path.exists(source):
        raise Exception(f"specified path: {source} not found")
    copy_contents = os.listdir(source)
    for content in copy_contents:
        if os.path.isfile(os.path.join(source, content)):
            shutil.copy(os.path.join(source, content), os.path.join(destination, content))
        elif os.path.isdir(os.path.join(source, content)):
            copy_file(os.path.join(source, content), os.path.join(destination, content))
        
            
    
def main(static, public):
    cleaned_public = clean_public(public)
    copy_file(static, cleaned_public)

if __name__ == "__main__":
    main(os.path.join("static"), os.path.join("public"))