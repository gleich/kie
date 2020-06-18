#!/bin/bash
# This file is to serve more as a list of all the configs you need to run. That is why it exits immediately

exit

sudo apt-get update

# ZSH
sudo apt-get install zsh git -y
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# p10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>! ~/.zshrc
