# Client configuration file (w/ Puppet)

include stdlib
file_line { 'no password authentication':
  ensure  => 'present',
  line    => 'PasswordAuthentication no',
  path    => '/etc/ssh/ssh_config',
  match   => '^PasswordAuthentication',
  replace => true,
}
file_line { 'identity file':
  ensure => 'present',
  line   => 'IdentityFile ~/.ssh/holberton',
  path   => '/etc/ssh/ssh_config',
}
