# create a file in /tmp
file {'/tmp/school':
  ensure  => present,
  mode    => '0744',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
}
