from TOOLS import ns_math_tools,fs
TOOL_MAP = {
    'add':ns_math_tools.add,
    'sub':ns_math_tools.sub,
    'mul':ns_math_tools.mul,
    'div':ns_math_tools.div,
    'pow':ns_math_tools.pow,
    'mod':ns_math_tools.mod,
    'sqrt':ns_math_tools.sqrt,
    'read_file':fs.fs_read_file,
    'write_file':fs.fs_write_file,
    'make_directory':fs.fs_make_dir,
    'list_directory':fs.fs_list_dir,
    'get_root_directory':fs.fs_get_root_dir,
    'fs_dir_exists':fs.fs_dir_exists

}