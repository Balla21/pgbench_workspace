def generate_file(filename, dbname, timing, scaling) :
    file_shell = filename+".sh"
    db_drop_command = f'dropdb {dbname}'
    db_create_command = f'createdb {dbname}'
    scaling_command = f"pgbench -s {scaling} -i {dbname}"
    timing_command = f"pgbench -c 10 -j 2 -t {timing} {dbname}"
    echo_command = f'''echo '$pgbench -c 10 -j 2 -t {timing} {dbname}' '''
    exit_command = 'exit 0'

    with open(file_shell,"wt") as file :
        file.writelines(db_drop_command +'\n')
        file.writelines(db_create_command + '\n')
        file.writelines(scaling_command +'\n')
        file.writelines(echo_command +'\n')
        file.writelines(timing_command +'\n')
        file.writelines(exit_command)

    return file_shell


