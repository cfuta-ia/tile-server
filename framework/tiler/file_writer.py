import os
import shutil

class Writer:
    """ """
    DIR = ('.', 'tiles')
    @classmethod
    def getBasePath(cls):
        """Get the base path of the Tile File Writer
        
        Returns:
            Tile File Write base directory path
        """
        return os.path.join(*cls.DIR)

    @classmethod
    def isBaseDirectory(cls, dir_path: str):
        """Function to get the base directory path string
        Args:
            dir_path: directory path to check against
        Returns:
            True/False
        """
        return dir_path == cls.getBasePath()

    @classmethod
    def createDirectory(cls, *args: any, overwriteOnExists=False):
        """Create a directory for the tiles or subdirectory to go in
        
        Args:
            args: inputs to build the directory path
            overwriteOnExists: boolean flag to overwrite directory if already exists
        Returns:
            boolean if operation was a success
        """
        dir_path = os.path.join(cls.getBasePath(), *args)
        # Check Input Path
        if os.path.exists(dir_path):
            if os.path.isfile(dir_path):
                # Path Leads to File
                print(f"Path leads to a file. ({dir_path})")
                _return = False
            elif overwriteOnExists:
                if cls.isBaseDirectory(dir_path):
                    # Path Leads to Base Directory
                    print(f"Path is the base directory and cannot be overwritten. ({dir_path})")
                    _return = False
                else:
                    # Path Exists >> Overwrite
                    shutil.rmtree(dir_path)
                    #cls.remove_directory(*args)
                    os.makedirs(dir_path)
                    print(f"Overwrote directory. ({dir_path})")
                    _return = True
            else:
                # Path Already Exists
                print(f"Directory already exists. ({dir_path})")
                _return = False
        else:
            # Create Directory
            os.makedirs(dir_path)
            print(f"Created new directory. ({dir_path})")
            _return = True
        return _return

    @classmethod
    def removeDirectory(cls, *args: any, dir_path=None):
        """Remove a directory function
        
        Args:
            args: 
            dir_path:
        Returns:
            boolean if operation was a success
        """
        if dir_path:
            _path = os.path.join(cls.getBasePath(), dir_path)
        else:
            _path = os.path.join(cls.getBasePath(), *args)

        # Check valid path
        if os.path.exists(_path):
            if os.path.isdir(_path):
                # Path is a directory
                if cls.isBaseDirectory(_path):
                    # Path Leads to Base Directory
                    print(f"Path is the base directory and cannot be removed. ({_path})")
                    _return = False
                else:
                    shutil.rmtree(_path)
                    print(f"Removed directory. ({_path})")
                    _return = True
            elif os.path.isfile(_path):
                # Path is a file
                print(f"Path is not valid. ({_path})")
                _return = False
            else:
                # Catch All Error
                print(f"Path error cannot remove. ({_path})")
                _return = False
        else:
            # Path is not valid
            print(f"Path is not valid. ({_path})")
            _return = False
        return _return

    @classmethod
    def removeFile(cls, filepath: str):
        """Remove a file function
        
        Args:
            filepath: path to the file inside of the tiles directory
        Returns:
            boolean if operation was a success
        """
        _path = os.path.join(cls.getBasePath(), filepath)
        # Check valid path
        if os.path.exists(_path):
            if os.path.isdir(_path):
                # Path is a directory
                print(f"Path is a directory cannot remove with this function. ({_path})")
                _return = False
            elif os.path.isfile(_path):
                # Path is a file
                os.remove(_path)
                print(f"File at path removed. ({_path})")
                _return = True
            else:
                # Catch All Error
                print(f"Path error cannot remove. ({_path})")
                _return = False
        else:
            # Path is not valid
            print(f"Path is not valid. ({_path})")
            _return = False
        return _return

    @classmethod
    def createFile(cls, content, *args, file_path=None):
        """Create File"""
        if file_path:
            _path = os.path.join(cls.getBasePath(), file_path)
        else:
            _path = os.path.join(cls.getBasePath(), *args)
        with open(_path, 'w') as f:
            f.write(content)
        return None
