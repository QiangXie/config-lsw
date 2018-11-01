import os
import subprocess
#config zsh
print("Config zsh...")
if not os.path.exists("/usr/bin/zsh"):
    print("Please install zsh, sudo apt-get install zsh")
    exit(1)
else:
    subprocess.call("cp ./.zshrc ~/", shell=True)
    pass
    


#config tmux
print("Config tmux...")
if not os.path.exists("/usr/bin/tmux"):
    print("Please install zsh, sudo apt-get install tmux")
    exit(1)
else:
    subprocess.call("cp ./.tmux.conf ~/", shell=True)


