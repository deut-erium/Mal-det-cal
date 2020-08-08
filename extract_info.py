import pefile
import argparse
from hashlib import sha256
import re
import os

def sha256_sum(file_name):
    """
    Calculates the sha256sum of file provided

    Args:
        file_name: path of the file to be hashed
    Returns:
        sha256_sum: sha256 hash of the file contents
    """
    sha_hash = sha256()
    with open(file_name,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha_hash.update(byte_block)
    return sha_hash.hexdigest()

def strings(file_name, output_file):
    """
    Generates the strings output of file

    Args:
        file_name: name of the file for which ascii strings to be extracted
        output_file: name of the file in which output is stored
    Returns:
        None: output is stored in output_file
    """
    f = open(file_name, 'rb')
    with open(output_file,'wb') as output:
        while True:
            line = f.readline()
            if line == b'':
                break
            for string in re.findall(b'[^\x00-\x1f\x7f-\xff]{4,}',line):
                output.write(string+b'\n')
    f.close()

def structure_info(file_name, output_file):
    """
    Writes structure info of PE executable in output_file

    Args:
        file_name: name of suspected PE
        output_file: name of output file to save output
    Returns:
        None: writes output in output_file
    """
    try:
        with open(output_file,'w') as output:
            output.write(pefile.PE("bin/ZipCrack.exe").dump_info())
    except pefile.PEFormatError:
        #print("{} not a PE".format(file_name))
        return False
    return True
    
def extract_info_file(file_name, output_path):
    """
    Extracts strings info and structure info of given file

    Args:
        file_name: Name of the PE file
        output_path: path of output directory in which to save files
    Returns:
        None: If a valid PE file is supplied, a directory named sha265sum(file_name) is generated
        containing String.txt and Structure_Info.txt
    """
    sha256 = sha256_sum(file_name)
    savepath = os.path.join(output_path,sha256)
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    status = structure_info(file_name,os.path.join(savepath, "Structure_Info.txt"))
    if status:
        strings(file_name, os.path.join(savepath, "String.txt"))
    else:
        if not os.listdir(savepath): # do not kick pre existing stuff
            os.rmdir(savepath)
    
def list_files(path):
    """
    Generator to list all files under a path

    Args:
        path: path to scan
    Returns:
        list of relative paths of files to `path`
    """
    for subpath, dirs, files in os.walk(path):
        for file in files:
            yield os.path.join(subpath, file)
    
def extract_all(path, output_path):
    """
    extract structure and strings info for all files under path

    Args:
        path: path under which all files need to be extracted
        output_path: path under which output files need to be stored
    Returns:
        None: extracts structure and strings info for all valid PE files under path
    """
    for file in list_files(path):
        extract_info_file(file, output_path)

if __name__ == "__main__":
    USAGE = """ for extracting info for a single file use
python3 extract_info.py file <path/to/file> <path/to/savepath>

for extracting info for all files under a path use
python3 extract_info.py path <path> <path/to/savepath>"""

