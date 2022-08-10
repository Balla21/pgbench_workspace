import os  # module needed in order to run command line through Python


def generate_file(filename, dbname, timing, scaling) :
    '''
        This utility function will be in charge of creating a shell file based
        on the data provided by the user from the form and return the name of the
        shell file created
    '''
    file_shell_name = f'{filename}.sh'
    shell_file_content = f'''
        dropdb {dbname}
        createdb {dbname}
        pgbench -s {scaling} -i {dbname}
        pgbench -c 10 -j 2 -t {timing} {dbname}
        echo '$pgbench -c 10 -j 2 -t {timing} {dbname}'
        exit 0
    '''
    with open(file_shell_name,"wt") as file :
        file.writelines(shell_file_content)
    return  file_shell_name


def execute_file(file) :
    '''
        This utility function is in charge of executing the shell file and forward the scripting result
        into a file called output.txt. From this step, data from the text file will be read and provide
        as an output in the array and return from the function result
    '''
    output_data = []
    os.system(f'bash {file} > output.txt')
    with open('output.txt', 'rt') as file :
        for line in file :
            output_data.append(line)
    return output_data