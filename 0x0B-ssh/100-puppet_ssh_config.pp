# Updating my config file using puppet
include stdlib

# this code block disables password authentication
file_line { 'Turn off passwd auth':
  ensure  => present,
  line    => '    PasswordAuthentication no',
  path    => '/etc/ssh/ssh_config',
  replace => true,
}

# this block sets identity for ssh
file_line { 'Declare identity file':
  ensure  => present,
  line    => '    IdentityFile ~/.ssh/school',
  path    => '/etc/ssh/ssh_config',
  replace => true,
}
