import argparse
import os
import subprocess
import sys
import yaml

from termcolor import colored


def load_config(filename):
    with open(filename, "r") as config_file:
        return yaml.load(config_file, Loader=yaml.SafeLoader)


def filter_repos(repos, include, exclude):
    # Filter the repositories based on the include and exclude options
    if include:
        repos = [repo for repo in repos if any(tag in repo["tags"] for tag in include)]
    if exclude:
        repos = [
            repo for repo in repos if not any(tag in repo["tags"] for tag in exclude)
        ]
    return repos


def clone(args):
    # Read the configuration file
    with open(args.config, "r") as config_file:
        config = yaml.load(config_file, Loader=yaml.SafeLoader)

    # Filter the repositories based on the include and exclude options
    repos = filter_repos(config["repositories"], args.include, args.exclude)

    # Iterate over the repositories in the configuration file
    for repo in repos:
        # Join the repository folder with the root folder
        repo_folder = os.path.join(config["root_folder"], repo["path"])

        # Check if the repository folder already exists
        if os.path.exists(repo_folder):
            print(f"Repository folder {repo_folder} already exists, skipping.")
        else:
            # Create the repository folder if it does not exist
            os.makedirs(repo_folder, exist_ok=True)

            # Clone the repository
            print(f"Cloning {repo['url']} into {repo_folder}.")
            subprocess.run(["git", "clone", repo["url"], repo_folder])


def pull(args):
    """Pull the latest changes from the specified repositories.

    This function loads the configuration file and filters the list of repositories
    based on the specified tags. For each repository, it checks if the repository's
    folder exists and, if it does, runs the 'git pull' command in that folder.

    Args:
        args: The parsed command-line arguments. This should include the following:
            - config: The path to the configuration file.
            - include: A list of tags to include. Only repositories with these tags
                       will be pulled.
            - exclude: A list of tags to exclude. Repositories with these tags will
                       not be pulled.

    """
    # Load the configuration
    config = load_config(args.config)

    # Filter the repositories based on the specified tags
    repos = filter_repos(config["repositories"], args.include, args.exclude)

    # Loop through the repositories and run 'git pull' for each one
    for repo in repos:
        repo_path = os.path.join(config["root_folder"], repo["path"])
        if os.path.exists(repo_path):
            print(f"Pulling changes for repository {repo['name']}...")
            subprocess.run(["git", "-C", repo_path, "pull", "--rebase"])
        else:
            print(f"Repository {repo['name']} not found at {repo_path}")


def help(args):
    # Print the usage message
    print("Usage: repo_ranger [OPTIONS] COMMAND [ARGS]...")
    print()

    # Print the list of available commands
    print("Commands:")
    print("  init      Create a new configuration file")
    print("  list      List the configured repositories")
    print("  clone     Clone the specified repositories")
    print("  pull      Pull the specified repositories")
    print("  help      Show this message and exit")
    print()
    print("Options:")
    print("  -c, --config FILE\tPath to the configuration file")
    print()


def init(args):
    """
    Initialize the repository structure by creating the default configuration
    file in the current working directory.
    """
    # Create the default configuration file
    config_file = os.path.join(os.getcwd(), "repo_ranger.yaml")

    default_config = {"root": "repos", "repositories": []}

    with open(config_file, "w") as f:
        f.write("# Configuration file for the repo_ranger app\n")
        f.write("# See https://github.com/user/repo_ranger for details\n")
        f.write("\n")
        yaml.dump(default_config, f, default_flow_style=False)

    print(f"The default configuration file was created at {config_file}")
    print("Modify the file to add the repositories you want to manage")


def pretty_print(repos, file=None):
    """
    Pretty-print the list of repositories to the specified file.

    If no file is specified, the list is printed to the standard output.
    """
    if file is None:
        file = sys.stdout

    for repo in repos:
        path = repo["path"]
        name = repo["name"]
        summary = repo["summary"]
        tags = repo["tags"]

        file.write(colored(path, "cyan"))
        file.write(" ")
        file.write(colored(name, "green"))

        if summary:
            file.write(" - ")
            file.write(colored(summary, "white"))

        if tags:
            file.write(" [")
            file.write(colored(", ".join(tags), "magenta"))
            file.write("]")

        file.write("\n")


def list_repos(args):
    """
    Display the list of configured repositories.

    The configuration file is specified by the "args.config" attribute, which
    is set by the "-c" or "--config" option of the "list" command.
    """
    # Read the configuration file
    with open(args.config) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    # Print the list of repositories
    pretty_print(config["repositories"])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="The command to run")
    parser.add_argument("-c", "--config", help="Path to the configuration file")
    parser.add_argument(
        "--exclude", nargs="+", help="Exclude repositories with certain tags"
    )
    parser.add_argument(
        "--include", nargs="+", help="Include repositories with certain tags"
    )

    args = parser.parse_args()

    if args.command == "init":
        # Initialize the repository structure
        init(args)
    elif args.command == "pull":
        # Pull the latest changes from the remote repositories
        pull(args)
    elif args.command == "list":
        # List the configured repositories
        list_repos(args)
    elif args.command == "clone":
        # Clone the configured repositories
        clone(args)
    elif args.command == "help":
        # Display help information
        help(args)
    else:
        print(f"error: invalid command: {args.command}")
        print("Use the 'help' command to see the available commands")


if __name__ == "__main__":
    main()
