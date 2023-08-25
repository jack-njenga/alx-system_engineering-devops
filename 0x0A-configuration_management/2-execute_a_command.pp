# A manifest that Kills a process named "killmenow".

exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow', # checking if the killmenow is running b4 killing
}
