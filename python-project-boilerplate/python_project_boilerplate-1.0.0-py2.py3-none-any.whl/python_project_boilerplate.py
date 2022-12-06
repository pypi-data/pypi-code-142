import os

# Creating a folder structure for the project.
current_directory = os.getcwd()
folder_name=input("Enter Project Name : ")
final_directory = os.path.join(current_directory, folder_name)

docs_folder_name = f"{final_directory}/docs"
utility_folder_name = f"{final_directory}/utility"
logs_folder_name = f"{final_directory}/logs"
config_folder_name = f"{final_directory}/config"
src_folder_name = f"{final_directory}/src"


# Creating a folder structure for the project.

def create_project_structure():
   try:
      if not os.path.exists(final_directory):
         os.makedirs(final_directory)
         os.makedirs(docs_folder_name)
         os.makedirs(utility_folder_name)
         os.makedirs(logs_folder_name)
         os.makedirs(config_folder_name)
         os.makedirs(src_folder_name)

         print(final_directory)
         with open(f'{final_directory}/main.py', 'a+') as fp:
            fp.write("# Main code")

         with open(f'{final_directory}/README.md', 'a+') as fp:
            fp.write("# Readme file")
         print(f"Directory {final_directory} has been Created")

   except Exception as e:
       print(f"Directory {final_directory} already exists")

create_project_structure()