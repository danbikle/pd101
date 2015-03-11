/home/ann/pd101/README.txt

The files in this repo are for Dan's Machine Learning Class.

They are related to the 5th lecture: Pandas101

The steps to use these files are listed below:

- Install Ubuntu 14.04 Linux on your laptop or somewhere on the cloud

- apt-get install sqlite3

- useradd -m -s /bin/bash ann

- Login as ann

- Download 64 bit Anaconda for Linux:

- http://continuum.io/downloads#py34

- Install Anaconda3:

- bash Anaconda3-2.1.0-Linux-x86.sh

- mv ~ann/anaconda3/bin/curl  ~ann/anaconda3/bin/curl_ann

- vi ~ann/.bashrc

- I want this syntax in there:

if [ -e ${HOME}/anaconda3/bin ]; then
  export PATH="/home/dan/anaconda3/bin:$PATH"
fi

- type bash 

- which python

- get the files for this repo

