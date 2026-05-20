import os
import json
SANDBOX_ROOT = os.path.expanduser("~/OneDrive/Desktop/sandbox")
os.makedirs(SANDBOX_ROOT, exist_ok=True)
WRITE_MODE_SET = {"x","w","a","+"}
READ_MODE_SET = {'r','+','rb','r+b'}
def _santize_mode(mode:str,IS_WRITE:bool)->str:
    result = ""
    for c in mode:
        if c in (WRITE_MODE_SET if IS_WRITE else READ_MODE_SET):
            result += c
    return result

def make_real_path(filepath:str)->str:
    real_path = SANDBOX_ROOT
    if not filepath.startswith(SANDBOX_ROOT):
        return os.path.join(SANDBOX_ROOT, filepath)
    else:
        real_path = filepath
    return real_path
def _is_parent_traversal(path:str)->bool:
    if "../" in path or "/.." in path:
        return True
    return False

def fs_write_file(filepath:str,mode:str,content:str)->str:
    if _is_parent_traversal(filepath):
        return json.dumps({'status':'error','message':'parent directory traversal is not allowed'})
    real_path = make_real_path(filepath)
    try:
        with open(real_path,_santize_mode(mode,True)) as f:
            bytes_written = f.write(content)
            return json.dumps({'status':'success','bytes_written':bytes_written})
    except IOError as e:
        return json.dumps({'status':'error','message':str(e)})  
    
     

def fs_make_dir(filepath:str,create_if_not_exist:bool)->str:
    if _is_parent_traversal(filepath):
        return json.dumps({'status':'error','message':'parent directory traversal is not allowed'})
    real_path = make_real_path(filepath)
    try:
        os.makedirs(real_path,exist_ok=True) if create_if_not_exist else os.mkdir(real_path)
        return json.dumps({'status':'success'})         
    except IOError as e:
        return json.dumps({'status':'error','message':{real_path}})

def fs_list_dir(filepath:str)->str:
    if _is_parent_traversal(filepath):
        return json.dumps({'status':'error','message':'parent directory traversal is not allowed'})
    real_path = make_real_path(filepath)
    try:
        dirs = os.listdir(real_path)
        dirs = list(filter(lambda x: x not in (".", ".."), dirs))
        return json.dumps({'status':'success','files':dirs})
    except IOError as e:
        return json.dumps({'status':'error','message':{real_path}})              

def fs_get_root_dir()->str:
    
    return json.dumps({"status":"success","root_dir":SANDBOX_ROOT})

def fs_read_file(filepath:str,mode:str)->str:
    if _is_parent_traversal(filepath):
        return json.dumps({'status':'error','message':'parent directory traversal is not allowed'})
    real_path = make_real_path(filepath)
    try:
        with open(real_path,_santize_mode(mode,False)) as f:
            content = f.read()
            return json.dumps({'status':'success','content':content})
    except IOError as e:
        return json.dumps({'status':'error','message':{real_path}})
    

def fs_dir_exists(filepath:str)->str:
    if _is_parent_traversal(filepath):
        return json.dumps({'status':'error','message':'parent directory traversal is not allowed'})
    real_path = make_real_path(filepath)
    exists = os.path.isdir(real_path)
    return json.dumps({'status':'success','exists':exists})