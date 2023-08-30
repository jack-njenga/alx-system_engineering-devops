# Nginx configurations

package {'nginx':
ensure => installed,
}

file {'/var/www/html/index.html':
enusure => file,
content => 'Hello World!',
}

file_line {'Redirect':
ensure 	=> present
path	=> '/etc/nginx/sites-available/default',
after	=> 'listen 80 default_server;',
line	=> 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;'
}

service {'nginx':
ensure	=> runing,
require	=> Package['nginx'],
}
