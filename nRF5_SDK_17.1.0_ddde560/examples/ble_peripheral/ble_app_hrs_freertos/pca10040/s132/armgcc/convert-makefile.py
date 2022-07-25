#!/usr/bin/python3

# Copy this file to ~/Projects/NRF52/nRF5_SDK_17.1.0_ddde560/examples/ble_xxx/xxxxx/pca10040/s132/armgcc
import os

# Path where nRF5 SDK is installed
SDK_INSTALL_PATH = '/home/luyaohan1001/Projects/NRF52/nRF5_SDK_17.1.0_ddde560'

def create_subdir_and_copy_src(src_path):
    '''
    Given a source path in another directory, make a same directory here and copy over the source. 

        Parameters:
            src_path (string) : path to the source file
            example: $(SDK_ROOT)/components/ble/nrf_ble_gatt/nrf_ble_gatt.c

        Returns:
            None.
    '''
    items = src_path.split('/')
    # List of subdirectory names to be joined with '/' and becomes the path
    from_path_list = []
    to_path_list = []
    for item in items:
        if item == '$(SDK_ROOT)':
            from_path_list.append(SDK_INSTALL_PATH)
            to_path_list.append('../../../src') # make a src directory in project directory
        elif item == '$(PROJ_DIR)':
            curr_dir = os.getcwd()
            from_path_list.append(curr_dir + '/../../../')
            to_path_list.append('../../../src') # make a src directory in project directory
        else:
            from_path_list.append(item)
            to_path_list.append(item) # current directory
    from_path = '/'.join(from_path_list[:-1]) # example  ../../../src/components/ble/common
    from_file = '/'.join(from_path_list[:]) # example  ../../../src/components/ble/common/ble_srv_common.c
    to_path = '/'.join(to_path_list[:-1]) # example /home/luyaohan1001/Projects/NRF52/nRF5_SDK_17.1.0_ddde560/components/ble/nrf_ble_gatt
    to_file = '/'.join(to_path_list[:]) # example /home/luyaohan1001/Projects/NRF52/nRF5_SDK_17.1.0_ddde560/components/ble/nrf_ble_gatt/nrf_ble_gatt.c
    
    os.system('mkdir -p ' + to_path) # create directory and subdirectory. 
    os.system('cp ' + from_file + ' ' + to_file)


def copy_inc(inc_path):
    '''
    Given a include path in another directory, make a same directory here and copy over the source. 

        Parameters:
            src_path (string) : path to the source file
            example: $(SDK_ROOT)/components/ble/nrf_ble_gatt/nrf_ble_gatt.c

        Returns:
            None.
    '''
    items = inc_path.split('/')
    # List of subdirectory names to be joined with '/' and becomes the path
    from_path_list = []
    to_path_list = []
    for item in items:
        if item == '$(SDK_ROOT)':
            from_path_list.append(SDK_INSTALL_PATH)
            to_path_list.append('../../../src') # make a src directory in project directory
        elif item == '$(PROJ_DIR)':
            curr_dir = os.getcwd()
            from_path_list.append(curr_dir + '/../../../')
            to_path_list.append('../../../src') # make a src directory in project directory
        else:
            from_path_list.append(item)
            to_path_list.append(item) # current directory
    from_path = '/'.join(from_path_list) # example  ../../../src/components/ble/common
    to_path = '/'.join(to_path_list) # example /home/luyaohan1001/Projects/NRF52/nRF5_SDK_17.1.0_ddde560/components/ble/nrf_ble_gatt
    
    os.system('mkdir -p ' + to_path) # create directory and subdirectory. 
    os.system('cp -r ' + from_path + '/*' + ' ' + to_path)

def copy_makefile_common():
    to_path = '../../../src/components/toolchain/gcc'
    os.system('mkdir -p ' + to_path)
    from_path = SDK_INSTALL_PATH + '/components/toolchain/gcc/Makefile.common'
    os.system('cp ' + from_path + ' ' + to_path)

def main():
    copy_makefile_common()

    src_file_flag = False 
    inc_folders_flag = False 
    temp = ''
    with open('Makefile', 'r') as makefile:
        for line in makefile:

            # Capture 'SRC_FILES += \' ...
            if src_file_flag == True:
                if len(line.strip('\n')) == 0:
                    src_file_flag = False
                    pass
                else:
                    create_subdir_and_copy_src(line.strip('\n \\'))
                    pass
            if 'SRC_FILES += ' in line:
                src_file_flag = True

            # Capture 'INC_FOLDERS += \'...
            if inc_folders_flag == True:
                if len(line.strip('\n')) == 0:
                    inc_folders_flag = False
                    pass
                else:
                    copy_inc(line.strip('\n \\'))
            if 'INC_FOLDERS += ' in line:
                inc_folders_flag = True
        
if __name__ == '__main__':
    main()