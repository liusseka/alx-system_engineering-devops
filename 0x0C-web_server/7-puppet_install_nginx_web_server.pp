# This file encapsulates puppet functions for setting up
# Andf configuring a nginx web server

# STEP 1: Downloading nginx
# This block downloads the repository
exec { 'add nginx repository':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  unless  => 'test -f /etc/apt/sources.list.d/nginx_stable.list',
}

# STEP 2:  Updating the system package list
# This block updates the ubuntu pacakage list
exec { 'update packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# STEP 3: Installing the nginx
# This block installs the nginx web server
package { 'nginx':
  ensure     => 'installed',
}

# STEP 4: Opening up the http port in the firewall
# onlyif ensures it runs only if nginx is installed.
exec { 'allow HTTP':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

# STEP 5: Setting permissions on the /var/www director
# Allows allow the Nginx user to access files.
exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# STEP 6: Creating basic index and 404 files
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# STEP 8: Configuring the web server
# Adds redirection and error page
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
               root /var/www/html;
        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files \$uri \$uri/ =404;
        }
        error_page 404 /404.html;
        location  /404.html {
            internal;
        }
        
        if (\$request_filename ~ redirect_me){
            rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
}
",
}
# STEP 9: Restarting the nginx webserver
# This applies the configuration changes.
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# STEP 10: Starting the Nginx service
# Ensures the Nginx service is running.
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}