class ViewBase:
    def render(self):
        pass

class BaseView(ViewBase):
    def render(self):
        print("Admin page render start")
        super().render()
        print("Admin page render end")

class LoggingMixin(ViewBase):
    def render(self):
        print("Log start")
        super().render()
        print("Log end")

class AuthRequiredMixin(ViewBase):
    def __init__(self, auth = True):
        self.auth = auth
        super().__init__()

    def render(self):
        if self.auth:
            print("Auth OK\n"
                  "Template render")
        else:
            print("Access denied")
        super().render()

class AdminPageView(BaseView, LoggingMixin, AuthRequiredMixin):
    def render(self):
        super().render()

admin1 = AdminPageView()
admin1.render()