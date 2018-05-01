# ------------------------------------------------------------------------------
# Facade Implementation.
#--------------------------------------------------------------------------------
# Provide a unified interface to a set of interfaces in a subsystem. 
# Façade defines a higher-level interface that makes the subsystem easier to use.
# -------------------------------------------------------------------------------

class ResourceManager:
    def __init__(self):
        print("Update all resources.")


    def update_resources(self):
        self.reportDb = ReportDb()
        self.reportDb.update()

        self.intranetDb = InntranetDb()
        self.intranetDb.save()

        self.site = Site()
        self.site.update()

        self.Api = Api()
        self.Api.post()

class ReportDb:
    def __init__(self):
        print ("ReportDb called.")

    def update(self):
        print("ReportDb updated.")

class InntranetDb:
    def __init__(self):
        print("InntranetDb called.")

    def save(self):
        print("InntranetDb updated.")

class Site:
    def __init__(self):
        print("SiteDb called.")

    def update(self):
        print("Site updated.")

class Api:
    def __init__(self):
        print("Api called.")

    def post(self):
        print("Api post called.")


# ------------
# CLient code
# ------------
resource_manager =  ResourceManager()
resource_manager.update_resources()
