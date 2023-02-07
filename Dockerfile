# base image  
FROM python:3.11   

# Set the working directory in the container
WORKDIR /app

# Copy the local requirements.txt file to the container
COPY requirements.txt .

# update pip  
RUN pip install --upgrade pip  

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy whole project to your docker home directory. 
COPY . . 

# run this command to install all dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Export port 8000
# EXPOSE 8000

# start server  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]