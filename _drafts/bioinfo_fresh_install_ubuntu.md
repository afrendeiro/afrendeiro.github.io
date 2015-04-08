


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
# sudo hostname new-name
# or 
# edit /etc/hostname (and /etc/hosts)
# requires reboot in both cases

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

# perl always complains if localle is not set.
# add these lines to /etc/environment:
# export LANGUAGE=en_US.UTF-8
# export LC_ALL=en_US.UTF-8
# export LANG=en_US.UTF-8
# export LC_TYPE=en_US.UTF-8

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
sudo pip install pysam htseq macs2 rpy2

# R
sudo apt-get install r-base r-base-dev

# R packages (install for everyone)
sudo R
install.packages("ggplot2", "reshape")

# R bioconductor
source("http://bioconductor.org/biocLite.R")
biocLite("DiffBind", "DESeq", "GenomicRanges")

# EC2 <--> S3 data transfer
sudo apt-get install s3cmd
s3cmd --configure

# Libraries installed from source
# globally

# install to: /usr/local/bin/ or /usr/local/lib/
# edit /etc/environment with paths if needed 
# (not needed if not copying executables to bin)

# locally for a user
# mkdir -p .local/bin
# Add to .bashrc or .bash_profile:
# PATH=$PATH:/home/username/.local/bin
# source .bashrc

# sambamba
wget https://github.com/lomereiter/sambamba/releases/download/v0.5.2/sambamba_v0.5.2_linux.tar.bz2
tar -xjvf sambamba_v0.5.2_linux.tar.bz2
rm sambamba*.tar.bz2
sudo mv sambamba* /usr/local/bin/sambamba

# trimmomatic
wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.33.zip
unzip Trimmomatic-0.33.zip
chmod +x Trimmomatic-0.33/trimmomatic-0.33.jar
sudo mv Trimmomatic-0.33/trimmomatic-0.33.jar /usr/bin/
# run as java -jar `which trimmomatic-0.33.jar`

# skewer
git clone https://github.com/relipmoc/skewer.git
cd skewer
make
sudo make install
cd
sudo rm -r skewer

# ucsc tools
rsync -aP rsync://hgdownload.cse.ucsc.edu/genome/admin/exe/linux.x86_64/ ucscTools
sudo cp ucscTools/* /usr/local/bin
sudo cp ucscTools/blat/blat /usr/local/bin

# homer
sudo mkdir /usr/local/lib/homer
cd /usr/local/lib/homer
sudo wget http://homer.salk.edu/homer/configureHomer.pl
perl configureHomer.pl -install
# add 
# :/usr/local/homer/bin
# to /etc/environment

# spp + phantompeakqualtools
sudo apt-get install libboost-all-dev
sudo R
install.packages("caTools", "snow")

wget https://phantompeakqualtools.googlecode.com/files/ccQualityControl.v.1.1.tar.gz
tar xfz ccQualityControl.v.1.1.tar.gz
sudo R CMD INSTALL phantompeakqualtools/spp_1.10.1.tar.gz
# add #! /usr/bin/env R to first line of phantompeakqualtools/run_spp*
chmod +x phantompeakqualtools/run_spp*
sudo mv phantompeakqualtools/run_spp* /usr/local/bin


```
