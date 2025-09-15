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