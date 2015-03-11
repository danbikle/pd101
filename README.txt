/home/ann/pd101/README.txt

The files in this repo are for Dan's Machine Learning Class.

They are related to the 5th lecture: Pandas101

The steps I follow to use these files are listed below:

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

- Type bash 

- which python

- Get the files for this repo

- https://github.com/danbikle/pd101/archive/master.zip

- Put the files here:

- ~ann/pd101

- Verify I did it:

- head ~ann/pd101/README.txt

- cd ~ann/pd101

- ./pd101.bash

- I should see something like this:

- https://github.com/danbikle/pd101/blob/master/screendump2015_0311.txt

- If you have questions contact Dan:

- dan@bot4.us

- Put not-spam in subject.

