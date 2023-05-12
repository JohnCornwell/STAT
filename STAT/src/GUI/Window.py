# This is a simple window interface that ensures linked windows have common methods
# that they can request from each other
import abc
from abc import abstractmethod


class Window (abc.ABC):

    # User requests to log out, so all windows should be destroyed
    @abstractmethod
    def log_out(self):
        pass

    # Destroy this window
    @abstractmethod
    def destroy(self):
        pass
