# ssh private key config using puppet

include stdlib
file_line{'Identity file':
path => '/etc/ssh/config',
line => 'IdentityFile ~/.ssh/school'
}

file_line{'Disable password authentication':
path => '/etc/ssh/config',
line => 'PasswordAuthentication no'
}
