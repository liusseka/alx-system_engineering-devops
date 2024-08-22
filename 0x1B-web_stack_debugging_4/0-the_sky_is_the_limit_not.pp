# This script inceases the limit of the requests that...
# can be served by the nginx server

# This section increase the ULIMIT
exec { 'fix--for-nginx':
  # This line modifies the ulimit value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # This line specifies the path for the sed command
  path    => '/usr/local/bin/:/bin/'
}

# This sectionestart Nginx
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/'
}