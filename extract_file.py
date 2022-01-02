path_to_file = input().split('\\')
file_name_and_extension = path_to_file[-1].split(".")
file_name = file_name_and_extension[0]
extension = file_name_and_extension[1]
print(f"File name: {file_name}")
print(f"File extension: {extension}")
