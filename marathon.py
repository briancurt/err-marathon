from errbot import BotPlugin, botcmd
from marathon import MarathonClient, MarathonError
import os


__author__ = 'Brian Curtich'


class Marathon(BotPlugin):
    """
    Perform basic operations over Marathon applications!
    """

    def get_configuration_template(self):

        return {'MARATHON_URL': None,
                'MARATHON_AUTH_TOKEN': None}


    def connect(self):
        url = self.config['MARATHON_URL']
        token = self.config['MARATHON_AUTH_TOKEN']

        return MarathonClient(url, auth_token=token)


    def status(self, msg, args):
        service = args[0]
        c = self.connect()
        app_data = c.get_app(service)

        if app_data.instances == app_data.tasks_healthy and not app_data.tasks_unhealthy:
            comment = "Everything looks alright! :rocket:"
        else:
            comment = "Something doesn't look right... :zap:"

        return ("Hey, \*{service}\* is running `{version}`. "
                "It has `{instances}` instances, `{healthy}` out of which are healthy "
                "and `{unhealthy}` unhealthy. Each of them has `{cpus}` cpus and `{mem}` mem. {comment}"
                "".format(service=service,
                          version=app_data.container.docker.image.split(":")[1],
                        instances=str(app_data.instances),
                          healthy=str(app_data.tasks_healthy),
                        unhealthy=str(app_data.tasks_unhealthy),
                             cpus=str(app_data.cpus),
                              mem=str(app_data.mem),
                          comment=comment
                         ))


    def restart(self, msg, args):
        service = args[0]
        c = self.connect()

        c.restart_app(service)

        return ("The service \*{service}\* is now restarting... :robot_face:"
                "".format(service=service))


    @botcmd
    def marathon_status(self, msg, args):
        """Get live information about a service"""
        return self.status(msg, args.split())


    @botcmd
    def marathon_restart(self, msg, args):
        """Restart a service"""
        return self.restart(msg, args.split())
