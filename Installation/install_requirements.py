import subprocess

def install_requirements(requirements_file='./Installation/requirements.txt'):
    try:
        # Run pip install command to install requirements
        subprocess.check_call(['pip', 'install', '-r', requirements_file])
        print("Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing requirements: {e}")

if __name__ == "__main__":
    install_requirements()
