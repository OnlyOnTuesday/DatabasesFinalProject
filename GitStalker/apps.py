from django.apps import AppConfig
# import GitStalker.parseData as p

class MyAppConfig(AppConfig):
    name = "GitStalker"
    verbose_name = "Git Stalker"
    def ready(self):
        # yes, I know this is awful, please forgive me
        import GitStalker.parseData as p
        print("READY IS RUNNING")
        print("Probably want to put code here to populate database")

        p.parse_database()
