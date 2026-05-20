FS_TOOLS = [
    {
        'type':'function',
        'function':{
            'name':'make_directory',
            'description':'used to create a new directory',
            'parameters':{
                'type':'object',
                'properties':{
                    'filepath':{'type':'string','description':'path of the directory to create, relative to the sandbox root directory'},
                    'create_if_not_exist':{'type':'boolean','description':'whether to create the directory if it does not exist'}
                },
                'required':['filepath']
            }
        }
    },
    {
        'type':'function',
        'function':{
            'name':'list_directory',
            'description':'used to list files and directories in a directory',
            'parameters':{
                'type':'object',
                'properties':{
                    'filepath':{'type':'string','description':'path of the directory to list, relative to the sandbox root directory'}
                },
                'required':['filepath']
            }
        }
    },
    {
        'type':'function',
        'function':{
            'name':'get_root_directory',
            'description':'used to get the root directory of the sandboxed file system',
            'parameters':{
                'type':'object',
                'properties':{

                },
                'required':[]
            }
        }
    },
    {
        'type':'function',
        'function':{
            'name':'read_file',
            'description':'used to read a file in the sandboxed file system',
            'parameters':{
                'type':'object',
                'properties':{
                    'filepath':{'type':'string','description':'path of the file to be read, relative to the sandbox root directory'},
                    'mode':{'type':'string','description':'file opening mode, can be either "r" for read or "rb" for binary read'}
                },
                'required':['filepath']
            }
        }
    },
    {
        'type':'function',
        'function':{
            'name':'write_file',
            'description':'used to write a file in the sandboxed file system',
            'parameters':{
                'type':'object',
                'properties':{
                    'filepath':{'type':'string','description':'path of the file to be written, relative to the sandbox root directory'},
                    'mode':{'type':'string','description':'file opening mode, can be either "w" for overwrite or "a" for append'},
                    'content':{'type':'string','description':'content to be written to the file'}
                },
                'required':['filepath','content']
            }
        }
    },
    {
        'type':'function',
        'function':{
            'name':'fs_dir_exists',
            'description':'used to check if a directory exists in the sandboxed file system',
            'parameters':{
                'type':'object',
                'properties':{
                    'filepath':{'type':'string','description':'path of the directory to check, relative to the sandbox root directory'}
                },
                'required':['filepath']
            }
        }
    }
]


TOOLS =[
    {
        'type':'function',
        'function':{
            'name':'add',
            'description':'used to perform addition between 2 parameters',
            'parameters':{
                'type':'object',
                'properties':{
                    'x':{'type':'number'},
                    'y':{'type':'number'}
                },
                'required':['x','y']
            }
        }
    },
    {
        'type':'function',
        'function':{
            'name':'sub',
            'description':'used to perform substraction between parameters',
            'parameters':{
                'type':'object',
                'properties':{
                    'x':{'type':'number'},
                    'y':{'type':'number'}
                },
                'required':['x','y']
            }
        }
    },
    {
        'type':'function',
        'function':{
            'name':'mul',
            'description':'used to perform multiplication between 2 parameters',
            'parameters':{
                'type':'object',
                'properties':{
                    'x':{'type':'number'},
                    'y':{'type':'number'}
                },
                'required':['x','y']
            }
        }
    },
    {
        'type':'function',
        'function':{
            'name':'div',
            'description':'used to perform division between 2 parameters',
            'parameters':{
                'type':'object',
                'properties':{
                    'x':{'type':'number'},
                    'y':{'type':'number'}
                },
                'required':['x','y']
            }
        }
    },
    {
        'type':'function',
        'function':{
            'name':'pow',
            'description':'used to perform power between 2 parameters',
            'parameters':{
                'type':'object',
                'properties':{
                    'x':{'type':'number'},
                    'y':{'type':'number'}
                },
                'required':['x','y']
            }
        }
    },
    {
        'type':'function',
        'function':{
            'name':'mod',
            'description':'used to perform modulus operation on the passed parameter',
            'parameters':{
                'type':'object',
                'properties':{
                    'x':{'type':'number'}
                },
                'required':['x']
            }
        }
    },
    {
        'type':'function',
        'function':{
            'name':'sqrt',
            'description':'used to perform square root operation on the passed parameter',
            'parameters':{
                'type':'object',
                'properties':{
                    'x':{'type':'number'}
                },
                'required':['x']
            }
        }
    }
]

TOOL_SET = []
TOOL_SET.extend(TOOLS)
TOOL_SET.extend(FS_TOOLS)