from abs import AMC, abstractmethod

class Tab(AMC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def group(self, group_id):
        pass

    