Script to send a YO for Nagios/Icinga alerts. 

Given an API token, it will send a YO to everyone subscribed to that
account. If a cgi-path and host and/or service are also included, it
will include a link to the problematic service in the Nagios web
interface, or the Icinga Classic web interface

If a username is included, it will YO that user. Otherwise, it will YO
all users subsubscribed to it.

In order to add this to nagioss, add a commands like the follwing:

```
define command{
	command_name	service_nagiyos_all
	command_line    $PATH_TO_NAGIYOS --api-key $API_KEY --host $HOSTNAME$ --service $SERVICEDESC$
}
define command{
	command_name	host_nagiyos_all
	command_line    $PATH_TO_NAGIYOS --api-key $API_KEY --host $HOSTNAME$
}

```
Then add a contact such as the following:

define contact{
        contact_name                    nagiyos_all
        alias                           Alert all with nagiyos
        service_notification_period     24x7
        host_notification_period        24x7
        service_notification_options    c,w
        host_notification_options       d
        service_notification_commands   service_nagiyos_all
        host_notification_commands      host_nagiyos_all
}
```
