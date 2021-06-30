import subprocess
import numpy as np

from canela.io.calculation import Calculation


class CP2K(Calculation):
    def get_final_energy(self) -> float:
        raise NotImplementedError

        cmd = f"grep 'ENERGY|' {self.output_path}"
        cmd += " | tail -1 | egrep -o '[^ ]+$'"
        res = subprocess.check_output(cmd, shell=True).decode()
        return float(res)

    def get_vibrational_frequencies(self, output_path: str) -> np.ndarray:
        """pull vibrational frequencies from CP2K output file
        """
        # bash command to pull vibrational frequencies
        cmd = f"grep 'VIB|Freq' {output_path} | egrep -o '\-?[0-9]+\.[0-9]+'"

        # get the frequencies and convert to np array of floats
        output = subprocess.check_output(cmd, shell=True)
        output = output.decode().strip('\n')
        vib = np.array([float(v) for v in output.split('\n')])

        return vib
