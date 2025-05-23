#Deriving the latest base image
FROM python:latest


#Labels as key value pair
LABEL Maintainer="adrian.robles"

# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/src

#to COPY the remote file at working directory in container
COPY wrapping_test.py .
# Now the structure looks like this '/usr/app/src/wrapping_test.py'
# Copy requirements.txt if you have dependencies
# COPY requirements.txt .

# If you want to copy more files, use relative paths from the Dockerfile location
# Example: COPY another_file.py .

# Avoid using Windows-style paths in COPY; use relative Unix-style paths instead
#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "./wrapping_test.py"]