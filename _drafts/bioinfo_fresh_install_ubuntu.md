


```bash
#
# Software install from fresh Ubuntu 14.04 LTS image on AWS EC2
#

# New users
sudo adduser username

# Grant the new user sudo privileges
sudo visudo
# username ALL=(ALL:ALL) ALL
# add this line ^^

# change to that user
su - username

# change server name
# edit /etc/hostname (and /etc/hosts)

# system update
sudo apt-get update
sudo apt-get install build-essential # just to make sure
sudo apt-get upgrade
sudo apt-get dist-upgrade

# configs
# keep ssh sessions alive
# edit /etc/ssh/ssh_config
# add the line:
# ServerAliveInterval 120
# under Host *
sudo service ssh restart

# basics
sudo apt-get install git github-backup

# python
sudo apt-get install python-dev python-pip python-virtualenv 

# python dependencies
# since neither pip or easy_install can install system-level dependencies, let's use apt-get
sudo apt-get install libatlas-base-dev libfreetype6-dev

sudo apt-get install python-numpy cython python-scipy python-pandas python-matplotlib ipython python-biopython
sudo pip install seaborn

# bioinfo
sudo apt-get install bedtools samtools piccard-tools fastqc

# python bioinfo
sudo pip install pysam htseq macs2

# R
sudo apt-get install r-base r-base-dev

# R packages (install for everyone)
sudo R
install.packages("ggplot2")

# R bioconductor
source("http://bioconductor.org/biocLite.R")
biocLite("DiffBind", "DESeq", "GenomicRanges")

# EC2 <--> S3 data transfer
sudo apt-get install s3cmd
s3cmd --configure

# Libraries installed from source
# globally

# install to: /usr/local/lib/
# edit /etc/environment with paths

# locally for a user
mkdir -p .local/bin

# Add to .bashrc:
PATH=$PATH:/home/username/.local/bin
source .bashrc

# sambamba
wget https://github.com/lomereiter/sambamba/releases/download/v0.5.2/sambamba_v0.5.2_linux.tar.bz2
tar -xjvf sambamba_v0.5.2_linux.tar.bz2
rm sambamba*.tar.bz2
mv sambamba* .local/bin/sambamba
chmod +x .local/bin/sambamba



# ucsc tools
rsync -aP rsync://hgdownload.cse.ucsc.edu/genome/admin/exe/linux.x86_64/ ./local/software/ucscTools

# add to .bashrc:
PATH=$PATH:/home/username/.local/software/ucscTools
source .bashrc


# phanthompeak

```
