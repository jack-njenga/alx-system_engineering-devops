# ssh private key path config and passwdAuth config using puppet

Exec {
  path => '/bin:/usr/bin:/usr/local/bin',
}

exec { 'IdentityFile':
  command => 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  unless  => 'grep -q "^IdentityFile ~/.ssh/school" /etc/ssh/ssh_config',
}

exec { 'disable password authentication':
command => "sed -i 's/^.*PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/ssh_config",
}

file { '/root/.ssh/config':
  ensure  => file,
  mode    => '0600',
  content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
}
