class BaseView:
    def render(self):
        print("Template render")

class LoggingMixin(BaseView):
    def render(self):
        print("Log start")
        super().render()
        print("Log end")

class AuthRequiredMixin(BaseView):
    def __init__(self, auth = True):
        self.auth = auth
        super().__init__()

    def render(self):
        if self.auth:
            print("Auth OK")
            super().render()

        else:
            print("Access denied")

class AdminPageView(LoggingMixin, AuthRequiredMixin , BaseView):
    def render(self):
        print("Admin page render")
        super().render()
        print("Admin page end")

admin1 = AdminPageView()
admin1.render()