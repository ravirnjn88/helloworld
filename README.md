Message Passing System (MPS)

The main function of this tool is to facilitate the message passing between different services.

Requirements and installation Instruction

1. Code Tested on Ubuntu 14.04	

2. Install the dependencies using following command

	```sudo apt-get install python-pip python-dev nginx rabbitmq-server python-requests mysql-server libmysqlclient-dev```
	```pip install Celery sqlalchemy uwsgi flask MySQL-python```

3. Run the create_table.py file to create the database

4. Copy the upstart script start.conf to the /etc/init/ directory so that the script can start automatically on restart.

5. Create nginx configuration file similar to nginx_config and enable that in nginx

6. Run the celeray worker using following command

	```celery -A mps.tasks worker```

Usage:

1. http://your_server_ip/mps/acceptmsg?senders_endpoint={x}&msgid={x}&msgdata={x}

Demourl: http://raviranjan.xyz/demo