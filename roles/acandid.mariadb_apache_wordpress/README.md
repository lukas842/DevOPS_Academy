# Ansible Role: mariadb_apache_wordpress
=========

A simple Ansible role for installing and configuring the MariaDB, Apache and WordPress for RHEL/CentOS 7 and Debian 10.

- Install the necessary packages;
- Create configuration file;


Requirements
------------

- The firewall settings are not considered to be a concern of this role.

Role Variables
--------------


None of the variables below are required

| Variable                                     | Default                       | Comments                                     |
| :---                                         | :---                          | :---                                         |
| `db_name`                                    |                               | Inform wordpress database name
|                                              |                               | 
| `db_user`                                    |                               | Inform user for database
|                                              |                               |
| `root_login`                                 |                               | user root mariadb
|                                              |                               |
| `root_password`                              |                               | root password mariadb
|                                              |                               |
| `db_host`                                    |                               | Database host
|                                              |                               |



Dependencies
------------

You need to install python-apt package on debian 10 


Example Playbook
----------------

---
- hosts: server

  roles:
  
    - /path/mariadb_apache_wordpress
...

## Contributing

Issues, feature requests, ideas are appreciated and can be posted in the Issues section.


Author Information
------------------
LinkedIn: https://br.linkedin.com/in/almircandido
