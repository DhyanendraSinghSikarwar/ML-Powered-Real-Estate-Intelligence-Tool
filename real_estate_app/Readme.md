
# Website

It's a 99-acres properties application to process the data.

# How to setup the project.
  
  - python version should be 3.11
  
### Follow below instruction to install the depedencies.

##### Ubuntu

- Install python3.11
	```sh
	sudo add-apt-repository ppa:deadsnakes/ppa
  	sudo apt-get update
	sudo apt-get install python3.11
  	sudo apt-get install python3.11-dev
	```
- Install Virtualenv
	```sh
	sudo apt-get install python3-pip
	sudo pip3 install virtualenv
	```

### Follow below setups to setup the application.

- Create the virtual envoirments with python 3.11 version and activate.
    ```sh
    virtualenv --python=python3.11 myenv
    source myenv/bin/activate
    ```

- Install python dependencies,run into the project root directory.
    ```sh
    pip install -r requirements.txt
  ```
- Run server
	```sh
	streamlit run home.py
	````
