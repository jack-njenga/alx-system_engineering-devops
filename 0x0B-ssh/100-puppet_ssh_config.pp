# ssh private key config using puppet
file { 'Identity File':
  path	  => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school'
  replace => true,
}

file_line { 'disable passwd authentication':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no'
  replace => true,
}
