import abc


class Calculation(abc.ABC):
    def __init__(self, output_path: str) -> None:
        self.output_path = output_path

    @abc.abstractmethod
    def get_final_energy(self) -> float:
        """Return final energy in Ha
        """

    def get_vibrational_frequencies(self) -> None:
        raise NotImplementedError
