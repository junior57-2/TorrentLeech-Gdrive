#


def get_lst_of_files(input_directory, output_lst):
    for root, dirs, files in os.walk(input_directory):
        for file_name in files:
            output_lst.append(os.path.join(root, file_name))
    return output_lst


#wip
